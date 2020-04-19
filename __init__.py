#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Document, Mydocuments, Vote
from flask import session as login_session
import random
import string

# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import sqlite3
from flask import make_response
import requests
app = Flask(__name__)



APPLICATION_NAME = "nocode-editor"

# Connect to Database and create database session
engine = create_engine('sqlite:///editor.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def sumlikes():
    connection = sqlite3.connect("editor.db")
    # cursor object
    crsr = connection.cursor()
    # execute the command to fetch the Sum of users likes from vote 
    crsr.execute("SELECT SUM(Vote.likes) FROM Vote")
    # store the fetched data in the ans variable 
    ans = crsr.fetchone()
    # store the sum of likes in virable ans[0] first index in the row
    first_query = ans[0]
    return first_query
    
def sumdislikes():
    connection = sqlite3.connect("editor.db")
    crsr = connection.cursor()
    # execute the command to fetch the Sum of users dislikes from vote
    crsr.execute("SELECT SUM(Vote.dislike) FROM Vote")
    second = crsr.fetchone()
    secod_query = second[0]
    return secod_query
    
  
    
 



# App Interface
@app.route('/')
@app.route('/editor/', methods=['GET', 'POST'])
def showEditor():

    count_likes = sumlikes()
    count_dislikes = sumdislikes()
            
    return render_template('editor.html', likes = count_likes, dislikes = count_dislikes)
    

@app.route('/votehandle/', methods=['GET', 'POST'])
def makeVote():
    
    if request.method == 'POST':
        try:
            like =  request.form['user_like']
        except:
            like =  0       
          
        
        try:
            dislike = request.form['user_dislike']
        except:
            dislike = 0        
            
        
        if like:
            newVote = Vote(likes=1, dislike=dislike)            
            session.add(newVote)
            flash('New Vote Added, Thanks, Your Last Vote Was I Like This')
            session.commit()            
            count_likes = sumlikes()
            count_dislikes = sumdislikes()
            return redirect(url_for('showEditor'))
        if dislike:
            newVote = Vote(dislike=1, likes=like)
            session.add(newVote)
            flash('New Vote Added, Thanks, Your Last Vote Was I Don\'t Like This')          
            session.commit()
            count_likes = sumlikes()
            count_dislikes = sumdislikes()
            return redirect(url_for('showEditor'))
            
    else:
        return render_template('voting.html')   




if __name__ == '__main__':
    app.secret_key = 'AS&S^1234Aoshsheo152h23h5j7ks9-1---3*-s,#k>s'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
