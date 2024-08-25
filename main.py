import sys
from PyQt5 import QtWidgets, uic

# Define your custom classes for each UI file
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/gitai-main.ui', self)  # Load the UI file
        # Additional initialization code here

# Main application entry point
def main():
    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()  # Instantiate the main window
    # Show the main window
    main_window.show()

    # Execute the application
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
