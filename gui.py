from PIL import Image
import PIL
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout,
    QVBoxLayout, QGroupBox, QDialog, QTextBrowser, QComboBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import (Slot, Qt)


class ResultsWindow(QWidget):
    """
    Create a new window which uses the text passed into the search bar 
    from the main window.

    Searches YouTube for `query` and plays the sound and displays the information
    of the video.

    + `query` : The user's input which will be sent to YouTube.
    + `app_name` : The name of the application (to prevent manually changing each instance).
    """

    def __init__(self, query, app_name) -> ResultsWindow:
        super().__init__()
        self.__SearchResultsWindow(query, app_name)

    def __search(self, query) -> dict:
        """
        Performs the YouTube search using `query` and returns a dictionary containing each
        key-value pair of data sent back.

        Returns a dictionary object containing `"title"`, the name of the video title and 
        `"thumbnail"`, the path to the image file.

        + `query` : The user's input which will be sent to YouTube.
        """
        # TODO: Connect API media search **

        # Sample Image:
        # "debug/img/i1.jpg"
        return {
            "title": "ThumbnailName",
            "thumbnail": "debug/img/i1.jpg"
        }

    def __SearchResultsWindow(self, query, app_name) -> None:
        """
        Contains all the Qt objects needed to construct the window and its widgets.

        + `query` : The user's input which will be sent to YouTube.
        + `app_name` : The name of the application (to prevent manually changing each instance).
        """
        self.appName = QLabel(self)
        self.null_space = QLabel("\t")
        self.media_entry_field = QLineEdit(f"{query}")
        self.search_button = QPushButton("Search")

        self.thumbnail_frame = QLabel()
        thumbnail = QPixmap(self.search(query)["thumbnail"])
        thumbnail = thumbnail.scaled(300, 360, Qt.KeepAspectRatio)
        self.thumbnail_frame.setPixmap(thumbnail)

        self.appName.setText(f"<h1>{app_name}</h1>")

        self.media_entry_field.setMinimumWidth(350)
        self.media_entry_field.setMaximumWidth(350)

        h1_layout = QHBoxLayout()
        h1_layout.addWidget(self.appName)
        h1_layout.addWidget(self.media_entry_field)
        h1_layout.addWidget(self.search_button)

        v1_layout = QVBoxLayout()
        v1_layout.addLayout(h1_layout)
        v1_layout.addWidget(self.null_space)
        v1_layout.addWidget(self.thumbnail_frame)

        self.setLayout(v1_layout)


class HomeWindow(QWidget):
    """

    """

    # TODO: Name for application.
    app_name = "AppName"

    def __init__(self):
        """

        """
        super().__init__()
        self.__HomePage()

    def __HomePage(self) -> None:
        """

        """
        self.appName = QLabel(self)
        self.null_space = QLabel("\t")
        self.media_entry_field = QLineEdit("Enter a query")
        self.search_button = QPushButton("Search")

        # TODO: Option to create an app logo once we figure out everything else.
        # This is currently at the lowest of priority.
        self.appName.setText(f"<h1>{self.app_name}</h1>")

        self.media_entry_field.setMinimumWidth(350)
        self.media_entry_field.setMaximumWidth(350)
        self.media_entry_field.selectAll()

        v1_layout = QVBoxLayout()
        v1_layout.addWidget(self.appName)

        h1_layout = QHBoxLayout()
        h1_layout.addWidget(self.null_space)
        h1_layout.addWidget(self.media_entry_field)
        h1_layout.addWidget(self.search_button)

        v1_layout.addLayout(h1_layout)

        self.search_button.clicked.connect(self.call_results_HomeWindow)
        self.setLayout(v1_layout)

    @Slot()
    def call_results_HomeWindow(self) -> None:
        """

        """
        self.close()
        query = self.media_entry_field.text()
        self.results = ResultsWindow(query, self.app_name)
        self.results.show()


app = QApplication(sys.argv)
main = HomeWindow()
main.show()
sys.exit(app.exec_())
