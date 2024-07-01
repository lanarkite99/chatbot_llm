from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 600)

        self.chatbot = Chatbot()

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        self.text_input = QLineEdit(self)
        self.text_input.setGeometry(10, 340, 480, 40)
        self.text_input.returnPressed.connect(self.send_message)

        self.button = QPushButton("Enter", self)
        self.button.setGeometry(500, 340, 50, 30)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.text_input.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.text_input.clear()

        thread = threading.Thread(target=self.get_groq_response, args=(user_input,))
        thread.start()

    def get_groq_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'> Groq: {response}</p>")


app = QApplication(sys.argv)
mainwindow = ChatbotWindow()
sys.exit(app.exec())



