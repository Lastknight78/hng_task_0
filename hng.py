from fastapi import FastAPI, status
from datetime import datetime
from pydantic import BaseModel


class EmailTimestampResponse(BaseModel):
    email: str
    timestamp: str
    
app = FastAPI()

@app.get("/profile", response_model=EmailTimestampResponse, status_code=status.HTTP_200_OK)
def get_email_and_timestamp():
    return {
        "email": "adekunleabioye27@gmail.com",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "github" : "https://github.com/Lastknight78/hng_task_0"
        }