
from src.database.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey


class Conversation(Base):
    __tablename__ ="conversations"
    id = Column(String, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
