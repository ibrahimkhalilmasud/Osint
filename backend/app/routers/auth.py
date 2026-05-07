from fastapi import APIRouter
from pydantic import BaseModel

from ..security import create_access_token


router = APIRouter(prefix="/auth", tags=["auth"])


class TokenRequest(BaseModel):
    username: str
    role: str = "analyst"


@router.post("/token")
def issue_token(payload: TokenRequest) -> dict[str, str]:
    token = create_access_token(payload.username, payload.role)
    return {"access_token": token, "token_type": "bearer"}
