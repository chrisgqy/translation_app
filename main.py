import sys
import asyncio

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTextEdit,
    QComboBox,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QGraphicsDropShadowEffect,
)

from googletrans import Translator
from languages import LANGUAGES, values


class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()
        self.load_stylesheet("style.qss")   # remove this line if you want inline style only
        self.button_click()
        self.apply_shadow_effects()

    def initUI(self):
        self.input_box = QTextEdit()
        self.output_box = QTextEdit()
        self.reverse = QPushButton("Reverse")
        self.reset = QPushButton("Reset")
        self.submit = QPushButton("Translate Now")
        self.input_option = QComboBox()
        self.output_option = QComboBox()
        self.title = QLabel("PyLate")

        self.input_option.addItems(values)
        self.output_option.addItems(values)

        self.output_box.setReadOnly(True)
        self.input_box.setPlaceholderText("Enter text to translate...")
        self.output_box.setPlaceholderText("Translation will appear here...")

        # object names for styling
        self.setObjectName("mainWindow")
        self.title.setObjectName("titleLabel")
        self.input_box.setObjectName("inputBox")
        self.output_box.setObjectName("outputBox")
        self.input_option.setObjectName("comboBox")
        self.output_option.setObjectName("comboBox")
        self.submit.setObjectName("primaryButton")
        self.reset.setObjectName("secondaryButton")
        self.reverse.setObjectName("secondaryButton")

        self.master = QHBoxLayout()
        self.master.setContentsMargins(24, 24, 24, 24)
        self.master.setSpacing(20)

        col1 = QVBoxLayout()
        col1.setSpacing(14)

        col2 = QVBoxLayout()
        col2.setSpacing(14)

        col1.addWidget(self.title)
        col1.addWidget(self.input_option)
        col1.addWidget(self.output_option)
        col1.addWidget(self.submit)
        col1.addWidget(self.reset)
        col1.addStretch()

        col2.addWidget(self.input_box)
        col2.addWidget(self.reverse)
        col2.addWidget(self.output_box)

        self.master.addLayout(col1, 25)
        self.master.addLayout(col2, 75)

        self.setLayout(self.master)

    def settings(self):
        self.setWindowTitle("PyLate 1.0")
        self.setGeometry(250, 150, 900, 600)

    def load_stylesheet(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print(f"Stylesheet '{filename}' not found. Running without external style.")

    def button_click(self):
        self.submit.clicked.connect(self.translate_click)
        self.reverse.clicked.connect(self.reverse_click)
        self.reset.clicked.connect(self.reset_app)

    def apply_shadow_effects(self):
        self.add_shadow(self.input_box, blur=28, x=0, y=6, color="#04101f")
        self.add_shadow(self.output_box, blur=28, x=0, y=6, color="#04101f")
        self.add_shadow(self.submit, blur=18, x=0, y=4, color="#0a1d36")
        self.add_shadow(self.reset, blur=18, x=0, y=4, color="#0a1d36")
        self.add_shadow(self.reverse, blur=18, x=0, y=4, color="#0a1d36")

    def add_shadow(self, widget, blur=25, x=0, y=6, color="#04101f"):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(blur)
        shadow.setOffset(x, y)
        shadow.setColor(QColor(color))
        widget.setGraphicsEffect(shadow)

    def translate_click(self):
        try:
            text = self.input_box.toPlainText().strip()
            if not text:
                self.input_box.setText("You must enter text to translate here...")
                return

            dest_lang_name = self.output_option.currentText()
            src_lang_name = self.input_option.currentText()

            dest_lang = [k for k, v in LANGUAGES.items() if v == dest_lang_name][0]
            src_lang = [k for k, v in LANGUAGES.items() if v == src_lang_name][0]

            translated_text = asyncio.run(
                self.translate_text(text, dest_lang, src_lang)
            )

            self.output_box.setText(translated_text)

        except Exception as e:
            print("Exception:", e)
            self.input_box.setText("You must enter text to translate here...")

    async def translate_text(self, text, dest_lang, src_lang):
        speaker = Translator()
        translation = await speaker.translate(text, dest=dest_lang, src=src_lang)
        return translation.text

    def reset_app(self):
        self.input_box.clear()
        self.output_box.clear()

    def reverse_click(self):
        s1, l1 = self.input_box.toPlainText(), self.input_option.currentText()
        s2, l2 = self.output_box.toPlainText(), self.output_option.currentText()

        self.input_box.setText(s2)
        self.output_box.setText(s1)

        self.input_option.setCurrentText(l2)
        self.output_option.setCurrentText(l1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Home()
    main.show()
    sys.exit(app.exec_())
