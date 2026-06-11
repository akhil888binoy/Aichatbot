from src.database.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey,UUID


class Model(Base):
    __tablename__='models'
    id = Column(UUID, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
