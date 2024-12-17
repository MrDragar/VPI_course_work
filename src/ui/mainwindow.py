# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 705)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.add_instrument_button = QPushButton(self.centralwidget)
        self.add_instrument_button.setObjectName(u"add_instrument_button")
        self.add_instrument_button.setGeometry(QRect(10, 20, 161, 51))
        self.list_client_button = QPushButton(self.centralwidget)
        self.list_client_button.setObjectName(u"list_client_button")
        self.list_client_button.setGeometry(QRect(540, 70, 161, 51))
        self.give_tool_button = QPushButton(self.centralwidget)
        self.give_tool_button.setObjectName(u"give_tool_button")
        self.give_tool_button.setGeometry(QRect(10, 210, 161, 51))
        self.accept_tool_button = QPushButton(self.centralwidget)
        self.accept_tool_button.setObjectName(u"accept_tool_button")
        self.accept_tool_button.setGeometry(QRect(10, 270, 161, 51))
        self.instrument_list_button = QPushButton(self.centralwidget)
        self.instrument_list_button.setObjectName(u"instrument_list_button")
        self.instrument_list_button.setGeometry(QRect(10, 80, 161, 51))
        self.employee_list_button = QPushButton(self.centralwidget)
        self.employee_list_button.setObjectName(u"employee_list_button")
        self.employee_list_button.setGeometry(QRect(540, 210, 161, 51))
        self.agreements_button = QPushButton(self.centralwidget)
        self.agreements_button.setObjectName(u"agreements_button")
        self.agreements_button.setGeometry(QRect(10, 330, 161, 51))
        self.add_client_button = QPushButton(self.centralwidget)
        self.add_client_button.setObjectName(u"add_client_button")
        self.add_client_button.setGeometry(QRect(540, 10, 161, 51))
        self.add_employee_button = QPushButton(self.centralwidget)
        self.add_employee_button.setObjectName(u"add_employee_button")
        self.add_employee_button.setGeometry(QRect(540, 270, 161, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 775, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_instrument_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        self.list_client_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.give_tool_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u0442\u044c \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        self.accept_tool_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        self.instrument_list_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.employee_list_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.agreements_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b \u043e\u0431 \u0430\u0440\u0435\u043d\u0434\u0435", None))
        self.add_client_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.add_employee_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
    # retranslateUi

