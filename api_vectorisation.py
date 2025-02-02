from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

class VectorizeRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de vectorisation !"}

@app.get("/vectorize/")
def vectorize(prompt: str = Query(..., description="Le texte à vectoriser")):
    """
    Endpoint pour vectoriser un prompt.
    """
    vectorized_prompt = f"Vectorisation de : {prompt}"
    return {"vectorized_prompt": vectorized_prompt}

@app.post("/vectorize/")
def vectorize_post(request: VectorizeRequest):
    """
    Endpoint pour vectoriser un prompt via une requête POST.
    """
    vectorized_prompt = f"Vectorisation de : {request.prompt}"
    return {"vectorized_prompt": vectorized_prompt}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Utilisation du port dynamique sur Render
    uvicorn.run(app, host="0.0.0.0", port=port)



