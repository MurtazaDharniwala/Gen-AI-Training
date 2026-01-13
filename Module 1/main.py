import os
import time
import json
from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

 
load_dotenv()
 
app = FastAPI()
 
 
from typing import Any
 
class QueryRequest(BaseModel):
    question: str
 
from fastapi import Body
 
@app.post("/ask")
async def ask_question(req: QueryRequest = Body(...)):
    api_key = os.getenv("LLM_KEY")
    print(f" API key:{api_key}")
    if not api_key:
        return {"error": "API key not set"}
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=api_key,
    )
    start = time.time()
    systemPrompt = "You're a Production Support AI assistant. Answer the question as best as you can. If you don't know the answer, just say that you don't know. Do not make up an answer. Keep the answer in JSON format having severity, issue_type, recommended_action as keys."
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:groq",
            messages=[
                {"role": "system", "content": systemPrompt},
                {"role": "user", "content": req.question}
                ],
        )
        latency = time.time() - start
        usage = getattr(completion, 'usage', None)
        tokens = usage.total_tokens if usage else None
        cost = tokens * 0.00001 if tokens else None
        print(f"LLM raw response: {completion}")
        return {
            "response": json.loads(completion.choices[0].message.content),
            # "latency": latency,
            # "tokens": tokens,
            # "estimated_cost": cost
        }
    except Exception as e:
        return {"error": str(e)}