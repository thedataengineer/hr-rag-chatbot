# backend/llm/bedrock_client.py
import boto3
import json

class NativeBedrockClient:
    def __init__(self, model_id="anthropic.claude-3-sonnet-20240229-v1:0"):
        self.client = boto3.client('bedrock-runtime')
        self.model_id = model_id
    
    def generate(self, prompt, system_prompt=None):
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [{
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            }],
            "max_tokens": 1024
        }
        
        if system_prompt:
            body["system"] = system_prompt
            
        response = self.client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(body)
        )
        return json.loads(response['body'].read())['content'][0]['text']
