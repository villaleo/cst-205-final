import sys
import PySide6.QtGui
import urllib.request
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QHBoxLayout, QVBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QImage
from PySide6.QtCore import (Slot, Qt)
from PySide6.QtWidgets import QListWidget

# NOTE: New imports from base-code branch:
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

author_names = "Leonardo Villalobos, Luz Violeta Robles, Austin Seidel"
