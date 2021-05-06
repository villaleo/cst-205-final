import header as h


class ResultsWindow(h.QWidget):
    """
    Create a new window which uses the text passed into the search bar 
    from the main window.

    Searches YouTube for `query` and plays the sound and displays the information
    of the video.

    + `query` : The user's input which will be sent to YouTube.
    + `app_name` : The name of the application (to prevent manually changing each instance).
    """

    def __init__(self, query, app_name):
        super().__init__()
        self.__SearchResultsWindow(query, app_name)

    def __trim_window_title(self, window_title) -> str:
        """
        # TODO: DOCUMENT ME **
        """
        pass

    def __trim_media_title(self, media_title) -> str:
        """
        # TODO: DOCUMENT ME **
        """
        pass

    def __search(self, query) -> dict:
        """
        # TODO: UPDATE THE DOCSTRING **

        Performs the YouTube search using `query` and returns a dictionary containing each
        key-value pair of data sent back.

        Returns a dictionary object containing `"title"`, the name of the video title and 
        `"thumbnail"`, the path to the image file.

        + `query` : The user's input which will be sent to YouTube.
        """

        # TODO: Connect API media search **

        # Source: https://stackoverflow.com/questions/24003043/pyqt4-and-python-3-display-an-image-from-url

        # NOTE: Current thumbnail image is a sample.
        image_url = "https://f4.bcbits.com/img/a3122062570_10.jpg"
        image_data = h.urllib.request.urlopen(image_url).read()

        img = h.PySide6.QtGui.QImage()
        img.loadFromData(image_data)

        return {
            # NOTE: 53 chars..
            "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZ_ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "thumbnail": img
        }

    def __SearchResultsWindow(self, query, app_name) -> None:
        """
        Contains the Qt objects needed to construct the window and its widgets.

        + `query` : The user's input which will be sent to YouTube.
        + `app_name` : The name of the application (to prevent manually changing each instance).
        """
        self.appName = h.QLabel(self)
        self.null_space = h.QLabel("\t")
        self.media_entry_field = h.QLineEdit(f"{query}")
        self.search_button = h.QPushButton("Queue?")

        self.media_title = self.__search(query)["title"]
        self.media_title_label = h.QLabel(self)
        self.media_title_label.setText(f"<h3>{self.media_title}</h3>")

        self.media_thumbnail = h.QLabel(self)
        thumbnail = self.__search(query)["thumbnail"]
        self.media_thumbnail.setPixmap(
            h.PySide6.QtGui.QPixmap(thumbnail)
            .scaled(250, 250, h.Qt.KeepAspectRatio)
        )

        self.appName.setText(f"<h1>{app_name}</h1>")

        self.media_entry_field.setMinimumWidth(350)
        self.media_entry_field.setMaximumWidth(350)
        self.media_entry_field.selectAll()

        h1_layout = h.QHBoxLayout()
        h1_layout.addWidget(self.appName)
        h1_layout.addWidget(self.null_space)
        h1_layout.addWidget(self.media_entry_field)
        h1_layout.addWidget(self.search_button)
        h1_layout.addWidget(self.null_space)

        v1_layout = h.QVBoxLayout()
        v1_layout.addLayout(h1_layout)
        v1_layout.addWidget(self.null_space)
        v1_layout.addWidget(self.media_title_label)
        v1_layout.addWidget(self.media_thumbnail)

        self.setWindowTitle(self.media_title)
        self.setLayout(v1_layout)
