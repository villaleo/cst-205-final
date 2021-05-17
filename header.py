import sys
import PySide6.QtGui
import urllib.request
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QHBoxLayout, QVBoxLayout, QMenu
)
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QImage
from PySide6.QtCore import (Slot, Qt)
from PySide6.QtWidgets import QListWidget
import subprocess
from googleapiclient.discovery import build
import time
import vlc
import pafy

dev_names = "Austin Seidel, Luz Violeta Robles, Leonardo Villalobos"

# NOTE: After changing API keys, perform `pip install youtube-dl --upgrade`
#       to fix error message.
# Current key:
api_key = 'AIzaSyBCxD4_4bN4Tlfpw8p-5SFBrE9OxhkFYko'

# Other keys:
# - Quota met @5/16 3:24p: 'AIzaSyCrJoYWAYN2QH_kcNFxIPFXd88jGpzSapg'
# - Quota met @5/16 12:30p: 'AIzaSyCKAu3TpYJahOHnYmvr_be9-cK-KbGN4C4'
