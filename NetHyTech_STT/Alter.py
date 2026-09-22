from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel
import edge_tts

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CommandRequest(BaseModel):
    text: str

@app.post("/chat")
async def chat(request: CommandRequest):
    user_text = request.text.lower()
    
    if any(greet in user_text for greet in ["hello", "hi", "hey"]):
        reply = "Hello sir. All systems are operational."
    elif "who are you" in user_text:
        reply = "I am Jarvis, your web-integrated assistant."
    elif "status" in user_text:
        reply = "Power levels are nominal, and network streams are stable."
    else:
        reply = f"You said: {request.text}"

    return {"response": reply}

@app.get("/tts")
async def text_to_speech(text: str):
    try:
        communicate = edge_tts.Communicate(text, "en-GB-RyanNeural")
        audio_data = bytearray()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data.extend(chunk["data"])
        
        return Response(content=bytes(audio_data), media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
