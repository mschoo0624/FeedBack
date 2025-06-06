# 
from sqlalchemy import Column, Integer, String, Float
from database import Base 

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    sentiment = Column(String)  # "like"/"dislike"
    confidence = Column(Float)
    source = Column(String)     # e.g., URL

class CustomKeyword(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, unique=True)
    category = Column(String)   # "positive"/"negative"
