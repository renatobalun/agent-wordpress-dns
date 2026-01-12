import logging
import os
from pathlib import Path

from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    SimpleDirectoryReader,
)

from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client
from dotenv import load_dotenv

load_dotenv()

qdrant_link = os.getenv("QDRANT_LINK")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

BASE_DIR = Path(__file__).resolve().parent

def generate_datasource():

    data_dir = (BASE_DIR / "../../data/wordpress").resolve()
    documents = SimpleDirectoryReader(str(data_dir)).load_data()
    
    logger.info("Connecting to qdrant")

    client = qdrant_client.QdrantClient(
        qdrant_link
    )
    logger.info("Creating new index")

    vector_store = QdrantVectorStore(client=client, collection_name="wordpress")
    logger.info("Created QdrantVectorStore")

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    logger.info("Created StorageContext")
    
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
    )

    logger.info("Done")
    
if __name__ == "__main__":
    generate_datasource()