from fastapi import FastAPI, HTTPException
import requests
app = FastAPI()


@app.get("/repositories/{Nom_user}/{Nom_repo}")
def get_repository(Nom_user: str, Nom_repo: str):
    url = f"https://api.github.com/repos/{Nom_user}/{Nom_repo}"#construction de l'url de l'api github
    response = requests.get(url)
# Vérifier si le code de statut de la réponse est égal à 200, ce qui signifie que la requête a réussi.
    if response.status_code == 200:
        return response.json()#Renvoie les données de réponse sous forme de JSON.
    else:
        raise HTTPException(status_code=response.status_code, detail="Repository not found")#Lève une exception HTTP avec le code de statut et le message spécifiés.


@app.post("/repositories")
def create_repository(Nom_user: str, Nom_repo: str):
    url = "https://api.github.com/user/repos"
    payload = {
        "name": Nom_repo,
        "private": False
    }
    response = requests.post(url, json=payload)

    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to create repository")


@app.put("/repositories/{Nom_user}/{Nom_repo}")
def update_repository(Nom_user: str, Nom_repo: str, new_name: str):
    url = f"https://api.github.com/repos/{Nom_user}/{Nom_repo}"
    payload = {
        "name": new_name
    }
    response = requests.patch(url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to update repository")


@app.delete("/repositories/{Nom_user}/{Nom_repo}")
def delete_repository(Nom_user: str, Nom_repo: str):
    url = f"https://api.github.com/repos/{Nom_user}/{Nom_repo}"
    response = requests.delete(url)

    if response.status_code == 204:
        return "Repository deleted"
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to delete repository")
if __name__ == "__main__":#Démarre le serveur FastAPI en utilisant Uvicorn avec l'application
    # Cela permet de lancer l'application et d'écouter les requêtes entrantes.
    uvicorn.run(app, host="0.0.0.0", port=8000)

# exécute l'application avec la commande suivante dans terminal:
# uvicorn main:app --reload
#