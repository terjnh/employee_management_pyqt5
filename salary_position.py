from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from database import Database
from change_salary_dialog import SalaryDialog
from change_position_dialog import PositionDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)
        self.salaryLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.salaryLogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.salaryLogLabel.setObjectName("salaryLogLabel")
        self.gridLayout.addWidget(self.salaryLogLabel, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 2, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 4, 1, 1)
        self.positionLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.positionLogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.positionLogLabel.setObjectName("positionLogLabel")
        self.gridLayout.addWidget(self.positionLogLabel, 0, 5, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 6, 1, 2)
        self.salaryTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.salaryTableWidget.setObjectName("salaryTableWidget")
        self.salaryTableWidget.setColumnCount(0)
        self.salaryTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.salaryTableWidget, 1, 0, 1, 4)
        self.positionTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.positionTableWidget.setObjectName("positionTableWidget")
        self.positionTableWidget.setColumnCount(0)
        self.positionTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.positionTableWidget, 1, 4, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.changeSalaryButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeSalaryButton.setObjectName("changeSalaryButton")
        self.gridLayout.addWidget(self.changeSalaryButton, 2, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 1)
        self.changePositionButton = QtWidgets.QPushButton(self.centralwidget)
        self.changePositionButton.setObjectName("changePositionButton")
        self.gridLayout.addWidget(self.changePositionButton, 2, 5, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 7, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)



        # CSS Styling
        self.centralwidget.setStyleSheet("""
            QWidget#centralwidget {
                background-color: rgb(55, 64, 88);
            }

            QLabel {
                color: white;
                font-size: 12pt;
                font-family: Verdana;
            }

            QPushButton {
                color: white;
                border-radius: 10px;
                padding-left: 10px;
                padding-right: 10px;
                padding-top: 4px;
                padding-bottom: 4px;
                background-color: rgb(90, 90, 90);

            }
        """)




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.salaryLogLabel.setText(_translate("MainWindow", "Salary Log"))
        self.positionLogLabel.setText(_translate("MainWindow", "Position Log"))
        self.changeSalaryButton.setText(_translate("MainWindow", "Change Salary"))
        self.changePositionButton.setText(_translate("MainWindow", "Change Position"))




class EmployeeInfoWindow(QtWidgets.QMainWindow):

    def __init__(self, id):
        super(EmployeeInfoWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id = id
        # print(self.id)

        self.init_tables()

        # connect change salary button to a SLOT
        self.ui.changeSalaryButton.clicked.connect(self.change_salary_button_clicked)
        self.ui.changePositionButton.clicked.connect(self.change_position_button_clicked)


    def init_tables(self):
        self.database = Database()

        result_salary = self.database.get_salary_log_for_employee(self.id)
        result_position = self.database.get_position_log_for_employee(self.id)

        self.init_table(self.ui.salaryTableWidget, result_salary[0], result_salary[1])
        self.init_table(self.ui.positionTableWidget, result_position[0], result_position[1])



    def init_table(self, tableWidget, header_list, values_list):
        no_rows = len(values_list)
        no_columns = len(header_list)

        tableWidget.clear()
        tableWidget.setRowCount(no_rows)
        tableWidget.setColumnCount(no_columns)

        tableWidget.setHorizontalHeaderLabels(tuple(header_list))
        tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        # stretch table to fill the tableWidget
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Able to select the whole row
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Hide database internal ID column
        tableWidget.verticalHeader().hide()

        #Load data into the table
        for row in range(no_rows):
            for col in range(no_columns):
                tableWidget.setItem(row, col, QTableWidgetItem(str(values_list[row][col])))


    def change_salary_button_clicked(self):
        # self.ui.salaryTableWidget.rowCount - 1 : to get the last row of salaryTableWidget
        last_row = self.ui.salaryTableWidget.rowCount() - 1

        # SalaryDialog from change_salary_dialog
        self.salaryDialog = SalaryDialog(self.ui.salaryTableWidget.item(last_row, 0).text(),
            self.ui.salaryTableWidget.item(last_row, 1).text(),
            self.ui.salaryTableWidget.item(last_row, 3).text())

        result = self.salaryDialog.exec()

        # waits for dialog to be accepted
        if result == QtWidgets.QDialog.Accepted:
            # Retrieve informaton from dialog, then update the table accordingly by inserting new row in log_salary
            self.database.insert_new_salary(self.id, self.salaryDialog.new_salary, self.salaryDialog.reason)

            # Re-initialize salary_log table
            print("reinitializing salary_log table")
            self.init_tables()



    def change_position_button_clicked(self):
        last_row = self.ui.positionTableWidget.rowCount() - 1

        self.positionDialog = PositionDialog(self.ui.positionTableWidget.item(last_row, 0).text(),
            self.ui.positionTableWidget.item(last_row, 1).text(),
            self.ui.positionTableWidget.item(last_row, 3).text())

        result = self.positionDialog.exec()

        if result == QtWidgets.QDialog.Accepted:
            self.database.insert_new_position(self.id, self.positionDialog.new_position)

            self.init_tables()




