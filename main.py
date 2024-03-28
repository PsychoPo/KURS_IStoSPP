from os import getcwd
from PyQt6 import QtWidgets
from random import randint
from ui.main_window import Ui_MainWindow
from ui.enter_values import Ui_Dialog_enter_values

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	'''MainWindow class'''
	def __init__(self):
		super().__init__()

		self.setupUi(self)

		self.action_generate_data.triggered.connect(self.trigger_actn_gererate_data)

	def trigger_actn_gererate_data(self):
		dialog_enter_values = EnterValues(self)
		dialog_enter_values.exec()

	def filling_matrix_table(self, row, column, min, max):

		self.tableWidget_matrix.setRowCount(row)
		self.tableWidget_matrix.setColumnCount(column)

		headers = []

		for i in range(column):
			headers.append(f"Станок {i+1}")
		
		self.tableWidget_matrix.setHorizontalHeaderLabels(headers)

		for row in range(self.tableWidget_matrix.rowCount()):
			for col in range(self.tableWidget_matrix.columnCount()):
				item = QtWidgets.QTableWidgetItem(str(randint(min, max)))
				self.tableWidget_matrix.setItem(row, col, item)

		self.tableWidget_matrix.resizeColumnsToContents()
		self.tableWidget_matrix.resizeRowsToContents()

class EnterValues(QtWidgets.QDialog, Ui_Dialog_enter_values):
	'''Dialog_enter_values class'''
	def __init__(self, main_window):
		super().__init__()
		self.main_window = main_window

		self.setupUi(self)

		self.pushButton_ok.clicked.connect(self.clicked_btn_ok)

	def clicked_btn_ok(self):
		if self.textEdit_count_details.toPlainText() == "":
			self.textEdit_count_details.setPlainText("Введите данные!")
		elif self.textEdit_count_machienes.toPlainText() == "":
			self.textEdit_count_machienes.setPlainText("Введите данные!")
		elif self.textEdit_min.toPlainText() == "":
			self.textEdit_min.setPlainText("Введите данные!")
		elif self.textEdit_max.toPlainText() == "":
			self.textEdit_max.setPlainText("Введите данные!")
		else:
			self.main_window.filling_matrix_table(int(self.textEdit_count_details.toPlainText()), int(self.textEdit_count_machienes.toPlainText()),
			int(self.textEdit_min.toPlainText()), int(self.textEdit_max.toPlainText()))
			self.main_window.radioButton_metod_johns.setEnabled(True)
			self.main_window.radioButton_metod_petrova_sokolicina.setEnabled(True)
			self.main_window.comboBox_variants.setEnabled(True)
			self.reject()

def main():
	app = QtWidgets.QApplication([])
	main_window = MainWindow()
	main_window.show()
	app.exec()

if __name__ == "__main__":
	main()