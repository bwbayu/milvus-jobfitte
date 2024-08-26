from sentence_transformers import SentenceTransformer
from model import resume
from preprocessing import preprocessing_data
from dotenv import load_dotenv
import os
from pymilvus import (
    Collection, connections,
)

# load env and key 
load_dotenv()
COLLECTION_NAME = os.getenv('COLLECTION_NAME')
ZILLIZ_API_KEY = os.getenv('ZILLIZ_API_KEY')
ZILLIZ_URI = os.getenv('ZILLIZ_URI')
print("load key done")

# load model and milvus
model_sbert = SentenceTransformer("bwbayu/sbert_model_jobcv")
connections.connect("default", uri=ZILLIZ_URI, token=ZILLIZ_API_KEY)
collection = Collection(COLLECTION_NAME)
print("load model and milvus done")

# preprocessing and convert resume data
preprocessed_text = preprocessing_data(resume)
resume_embedding = model_sbert.encode(preprocessed_text, convert_to_tensor=False)
print("preprocessing done")

# search milvus
search_params = {"metric_type": "COSINE", "params": {"nprobe": 10}}
results = collection.search(
    data=[resume_embedding],
    anns_field="vector",
    param=search_params,
    limit=5,
    output_fields=["id", "title", "description"]
)
print("search done")

for result in results[0]:
    print(f"Job ID: {result.id}, Title: {result.entity.get('title')}, Distance: {result.distance}")