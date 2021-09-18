<h1>BeatFetch</h1>

Developed by Austin Seidel, Luz Violeta Robles, and Leonardo Villalobos<br>
CST-205 Multimedia Design and Programming<br>
May 17, 2021<br>

<h2>Dependencies</h2>

<h3>Software</h3>
+ Python
+ VLC Media Player
<h3>Libraries (or pip installs)</h3>
+ pip install google-api-python-client
+ pip install python-vlc
+ pip install youtube-dl
+ pip install pafy
+ pip install requests
+ pip install PySide6 (Warning! May not function properly with Python 3.9.*)

It is recommended to use a virtual environment to organize all the installs.
Once you have all the programs and pip modules installed, run the main.py
file on your machine. This program sends requests to a YouTube API, therefore
the amount of requests per day are limited. 

Link to the GitHub repository:
https://github.com/villaleo/cst-205-final.git
Link to the Trello Workspace:
https://trello.com/b/VhmhfNPY/final-project-group-36

If we had more time to build onto the project, we would have implemented a 
previous song button and displayed the result video instead of just the 
thumbnail. We would have also fixed a known bug where the labels each
display the last queued song's values instead of the actual next song's
values.