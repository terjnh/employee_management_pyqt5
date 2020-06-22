from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from new_employee import EmployeeDialog
from database import Database

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.upperGridLayout = QtWidgets.QGridLayout()
        self.upperGridLayout.setObjectName("upperGridLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.upperGridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(638, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.upperGridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.upperGridLayout, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.idLabel = QtWidgets.QLabel(self.widget)
        self.idLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.idLabel.setObjectName("idLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.idLabel)
        self.idLineEdit = QtWidgets.QLineEdit(self.widget)
        self.idLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idLineEdit)
        self.firstNameLabel = QtWidgets.QLabel(self.widget)
        self.firstNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.firstNameLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastNameLabel = QtWidgets.QLabel(self.widget)
        self.lastNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.lastNameLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.birthdayLabel = QtWidgets.QLabel(self.widget)
        self.birthdayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.birthdayLabel.setObjectName("birthdayLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthdayLabel)
        self.birthdayLineEdit = QtWidgets.QLineEdit(self.widget)
        self.birthdayLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.birthdayLineEdit.setText("")
        self.birthdayLineEdit.setObjectName("birthdayLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.birthdayLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 3, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.departmentLabel = QtWidgets.QLabel(self.widget)
        self.departmentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.departmentLabel.setObjectName("departmentLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.departmentLabel)
        self.departmentLineEdit = QtWidgets.QLineEdit(self.widget)
        self.departmentLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.departmentLineEdit.setObjectName("departmentLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.departmentLineEdit)
        self.salaryLabel = QtWidgets.QLabel(self.widget)
        self.salaryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.salaryLabel.setObjectName("salaryLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.salaryLabel)
        self.salaryLineEdit = QtWidgets.QLineEdit(self.widget)
        self.salaryLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.salaryLineEdit.setObjectName("salaryLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.salaryLineEdit)
        self.positionLabel = QtWidgets.QLabel(self.widget)
        self.positionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.positionLabel.setObjectName("positionLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.positionLabel)
        self.positionLineEdit = QtWidgets.QLineEdit(self.widget)
        self.positionLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.positionLineEdit.setText("")
        self.positionLineEdit.setObjectName("positionLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.positionLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 5, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.applyButton = QtWidgets.QPushButton(self.widget)
        self.applyButton.setObjectName("applyButton")
        self.gridLayout.addWidget(self.applyButton, 0, 1, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.widget)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 6)
        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.bottomGridLayout = QtWidgets.QGridLayout()
        self.bottomGridLayout.setObjectName("bottomGridLayout")
        spacerItem7 = QtWidgets.QSpacerItem(438, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomGridLayout.addItem(spacerItem7, 0, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.bottomGridLayout.addWidget(self.backButton, 0, 1, 1, 1)
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setObjectName("newButton")
        self.bottomGridLayout.addWidget(self.newButton, 0, 2, 1, 1)
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setObjectName("exportButton")
        self.bottomGridLayout.addWidget(self.exportButton, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.bottomGridLayout, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Employees"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.idLabel.setText(_translate("MainWindow", "Id"))
        self.firstNameLabel.setText(_translate("MainWindow", "First Name"))
        self.lastNameLabel.setText(_translate("MainWindow", "Last Name"))
        self.birthdayLabel.setText(_translate("MainWindow", "Birthday"))
        self.departmentLabel.setText(_translate("MainWindow", "Department"))
        self.salaryLabel.setText(_translate("MainWindow", "Salary"))
        self.positionLabel.setText(_translate("MainWindow", "Position"))
        self.applyButton.setText(_translate("MainWindow", "Apply"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.newButton.setText(_translate("MainWindow", "New"))
        self.exportButton.setText(_translate("MainWindow", "Export"))



class EmployeeWindow(QtWidgets.QMainWindow):

    # need to pass 'mainMenu' parameter in. (We need the ability to return to mainmenu)
    def __init__(self, mainMenu):
        super(EmployeeWindow, self).__init__()
        self.mainMenu = mainMenu

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_table()

        self.ui.backButton.clicked.connect(self.back_button_clicked)
        self.ui.newButton.clicked.connect(self.new_button_clicked)


    def init_table(self):
        self.db = Database()
        employee_list = self.db.get_employee_full_info()
        header_list = employee_list[0]
        value_list = employee_list[1]

        no_rows = len(value_list)
        no_columns = len(header_list)

        self.ui.tableWidget.setRowCount(no_rows)
        self.ui.tableWidget.setColumnCount(no_columns)

        self.ui.tableWidget.setHorizontalHeaderLabels(tuple(header_list))
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        # stretch table to fill the tableWidget
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Able to select the whole row
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Hide database internal ID column
        self.ui.tableWidget.verticalHeader().hide()

        #Load data into the table
        for row in range(no_rows):
            for col in range(no_columns):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(value_list[row][col])))


    def back_button_clicked(self):
        self.hide()
        self.mainMenu.show()

    def new_button_clicked(self):
        self.employeeDialog = EmployeeDialog()
        result = self.employeeDialog.exec()
        #exec() will return a value: either accepted or rejected


