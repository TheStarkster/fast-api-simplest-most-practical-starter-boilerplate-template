from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.password import hash_password
from routes.deps import DBSession
from models.user import User
from schemas.user import UserCreate, UserResponse
from config.jwt import create_access_token
from config.password import verify_password
from routes.deps import get_current_user, DBSession
from models.user import User
from schemas.token import TokenRequest, TokenResponse
from typing import Annotated

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: DBSession):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Hash the password
    hashed_password = hash_password(user_data.password)
    
    # Create new user
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hashed_password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.post("/login", response_model=TokenResponse)
def login(request: TokenRequest, db: DBSession):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": str(user.id)})
    return TokenResponse(access_token=token, token_type="bearer")

@router.get("/me")
def get_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
