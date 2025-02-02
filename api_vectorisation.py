from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

class VectorizeRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    """
    Endpoint racine qui confirme que l'API est en ligne.
    """
    return {"message": "Bienvenue sur l'API de vectorisation !"}

@app.get("/vectorize/")
def vectorize(prompt: str = Query(..., description="Le texte à vectoriser")):
    """
    Endpoint GET qui accepte un paramètre `prompt` et retourne un texte vectorisé.
    """
    return {"vectorized_prompt": f"Vectorisation de : {prompt}"}

@app.post("/vectorize/")
def vectorize_post(request: VectorizeRequest):
    """
    Endpoint POST qui prend un JSON avec `prompt` et retourne le texte vectorisé.
    """
    return {"vectorized_prompt": f"Vectorisation de : {request.prompt}"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Render gère dynamiquement le port
    uvicorn.run(app, host="0.0.0.0", port=port)




