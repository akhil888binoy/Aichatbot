from src.database.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey


class Model(Base):
    __tablename__='models'
    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
