from model import title_list, jd_list, embeddings_list, idx
from pymilvus import (
    connections,
    Collection,
)
connections.connect("default", host="localhost", port="19530")
collection = Collection("jobs_collection")

data = [ title_list, jd_list, embeddings_list]

collection.insert(data)
collection.load()
