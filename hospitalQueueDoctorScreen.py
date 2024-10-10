# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hospitalQueueDoctorScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from hospitalQueueScreen import hospitalQueueScreenUiForm
from erasingDataConfirmationWindow import erasingDataConfirmationWindowUiDialog
from datetime import datetime
import mysql.connector as connector
import pandas as pd

class hospitalQueueDoctorScreenUiForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(501, 159)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.docNameLineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(15)
        self.docNameLineEdit.setFont(font)
        self.docNameLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.docNameLineEdit.setObjectName("docNameLineEdit")
        self.verticalLayout.addWidget(self.docNameLineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.clinicNameLineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(15)
        self.clinicNameLineEdit.setFont(font)
        self.clinicNameLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.clinicNameLineEdit.setObjectName("clinicNameLineEdit")
        self.verticalLayout_2.addWidget(self.clinicNameLineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nextPatientPushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(13)
        self.nextPatientPushButton.setFont(font)
        self.nextPatientPushButton.setObjectName("nextPatientPushButton")
        self.horizontalLayout.addWidget(self.nextPatientPushButton)
        self.clearDataPushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(13)
        self.clearDataPushButton.setFont(font)
        self.clearDataPushButton.setObjectName("clearDataPushButton")
        self.horizontalLayout.addWidget(self.clearDataPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.statusLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout_3.addWidget(self.statusLabel)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        
        self.hospitalQueueDatabaseConnection = connector.connect(
            host = "localhost",
            user = "Emirhan Ak",
            password = "Ak004755590*",
            database = "hospitalQueueDatabase"
            )
        
        self.connectionCursor = self.hospitalQueueDatabaseConnection.cursor()
        
        self.nextPatientPushButton.clicked.connect(self.nextPatient)
        self.clearDataPushButton.clicked.connect(self.confirmationWindowPopUp)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def erasePatientInfo(self):
        self.connectionCursor.execute("DELETE FROM patientInfo")
        self.hospitalQueueDatabaseConnection.commit()
        
        self.statusLabel.setText("Veriler temizlendi.")
        self.confirmationWindow.close()
        
    def nextPatient(self):
        try:
            if self.docNameLineEdit.text() == "" or self.clinicNameLineEdit.text() == "":
                raise
            
            hospitalQueueScreenUi.docNameLabel.setText("DT. " + self.docNameLineEdit.text().upper())
            hospitalQueueScreenUi.clinicNameLabel.setText(self.clinicNameLineEdit.text().upper())
            self.calculateDateTime()
            
            getPatientInfoOperation = "SELECT * FROM patientInfo WHERE doctorName = '%s' AND clinicName = '%s'" % (self.docNameLineEdit.text().upper(), self.clinicNameLineEdit.text().upper())
            self.connectionCursor.execute(getPatientInfoOperation)
            self.patientDataFrame = pd.DataFrame(self.connectionCursor.fetchall(), columns = ["patientNo", "patientName", "doctorName", "clinicName"])
            
            self.censoredPatientNames = pd.Series(self.patientDataFrame["patientName"]).copy()
            #print(self.censoredPatientNames)
            i = 0
            for name in self.censoredPatientNames:
                tempString = ""
                for word in name.split():
                    tempString += word[0:2] + "*** "
                self.censoredPatientNames[i] = tempString
                i += 1
            #print(self.censoredPatientNames)
            #hospitalQueueScreenUi.firstPatientLabel.setText(self.censoredPatientNames[0] + " - " + str(self.patientDataFrame["patientNo"][0]))
            try:
                hospitalQueueScreenUi.firstPatientLabel.setText("-")
                hospitalQueueScreenUi.secondPatientLabel.setText("-")
                hospitalQueueScreenUi.thirdPatientLabel.setText("-")
                
                hospitalQueueScreenUi.firstPatientLabel.setText(self.censoredPatientNames[0] + " - " + str(self.patientDataFrame["patientNo"][0]))
                hospitalQueueScreenUi.secondPatientLabel.setText(self.censoredPatientNames[1] + " - " + str(self.patientDataFrame["patientNo"][1]))
                hospitalQueueScreenUi.thirdPatientLabel.setText(self.censoredPatientNames[2] + " - " + str(self.patientDataFrame["patientNo"][2]))
            except:
                pass
            #print(self.patientDataFrame)
            deletePatientInfoOperation = "DELETE FROM patientInfo WHERE patientName = '%s'" % (str(self.patientDataFrame["patientName"][0]))
            self.connectionCursor.execute(deletePatientInfoOperation)
            self.hospitalQueueDatabaseConnection.commit()
            
            self.patientDataFrame = self.patientDataFrame.shift(-1)
            self.patientDataFrame = self.patientDataFrame[:-1]
            
            self.statusLabel.setText("Sıradaki hasta çağırıldı.")
        except:
            self.statusLabel.setText("Bilgileri kontrol edip tekrar deneyin.")
            
    def calculateDateTime(self):
        self.currentDateTime = datetime.now()
        hospitalQueueScreenUi.dateLabel.setText(self.currentDateTime.strftime("%d.%m.%Y"))
        hospitalQueueScreenUi.timeLabel.setText(self.currentDateTime.strftime("%H:%M:%S"))
        
    def confirmationWindowPopUp(self):
        self.confirmationWindow = QtWidgets.QDialog()
        self.confirmationWindowUi = erasingDataConfirmationWindowUiDialog()
        self.confirmationWindowUi.setupUi(self.confirmationWindow)
        self.confirmationWindow.show()
        
        self.confirmationWindowUi.yesPushButton.clicked.connect(self.erasePatientInfo)
        self.confirmationWindowUi.noPushButton.clicked.connect(self.confirmationWindow.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hasta Sırası Kontrol Sistemi Doktor Ekranı"))
        self.label.setText(_translate("Form", "HEKİM ADI"))
        self.label_2.setText(_translate("Form", "BÖLÜM ADI"))
        self.nextPatientPushButton.setText(_translate("Form", "SIRADAKİ HASTA"))
        self.clearDataPushButton.setText(_translate("Form", "VERİLERİ SİL"))
        self.statusLabel.setText(_translate("Form", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    hospitalQueueScreenDoctorForm = QtWidgets.QWidget()
    hospitalQueueScreenForm = QtWidgets.QWidget()
    
    secondMonitor = QtWidgets.QDesktopWidget().screenGeometry(1)
    
    hospitalQueueDoctorScreenUi = hospitalQueueDoctorScreenUiForm()
    hospitalQueueScreenUi = hospitalQueueScreenUiForm()
    
    hospitalQueueDoctorScreenUi.setupUi(hospitalQueueScreenDoctorForm)
    hospitalQueueScreenUi.setupUi(hospitalQueueScreenForm)
    
    hospitalQueueScreenDoctorForm.show()
    hospitalQueueScreenForm.move(secondMonitor.left(), secondMonitor.top())
    #hospitalQueueScreenForm.show()
    hospitalQueueScreenForm.showFullScreen()
    
    sys.exit(app.exec_())
