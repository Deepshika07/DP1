from sqlalchemy import TIMESTAMP, Boolean, create_engine, Column, Integer, String, text
from app.database import Base

class User(Base):
    __tablename__ = "users" 
    
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email_id = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_ts = Column(TIMESTAMP(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    status = Column(Boolean, server_default="true")
    