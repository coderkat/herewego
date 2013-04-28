from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref
import os

# db interactions with sessions
engine = create_engine("sqlite:///news.db", echo=True)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base() # required for sqlalchemy magics
Base.query = session.query_property()

# think about table names, not pluralizing ALL THE THINGS

class Stories(Base):
	__tablename__ = "stories" # store instances of this class in tbl 'stories'

	id = Column(Integer, primary_key=True)
	title = Column(String(128))
	abstract = Column(String(256))
	url = Column(String(128))
	source = Column(String(128))

# mapping table: predicted relationship b/t user and story
class Queue(Base):
	__tablename__ = "queue"

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey("users.id"))
	story_id = Column(Integer, ForeignKey("stories.id"))
	score = Column(Integer) # calculated value

	story = relationship("Stories", backref=backref("queue", order_by=id))
	user = relationship("Users", backref=backref("queue", order_by=id))

class Users(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	email = Column(String(64))
	password = Column(String(64))
	name = Column(String(128))

class Preferences(Base):
	__tablename__ = "preferences" 

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey("users.id"))
	story_id = Column(Integer, ForeignKey("stories.id"))
	preference = Column(Integer)

	user = relationship("Users", backref=backref("preferences", order_by=id))
	story = relationship("Stories", backref=backref("preferences", order_by=id))



# class Tags(Base):
# 	__tablename__ = "tags" 

# 	id = Column(Integer, primary_key=True)
# 	story_id = Column(Integer, ForeignKey("stories.id"))
# 	tag = Column(String(128), nullable=True)
# 	source = Column(String(128), nullable=False)

# 	story = relationship("Stories", backref=backref("tags", order_by=id))

### End class declarations
# def connect():
# 	global ENGINE
# 	global Session # a class generated by SQLAlchemy, describing how to interact with the db

# 	ENGINE = create_engine("sqlite:///ratings.db", echo=True)
# 	Session = sessionmaker(bind=ENGINE) # instantiate a session and return the instance below (can later use session = Session())
# 	return Session()

def main():
	"""For when we need to, you know, do stuff"""
	pass

if __name__ == "__main__":
	main()