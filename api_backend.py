import header as h

songsplayed = 0
songcount = 0
songlist = []
songurls = []
songthumbnails = []


def getSong():
    # Search for song via user input
    searchq = input("Input song to search for: ")
    # build api access
    youtube = h.build('youtube', 'v3', developerKey=h.api_key)
    # NOTE: UNUSED -> type(youtube)
    requests = youtube.search().list(
        q=searchq, part='snippet', type='video', maxResults=1)
    # NOTE: UNUSED -> type(requests)

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
    songtr = h.pafy.new(videourl)
    songtitle = songtr.title
    # insert title and url into list to grab
    songlist.insert(songcount, songtitle)
    songurls.insert(songcount, videourl)
    songthumbnails.insert(songcount, thumbnail)
    print(songlist[songcount], ", has been Added!")
    songcount = songcount + 1
    return videourl


def playFirst():
    # Pafy is getting the best audio/video qaulity
    global media
    global songsplayed
    pvideo = h.pafy.new(songurls[songsplayed])
    songsplayed = songsplayed + 1
    best = pvideo.getbestaudio()
    playurl = best.url
    # VLC python player playing song
    media = h.vlc.MediaPlayer(best.url)
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
    # NOTE: Debugging:
    print(f"songslist: {songlist}")
    print(f"songs played: {songsplayed}")
    print(f"song count: {songcount}")
    print(f"song urls: {songurls}")
    print(f"song thumbnails: {songthumbnails}")
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

# NOTE: Unused code:
# def playaudio():
#     media = songplayer()
#     media.play()
#     h.time.sleep(5)
#     while media.is_playing():
#         h.time.sleep(1)


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


app = h.QApplication(h.sys.argv)
w = h.QWidget()
l = h.QVBoxLayout(w)
addsongbutton = h.QPushButton("Add Song")
playbutton = h.QPushButton("Play")
startbutton = h.QPushButton("Start")
pausebutton = h.QPushButton("Pause")
nextbutton = h.QPushButton("Next")
stopbutton = h.QPushButton("Stop")
incbutton = h.QPushButton("Increase Volume")
decbutton = h.QPushButton("Decrease Volume")
startbutton.clicked.connect(startButton)
playbutton.clicked.connect(playButton)
pausebutton.clicked.connect(pButton)
addsongbutton.clicked.connect(addSong)
nextbutton.clicked.connect(nextSong)
stopbutton.clicked.connect(stopSong)
incbutton.clicked.connect(incVol)
decbutton.clicked.connect(decVol)
menu = h.QMenu()
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
