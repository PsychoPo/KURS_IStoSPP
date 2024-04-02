# Form implementation generated from reading ui file '.\ui\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1476, 875)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Liberation Serif;")
        self.centralwidget_main = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget_main.setStyleSheet("")
        self.centralwidget_main.setObjectName("centralwidget_main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget_main)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_matrix = QtWidgets.QVBoxLayout()
        self.verticalLayout_matrix.setObjectName("verticalLayout_matrix")
        self.verticalLayout_metods = QtWidgets.QVBoxLayout()
        self.verticalLayout_metods.setObjectName("verticalLayout_metods")
        self.label_choose_metod = QtWidgets.QLabel(parent=self.centralwidget_main)
        self.label_choose_metod.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.label_choose_metod.setObjectName("label_choose_metod")
        self.verticalLayout_metods.addWidget(self.label_choose_metod)
        self.radioButton_metod_johns = QtWidgets.QRadioButton(parent=self.centralwidget_main)
        self.radioButton_metod_johns.setEnabled(False)
        self.radioButton_metod_johns.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.radioButton_metod_johns.setObjectName("radioButton_metod_johns")
        self.verticalLayout_metods.addWidget(self.radioButton_metod_johns)
        self.radioButton_metod_petrova_sokolicina = QtWidgets.QRadioButton(parent=self.centralwidget_main)
        self.radioButton_metod_petrova_sokolicina.setEnabled(False)
        self.radioButton_metod_petrova_sokolicina.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.radioButton_metod_petrova_sokolicina.setObjectName("radioButton_metod_petrova_sokolicina")
        self.verticalLayout_metods.addWidget(self.radioButton_metod_petrova_sokolicina)
        self.pushButton_do = QtWidgets.QPushButton(parent=self.centralwidget_main)
        self.pushButton_do.setEnabled(False)
        self.pushButton_do.setStyleSheet("QPushButton {\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"text-align: center;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pushButton_do.setObjectName("pushButton_do")
        self.verticalLayout_metods.addWidget(self.pushButton_do)
        self.tableWidget_matrix = QtWidgets.QTableWidget(parent=self.centralwidget_main)
        self.tableWidget_matrix.setStyleSheet("QTableWidget{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"   background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"}")
        self.tableWidget_matrix.setObjectName("tableWidget_matrix")
        self.tableWidget_matrix.setColumnCount(0)
        self.tableWidget_matrix.setRowCount(0)
        self.verticalLayout_metods.addWidget(self.tableWidget_matrix)
        self.verticalLayout_matrix.addLayout(self.verticalLayout_metods)
        self.horizontalLayout.addLayout(self.verticalLayout_matrix)
        self.verticalLayout_results = QtWidgets.QVBoxLayout()
        self.verticalLayout_results.setObjectName("verticalLayout_results")
        self.label_results = QtWidgets.QLabel(parent=self.centralwidget_main)
        self.label_results.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.label_results.setObjectName("label_results")
        self.verticalLayout_results.addWidget(self.label_results)
        self.pushButton_restart = QtWidgets.QPushButton(parent=self.centralwidget_main)
        self.pushButton_restart.setEnabled(False)
        self.pushButton_restart.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.pushButton_restart.setTabletTracking(True)
        self.pushButton_restart.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.pushButton_restart.setStyleSheet("QPushButton {\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"text-align: center;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pushButton_restart.setObjectName("pushButton_restart")
        self.verticalLayout_results.addWidget(self.pushButton_restart)
        self.graphicsView_grantt_chart = QtWidgets.QGraphicsView(parent=self.centralwidget_main)
        self.graphicsView_grantt_chart.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.graphicsView_grantt_chart.setObjectName("graphicsView_grantt_chart")
        self.verticalLayout_results.addWidget(self.graphicsView_grantt_chart)
        self.horizontalLayout.addLayout(self.verticalLayout_results)
        MainWindow.setCentralWidget(self.centralwidget_main)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1476, 25))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(12)
        font.setItalic(False)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(parent=self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_data = QtWidgets.QMenu(parent=self.menubar)
        self.menu_data.setObjectName("menu_data")
        MainWindow.setMenuBar(self.menubar)
        self.action_save_data = QtGui.QAction(parent=MainWindow)
        self.action_save_data.setEnabled(False)
        self.action_save_data.setObjectName("action_save_data")
        self.action_save_chart = QtGui.QAction(parent=MainWindow)
        self.action_save_chart.setEnabled(False)
        self.action_save_chart.setObjectName("action_save_chart")
        self.action_generate_data = QtGui.QAction(parent=MainWindow)
        self.action_generate_data.setObjectName("action_generate_data")
        self.menu_file.addAction(self.action_save_data)
        self.menu_data.addAction(self.action_generate_data)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_data.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное окно"))
        self.label_choose_metod.setText(_translate("MainWindow", "Выберите метод и вариант"))
        self.radioButton_metod_johns.setText(_translate("MainWindow", "Метод Джонсона"))
        self.radioButton_metod_petrova_sokolicina.setText(_translate("MainWindow", "Метод Петрова-Соколицына"))
        self.pushButton_do.setText(_translate("MainWindow", "Рассчитать"))
        self.label_results.setText(_translate("MainWindow", "Здесь будут ваши результаты"))
        self.pushButton_restart.setText(_translate("MainWindow", "Сбросить"))
        self.menu_file.setTitle(_translate("MainWindow", "Файл"))
        self.menu_data.setTitle(_translate("MainWindow", "Данные"))
        self.action_save_data.setText(_translate("MainWindow", "Сохранить данные"))
        self.action_save_chart.setText(_translate("MainWindow", "Сохранить диаграмму"))
        self.action_generate_data.setText(_translate("MainWindow", "Генерация случайных данных"))
