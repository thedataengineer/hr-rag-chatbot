# backend/retrieval/opensearch_client.py
from opensearchpy import OpenSearch
import numpy as np

class NativeVectorClient:
    def __init__(self, host, port=443):
        self.client = OpenSearch(
            hosts=[{'host': host, 'port': port}],
            use_ssl=True,
            verify_certs=True
        )
    
    def create_index(self, index_name, dim=384):
        body = {
            "settings": {
                "index": {
                    "knn": True,
                    "knn.algo_param.ef_search": 100
                }
            },
            "mappings": {
                "properties": {
                    "embedding": {
                        "type": "knn_vector",
                        "dimension": dim,
                        "method": {
                            "name": "hnsw",
                            "space_type": "l2",
                            "engine": "nmslib"
                        }
                    },
                    "text": {"type": "text"},
                    "metadata": {"type": "object"}
                }
            }
        }
        self.client.indices.create(index=index_name, body=body)
    
    def index_document(self, index_name, text, embedding, metadata):
        doc = {
            "text": text,
            "embedding": embedding.tolist(),
            "metadata": metadata
        }
        self.client.index(index=index_name, body=doc)
