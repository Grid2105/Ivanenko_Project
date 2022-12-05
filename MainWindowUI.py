from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 889)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oblastComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.oblastComboBox.setGeometry(QtCore.QRect(30, 90, 381, 47))
        self.oblastComboBox.setStyleSheet("font: 18pt \"Yu Gothic UI\";")
        self.oblastComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.oblastComboBox.setObjectName("oblastComboBox")
        self.listPeople = QtWidgets.QListWidget(self.centralwidget)
        self.listPeople.setGeometry(QtCore.QRect(450, 90, 411, 751))
        self.listPeople.setStyleSheet("font: 14pt \"Verdana\";")
        self.listPeople.setObjectName("listPeople")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(1370, 90, 171, 231))
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap("img/user.png"))
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.description_label = QtWidgets.QTextBrowser(self.centralwidget)
        self.description_label.setGeometry(QtCore.QRect(880, 360, 671, 481))
        self.description_label.setObjectName("description_label")
        self.name_label = QtWidgets.QTextBrowser(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(880, 90, 231, 121))
        self.name_label.setObjectName("name_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1090, 330, 271, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(880, 60, 231, 31))
        self.label_2.setObjectName("label_2")
        self.birthYear_label = QtWidgets.QTextBrowser(self.centralwidget)
        self.birthYear_label.setGeometry(QtCore.QRect(1120, 90, 231, 41))
        self.birthYear_label.setObjectName("birthYear_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1120, 60, 231, 31))
        self.label_3.setObjectName("label_3")
        self.deathYear_label = QtWidgets.QTextBrowser(self.centralwidget)
        self.deathYear_label.setGeometry(QtCore.QRect(1120, 170, 231, 41))
        self.deathYear_label.setObjectName("deathYear_label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1120, 140, 231, 31))
        self.label_4.setObjectName("label_4")
        self.link_label = QtWidgets.QTextBrowser(self.centralwidget)
        self.link_label.setGeometry(QtCore.QRect(880, 250, 471, 71))
        self.link_label.setObjectName("link_label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(540, 60, 231, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(990, 220, 271, 31))
        self.label_6.setObjectName("label_6")
        self.dateEdit_bottom = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_bottom.setGeometry(QtCore.QRect(40, 220, 171, 41))
        self.dateEdit_bottom.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.dateEdit_bottom.setDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_bottom.setObjectName("dateEdit_bottom")
        self.dateEdit_top = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_top.setGeometry(QtCore.QRect(230, 220, 171, 41))
        self.dateEdit_top.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.dateEdit_top.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_top.setObjectName("dateEdit_top")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Довідник українських акторів"))
        self.description_label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.name_label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Загальна інформація</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Ім\'я</span></p></body></html>"))
        self.birthYear_label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Дата народження</span></p></body></html>"))
        self.deathYear_label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Дата смерті</span></p></body></html>"))
        self.link_label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Результат пошуку</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Посилання</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
