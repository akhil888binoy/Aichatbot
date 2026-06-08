
from src.database.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey


class Message(Base):
    __tablename__ ="messages"
    id = Column(String, primary_key=True, nullable=False)
    conversation_id = Column(String, ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    role = Column(String, nullable=False)
    content = Column(String, nullable=False)


