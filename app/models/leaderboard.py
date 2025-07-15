from pydantic import BaseModel

class LeaderboardUser(BaseModel):
    username: str
    scoreTotal: int
