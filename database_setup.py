#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    gender = Column(String(250))

class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    # main elements
    d_h1 = Column(String(200))
    d_p = Column(String(3000))
    d_img = Column(String(3000))
    count_h1 = Column(Integer)
    count_p = Column(Integer)
    count_img = Column(Integer)
    # style section fixed values for h1 or p
    d_textcolor = Column(String(50))
    d_pagecolor = Column(String(50))
    d_background = Column(String(300))
    d_pwidth = Column(String(50))
    d_margin = Column(String(50))
    d_padding = Column(String(50))
    d_textalign = Column(String(50))
    # style section fixed image
    d_imgwidth = Column(String(500))
    d_imgheight = Column(String(50))
    d_imgradius = Column(String(50))
    d_borderwidth = Column(Integer)
    d_bordertype = Column(String(50))
    d_bordercolor = Column(String(100))
    # style section variable for h1
    h1_image = Column(String(500))
    h1_b = Column(String(50))
    h1_bradius = Column(String(50))
    h1_fsize = Column(String(50))
    h1_customsize = Column(String(100))
    h1_width = Column(String(100))
    # users comments and post
    user_post = Column(String(2000))
    comment = Column(String(2000))
    # some extra storage
    extra = Column(String(500))
    extra_string = Column(String(500))
    another_string = Column(String(500))
    last_extra = Column(String(500))
    extra_int = Column(Integer)
    
    

class Mydocuments(Base):
    __tablename__ = 'mydocuments'

    id = Column(Integer, primary_key=True)
    domain_name = Column(String(37), nullable=False)
    description = Column(String(2000))    
    document_id = Column(Integer, ForeignKey('document.id'))
    document = relationship(Document)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Vote(Base):
    __tablename__ = 'vote'

    id = Column(Integer, primary_key=True)
    likes = Column(Integer)
    dislike = Column(Integer)    


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'likes': self.likes,
            'dislike': self.dislike,
            'id': self.id,
        }
        
        
engine = create_engine('sqlite:///editor.db')
Base.metadata.create_all(engine)
