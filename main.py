from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://front-end-vert-nine-45.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

client = OpenAI(api_key=api_key)

class ChatMessage(BaseModel):
    message: str
    
@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running!"}


@app.post("/api/chat")
async def chat(message: ChatMessage):
    try:
        print(f"Received message: {message.message}") 
        
        if not message.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
            
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": message.message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        ai_response = response.choices[0].message.content
        print(f"AI Response: {ai_response}")  # Debug log
        return {"response": ai_response}
        
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug log
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000) 