from sqlalchemy.orm import Session
# from app import models, schema
from app.schema import user
from app.models.user import User
from app.core.security import hash_password, verify_password

def create_user(db : Session, user : user.UserCreate):
    db_user = User(
        firstname=user.firstname,
        lastname=user.lastname,
        email_id=user.email_id,
        password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def user_login(db: Session, user : user.UserLogin):
    db_user = db.query(User).filter(User.email_id==user.email_id).first()
    
    token= db.query(User)
    print(token)
    if not db_user:
        return None, "The email id does not exist."
    
    if not verify_password(user.password, db_user.password ):
        return None, "Incorrect password"
    
    return db_user, None