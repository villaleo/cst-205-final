import sys
import subprocess
from googleapiclient.discovery import build
import time
import vlc
import pafy
from PIL import Image
from PIL.ImageQt import ImageQt
from requests import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

api_key = 'AIzaSyCrJoYWAYN2QH_kcNFxIPFXd88jGpzSapg'
songsplayed = 0
songcount = 0
songlist = []
songurls = []
songthumbnails = []


def getSong():
    # Search for song via user input
    searchq = input("Input song to search for: ")
    # build api access
    youtube = build('youtube', 'v3', developerKey=api_key)
    type(youtube)

    requests = youtube.search().list(
        q=searchq, part='snippet', type='video', maxResults=1)
    type(requests)

    results = requests.execute()
    # from results grab video id
    global videourl
    global thumbnail
    for item in results['items']:
        videourl = (item['id']['videoId'])
        thumbnail = (item['snippet']['thumbnails']['high']['url'])
    # assign video id to a url
    videourl = 'https://www.youtube.com/watch?v=' + videourl
    # get song title
    global songcount
    songtr = pafy.new(videourl)
    songtitle = songtr.title
    # insert title and url into list to grab
    songlist.insert(songcount, songtitle)
    songurls.insert(songcount, videourl)
    songthumbnails.insert(songcount, thumbnail)
    print(songlist[songcount], ", Has been Added!")
    songcount = songcount + 1
    return videourl


def playFirst():
    # Pafy is getting the best audio/video qaulity
    global media
    global songsplayed
    pvideo = pafy.new(songurls[songsplayed])
    songsplayed = songsplayed + 1
    best = pvideo.getbestaudio()
    playurl = best.url
    # VLC python player playing song
    media = vlc.MediaPlayer(best.url)
    # enable input
    media.video_set_key_input(True)
    media.video_set_mouse_input(True)
    print("Now Playing: ", pvideo.title)
    # return media
    # media.play()
    return media

# Functions to start play/pause


def incVol():
    global volume
    volume = volume + 10
    media.audio_set_volume(volume)


def decVol():
    global volume
    volume = volume - 10
    media.audio_set_volume(volume)


def addSong():
    getSong()


def nextSong():
    if songsplayed == songcount:
        media.stop()
        print('No more tracks have been added, please add another.')
    else:
        media.stop()
        playFirst()
        media.play()


def stopSong():
    media.stop()


def playaudio():
    media = songplayer()
    media.play()
    time.sleep(5)
    while media.is_playing():
        time.sleep(1)


def startButton():
    getSong()
    global volume
    volume = 50
    media = playFirst()
    media.play()


def playButton():
    media.play()


def pButton():
    media.pause()


app = QApplication(sys.argv)
w = QWidget()
l = QVBoxLayout(w)
addsongbutton = QPushButton("Add Song")
playbutton = QPushButton("Play")
startbutton = QPushButton("Start")
pausebutton = QPushButton("Pause")
nextbutton = QPushButton("Next")
stopbutton = QPushButton("Stop")
incbutton = QPushButton("Increase Volume")
decbutton = QPushButton("Decrease Volume")
startbutton.clicked.connect(startButton)
playbutton.clicked.connect(playButton)
pausebutton.clicked.connect(pButton)
addsongbutton.clicked.connect(addSong)
nextbutton.clicked.connect(nextSong)
stopbutton.clicked.connect(stopSong)
incbutton.clicked.connect(incVol)
decbutton.clicked.connect(decVol)
menu = QMenu()
l.addWidget(startbutton)
l.addWidget(playbutton)
l.addWidget(pausebutton)
l.addWidget(addsongbutton)
l.addWidget(nextbutton)
l.addWidget(stopbutton)
l.addWidget(incbutton)
l.addWidget(decbutton)
w.show()
app.exec_()
