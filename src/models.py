import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship(Usuario)

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable=False)
    author_id = Column(Integer, ForeignKey("usuario.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    usuario = relationship(Usuario)
    post = relationship(Post)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)

class Seguidor(Base):
    __tablename__ = 'seguidor'
    # id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("usuario.id"),  primary_key=True)
    user_to_id = Column(Integer, ForeignKey("usuario.id"),  primary_key=True)
    usuario = relationship(Usuario)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Ta re bien! Check the diagram.png file")
except Exception as e:
    print("Te mandaste alguna")
    raise e
