# Created by Austin Seidel
import header as h

songsplayed = 0
songcount = 0
songlist = []
songurls = []
songthumbnails = []
searchq = ""


def getSong(add_song=False) -> dict:
    # build api access
    youtube = h.build('youtube', 'v3', developerKey=h.api_key)
    requests = youtube.search().list(
        q=searchq, part='snippet', type='video', maxResults=1)
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
    if add_song:
        songlist.insert(songcount, songtitle)
        songurls.insert(songcount, videourl)
        songthumbnails.insert(songcount, thumbnail)
        print(songlist[songcount], ", has been Added!")

        print(songcount)
        songcount = songcount + 1

    return {
        'url': videourl,
        'title': songtitle,
        'thumbnail': thumbnail
    }


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
    return media


def queueIsEmpty():
    return songsplayed == songcount


def nextSong():
    if queueIsEmpty():
        media.stop()
        print('No more tracks have been added, please add another.')
        return False
    else:
        media.stop()
        playFirst()
        media.play()
