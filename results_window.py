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
        Contains the Qt objects needed to construct the window and its widgets.

        + `query` : The user's input which will be sent to YouTube.
        + `app_name` : The name of the application (to prevent manually changing each instance).
        """
        self.appName = h.QLabel(self)
        self.null_space = h.QLabel("\t")
        self.media_entry_field = h.QLineEdit(f"{query}")
        self.search_button = h.QPushButton("Search")

        self.thumbnail_frame = h.QLabel()
        thumbnail = h.QPixmap(self.__search(query)["thumbnail"])
        thumbnail = thumbnail.scaled(300, 360, h.Qt.KeepAspectRatio)
        self.thumbnail_frame.setPixmap(thumbnail)

        self.appName.setText(f"<h1>{app_name}</h1>")

        self.media_entry_field.setMinimumWidth(350)
        self.media_entry_field.setMaximumWidth(350)

        h1_layout = h.QHBoxLayout()
        h1_layout.addWidget(self.appName)
        h1_layout.addWidget(self.media_entry_field)
        h1_layout.addWidget(self.search_button)

        v1_layout = h.QVBoxLayout()
        v1_layout.addLayout(h1_layout)
        v1_layout.addWidget(self.null_space)
        v1_layout.addWidget(self.thumbnail_frame)

        self.setLayout(v1_layout)
