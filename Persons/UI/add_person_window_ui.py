# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_person_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import Icons_rc

class Ui_d_Person(object):
    def setupUi(self, d_Person):
        if not d_Person.objectName():
            d_Person.setObjectName(u"d_Person")
        d_Person.resize(400, 260)
        font = QFont()
        font.setPointSize(12)
        d_Person.setFont(font)
        icon = QIcon()
        icon.addFile(u":/dollar/dollar.png", QSize(), QIcon.Normal, QIcon.Off)
        d_Person.setWindowIcon(icon)
        self.gridLayout = QGridLayout(d_Person)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Close = QPushButton(d_Person)
        self.pb_Close.setObjectName(u"pb_Close")

        self.gridLayout.addWidget(self.pb_Close, 3, 2, 1, 1)

        self.pb_Submit = QPushButton(d_Person)
        self.pb_Submit.setObjectName(u"pb_Submit")
        self.pb_Submit.setCheckable(False)

        self.gridLayout.addWidget(self.pb_Submit, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 3)

        self.gb_Person = QGroupBox(d_Person)
        self.gb_Person.setObjectName(u"gb_Person")
        self.gb_Person.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.gb_Person)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.gb_Person)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_FirstName = QLineEdit(self.gb_Person)
        self.le_FirstName.setObjectName(u"le_FirstName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_FirstName)

        self.label_2 = QLabel(self.gb_Person)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_LastName = QLineEdit(self.gb_Person)
        self.le_LastName.setObjectName(u"le_LastName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_LastName)


        self.gridLayout.addWidget(self.gb_Person, 0, 0, 1, 3)

        self.lb_Message = QLabel(d_Person)
        self.lb_Message.setObjectName(u"lb_Message")

        self.gridLayout.addWidget(self.lb_Message, 5, 0, 1, 3)


        self.retranslateUi(d_Person)

        QMetaObject.connectSlotsByName(d_Person)
    # setupUi

    def retranslateUi(self, d_Person):
        d_Person.setWindowTitle(QCoreApplication.translate("d_Person", u"Sample Application", None))
        self.pb_Close.setText(QCoreApplication.translate("d_Person", u"Close", None))
        self.pb_Submit.setText(QCoreApplication.translate("d_Person", u"Submit", None))
        self.gb_Person.setTitle(QCoreApplication.translate("d_Person", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("d_Person", u"First Name:", None))
        self.label_2.setText(QCoreApplication.translate("d_Person", u"Last Name:", None))
        self.lb_Message.setText(QCoreApplication.translate("d_Person", u"Message", None))
    # retranslateUi

