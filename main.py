from os import getcwd
from PyQt6 import QtWidgets
from ui.main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	'''MainWindow class'''
	def __init__(self):
		super().__init__()

		self.setupUi(self)

def main():
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec()

if __name__ == "__main__":
	main()