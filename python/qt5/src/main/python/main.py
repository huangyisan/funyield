from fbs_runtime.application_context.PyQt5 import ApplicationContext
# from PyQt5.QtWidgets import QMainWindow
#
import sys
#
# if __name__ == '__main__':
#     appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
#     window = QMainWindow()
#     window.resize(250, 150)
#     window.show()
#     exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
#     sys.exit(exit_code)


from PyQt5.QtWidgets import *

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

if __name__ == '__main__':
    appctxt = ApplicationContext()

    app = QApplication([])
    button = QPushButton('Click')

    button.clicked.connect(on_button_clicked)
    button.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
