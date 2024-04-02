from os import getcwd
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt, QRectF
from random import randint
from ui.main_window import Ui_MainWindow
from ui.enter_values import Ui_Dialog_enter_values
import csv
import calculating


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    '''MainWindow class'''

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene(self)
        self.graphicsView_grantt_chart.setScene(self.scene)

        self.action_generate_data.triggered.connect(
            self.trigger_actn_gererate_data)
        self.radioButton_metod_johns.toggled.connect(
            lambda: self.pushButton_do.setEnabled(True))
        self.radioButton_metod_petrova_sokolicina.toggled.connect(
            lambda: self.pushButton_do.setEnabled(True))
        self.pushButton_do.clicked.connect(self.gantt_chart)
        self.pushButton_do.clicked.connect(lambda: self.set_results(calculating.calculate
                                                                    (self.get_matrix_from_qtablewidget(self.tableWidget_matrix),
                                                                     self.radioButton_metod_johns, self.radioButton_metod_petrova_sokolicina,
                                                                     self.tableWidget_matrix)))
        self.pushButton_restart.clicked.connect(self.restart)
        self.action_save_data.triggered.connect(self.save_data)

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

    def get_matrix_from_qtablewidget(self, table_widget):
        rows = table_widget.rowCount()
        cols = table_widget.columnCount()
        matrix = []

        for row in range(rows):
            row_data = []
            for col in range(cols):
                item = table_widget.item(row, col)
                if item is not None:
                    row_data.append(int(item.text()))
                else:
                    row_data.append("")
            matrix.append(row_data)

        return matrix

    def set_results(self, res):
        self.label_results.setText(res)
        self.pushButton_restart.setEnabled(True)
        self.action_save_data.setEnabled(True)
        self.action_save_chart.setEnabled(True)

    def gantt_chart(self):
        self.scene.clear()
        calculating.draw_gantt_chart(self.get_matrix_from_qtablewidget(self.tableWidget_matrix),
                                     self.scene, self.graphicsView_grantt_chart)

    def restart(self):
        self.tableWidget_matrix.clear()
        self.pushButton_do.setEnabled(False)
        self.radioButton_metod_johns.setEnabled(False)
        self.radioButton_metod_petrova_sokolicina.setEnabled(False)
        self.pushButton_restart.setEnabled(False)
        self.action_save_data.setEnabled(False)
        self.action_save_chart.setEnabled(False)

    def save_data(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Сохранить файл', '', "Файлы Excel (*.xls)")
        if filename:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter='\t')
                self.add_data(writer)

    def add_data(self, writer):
        for row in range(self.tableWidget_matrix.rowCount()):
            row_data = []
            for col in range(self.tableWidget_matrix.columnCount()):
                try:
                    text = str(self.tableWidget_matrix.item(row, col).text())
                    row_data.append(text)
                except AttributeError:
                    row_data.append("No data")
            writer.writerow(row_data)

        
        

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
            self.main_window.filling_matrix_table(int(self.textEdit_count_details.toPlainText()),
                                                  int(self.textEdit_count_machienes.toPlainText(
                                                  )),
                                                  int(self.textEdit_min.toPlainText()),
                                                  int(self.textEdit_max.toPlainText()))
            self.main_window.radioButton_metod_johns.setEnabled(True)
            self.main_window.radioButton_metod_petrova_sokolicina.setEnabled(
                True)
            self.reject()


def main():
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()


if __name__ == "__main__":
    main()
