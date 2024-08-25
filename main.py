import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal
from core.gen_name import generate_name



class Task(QThread):
    progress = pyqtSignal(int)
    # inherit from QThread
    def __init__(self,function):
        super().__init__()
        self.function = function
    def run(self):
        self.progress.emit(0)
        self.progress.emit(25)
        self.function()
        self.progress.emit(100)
        self.finished.emit()

        
# Define your custom classes for each UI file
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/gitai-main.ui', self)  # Load the UI file

        # result display 
        self.result = ''
        # Find the widgets in the UI file
        # buttons
        self.bgname = self.findChild(QtWidgets.QPushButton, 'bgname')
        self.bgrepo = self.findChild(QtWidgets.QPushButton, 'bgrepo')
        self.bgnotes = self.findChild(QtWidgets.QPushButton, 'bgnotes')
        self.bgreadme = self.findChild(QtWidgets.QPushButton, 'bgreadme')
        self.copy = self.findChild(QtWidgets.QPushButton, 'copy')

        # text browser
        self.logger = self.findChild(QtWidgets.QTextBrowser, 'logger')

        # progress bar 
        self.progressBar = self.findChild(QtWidgets.QProgressBar, 'progressBar')
        self.progressBar.setValue(0)
        self.progressBar.setDisabled(True)

        #init buttons with functions
        self.bgname.clicked.connect(self.naming_task)
        self.copy.clicked.connect(self.copy_to_clipboard)
        self.setWindowTitle("GitAI - *file path")

    def gen_name(self):
        result = generate_name()
        self.result = result
        return result
    
    def copy_to_clipboard(self):
        text = self.logger.toPlainText()
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(text)
        QtWidgets.QMessageBox.information(self, "Success", "Copied to clipboard!")
        

    def naming_task(self):
        self.progressBar.setDisabled(False)
        self.thread = Task(self.gen_name)
        self.thread.progress.connect(self.progressBar.setValue)
        self.thread.finished.connect(self.on_task_finished)
        self.thread.start()
        

    def on_task_finished(self):
        self.progressBar.setDisabled(True)
        self.logger.setText(self.result)
        # QtWidgets.QMessageBox.information(self, "Success", "Name generated successfully!")
        


# Main application entry point
def main():
    app = QtWidgets.QApplication(sys.argv)

    # Instantiate the main window
    main_window = MainWindow()  
    # Show the main window
    main_window.show()
    # Execute the application
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
