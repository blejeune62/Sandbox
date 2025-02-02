from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn

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
    # Simulation d'une vectorisation (ex : ajout de tags)
    vectorized_prompt = f"Vectorisation de : {prompt}"

    return {"vectorized_prompt": vectorized_prompt}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

