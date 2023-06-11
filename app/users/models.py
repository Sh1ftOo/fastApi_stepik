from sqlalchemy import Integer, String, Column

from app.db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String , nullable=False)
    password = Column(String, nullable=False)
