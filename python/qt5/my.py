import sys
from PyQt5.QtWidgets import  QWidget, QApplication
from ui_mywindow import Ui_mywindow

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mywindow()
        self.ui.setupUi(self)
        self.Lab = 'my new lab'
        self.ui.LabHello.setText(self.Lab)

    def setBtnText(self, aText):
        self.__ui.btnClose.setText(aText)

if  __name__ == "__main__":
   app = QApplication(sys.argv)     #创建app，用QApplication类
   myWidget=QmyWidget()
   myWidget.show()
   myWidget.setBtnText("间接设置")
   sys.exit(app.exec_())






