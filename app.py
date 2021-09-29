import flask
import json
from flask import request, render_template, redirect, url_for

app = flask.Flask(__name__)
app.config['DEBUG'] = True

SONGLIST = {'Apple': 1, 'Cameron': 2, 'BestSong': 3}

@app.route('/', methods=['GET'])
def getAll():
    sortedSongs = sorted(SONGLIST.items(), key=lambda x: x[1], reverse=True)
    return render_template("vote.html", songList=sortedSongs)

@app.route('/', methods=['POST'])
def addSong():
    songName = request.form.get('song')
    duplicateName = duplicate(songName, SONGLIST)
    if duplicateName:
        SONGLIST[duplicateName] += 1
    else:
        SONGLIST[songName] = 1
    return redirect(url_for("getAll"))

@app.route("/delete/<song>")
def delete(song):
    del SONGLIST[song]
    return redirect(url_for("getAll"))

@app.route('/upvote/<song>')
def upvote(song):
    duplicateName = duplicate(song, SONGLIST)
    if duplicateName:
        SONGLIST[duplicateName] += 1
    return redirect(url_for("getAll"))

@app.route('/downvote/<song>')
def downvote(song):
    duplicateName = duplicate(song, SONGLIST)
    if duplicateName:
        SONGLIST[duplicateName] -= 1
        if (SONGLIST[duplicateName] < -5):
            SONGLIST.pop(duplicateName)
    return redirect(url_for("getAll"))

def duplicate(song, songList):
    for name in songList:
        if (name.upper() == song.upper()):
            return name
    return None

app.run()