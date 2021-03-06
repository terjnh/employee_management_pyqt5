from PyQt5 import QtCore, QtGui, QtWidgets
from manage_employees import EmployeeWindow
from charts import ChartsWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 327)
        MainWindow.setMinimumSize(QtCore.QSize(250, 300))
        MainWindow.setMaximumSize(QtCore.QSize(350, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 62, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.manageEmployeesButton = QtWidgets.QPushButton(self.centralwidget)
        self.manageEmployeesButton.setMinimumSize(QtCore.QSize(200, 60))
        self.manageEmployeesButton.setObjectName("manageEmployeesButton")
        self.gridLayout.addWidget(self.manageEmployeesButton, 1, 0, 1, 1)
        self.viewChartsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewChartsButton.setMinimumSize(QtCore.QSize(200, 60))
        self.viewChartsButton.setObjectName("viewChartsButton")
        self.gridLayout.addWidget(self.viewChartsButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 61, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.centralwidget.setStyleSheet("""
            QWidget#centralwidget {
                background-color: rgb(55, 64, 88);
            }

            QLabel {
                color: white;
                font-size: 8pt;
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Menu"))
        self.manageEmployeesButton.setText(_translate("MainWindow", "Manage Employees"))
        self.viewChartsButton.setText(_translate("MainWindow", "View Charts"))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # instantiating ui item
        # self.ui to access items from the Ui_MainWindow class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.manageEmployeesButton.clicked.connect(self.manage_employees_button_clicked)
        self.ui.viewChartsButton.clicked.connect(self.view_charts_button_clicked)


    def manage_employees_button_clicked(self):
        self.hide()   # hide current window
        self.employeeWindow = EmployeeWindow(self)  # ** Need to pass in self into EmployeeWindow as required by EmployeeWindow class (manage_employees.py)
        self.employeeWindow.show()

    def view_charts_button_clicked(self):
        self.hide()
        self.chartsWindow = ChartsWindow(self)
        self.chartsWindow.show()


