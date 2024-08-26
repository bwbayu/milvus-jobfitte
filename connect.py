from model import embedding_dimension
from pymilvus import (
    connections,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)
connections.connect("default", host="localhost", port="19530")

fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=255),
    FieldSchema(name="description", dtype=DataType.VARCHAR, max_length=5000),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=embedding_dimension)
]

schema = CollectionSchema(fields, "job_description_embeddings")
collection = Collection("jobs_collection", schema)

index_params = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128}
}

collection.create_index(field_name="embedding", index_params=index_params)