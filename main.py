from model import resume_embedding
from pymilvus import (
    connections,
    Collection,
)

connections.connect("default", host="localhost", port="19530")
collection = Collection("jobs_collection")

collection.load()

# query
search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
results = collection.search(
    data=[resume_embedding],
    anns_field="embedding",
    param=search_params,
    limit=5,
    output_fields=["id", "title", "description"]
)

for result in results[0]:
    print(f"Job ID: {result.id}, Title: {result.entity.get('title')}, Distance: {result.distance}")