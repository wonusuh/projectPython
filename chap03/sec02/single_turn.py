from openai import OpenAI
from dotenv import load_dotenv
import os

# api key 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 오픈ai 클라이언트의 인스턴스 생성
client = OpenAI(api_key=api_key)

def get_response(messages) :
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        messages=messages
    )

    return response.choices[0].message.content

messages = [
    {"role" : "system", "content" : "너는 사용자를 도와주는 상담사야."}
]

while True :
    user_input = input("사용자 : ")

    if user_input == "exit" :
        break

    messages.append({"role" : "user", "content" : user_input})
    ai_response = get_response(messages)
    messages.append({"role" : "assistant", "content" : ai_response})

    print("AI : " + ai_response)
