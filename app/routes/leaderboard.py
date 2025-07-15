from typing import List
from fastapi import APIRouter
from app.models.leaderboard import LeaderboardUser
from app.db import db

router = APIRouter()

@router.get("/leaderboard", response_model=List[LeaderboardUser])
async def get_leaderboard():
    top_users = await db["users"].find(
        {}, {"_id": 0, "username": 1, "scoreTotal": 1}
    ).sort("scoreTotal", -1).limit(10).to_list(10)
    return top_users
