from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "Knowledge"
	id_of_stupid_knowledge = Column(Integer, primary_key = True)
	topic = Column(String)
	rating = Column(Integer)
	title = Column(String)
	def __repr__(self):

		return("topic:{}\n"
				"title:{}\n"
				"rating:{}\n").format(self.topic, self.title,self.rating)
	def pring():
		
		print("If you want to learn about "+self.topic+", you should look at the Wikipedia article called "+self.title+".We gave this article a rating of "+self.rating+ " out of 10!")
		if self.rating<= 7 :
			print("Unfortunately, this article does not have a better rating. Maybe, this is an article that should be replaced soon!.")
# pring()
print(repr(Knowledge.__table__))

	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	# pass
	# history and science and life
	# 2 and 10 and 1