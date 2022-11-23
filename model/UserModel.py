import json

from sqlalchemy import Column,Integer,String,UniqueConstraint,Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import config
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()

class User(Base):
    __tablename__ = 'test'
    auto_increment_id = Column(Integer,autoincrement=True,primary_key=True)
    segment_id = Column(Integer)
    text = Column(String(300))
    entity = Column(String(300))
    entity_kb = Column(String(300))
    data = Column(String(300))
    # predicate = Column(String(300))
    # object = Column(String(300))

    def __init__(self,auto_increment_id,segment_id,text,entity,entity_kb,data):
        self.auto_increment_id = auto_increment_id
        self.segment_id = segment_id
        self.text = text
        self.entity = entity
        self.entity_kb = entity_kb
        self.data= data
    def __str__(self):
        info = {
            "auto_increment_id": self.auto_increment_id,
            "segment_id": self.segment_id,
            "text": self.text,
            "entity": self.entity,
            "entity_kb": self.entity_kb,
            "data": self.data
        }
        return json.dumps(info)

# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
def query():
    sm = sessionmaker(bind=engine)
    session = sm()
    all = session.query(User).all()
    return all
