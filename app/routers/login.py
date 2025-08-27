from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.core.security import verify_password
from app.database import get_db
import app.schema as schemas
from app.dp_ops import user_ops
from app.models.user import User
from app.schema.user import UserCreate, UserLogin, UserResponse

router = APIRouter()

@router.post("/signup", tags=["Registration"], response_model=UserResponse)
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    db_user = db.query(User).filter(User.email_id==user.email_id).first() 
    #SELECT * FROM users WHERE email_id = 'xyz@example.com' LIMIT 1;

    if db_user:
        raise HTTPException(status_code=400, detail="This email already exixts")
    
    new_user = user_ops.create_user(db, user)    
    return new_user

@router.post("/login", tags=["Registration"], response_model=UserResponse)
def login(user: UserLogin, db: Session=Depends(get_db)):
    db_user, error = user_ops.user_login(db, user)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return db_user
    