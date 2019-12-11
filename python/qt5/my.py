import sys
from PyQt5.QtWidgets import  QWidget, QApplication,QMainWindow
from ui_form import Ui_Form
import datetime

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Lab = 'my new lab'
        # self.ui.LabHello.setText(self.Lab)
        self.ui.label.setText(self.Lab)
        self.ui.pushButton.clicked.connect(self.clicked)

    def setBtnText(self, aText):
        self.ui.label.setText(aText)

    def clicked(self):
        self.ui.label.setText(self.get_now_date())

    @staticmethod
    def get_now_date():
        return str(datetime.datetime.now())

if  __name__ == "__main__":
   app = QApplication(sys.argv)     #创建app，用QApplication类
   myWidget=QmyWidget()
   myWidget.show()
   myWidget.setBtnText("点击显示时间")
   sys.exit(app.exec_())






