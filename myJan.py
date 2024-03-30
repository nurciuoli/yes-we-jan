import requests
import json

class Jan:
    def __init__(self,
                 system_prompt="You are a helpful assistant.",
                 model="mistral-ins-7b-q4"):
        self.model=model
        self.messages=[]
        self.payload = {}
        self.models = None
        self.headers = {}
        self.system_prompt=system_prompt
    
    def get_my_models(self):
        url = "http://localhost:1337/v1/models"
        response = requests.get(url)
        self.models=response.json()
        return response.json()
    
    def post_and_print(self,payload,headers):
        response = requests.post("http://localhost:1337/v1/chat/completions", json=payload, headers=headers)
        for print_response in response.json()['choices']:
            print(print_response['message']['content'])

    def post_print_and_append(self,payload,headers):
        response = requests.post("http://localhost:1337/v1/chat/completions", json=payload, headers=headers)
        for print_response in response.json()['choices']:
            print(print_response['message']['content'])
            self.messages.append({"content":print_response['message']['content'],"role":"assistant"})

        self.payload['messages']= self.messages

    def completion(self,user_msg,
    max_tokens=2048,
    frequency_penalty=0,
    presence_penalty=0,
    temperature=.5,
    top_p=.95
    ):
        payload = {
            "messages": [
                {
                    "content": self.system_prompt,
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

        self.post_and_print(payload,headers)

    def start_thread(self,user_msg,
    max_tokens=2048,
    frequency_penalty=0,
    presence_penalty=0,
    temperature=.5,
    top_p=.95
    ):
        self.messages =  [
                {
                    "content": self.system_prompt,
                    "role": "system"
                },
                {
                    "content": user_msg,
                    "role": "user"
                }
            ]
        self.payload = {
            "messages":self.messages,
            "model": self.model,
            "stream": False,
            "max_tokens": max_tokens,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
            "temperature": temperature,
            "top_p": top_p,
        }
        self.headers = {"Content-Type": "application/json"}

        self.post_print_and_append(self.payload,self.headers)

    
    def continue_thread(self,user_msg):
        self.payload['messages'].append({'content':user_msg,"role":"user"})
        self.post_print_and_append(self.payload,self.headers)
        