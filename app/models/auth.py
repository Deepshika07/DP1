from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from app.database import Base

class Auth(Base):
    __tablename__ = "auth"
    
    id = Column(Integer, primary_key=True, index=True)
    authtoken = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_ts = Column(TIMESTAMP(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    status = Column(Boolean, nullable=False )
    
    user = relationship("User", back_populates="auth_tokens")
    