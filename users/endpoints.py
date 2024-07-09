from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import UserCreate, UserLogin, User
import crud

router = APIRouter()

@router.post("/register/", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    return crud.create_user(db=db, user=user)

@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    authenticated_user = crud.authenticate_user(db, username=user.username, password=user.password)
    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username or password",
        )
    return {"message": "Login successful"}
