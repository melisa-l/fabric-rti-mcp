"""
Fabric Semantic Model service - queries Power BI/Fabric semantic layer for relationships.

Uses Fabric REST APIs and XMLA endpoint to access semantic model metadata
that's not available through SQL Analytics endpoint.
"""
import os
from typing import List, Dict, Any, Optional, Tuple
import requests
from azure.identity import DefaultAzureCredential


def _get_fabric_token() -> str:
    """Get access token for Fabric APIs."""
    credential = DefaultAzureCredential()
    token = credential.get_token("https://analysis.windows.net/powerbi/api/.default")
    return token.token


def find_semantic_model_for_lakehouse(workspace_id: str, lakehouse_name: str) -> Optional[str]:
    """
    Find the semantic model (dataset) associated with a lakehouse.
    
    Args:
        workspace_id: Fabric workspace ID
        lakehouse_name: Name of the lakehouse
    
    Returns:
        Semantic model ID if found, None otherwise
    """
    token = _get_fabric_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Get all datasets in workspace
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/datasets"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to get datasets: {response.status_code} - {response.text}")
    
    datasets = response.json().get("value", [])
    
    # Look for dataset matching lakehouse name
    # Lakehouses typically create a default semantic model with the same name
    for dataset in datasets:
        if lakehouse_name.lower() in dataset.get("name", "").lower():
            return dataset["id"]
    
    return None


def get_semantic_model_relationships(workspace_id: str, dataset_id: str) -> List[Dict[str, Any]]:
    """
    Get relationships from a semantic model using XMLA/TOM (Tabular Object Model).
    
    Args:
        workspace_id: Fabric workspace ID
        dataset_id: Semantic model/dataset ID
    
    Returns:
        List of relationship definitions
    """
    token = _get_fabric_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Use Power BI REST API to execute XMLA query
    # This queries the Analysis Services tabular model
    xmla_query = """
    {
      "queries": [
        {
          "query": "EVALUATE SELECTCOLUMNS(INFO.RELATIONSHIPS(), \\"Name\\", [Name], \\"FromTable\\", [FromTable], \\"FromColumn\\", [FromColumn], \\"ToTable\\", [ToTable], \\"ToColumn\\", [ToColumn], \\"CrossFilteringBehavior\\", [CrossFilteringBehavior], \\"IsActive\\", [IsActive])"
        }
      ]
    }
    """
    
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/datasets/{dataset_id}/executeQueries"
    
    try:
        response = requests.post(url, headers=headers, data=xmla_query)
        
        if response.status_code != 200:
            # Try alternative: TMSCHEMA DMV query
            return _get_relationships_via_dmv(workspace_id, dataset_id, token)
        
        results = response.json()
        
        # Parse response
        relationships = []
        if "results" in results and len(results["results"]) > 0:
            rows = results["results"][0].get("tables", [{}])[0].get("rows", [])
            for row in rows:
                relationships.append({
                    "name": row.get("Name", ""),
                    "from_table": row.get("FromTable", ""),
                    "from_column": row.get("FromColumn", ""),
                    "to_table": row.get("ToTable", ""),
                    "to_column": row.get("ToColumn", ""),
                    "cross_filtering": row.get("CrossFilteringBehavior", ""),
                    "is_active": row.get("IsActive", True)
                })
        
        return relationships
        
    except Exception as e:
        print(f"Error querying relationships: {e}")
        return []


def _get_relationships_via_dmv(workspace_id: str, dataset_id: str, token: str) -> List[Dict[str, Any]]:
    """
    Alternative method: Query relationships using DMV (Dynamic Management Views).
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # DAX query to get relationships from $SYSTEM.TMSCHEMA_RELATIONSHIPS
    dax_query = """
    {
      "queries": [
        {
          "query": "EVALUATE $SYSTEM.TMSCHEMA_RELATIONSHIPS"
        }
      ]
    }
    """
    
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/datasets/{dataset_id}/executeQueries"
    
    try:
        response = requests.post(url, headers=headers, data=dax_query)
        
        if response.status_code != 200:
            return []
        
        results = response.json()
        relationships = []
        
        if "results" in results and len(results["results"]) > 0:
            rows = results["results"][0].get("tables", [{}])[0].get("rows", [])
            for row in rows:
                relationships.append({
                    "name": row.get("Name", ""),
                    "from_table": row.get("FromTable", ""),
                    "from_column": row.get("FromColumn", ""),
                    "to_table": row.get("ToTable", ""),
                    "to_column": row.get("ToColumn", ""),
                    "cross_filtering": row.get("CrossFilterDirection", ""),
                    "is_active": row.get("IsActive", True)
                })
        
        return relationships
        
    except Exception as e:
        print(f"DMV query failed: {e}")
        return []


def get_lakehouse_semantic_relationships() -> List[Tuple[str, str, str, str, str, str]]:
    """
    Get semantic model relationships for the configured lakehouse.
    
    Reads FABRIC_WORKSPACE_ID and FABRIC_LAKEHOUSE_NAME from environment,
    finds the associated semantic model, and returns its relationships.
    
    Returns:
        List of tuples: (from_table, from_column, to_table, to_column, relationship_name, cross_filtering)
    """
    workspace_id = os.getenv("FABRIC_WORKSPACE_ID")
    lakehouse_name = os.getenv("FABRIC_LAKEHOUSE_NAME")
    
    if not workspace_id:
        raise ValueError("FABRIC_WORKSPACE_ID environment variable not set")
    if not lakehouse_name:
        raise ValueError("FABRIC_LAKEHOUSE_NAME environment variable not set")
    
    # Find semantic model
    dataset_id = find_semantic_model_for_lakehouse(workspace_id, lakehouse_name)
    
    if not dataset_id:
        return []  # No semantic model found
    
    # Get relationships
    relationships = get_semantic_model_relationships(workspace_id, dataset_id)
    
    # Convert to tuple format for consistency with SQL-based tools
    results = []
    for rel in relationships:
        results.append((
            rel["from_table"],
            rel["from_column"],
            rel["to_table"],
            rel["to_column"],
            rel["name"],
            rel["cross_filtering"]
        ))
    
    return results


def get_semantic_model_info() -> Dict[str, Any]:
    """
    Get information about the semantic model associated with the lakehouse.
    
    Returns:
        Dictionary with semantic model details including relationships, tables, and measures
    """
    workspace_id = os.getenv("FABRIC_WORKSPACE_ID")
    lakehouse_name = os.getenv("FABRIC_LAKEHOUSE_NAME")
    
    if not workspace_id or not lakehouse_name:
        raise ValueError("FABRIC_WORKSPACE_ID and FABRIC_LAKEHOUSE_NAME must be set")
    
    dataset_id = find_semantic_model_for_lakehouse(workspace_id, lakehouse_name)
    
    if not dataset_id:
        return {
            "found": False,
            "message": f"No semantic model found for lakehouse '{lakehouse_name}'"
        }
    
    relationships = get_semantic_model_relationships(workspace_id, dataset_id)
    
    return {
        "found": True,
        "workspace_id": workspace_id,
        "dataset_id": dataset_id,
        "lakehouse_name": lakehouse_name,
        "relationship_count": len(relationships),
        "relationships": relationships
    }
