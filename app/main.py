from fastapi import FastAPI
from app.routes.leaderboard import router as leaderboard_router
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()  # Charge les variables d'environnement depuis .env

app = FastAPI(
    title="Leaderboard Service",
    description="Microservice qui expose le top 10 des utilisateurs selon leur score",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or "*" to allow all for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Inclusion de la route /leaderboard
app.include_router(leaderboard_router)

# Route de base pour test
@app.get("/")
async def root():
    return {"message": "Leaderboard service is running ✅"}
