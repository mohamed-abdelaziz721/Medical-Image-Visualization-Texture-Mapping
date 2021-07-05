# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 370)
        MainWindow.setMinimumSize(QtCore.QSize(720, 370))
        MainWindow.setMaximumSize(QtCore.QSize(720, 375))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.rendering_technique = QtWidgets.QComboBox(self.centralwidget)
        self.rendering_technique.setObjectName("rendering_technique")
        self.rendering_technique.addItem("")
        self.rendering_technique.addItem("")
        self.verticalLayout_12.addWidget(self.rendering_technique)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(701, 71))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.iso_defaults = QtWidgets.QPushButton(self.groupBox)
        self.iso_defaults.setObjectName("iso_defaults")
        self.horizontalLayout.addWidget(self.iso_defaults)
        self.iso_value = QtWidgets.QSlider(self.groupBox)
        self.iso_value.setMaximum(2500)
        self.iso_value.setProperty("value", 500)
        self.iso_value.setOrientation(QtCore.Qt.Horizontal)
        self.iso_value.setObjectName("iso_value")
        self.horizontalLayout.addWidget(self.iso_value)
        self.iso_label = QtWidgets.QLabel(self.groupBox)
        self.iso_label.setObjectName("iso_label")
        self.horizontalLayout.addWidget(self.iso_label)
        self.verticalLayout_12.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout_11.addWidget(self.label_24, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.skin_red = QtWidgets.QSlider(self.groupBox_2)
        self.skin_red.setMaximum(100)
        self.skin_red.setProperty("value", 0)
        self.skin_red.setOrientation(QtCore.Qt.Horizontal)
        self.skin_red.setObjectName("skin_red")
        self.gridLayout_3.addWidget(self.skin_red, 0, 0, 1, 1)
        self.skin_red_label = QtWidgets.QLabel(self.groupBox_2)
        self.skin_red_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skin_red_label.setObjectName("skin_red_label")
        self.gridLayout_3.addWidget(self.skin_red_label, 0, 1, 1, 1)
        self.muscle_red = QtWidgets.QSlider(self.groupBox_2)
        self.muscle_red.setMaximum(100)
        self.muscle_red.setProperty("value", 100)
        self.muscle_red.setOrientation(QtCore.Qt.Horizontal)
        self.muscle_red.setObjectName("muscle_red")
        self.gridLayout_3.addWidget(self.muscle_red, 1, 0, 1, 1)
        self.muscle_red_label = QtWidgets.QLabel(self.groupBox_2)
        self.muscle_red_label.setAlignment(QtCore.Qt.AlignCenter)
        self.muscle_red_label.setObjectName("muscle_red_label")
        self.gridLayout_3.addWidget(self.muscle_red_label, 1, 1, 1, 1)
        self.bones_red = QtWidgets.QSlider(self.groupBox_2)
        self.bones_red.setMaximum(100)
        self.bones_red.setProperty("value", 100)
        self.bones_red.setOrientation(QtCore.Qt.Horizontal)
        self.bones_red.setObjectName("bones_red")
        self.gridLayout_3.addWidget(self.bones_red, 2, 0, 1, 1)
        self.bones_red_label = QtWidgets.QLabel(self.groupBox_2)
        self.bones_red_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bones_red_label.setObjectName("bones_red_label")
        self.gridLayout_3.addWidget(self.bones_red_label, 2, 1, 1, 1)
        self.deep_bones_red = QtWidgets.QSlider(self.groupBox_2)
        self.deep_bones_red.setMaximum(100)
        self.deep_bones_red.setProperty("value", 100)
        self.deep_bones_red.setOrientation(QtCore.Qt.Horizontal)
        self.deep_bones_red.setObjectName("deep_bones_red")
        self.gridLayout_3.addWidget(self.deep_bones_red, 3, 0, 1, 1)
        self.deep_bones_red_label = QtWidgets.QLabel(self.groupBox_2)
        self.deep_bones_red_label.setAlignment(QtCore.Qt.AlignCenter)
        self.deep_bones_red_label.setObjectName("deep_bones_red_label")
        self.gridLayout_3.addWidget(self.deep_bones_red_label, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.skin_green = QtWidgets.QSlider(self.groupBox_2)
        self.skin_green.setMaximum(100)
        self.skin_green.setProperty("value", 0)
        self.skin_green.setOrientation(QtCore.Qt.Horizontal)
        self.skin_green.setObjectName("skin_green")
        self.gridLayout_2.addWidget(self.skin_green, 0, 0, 1, 1)
        self.skin_green_label = QtWidgets.QLabel(self.groupBox_2)
        self.skin_green_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skin_green_label.setObjectName("skin_green_label")
        self.gridLayout_2.addWidget(self.skin_green_label, 0, 1, 1, 1)
        self.muscle_green = QtWidgets.QSlider(self.groupBox_2)
        self.muscle_green.setMaximum(100)
        self.muscle_green.setProperty("value", 50)
        self.muscle_green.setOrientation(QtCore.Qt.Horizontal)
        self.muscle_green.setObjectName("muscle_green")
        self.gridLayout_2.addWidget(self.muscle_green, 1, 0, 1, 1)
        self.muscle_green_label = QtWidgets.QLabel(self.groupBox_2)
        self.muscle_green_label.setAlignment(QtCore.Qt.AlignCenter)
        self.muscle_green_label.setObjectName("muscle_green_label")
        self.gridLayout_2.addWidget(self.muscle_green_label, 1, 1, 1, 1)
        self.bones_green = QtWidgets.QSlider(self.groupBox_2)
        self.bones_green.setMaximum(100)
        self.bones_green.setProperty("value", 50)
        self.bones_green.setOrientation(QtCore.Qt.Horizontal)
        self.bones_green.setObjectName("bones_green")
        self.gridLayout_2.addWidget(self.bones_green, 2, 0, 1, 1)
        self.bones_green_label = QtWidgets.QLabel(self.groupBox_2)
        self.bones_green_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bones_green_label.setObjectName("bones_green_label")
        self.gridLayout_2.addWidget(self.bones_green_label, 2, 1, 1, 1)
        self.deep_bones_green = QtWidgets.QSlider(self.groupBox_2)
        self.deep_bones_green.setMaximum(100)
        self.deep_bones_green.setProperty("value", 100)
        self.deep_bones_green.setOrientation(QtCore.Qt.Horizontal)
        self.deep_bones_green.setObjectName("deep_bones_green")
        self.gridLayout_2.addWidget(self.deep_bones_green, 3, 0, 1, 1)
        self.deep_bones_green_label = QtWidgets.QLabel(self.groupBox_2)
        self.deep_bones_green_label.setAlignment(QtCore.Qt.AlignCenter)
        self.deep_bones_green_label.setObjectName("deep_bones_green_label")
        self.gridLayout_2.addWidget(self.deep_bones_green_label, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.skin_blue = QtWidgets.QSlider(self.groupBox_2)
        self.skin_blue.setMaximum(100)
        self.skin_blue.setProperty("value", 0)
        self.skin_blue.setOrientation(QtCore.Qt.Horizontal)
        self.skin_blue.setObjectName("skin_blue")
        self.gridLayout.addWidget(self.skin_blue, 0, 0, 1, 1)
        self.skin_blue_label = QtWidgets.QLabel(self.groupBox_2)
        self.skin_blue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skin_blue_label.setObjectName("skin_blue_label")
        self.gridLayout.addWidget(self.skin_blue_label, 0, 1, 1, 1)
        self.muscle_blue = QtWidgets.QSlider(self.groupBox_2)
        self.muscle_blue.setMaximum(100)
        self.muscle_blue.setProperty("value", 30)
        self.muscle_blue.setOrientation(QtCore.Qt.Horizontal)
        self.muscle_blue.setObjectName("muscle_blue")
        self.gridLayout.addWidget(self.muscle_blue, 1, 0, 1, 1)
        self.muscle_blue_label = QtWidgets.QLabel(self.groupBox_2)
        self.muscle_blue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.muscle_blue_label.setObjectName("muscle_blue_label")
        self.gridLayout.addWidget(self.muscle_blue_label, 1, 1, 1, 1)
        self.bones_blue = QtWidgets.QSlider(self.groupBox_2)
        self.bones_blue.setMaximum(100)
        self.bones_blue.setProperty("value", 30)
        self.bones_blue.setOrientation(QtCore.Qt.Horizontal)
        self.bones_blue.setObjectName("bones_blue")
        self.gridLayout.addWidget(self.bones_blue, 2, 0, 1, 1)
        self.bones_blue_label = QtWidgets.QLabel(self.groupBox_2)
        self.bones_blue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bones_blue_label.setObjectName("bones_blue_label")
        self.gridLayout.addWidget(self.bones_blue_label, 2, 1, 1, 1)
        self.deep_bones_blue = QtWidgets.QSlider(self.groupBox_2)
        self.deep_bones_blue.setMaximum(100)
        self.deep_bones_blue.setProperty("value", 90)
        self.deep_bones_blue.setOrientation(QtCore.Qt.Horizontal)
        self.deep_bones_blue.setObjectName("deep_bones_blue")
        self.gridLayout.addWidget(self.deep_bones_blue, 3, 0, 1, 1)
        self.deep_bones_blue_label = QtWidgets.QLabel(self.groupBox_2)
        self.deep_bones_blue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.deep_bones_blue_label.setObjectName("deep_bones_blue_label")
        self.gridLayout.addWidget(self.deep_bones_blue_label, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_10.addWidget(self.label_31)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.skin_opacity = QtWidgets.QSlider(self.groupBox_2)
        self.skin_opacity.setMaximum(100)
        self.skin_opacity.setProperty("value", 15)
        self.skin_opacity.setOrientation(QtCore.Qt.Horizontal)
        self.skin_opacity.setObjectName("skin_opacity")
        self.gridLayout_10.addWidget(self.skin_opacity, 0, 0, 1, 1)
        self.skin_opacity_label = QtWidgets.QLabel(self.groupBox_2)
        self.skin_opacity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skin_opacity_label.setObjectName("skin_opacity_label")
        self.gridLayout_10.addWidget(self.skin_opacity_label, 0, 1, 1, 1)
        self.muscle_opacity = QtWidgets.QSlider(self.groupBox_2)
        self.muscle_opacity.setMaximum(100)
        self.muscle_opacity.setProperty("value", 30)
        self.muscle_opacity.setOrientation(QtCore.Qt.Horizontal)
        self.muscle_opacity.setObjectName("muscle_opacity")
        self.gridLayout_10.addWidget(self.muscle_opacity, 1, 0, 1, 1)
        self.muscle_opacity_label = QtWidgets.QLabel(self.groupBox_2)
        self.muscle_opacity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.muscle_opacity_label.setObjectName("muscle_opacity_label")
        self.gridLayout_10.addWidget(self.muscle_opacity_label, 1, 1, 1, 1)
        self.bone_opacity = QtWidgets.QSlider(self.groupBox_2)
        self.bone_opacity.setMaximum(100)
        self.bone_opacity.setProperty("value", 45)
        self.bone_opacity.setOrientation(QtCore.Qt.Horizontal)
        self.bone_opacity.setObjectName("bone_opacity")
        self.gridLayout_10.addWidget(self.bone_opacity, 2, 0, 1, 1)
        self.bones_opacity_label = QtWidgets.QLabel(self.groupBox_2)
        self.bones_opacity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bones_opacity_label.setObjectName("bones_opacity_label")
        self.gridLayout_10.addWidget(self.bones_opacity_label, 2, 1, 1, 1)
        self.deep_bone_opacity = QtWidgets.QSlider(self.groupBox_2)
        self.deep_bone_opacity.setMaximum(100)
        self.deep_bone_opacity.setProperty("value", 60)
        self.deep_bone_opacity.setOrientation(QtCore.Qt.Horizontal)
        self.deep_bone_opacity.setObjectName("deep_bone_opacity")
        self.gridLayout_10.addWidget(self.deep_bone_opacity, 3, 0, 1, 1)
        self.deep_bones_opacity_label = QtWidgets.QLabel(self.groupBox_2)
        self.deep_bones_opacity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.deep_bones_opacity_label.setObjectName("deep_bones_opacity_label")
        self.gridLayout_10.addWidget(self.deep_bones_opacity_label, 3, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.gridLayout_11.addLayout(self.horizontalLayout_2, 0, 1, 5, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_11.addWidget(self.label_27, 1, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_11.addWidget(self.label_28, 2, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_11.addWidget(self.label_29, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_11.addWidget(self.label, 4, 0, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.transfer_function_defaults = QtWidgets.QPushButton(self.groupBox_2)
        self.transfer_function_defaults.setObjectName("transfer_function_defaults")
        self.horizontalLayout_3.addWidget(self.transfer_function_defaults)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.verticalLayout_12.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.iso_value.valueChanged['int'].connect(self.iso_label.setNum)
        self.skin_red.valueChanged['int'].connect(self.skin_red_label.setNum)
        self.skin_green.valueChanged['int'].connect(self.skin_green_label.setNum)
        self.skin_blue.valueChanged['int'].connect(self.skin_blue_label.setNum)
        self.skin_opacity.valueChanged['int'].connect(self.skin_opacity_label.setNum)
        self.muscle_red.valueChanged['int'].connect(self.muscle_red_label.setNum)
        self.muscle_green.valueChanged['int'].connect(self.muscle_green_label.setNum)
        self.muscle_blue.valueChanged['int'].connect(self.muscle_blue_label.setNum)
        self.muscle_opacity.valueChanged['int'].connect(self.muscle_opacity_label.setNum)
        self.bones_red.valueChanged['int'].connect(self.bones_red_label.setNum)
        self.bones_green.valueChanged['int'].connect(self.bones_green_label.setNum)
        self.bones_blue.valueChanged['int'].connect(self.bones_blue_label.setNum)
        self.bone_opacity.valueChanged['int'].connect(self.bones_opacity_label.setNum)
        self.deep_bones_red.valueChanged['int'].connect(self.deep_bones_red_label.setNum)
        self.deep_bones_green.valueChanged['int'].connect(self.deep_bones_green_label.setNum)
        self.deep_bones_blue.valueChanged['int'].connect(self.deep_bones_blue_label.setNum)
        self.deep_bone_opacity.valueChanged['int'].connect(self.deep_bones_opacity_label.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "vtkRendering"))
        self.rendering_technique.setItemText(0, _translate("MainWindow", "Surface Rendering"))
        self.rendering_technique.setItemText(1, _translate("MainWindow", "Ray Casting Rendering"))
        self.groupBox.setTitle(_translate("MainWindow", "ISO Value"))
        self.iso_defaults.setText(_translate("MainWindow", "Restore Defaults"))
        self.iso_label.setText(_translate("MainWindow", "500"))
        self.groupBox_2.setTitle(_translate("MainWindow", "RGB Ray Casting Transfer Function"))
        self.label_2.setText(_translate("MainWindow", "Red"))
        self.skin_red_label.setText(_translate("MainWindow", "0"))
        self.muscle_red_label.setText(_translate("MainWindow", "100"))
        self.bones_red_label.setText(_translate("MainWindow", "100"))
        self.deep_bones_red_label.setText(_translate("MainWindow", "100"))
        self.label_3.setText(_translate("MainWindow", "Green"))
        self.skin_green_label.setText(_translate("MainWindow", "0"))
        self.muscle_green_label.setText(_translate("MainWindow", "50"))
        self.bones_green_label.setText(_translate("MainWindow", "50"))
        self.deep_bones_green_label.setText(_translate("MainWindow", "100"))
        self.label_4.setText(_translate("MainWindow", "Blue"))
        self.skin_blue_label.setText(_translate("MainWindow", "0"))
        self.muscle_blue_label.setText(_translate("MainWindow", "30"))
        self.bones_blue_label.setText(_translate("MainWindow", "30"))
        self.deep_bones_blue_label.setText(_translate("MainWindow", "90"))
        self.label_31.setText(_translate("MainWindow", "Opacity"))
        self.skin_opacity_label.setText(_translate("MainWindow", "15"))
        self.muscle_opacity_label.setText(_translate("MainWindow", "30"))
        self.bones_opacity_label.setText(_translate("MainWindow", "45"))
        self.deep_bones_opacity_label.setText(_translate("MainWindow", "60"))
        self.label_27.setText(_translate("MainWindow", "Skin"))
        self.label_28.setText(_translate("MainWindow", "Muscle"))
        self.label_29.setText(_translate("MainWindow", "Bones"))
        self.label.setText(_translate("MainWindow", "Deep Bones"))
        self.transfer_function_defaults.setText(_translate("MainWindow", "Restore Defaults"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())