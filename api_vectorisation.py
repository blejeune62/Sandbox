import os
import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Vérification des clés API
if not OPENAI_API_KEY:
    raise ValueError("❌ Clé API OpenAI manquante.")

# Initialisation de l'API OpenAI
openai.api_key = OPENAI_API_KEY

# Création de l'application FastAPI
app = FastAPI()

# Schéma pour la requête utilisateur
class PromptRequest(BaseModel):
    prompt: str

@app.post("/vectorize/")
async def vectorize_prompt(request: PromptRequest):
    user_prompt = request.prompt

    # 🔹 Étape 1 : Vectorisation du prompt enrichi
    try:
        embedding = openai.embeddings.create(
            model="text-embedding-3-small",
            input=user_prompt
        )
        vectorized_prompt = embedding["data"][0]["embedding"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur de vectorisation OpenAI : {str(e)}")

    return {
        "original_prompt": user_prompt,
        "vectorized_prompt": vectorized_prompt
    }

# 🚀 Démarrer l'API avec uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
