# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabla_impactos.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg_impactos(object):
    def setupUi(self, dlg_impactos):
        dlg_impactos.setObjectName("dlg_impactos")
        dlg_impactos.resize(400, 300)
        self.tbl_impactos = QtWidgets.QTableWidget(dlg_impactos)
        self.tbl_impactos.setGeometry(QtCore.QRect(20, 20, 361, 261))
        self.tbl_impactos.setAlternatingRowColors(True)
        self.tbl_impactos.setObjectName("tbl_impactos")
        self.tbl_impactos.setColumnCount(3)
        self.tbl_impactos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_impactos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_impactos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_impactos.setHorizontalHeaderItem(2, item)

        self.retranslateUi(dlg_impactos)
        QtCore.QMetaObject.connectSlotsByName(dlg_impactos)

    def retranslateUi(self, dlg_impactos):
        _translate = QtCore.QCoreApplication.translate
        dlg_impactos.setWindowTitle(_translate("dlg_impactos", "Tabla de impactos"))
        item = self.tbl_impactos.horizontalHeaderItem(0)
        item.setText(_translate("dlg_impactos", "Proyecto"))
        item = self.tbl_impactos.horizontalHeaderItem(1)
        item.setText(_translate("dlg_impactos", "Tipo"))
        item = self.tbl_impactos.horizontalHeaderItem(2)
        item.setText(_translate("dlg_impactos", "Distancia"))

