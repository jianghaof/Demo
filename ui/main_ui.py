from PySide2.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
)
from PySide2.QtCore import Qt

class DashboardUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard Report")
        self.setMinimumSize(900, 500)
        self.init_ui()
        self.setStyleSheet(self.qss())

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # Dashboard Template and output path
        row1 = QHBoxLayout()
        label1 = QLabel("Dashboard Template and output path:")
        self.edit1 = QLineEdit()
        row1.addWidget(label1)
        row1.addWidget(self.edit1)
        main_layout.addLayout(row1)

        # Reference
        row2 = QHBoxLayout()
        label2 = QLabel("Reference:")
        self.edit2 = QLineEdit()
        row2.addWidget(label2)
        row2.addWidget(self.edit2)
        main_layout.addLayout(row2)

        # MIP Input file path
        row3 = QHBoxLayout()
        label3 = QLabel("MIP Input file path:")
        self.edit3 = QLineEdit()
        row3.addWidget(label3)
        row3.addWidget(self.edit3)
        main_layout.addLayout(row3)

        # CMP Input file path
        row4 = QHBoxLayout()
        label4 = QLabel("CMP Input file path:")
        self.edit4 = QLineEdit()
        row4.addWidget(label4)
        row4.addWidget(self.edit4)
        main_layout.addLayout(row4)

        # Button row
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.btn = QPushButton("Run Report")
        btn_row.addWidget(self.btn)
        main_layout.addLayout(btn_row)

        # Messages
        label5 = QLabel("Messages:")
        main_layout.addWidget(label5)
        self.msg_box = QTextEdit()
        self.msg_box.setReadOnly(True)
        main_layout.addWidget(self.msg_box)

    def qss(self):
        return """
        QWidget {
            background: #ededed;
            font-size: 15px;
        }
        QLabel {
            color: #333;
            font-weight: normal;
        }
        QLineEdit {
            background: #fff;
            border: 1px solid #d3d3d3;
            border-radius: 3px;
            padding: 4px;
            font-size: 15px;
        }
        QLineEdit:focus {
            border-bottom: 3px solid #2a7fc1;
        }
        QTextEdit {
            background: #fff;
            border: 1px solid #d3d3d3;
            border-radius: 3px;
            padding: 4px;
            font-size: 15px;
        }
        QPushButton {
            background: #ededed;
            border: 2px solid #2a7fc1;
            border-radius: 4px;
            color: #2a7fc1;
            font-weight: bold;
            min-width: 120px;
            min-height: 32px;
        }
        QPushButton:hover {
            background: #e0f0ff;
        }
        """

if __name__ == "__main__":
    app = QApplication([])
    win = DashboardUI()
    win.show()
    app.exec_()