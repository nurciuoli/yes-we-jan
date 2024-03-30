import requests
import json

class Jan:
    def __init__(self, model="mistral-ins-7b-q4"):
        self.model=model

    def completion(self,user_msg,system_prompt="You are a helpful assistant.",
    max_tokens=2048,
    frequency_penalty=0,
    presence_penalty=0,
    temperature=.5,
    top_p=.95
    ):
        payload = {
            "messages": [
                {
                    "content": system_prompt,
                    "role": "system"
                },
                {
                    "content": user_msg,
                    "role": "user"
                }
            ],
            "model": self.model,
            "stream": False,
            "max_tokens": max_tokens,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
            "temperature": temperature,
            "top_p": top_p,
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post("http://localhost:1337/v1/chat/completions", json=payload, headers=headers)
        for print_response in response.json()['choices']:
            print(print_response['message']['content'])