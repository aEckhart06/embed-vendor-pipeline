from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel


class dataObject():
    markdown: str 
    url: str

class UserCreate(BaseModel):
    data: list[dataObject]

router = APIRouter(prefix="/pipeline_routes", tags=["items"])

# Simple token-based auth (for example purposes)
security = HTTPBearer()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(security)):
    # In production, decode JWT and validate
    if token.credentials != "unvailed_data_pipeline_api_token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    return {"username": "demo_user"}  # normally comes from token payload

# GET all items
@router.post("/transform_data")
def transform_data(userData: UserCreate, user=Depends(get_current_user)):
    return {"user": user["username"], "data": userData.data}


