import header as h
import results_window as result


class HomeWindow(h.QWidget):
    """
    Create a main window, where the user can enter a query and YouTube will
    find a corresponding match.
    """

    # TODO: Name for application.
    app_name = "AppName"

    def __init__(self):
        super().__init__()
        self.__HomePage()

    def __HomePage(self) -> None:
        """
        Contains the Qt objects needed to construct the window and its widgets.
        """
        # Labels:
        self.appName = h.QLabel(self)
        # TODO: Option to create an app logo once we figure out everything else.
        # This is currently at the lowest of priority.
        self.appName.setText(f"<h1>{self.app_name}</h1>")

        self.null_space = h.QLabel("\t")

        self.authors_label = h.QLabel(self)
        self.authors_label.setText(
            "<p style=\"font-size:10px\">" + h.author_names + "</p>")

        # Text Fields:
        self.media_entry_field = h.QLineEdit("Enter a query")
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
        v1_layout.addWidget(self.authors_label, alignment=h.Qt.AlignRight)

        v1_layout.addLayout(h1_layout)

        # TODO: If query is empty or default, then display error.

        self.search_button.clicked.connect(self.get_results)
        self.setLayout(v1_layout)

    @h.Slot()
    def get_results(self) -> None:
        """
        Close the main window and opens a new window, containing the search results.
        """
        self.close()
        query = self.media_entry_field.text()
        self.results = result.ResultsWindow(query, self.app_name)
        self.results.show()
