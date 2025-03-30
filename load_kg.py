#  old code, I loaded using ADMIN IMPORT
# Done within 8 seconds


from neo4j import GraphDatabase
import pandas as pd
import logging
from tqdm import tqdm
import time
import os
from concurrent.futures import ThreadPoolExecutor
from load_dotenv import load_dotenv
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_kg_to_neo4j(uri, username, password, kg_df, batch_size=1000):
    """Load knowledge graph efficiently with larger batches and optimized queries"""
    logger.info(f"Starting to load knowledge graph with {len(kg_df)} rows")

    def create_batch_nodes(tx, batch):
        # More efficient UNWIND query without transaction control
        query = """
        UNWIND $batch AS row
        MERGE (source:`{row.x_type}` {id: row.x_id})
        ON CREATE SET source.name = row.x_name, source.source = row.x_source
        MERGE (target:`{row.y_type}` {id: row.y_id})
        ON CREATE SET target.name = row.y_name, target.source = row.y_source
        CREATE (source)-[:`{row.display_relation}` {type: row.relation}]->(target)
        """
        tx.run(query, batch=batch.to_dict('records'))

    try:
        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            with driver.session(database="neo4j") as session:
                logger.info("Loading data in batches...")
                total_rows = len(kg_df)
                
                with tqdm(total=total_rows, desc="Loading nodes") as pbar:
                    for i in range(0, total_rows, batch_size):
                        batch = kg_df.iloc[i:i+batch_size].copy()
                        session.execute_write(create_batch_nodes, batch)
                        pbar.update(len(batch))
                
                logger.info("Finished loading all rows")

    except Exception as e:
        logger.error(f"Error loading knowledge graph: {str(e)}")
        raise

def create_node_index_mapping(kg_df):
    """Create mapping from node_index to node_id using vectorized operations"""
    # Use more efficient pandas operations
    source_mapping = kg_df[['x_index', 'x_id']].drop_duplicates()
    target_mapping = kg_df[['y_index', 'y_id']].drop_duplicates()
    
    source_mapping.columns = ['node_index', 'node_id']
    target_mapping.columns = ['node_index', 'node_id']
    
    # Use concat with ignore_index for better performance
    all_mappings = pd.concat([source_mapping, target_mapping], ignore_index=True).drop_duplicates()
    return dict(zip(all_mappings['node_index'], all_mappings['node_id']))

def process_feature_batch(args):
    """Process a batch of feature updates"""
    driver, batch_df, columns, id_map, node_type = args
    
    def update_batch_properties(tx, rows, cols):
        property_sets = [f"n.{col} = row.{col}" for col in cols if col != 'node_index']
        property_string = ", ".join(property_sets)
        
        query = f"""
        UNWIND $rows as row
        MATCH (n:`{node_type}`)
        WHERE n.id = row.node_id
        SET {property_string}
        """
        
        data = []
        for _, row in rows.iterrows():
            row_dict = row.to_dict()
            node_index = row_dict['node_index']
            if node_index in id_map:
                row_dict['node_id'] = id_map[node_index]
                data.append(row_dict)
        
        if data:
            tx.run(query, rows=data)

    try:
        with driver.session(database="neo4j") as session:
            session.execute_write(update_batch_properties, batch_df, columns)
        return len(batch_df)
    except Exception as e:
        logger.error(f"Batch processing error: {str(e)}")
        return 0

def update_node_properties(uri, username, password, feature_df, node_type, index_to_id_map, batch_size=1000, max_workers=4):
    """Update node properties using parallel processing"""
    logger.info(f"Starting to update {node_type} properties for {len(feature_df)} nodes")
    
    feature_df = feature_df.dropna(axis=1, how='all')
    columns = feature_df.columns.tolist()
    
    try:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        
        # Split data into batches for parallel processing
        batches = [feature_df[i:i + batch_size] for i in range(0, len(feature_df), batch_size)]
        batch_args = [(driver, batch, columns, index_to_id_map, node_type) for batch in batches]
        
        total_updated = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            with tqdm(total=len(feature_df), desc=f"Updating {node_type} properties") as pbar:
                for result in executor.map(process_feature_batch, batch_args):
                    total_updated += result
                    pbar.update(result)
        
        driver.close()
        logger.info(f"Finished updating {node_type} properties. Updated {total_updated} nodes.")
        
    except Exception as e:
        logger.error(f"Error updating {node_type} properties: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        # Neo4j connection details
        uri = os.getenv("NEO4J_URI")
        username = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")

        # Step 1: Load the main knowledge graph
        logger.info("Reading knowledge graph CSV file...")
        kg = pd.read_csv('primeKG/kg.csv', low_memory=False)
        logger.info(f"Knowledge graph loaded successfully. Shape: {kg.shape}")
        
        # Create node_index to node_id mapping
        logger.info("Creating node index to ID mapping...")
        index_to_id_map = create_node_index_mapping(kg)
        logger.info(f"Created mapping for {len(index_to_id_map)} unique nodes")
        
        # Load the main graph
        load_kg_to_neo4j(uri, username, password, kg)
        
        # Step 2: Update disease properties
        logger.info("Reading disease features...")
        disease_features = pd.read_csv('primeKG/disease_features.csv', low_memory=False)
        logger.info(f"Disease features loaded successfully. Shape: {disease_features.shape}")
        update_node_properties(uri, username, password, disease_features, 'disease', index_to_id_map)
        
        # Step 3: Update drug properties
        logger.info("Reading drug features...")
        drug_features = pd.read_csv('primeKG/drug_features.csv', low_memory=False)
        logger.info(f"Drug features loaded successfully. Shape: {drug_features.shape}")
        update_node_properties(uri, username, password, drug_features, 'drug', index_to_id_map)
        
    except KeyboardInterrupt:
        logger.info("\nProcess interrupted by user. Cleaning up...")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
