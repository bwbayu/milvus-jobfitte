# Milvus Vector Database

# How to run (Locally)
### Model embeddings that i use here is Doc2Vec that we train using job-cv dataset
1. build docker image for milvus and attu (GUI for milvus vector db)
- docker compose up
2. Open browser and go to localhost:8000 or 127.0.0.1:8000
3. Create environtment and download package
- virtualenv env
- (windows) env\Scripts\activate
- pip install -r requiremnet.txt
4. Create collection and index
- python connect.py
5. Insert data to collection
- python insert.py
6. Query from collection
- python main.py

# How to run (Cloud) using zilliz, open-source cloud milvus vector database 
### Model embeddings that i use here is Sentence-BERT that we fine-tuning using job-cv dataset
- [https://zilliz.com/cloud]
1. Create collection and index in zilliz dashboard, metric_type that i use in this project is COSINE 
2. Create .env file that contains COLLECTION_NAME, ZILLIZ_API_KEY, and ZILLIZ_URI
3. Create environtment and download package
- virtualenv env
- (windows) env\Scripts\activate
- pip install -r requiremnet.txt
4. Query from collection
- python main_izziz.py