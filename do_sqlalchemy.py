#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))

Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()
new_user = User(id='7', name='Stan')
new_book = Book(id='1', name='learn python', user_id='7')
session.add(new_user)
session.commit()
session.add(new_book)
session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.id=='7').one()
print('type:', type(user))
print('name:', user.name)
print('books:', user.books[0].name)
session.close()