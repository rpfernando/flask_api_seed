from db import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    def __init__(self, name=None):
        self.name = name

    # def __repr__(self):
        # return '<User %r>' % self.name

    def to_hash(user):
        return {'id':user.id,'name':user.name}
