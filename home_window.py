import header as h
import results_window as result
import error_window as e


class HomeWindow(h.QWidget):
    """
    Create a main window, where the user can enter a query and YouTube will
    find a corresponding match.
    """

    app_name = "BeatFetch"
    default_message = "Enter a query"

    def __init__(self):
        super().__init__()
        self.__HomePage()

    def __HomePage(self) -> None:
        """
        Contains the Qt objects needed to construct the window and its widgets.
        """
        # Labels:
        self.appName = h.QLabel(self)
        self.appName.setText(f"<h1>{self.app_name}</h1>")

        self.null_space = h.QLabel("\t")

        self.devs_label = h.QLabel(self)
        self.devs_label.setText(
            "<p style=\"font-size:10px\">" + "Developed by " + h.dev_names + "</p>")

        self.error_message = h.QLabel("<b>Invalid query!</b>")

        # Text Fields:
        self.media_entry_field = h.QLineEdit(self.default_message)
        self.media_entry_field.setMinimumWidth(350)
        self.media_entry_field.setMaximumWidth(350)
        self.media_entry_field.selectAll()

        # Buttons:
        self.search_button = h.QPushButton("Search")

        # Layouts:
        h1_layout = h.QHBoxLayout()
        h1_layout.addWidget(self.null_space)
        h1_layout.addWidget(self.media_entry_field)
        h1_layout.addWidget(self.search_button)

        v1_layout = h.QVBoxLayout()
        v1_layout.addWidget(self.appName)
        v1_layout.addLayout(h1_layout)

        v1_layout.addWidget(self.devs_label, alignment=h.Qt.AlignRight)

        v1_layout.addLayout(h1_layout)

        self.search_button.clicked.connect(self.get_results)
        self.setLayout(v1_layout)

    @h.Slot()
    def get_results(self) -> None:
        """
        Close the main window and open a new window, containing the search results.
        If the query is invalid, then an error is displayed.
        """
        query = self.media_entry_field.text()

        if query != "" and query != self.default_message:
            self.close()
            self.results = result.ResultsWindow(query, self.app_name)
            self.results.show()
        else:
            self.error_win = e.ErrorWindow()
            self.error_win.show()
