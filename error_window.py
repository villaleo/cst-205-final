# Created by Leonardo Villalobos
import header as h


class ErrorWindow(h.QWidget):
    """
    Create an error window.
    """
    error_msg = ""

    def __init__(self, error_msg: str):
        super().__init__()
        self.error_msg = error_msg
        self.__show_error_window(self.error_msg)

    def __show_error_window(self, error_msg: str) -> None:
        """
        Displays the window.
        """
        # Labels:
        self.error_label = h.QLabel(error_msg)

        self.null_space = h.QLabel("\t\t")

        # Button:
        self.proceed_button = h.QPushButton("Ok")

        # Layouts:
        message_layout = h.QHBoxLayout()
        message_layout.addWidget(self.null_space)
        message_layout.addWidget(self.error_label)
        message_layout.addWidget(self.null_space)

        button_layout = h.QHBoxLayout()
        button_layout.addWidget(self.null_space)
        button_layout.addWidget(self.proceed_button)
        button_layout.addWidget(self.null_space)

        main_layout = h.QVBoxLayout()
        main_layout.addLayout(message_layout)
        main_layout.addLayout(button_layout)

        self.proceed_button.clicked.connect(self.__close_window)

        self.setWindowTitle("\t\tError\t\t")
        self.setLayout(main_layout)

    @h.Slot()
    def __close_window(self):
        """
        Closes the window.
        """
        self.close()
