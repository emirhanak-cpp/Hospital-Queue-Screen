# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hospitalQueueScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class hospitalQueueScreenUiForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1019, 407)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.dateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.horizontalLayout.addWidget(self.dateLabel)
        self.clinicNameLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.clinicNameLabel.setFont(font)
        self.clinicNameLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.clinicNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.clinicNameLabel.setObjectName("clinicNameLabel")
        self.horizontalLayout.addWidget(self.clinicNameLabel)
        self.timeLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.docNameLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(30)
        self.docNameLabel.setFont(font)
        self.docNameLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 194, 194);")
        self.docNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.docNameLabel.setObjectName("docNameLabel")
        self.verticalLayout.addWidget(self.docNameLabel)
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.firstPatientLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(30)
        self.firstPatientLabel.setFont(font)
        self.firstPatientLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 194, 194);")
        self.firstPatientLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.firstPatientLabel.setObjectName("firstPatientLabel")
        self.verticalLayout.addWidget(self.firstPatientLabel)
        self.secondPatientLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(30)
        self.secondPatientLabel.setFont(font)
        self.secondPatientLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 194, 194);")
        self.secondPatientLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.secondPatientLabel.setObjectName("secondPatientLabel")
        self.verticalLayout.addWidget(self.secondPatientLabel)
        self.thirdPatientLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(30)
        self.thirdPatientLabel.setFont(font)
        self.thirdPatientLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 194, 194);")
        self.thirdPatientLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.thirdPatientLabel.setObjectName("thirdPatientLabel")
        self.verticalLayout.addWidget(self.thirdPatientLabel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hastane Sıra Kontrol Sistemi"))
        self.dateLabel.setText(_translate("Form", "TARİH"))
        self.clinicNameLabel.setText(_translate("Form", "BÖLÜM ADI"))
        self.timeLabel.setText(_translate("Form", "SAAT"))
        self.label.setText(_translate("Form", "HEKİM ADI"))
        self.docNameLabel.setText(_translate("Form", "-"))
        self.label_6.setText(_translate("Form", "SIRADAKİ HASTALAR"))
        self.firstPatientLabel.setText(_translate("Form", "-"))
        self.secondPatientLabel.setText(_translate("Form", "-"))
        self.thirdPatientLabel.setText(_translate("Form", "-"))
