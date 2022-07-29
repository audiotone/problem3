import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QPlainTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program-client")
        self.resize(400,500)
        self.setLayout(QVBoxLayout())

        # Add button for generating unique identifier
        self.generate_unique_identifier_button = QPushButton("Generate Unique Identifier", self)
        self.layout().addWidget(self.generate_unique_identifier_button)
        self.generate_unique_identifier_button.clicked.connect(self.generate_unique_identifier)

        # Add button for receiving unique code from serverapp
        self.receive_unique_code_button = QPushButton("Receive Unique Code", self)
        self.layout().addWidget(self.receive_unique_code_button)
        self.receive_unique_code_button.clicked.connect(self.receive_unique_code)

        # Add field for writing message
        self.write_message_field = QPlainTextEdit(self)
        self.layout().addWidget(self.write_message_field)

        # Add button for sending message
        self.send_message_button = QPushButton("Send Message", self)
        self.layout().addWidget(self.send_message_button)
        self.send_message_button.clicked.connect(self.send_message)

        # Add status bar
        self.status_bar = QLabel()
        self.layout().addWidget(self.status_bar)

        self.showStatus("Ready to work")

    def showStatus(self, status_message):
        self.status_bar.setText(status_message)

    def generate_unique_identifier(self):
        print("generating unique identifier")

    def receive_unique_code(self):
        print("receiving unique code")

    def send_message(self):
        print("sending message")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())