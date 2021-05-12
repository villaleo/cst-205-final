import header as h
import trim as t


class ResultsWindow(h.QWidget):
    """
    Create a new window which uses the text passed into the search bar 
    from the main window.

    Searches YouTube for `query` and plays the sound and displays the information
    of the video.

    + `query` : The user's input which will be sent to YouTube.
    + `app_name` : The name of the application (to prevent manually changing each instance).
    """

    default_media_entry = "Enter a query to add to queue..."

    def __init__(self, query: str, app_name: str):
        super().__init__()
        self.__SearchResultsWindow(query, app_name)

    def __search(self, query: str) -> dict:
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
            "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZ_ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "thumbnail": img
        }

    def __SearchResultsWindow(self, query: str, app_name: str) -> None:
        """
        Contains the Qt objects needed to construct the window and its widgets.

        + `query` : The user's input which will be sent to YouTube.
        + `app_name` : The name of the application (to prevent manually changing each instance).
        """
        # Labels:
        self.appName = h.QLabel(self)
        self.appName.setText(f"<h1>{app_name}</h1>")

        self.null_space = h.QLabel("\t")

        self.media_title_label = h.QLabel(self)
        self.media_title = self.__search(query)["title"]
        self.media_title_label.setText(f"<h3>{self.media_title}</h3>")

        self.up_next_label = h.QLabel("<h4>Up next:</h4>")

        self.media_thumbnail = h.QLabel(self)

        # Text Fields:
        self.media_entry_field = h.QLineEdit(self.default_media_entry)
        self.media_entry_field.setMinimumWidth(350)
        self.media_entry_field.setMaximumWidth(350)
        self.media_entry_field.selectAll()

        # Buttons:
        self.search_button = h.QPushButton("Queue")
        self.search_button.setMaximumWidth(70)
        self.search_button.setMinimumWidth(70)

        self.play_button = h.QPushButton("▶︎")
        self.play_button.setMaximumWidth(70)
        self.play_button.setMinimumWidth(70)

        self.pause_button = h.QPushButton("❙❙")
        self.pause_button.setMaximumWidth(70)
        self.pause_button.setMinimumWidth(70)

        self.next_button = h.QPushButton("▶︎▶︎❙")
        self.next_button.setMaximumWidth(70)
        self.next_button.setMinimumWidth(70)

        # Thumbnail:
        thumbnail = self.__search(query)["thumbnail"]
        self.media_thumbnail.setPixmap(
            h.PySide6.QtGui.QPixmap(thumbnail)
            .scaled(250, 250, h.Qt.KeepAspectRatio)
        )

        # Layout: search space -> layouts:
        search_line_layout = h.QHBoxLayout()
        search_line_layout.addWidget(self.appName)
        search_line_layout.addWidget(self.null_space)
        search_line_layout.addWidget(self.media_entry_field)
        search_line_layout.addWidget(self.search_button)
        search_line_layout.addWidget(self.null_space)

        # Layout: empty layout -> layouts:
        null_layout = h.QHBoxLayout()
        null_layout.addWidget(self.null_space)
        null_layout.addWidget(self.null_space)
        null_layout.addWidget(self.null_space)

        # Layout: control space -> layouts:
        # Source: https://stackoverflow.com/questions/41405251/how-can-i-align-a-button-at-the-bottom-right-in-pyqt
        control_layout = h.QHBoxLayout()
        control_layout.addWidget(
            self.play_button, alignment=h.Qt.AlignHorizontal_Mask)
        control_layout.addWidget(
            self.pause_button, alignment=h.Qt.AlignBaseline)
        control_layout.addWidget(
            self.next_button, alignment=h.Qt.AlignLeft)

        # Layout: media space -> layouts:
        media_layout = h.QHBoxLayout()
        media_layout.addWidget(self.media_thumbnail)
        media_layout.addWidget(self.up_next_label)

        # Layout: main space -> layouts:
        main_layout = h.QVBoxLayout()
        main_layout.addLayout(search_line_layout)
        main_layout.addWidget(self.null_space)
        main_layout.addWidget(self.media_title_label)
        main_layout.addLayout(media_layout)
        main_layout.addLayout(null_layout)
        main_layout.addLayout(control_layout)

        # Signal Slot Connection: buttons -> functions:
        self.search_button.clicked.connect(self.__queue_song)
        self.play_button.clicked.connect(self.__play)
        self.pause_button.clicked.connect(self.__pause)
        self.next_button.clicked.connect(self.__skip)

        # Window: attributes -> window:
        self.setWindowTitle(self.media_title)
        self.setLayout(main_layout)

    def __not_default_entry(self, string: str) -> bool:
        """

        """
        return string != "" and string != self.default_media_entry

    @h.Slot()
    def __queue_song(self) -> str:
        """
        TODO: How is the queue implemented in the base-code branch? **
        """
        if self.__not_default_entry(self.media_entry_field.text()):
            print(f"{self.media_entry_field.text()} queued!")
            return self.media_entry_field.text()
        else:
            # Display this message in the window
            print("Cannot queue an empty query!")

    @h.Slot()
    def __play(self) -> None:
        """

        """
        print("play")

    @h.Slot()
    def __pause(self) -> None:
        """

        """
        print("pause")

    @h.Slot()
    def __skip(self) -> None:
        """
        TODO: How is the queue implemented in the base-code branch? **
        """
        next_song = self.media_entry_field.text()
        if self.__not_default_entry(next_song):
            print(f"skipping... now playing {next_song}")
        else:
            # Display this message in the window
            print("cannot skip.")
