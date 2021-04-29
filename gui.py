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

    """

    def __init__(self, query, app_name):
        super().__init__()
        self.__SearchResultsWindow(query, app_name)

    def search(self, query):
        """

        """
        # TODO: Connect API media search **
        pass

    def __SearchResultsWindow(self, query, app_name) -> None:
        self.appName = QLabel(self)
        self.null_space = QLabel("\t")
        self.media_entry_field = QLineEdit(f"{query}")
        self.search_button = QPushButton("Search")

        self.appName.setText(f"<h1>{app_name}</h1>")

        self.media_entry_field.setMinimumWidth(350)
        self.media_entry_field.setMaximumWidth(350)

        h1_layout = QHBoxLayout()
        h1_layout.addWidget(self.appName)
        h1_layout.addWidget(self.media_entry_field)
        h1_layout.addWidget(self.search_button)

        v1_layout = QVBoxLayout()
        v1_layout.addLayout(h1_layout)

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
