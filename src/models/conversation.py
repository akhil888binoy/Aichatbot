
from src.database.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey,UUID

class Conversation(Base):
    __tablename__ ="conversations"
    id = Column(UUID, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
