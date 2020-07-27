import sys
from PyQt5 import QtWidgets
from teleportUI import Ui_MainWindow
from PyQt5.QtCore import QUrl
 
class Main(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
    super(Main, self).__init__(parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    print("test")
  def webPageUpdate(self):
    self.ui.webView.setUrl(QUrl(self.ui.urlEdit.text()))

  def urlLineSet(self):
    self.ui.urlEdit.setText(self.ui.webView.url().url())
 
if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = Main()
  window.show()
  sys.exit(app.exec_())