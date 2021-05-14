import header as h
import api_backend as yt
import trim as t


def call_getSong(query: str) -> dict:
    """
    Calls the `getSong()` function from the api_backend.py file.
    Returns a `dict` with the `title` and `thumbnail` of `query`.

    + `query` : The user's input which will be sent to YouTube.
    """
    yt.searchq = query

    image_url = yt.getSong()['thumbnail']
    image_data = h.urllib.request.urlopen(image_url).read()

    img = h.PySide6.QtGui.QImage()
    img.loadFromData(image_data)

    return {
        "title": yt.getSong()['title'],
        "thumbnail": img
    }


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
    media_entry_field: h.QLineEdit
    current_media_values: dict
    song: None

    def __init__(self, query: str, app_name: str):
        super().__init__()
        self.media_entry_field = h.QLineEdit(self.default_media_entry)
        self.current_media_values = call_getSong(query)
        self.__SearchResultsWindow(query, app_name)

    def __search(self, query: str, call_func=False) -> dict:
        """
        Calls the `getSong()` function only if `call_func` is `True`.
        Returns a `dict` with the `title` and `thumbnail` of `query`.

        + `query` : The user's input which will be sent to YouTube.
        + `call_func` : Option to call `getSong()`. `False` by default. 
        """
        out = self.current_media_values

        if call_func:
            out = call_getSong(query)
        return out

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

        self.next_song = h.QLabel(self)
        self.next_song.setText("TEST")
        # TODO: Set the next_song label to appear if queued.
        # NOTE: Label is currently a sample

        # Text Fields:
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
        H_null_layout = h.QHBoxLayout()
        H_null_layout.addWidget(self.null_space)
        H_null_layout.addWidget(self.null_space)
        H_null_layout.addWidget(self.null_space)

        # Layout: control space -> layouts:
        # Source: https://stackoverflow.com/questions/41405251/how-can-i-align-a-button-at-the-bottom-right-in-pyqt
        control_layout = h.QHBoxLayout()
        control_layout.addWidget(
            self.pause_button, alignment=h.Qt.AlignHorizontal_Mask)
        control_layout.addWidget(
            self.play_button, alignment=h.Qt.AlignBaseline)
        control_layout.addWidget(
            self.next_button, alignment=h.Qt.AlignLeft)

        # Layout: queue space -> layouts:
        queue_layout = h.QVBoxLayout()
        queue_layout.addWidget(self.null_space)
        queue_layout.addWidget(self.up_next_label)
        queue_layout.addWidget(self.next_song)
        queue_layout.addWidget(self.null_space)
        queue_layout.addWidget(self.null_space)
        queue_layout.addWidget(self.null_space)

        # Layout: media space -> layouts:
        media_layout = h.QHBoxLayout()
        media_layout.addWidget(self.media_thumbnail)
        media_layout.addLayout(queue_layout)

        # Layout: main space -> layouts:
        main_layout = h.QVBoxLayout()
        main_layout.addLayout(search_line_layout)

        main_layout.addWidget(self.null_space)
        main_layout.addWidget(self.media_title_label)
        main_layout.addLayout(media_layout)
        main_layout.addLayout(H_null_layout)
        main_layout.addLayout(control_layout)

        # Signal Slot Connection: buttons -> functions:
        self.search_button.clicked.connect(self.__queue_song)
        self.play_button.clicked.connect(self.__play)
        self.pause_button.clicked.connect(self.__pause)
        self.next_button.clicked.connect(self.__skip)

        # Play the music automatically when window loads:
        self.song = yt.playFirst()
        self.__play()

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
        TODO: There is currently no 'queue'. The media that is played is whatever
              is in the search field at the time. **
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
        Plays the current song.
        """
        self.song.play()
        print("playing.")

    @h.Slot()
    def __pause(self) -> None:
        """
        Pauses the current song.
        """
        self.song.pause()
        print("paused.")

    @h.Slot()
    def __skip(self) -> None:
        """
        TODO: How is the queue implemented in the base-code branch? **
        TODO: When do we know that there are no songs left to skip to? **
        TODO: How will all the buttons and thumbnail be updated? **
        """
        next_song = self.media_entry_field.text()
        if self.__not_default_entry(next_song):
            print(f"skipping... now playing {next_song}")
        else:
            # Display this message in the window
            print("cannot skip.")
