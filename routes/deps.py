from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from backend.config.jwt import verify_token
from backend.config.db import get_db
from sqlalchemy.orm import Session
from backend.models.user import User

oauth2_scheme = OAuth2PasswordBearer()

DBSession = Annotated[Session, Depends(get_db)]

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: DBSession) -> User:
    user_id = verify_token(token)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user