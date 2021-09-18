<h1>BeatFetch</h1>

Developed by Austin Seidel, Luz Violeta Robles, and Leonardo Villalobos<br>
CST-205 Multimedia Design and Programming<br>
May 17, 2021<br>

<h2>Dependencies</h2>

<h3>Software</h3>
<ul>
  <li>Python</li>
  <li>VLC Media Player</li>
</ul>
<h3>Libraries (or pip installs)</h3>
<ul>
  <li><code>pip install google-api-python-client</code></li>
  <li><code>pip install python-vlc</code></li>
  <li><code>pip install youtube-dl</code></li>
  <li><code>pip install pafy</code></li>
  <li><code>pip install requests</code></li>
  <li><code>pip install PySide6</code> (Warning! May not function properly with Python 3.9.*)</li>
</ul>


It is recommended to use a virtual environment to organize all the installs.
Once you have all the programs and pip modules installed, run the main.py
file on your machine. This program sends requests to a YouTube API, therefore
the amount of requests per day are limited. 

<h2>Outro</h2><br>
<ul>
  <li><a href="https://github.com/villaleo/cst-205-final.git">GitHub repository</a></li>
  <li><a href="https://trello.com/b/VhmhfNPY/final-project-group-36">Trello Workspace</a></li>
<ul>

If we had more time to build onto the project, we would have implemented a 
previous song button and displayed the result video instead of just the 
thumbnail. We would have also fixed a known bug where the labels each
display the last queued song's values instead of the actual next song's
values.
