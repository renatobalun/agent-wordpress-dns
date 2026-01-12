import os

from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
)

from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client
from dotenv import load_dotenv

load_dotenv()

qdrant_link = os.getenv("QDRANT_LINK")

def generate_query_engine():

    client = qdrant_client.QdrantClient(qdrant_link)
    vector_store = QdrantVectorStore(client=client, collection_name="wordpress")

    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        storage_context=storage_context
        )
    return index.as_query_engine()

def search(query: str):
    query_engine = generate_query_engine()
    response = query_engine.query(query)
    return response