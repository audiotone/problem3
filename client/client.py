import sys
import uuid
from http import server
import settings
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QPlainTextEdit
from server_connector import ServerConnector

# Settings for local or production server's URL: local = True for local, local = False for production
local = True


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.server = server

        self.setWindowTitle("Program-client")
        self.resize(400, 500)
        self.setLayout(QVBoxLayout())

        # Set start's settings
        self.unique_identifier = 'Default unique identifier'
        self.unique_code = 'Place for unique code'

        # Add label for unique identifier
        self.unique_identifier_view = QLabel(self.unique_identifier)
        self.unique_identifier_view.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.unique_identifier_view)

        # Add button for generating unique identifier
        generate_unique_identifier_button = QPushButton("Generate Unique Identifier", self)
        self.layout().addWidget(generate_unique_identifier_button)
        generate_unique_identifier_button.clicked.connect(self.generate_unique_identifier)

        # Add label for unique code
        self.unique_code_view = QLabel(self.unique_code)
        self.unique_code_view.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.unique_code_view)

        # Add button for receiving unique code from serverapp
        get_unique_code_button = QPushButton("Get Unique Code", self)
        self.layout().addWidget(get_unique_code_button)
        get_unique_code_button.clicked.connect(self.get_unique_code)

        # Add field for writing message
        self.write_message_field = QPlainTextEdit(self)
        self.layout().addWidget(self.write_message_field)

        # Add button for sending message
        send_message_button = QPushButton("Send Message", self)
        self.layout().addWidget(send_message_button)
        send_message_button.clicked.connect(self.send_message)

        # Add status bar
        self.status_bar = QLabel()
        self.layout().addWidget(self.status_bar)
        self.showStatus("Ready to work")

    def showStatus(self, status_message):
        self.status_bar.setText(status_message)

    def generate_unique_identifier(self):
        """
        This method generate unique identifier for client's app
        :return: str
        """
        self.unique_identifier = str(uuid.uuid4())
        self.unique_identifier_view.setText(self.unique_identifier)
        self.unique_identifier_view.setAlignment(Qt.AlignCenter)
        self.showStatus("Generate unique identifier: OK")
        return self.unique_identifier

    def update_unique_identifier_view(self):
        pass

    def get_unique_code(self):
        print(f"Get unique code with parameters: {self.unique_identifier}")
        self.unique_code = connector.get_unique_code(self.unique_identifier)
        self.unique_code_view.setText(self.unique_code)
        print(self.unique_code)

    def send_message(self):
        print("sending message")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # TODO: remove hardcode settings
    if local:
        connector = ServerConnector(settings.URL, settings.PORT, local)
    else:
        connector = ServerConnector(settings.PROD_URL, settings.PROD_PORT, local)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
