from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(474, 270)
        Dialog.setMinimumSize(QtCore.QSize(474, 270))
        Dialog.setMaximumSize(QtCore.QSize(474, 270))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Birthday Picker"))
        self.saveButton.setText(_translate("Dialog", "Save"))



class CalendarDialog(QtWidgets.QDialog):

    def __init__(self):
        super(CalendarDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.date = None

        # date will be passed when we press saveButton
        self.ui.saveButton.clicked.connect(self.save_button_clicked)


    def save_button_clicked(self):
        # set date
        self.date = self.ui.calendarWidget.selectedDate()
        self.done(QtWidgets.QDialog.Accepted)







