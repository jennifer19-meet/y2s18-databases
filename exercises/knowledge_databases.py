from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, title, rating):
	knowledge_object = Knowledge(
		topic = topic,
		title = title,
		rating = rating)
	session.add(knowledge_object)
	session.commit()


# add_article("shiraz", "goat songs", 10000)

# print(repr(Knowledge.__table__))
def query_all_articles():
	q = session.query(Knowledge
		).all()
	return(q)
	
print(query_all_articles())
def query_article_by_topic(topic):

	fil = session.query(Knowledge
		).filter_by(
		topic= topic).first()
	return (fil)
print(query_article_by_topic("shir"))
# def delete_article_by_topic():


# def delete_all_articles():


# def edit_article_rating():
# 	pass
