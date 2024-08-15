from func2 import caesar
from PyQt5 import QtWidgets
from form import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setGeometry(800, 600, 1600, 1200)
        self.ui.pushButton.clicked.connect(self.func)
        self.ui.pushButton_2.clicked.connect(self.func2)
    
    def func(self):
        try:
            string = self.ui.plainTextEdit.toPlainText()
            if string == "":
                self.ui.plainTextEdit_2.setPlainText("Ошибка! Введите текст!")
                return
            key = self.ui.spinBox.value()
            key = int(key)
            if key == 0:
                self.ui.plainTextEdit_2.setPlainText("Ошибка! Введите ключ!")
                return
            result = caesar(string, key , 1)
            self.ui.plainTextEdit_2.setPlainText(result)
        except Exception as exp:
            print(str(exp))

    def func2(self):
        try:
            string = self.ui.plainTextEdit.toPlainText()
            if string == "":
                self.ui.plainTextEdit_2.setPlainText("Ошибка! Введите текст!")
                return
            key = self.ui.spinBox.value()
            key = int(key)
            if key == 0:
                self.ui.plainTextEdit_2.setPlainText("Ошибка! Введите ключ!")
                return
            result = caesar(string, key , -1)
            self.ui.plainTextEdit_2.setPlainText(result)
        except Exception as exp:
            print(str(exp))


 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())