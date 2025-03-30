from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_neo4j import Neo4jGraph
import os
from dotenv import load_dotenv
from kg_info import NODE_INFO, RELATIONSHIP_INFO, RELATIONSHIP_TYPES
load_dotenv()


class Querier:  
    def __init__(self):
        self.graph = self.init_neo4j_graph()
        # self.chain = self.create_nl2cypher_chain(self.graph)
        self.llm = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0.1,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
    
    def init_neo4j_graph():
        """Initialize Neo4j graph connection"""
        return Neo4jGraph(
            url=os.getenv("NEO4J_URI"),
            username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"), 
        database=os.getenv("NEO4J_DATABASE"),
        enhanced_schema=True
    )


    def custom_query(self, query: str):
        
        system_prompt = f"""You are an expert Cypher Query Generator. Given a natural language query, generate a Cypher query to retrieve information from the knowledge graph.
        You have access to the schema of the KG and it is as follows:
        Nodes_info: {NODE_INFO}
        Relationships_types: {RELATIONSHIP_TYPES}
        
        Do not generate query if it is not according to the schema.
        Return only the Cypher query and nothing else.

        IMPORTANT: nodes have node_name as property not only name
        """

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]

        cypher_query = self.llm.invoke(messages)
        cypher_query = cypher_query.content.strip().removeprefix("```cypher").removesuffix("```").strip()
        return cypher_query

    def error_handler(self, query, cypher_query, error):

        system_prompt = f"""You are an expert Cypher Query Generator. 
        Given a natural language query, a generated cypher query and an error message, generate a new cypher query to retrieve information from the knowledge graph, after analysing the error message.
        Make sure to adhere to the original natural language query and not get diverted too much by the error message.
        
        You have access to the schema of the KG and it is as follows:
        Nodes_info: {NODE_INFO}
        Relationships_types: {RELATIONSHIP_TYPES}
        
        Do not generate query if it is not according to the schema.
        Return only the Cypher query and nothing else.

        IMPORTANT: nodes have node_name as property not name (d.node_name and NOT d.name)

        """

        human_prompt = f"""Natural language query: {query}
        Generated cypher query: {cypher_query}
        Error message: {error}"""
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt)
        ]
        
        cypher_query = self.llm.invoke(messages)
        cypher_query = cypher_query.content.strip().removeprefix("```cypher").removesuffix("```").strip()
        return cypher_query
        

    

if __name__ == "__main__":
    querier = Querier()
    # Example usage
    test_queries = [
        "What diseases are associated with the BRCA1 gene?",
        "Find all drugs that target proteins involved in cancer pathways",
        "What is the cause of eruptive xanthomas?"
    ]

    # test_queries = [
    #     "What is the cause of eruptive xanthomas?"
    # ]
    
    # # Initialize once and reuse
    # graph = init_neo4j_graph()

    # # print(graph.schema)
    # chain = create_nl2cypher_chain(graph)
    
    # for query in test_queries:
    #     print(f"\nQuery: {query}")
    #     result = query_knowledge_graph(query, chain)
        
    #     if result['cypher_query']:
    #         print(f"\nGenerated Cypher:\n{result['cypher_query']}")
        
    #     if result['answer']:
    #         print(f"\nAnswer:\n{result['answer']}")
        
    #     if 'error' in result:
    #         print(f"\nError:\n{result['error']}")
        
    #     print("\n" + "="*50)
    
    for query in test_queries:
        cypher_query = querier.custom_query(query)
        for i in range(3):
            if cypher_query:
                print(f"\nAttempt {i}: Generated Cypher:\n{cypher_query}")
            
            # Execute the Cypher query
            try:
                graph = init_neo4j_graph()
                result = graph.query(cypher_query)
                print(f"\nResult:\n{result}")
                break
            except Exception as e:
                print(f"Error executing query: {str(e)}")
                cypher_query = querier.error_handler(query, cypher_query, str(e))
            
        print("\n" + "="*50)
        