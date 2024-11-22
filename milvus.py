from pymilvus import MilvusClient, DataType
from pymilvus import model
from pymilvus import Collection
import pandas as pd

# Step 1: Establish the Milvus client
client = MilvusClient(uri="http://localhost:19530")
if client.has_collection(collection_name="ondisk_collection"):
    client.drop_collection(collection_name="ondisk_collection")
client.create_collection(collection_name="ondisk_collection")
print("Collection created")
