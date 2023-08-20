# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/philippmochti/Documents/PlatformIO/Projects/ClampControl/ClampControl.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 520)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 520))
        MainWindow.setMaximumSize(QtCore.QSize(500, 520))
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setEnabled(True)
        self.MainWidget.setMinimumSize(QtCore.QSize(450, 470))
        self.MainWidget.setMaximumSize(QtCore.QSize(520, 470))
        self.MainWidget.setObjectName("MainWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ClampControlMainLayout = QtWidgets.QVBoxLayout()
        self.ClampControlMainLayout.setContentsMargins(-1, 1, -1, -1)
        self.ClampControlMainLayout.setObjectName("ClampControlMainLayout")
        self.StatusLayout = QtWidgets.QVBoxLayout()
        self.StatusLayout.setObjectName("StatusLayout")
        self.StatusLabel = QtWidgets.QLabel(self.MainWidget)
        self.StatusLabel.setEnabled(True)
        self.StatusLabel.setMinimumSize(QtCore.QSize(400, 40))
        self.StatusLabel.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StatusLabel.setAcceptDrops(False)
        self.StatusLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StatusLabel.setAutoFillBackground(False)
        self.StatusLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.StatusLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StatusLabel.setLineWidth(3)
        self.StatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusLabel.setWordWrap(False)
        self.StatusLabel.setObjectName("StatusLabel")
        self.StatusLayout.addWidget(self.StatusLabel, 0, QtCore.Qt.AlignHCenter)
        self.ClampControlMainLayout.addLayout(self.StatusLayout)
        self.line_3 = QtWidgets.QFrame(self.MainWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.ClampControlMainLayout.addWidget(self.line_3)
        self.SingeClampControlGrid = QtWidgets.QGridLayout()
        self.SingeClampControlGrid.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.SingeClampControlGrid.setObjectName("SingeClampControlGrid")
        self.LineC4 = QtWidgets.QFrame(self.MainWidget)
        self.LineC4.setFrameShape(QtWidgets.QFrame.VLine)
        self.LineC4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LineC4.setObjectName("LineC4")
        self.SingeClampControlGrid.addWidget(self.LineC4, 3, 1, 1, 1)
        self.LineC8 = QtWidgets.QFrame(self.MainWidget)
        self.LineC8.setFrameShape(QtWidgets.QFrame.VLine)
        self.LineC8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LineC8.setObjectName("LineC8")
        self.SingeClampControlGrid.addWidget(self.LineC8, 7, 1, 1, 1)
        self.LabelNameC4 = QtWidgets.QLabel(self.MainWidget)
        self.LabelNameC4.setObjectName("LabelNameC4")
        self.SingeClampControlGrid.addWidget(self.LabelNameC4, 3, 2, 1, 1)
        self.LineC2 = QtWidgets.QFrame(self.MainWidget)
        self.LineC2.setFrameShape(QtWidgets.QFrame.VLine)
        self.LineC2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LineC2.setObjectName("LineC2")
        self.SingeClampControlGrid.addWidget(self.LineC2, 1, 1, 1, 1)
        self.LineC5 = QtWidgets.QFrame(self.MainWidget)
        self.LineC5.setFrameShape(QtWidgets.QFrame.VLine)
        self.LineC5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LineC5.setObjectName("LineC5")
        self.SingeClampControlGrid.addWidget(self.LineC5, 4, 1, 1, 1)
        self.LabelNameC5 = QtWidgets.QLabel(self.MainWidget)
        self.LabelNameC5.setObjectName("LabelNameC5")
        self.SingeClampControlGrid.addWidget(self.LabelNameC5, 4, 2, 1, 1)
        self.LabelNameC8 = QtWidgets.QLabel(self.MainWidget)
        self.LabelNameC8.setEnabled(False)
        self.LabelNameC8.setObjectName("LabelNameC8")
        self.SingeClampControlGrid.addWidget(self.LabelNameC8, 7, 2, 1, 1)
        self.LineC3 = QtWidgets.QFrame(self.MainWidget)
        self.LineC3.setFrameShape(QtWidgets.QFrame.VLine)
        self.LineC3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LineC3.setObjectName("LineC3")
        self.SingeClampControlGrid.addWidget(self.LineC3, 2, 1, 1, 1)
        self.LineC7 = QtWidgets.QFrame(self.MainWidget)
        self.LineC7.setFrameShape(QtWidgets.QFrame.VLine)
        self.LineC7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LineC7.setObjectName("LineC7")
        self.SingeClampControlGrid.addWidget(self.LineC7, 6, 1, 1, 1)
        self.LineC1 = QtWidgets.QFrame(self.MainWidget)
        self.LineC1.setFrameShape(QtWidgets.QFrame.VLine)
        self.LineC1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LineC1.setObjectName("LineC1")
        self.SingeClampControlGrid.addWidget(self.LineC1, 0, 1, 1, 1)
        self.LabelNameC6 = QtWidgets.QLabel(self.MainWidget)
        self.LabelNameC6.setObjectName("LabelNameC6")
        self.SingeClampControlGrid.addWidget(self.LabelNameC6, 5, 2, 1, 1)
        self.LabelNameC7 = QtWidgets.QLabel(self.MainWidget)
        self.LabelNameC7.setObjectName("LabelNameC7")
        self.SingeClampControlGrid.addWidget(self.LabelNameC7, 6, 2, 1, 1)
        self.LineC6 = QtWidgets.QFrame(self.MainWidget)
        self.LineC6.setFrameShape(QtWidgets.QFrame.VLine)
        self.LineC6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LineC6.setObjectName("LineC6")
        self.SingeClampControlGrid.addWidget(self.LineC6, 5, 1, 1, 1)
        self.C8Button = QtWidgets.QRadioButton(self.MainWidget)
        self.C8Button.setEnabled(True)
        self.C8Button.setChecked(False)
        self.C8Button.setAutoExclusive(False)
        self.C8Button.setObjectName("C8Button")
        self.SingeClampControlGrid.addWidget(self.C8Button, 7, 0, 1, 1, QtCore.Qt.AlignRight)
        self.C7Button = QtWidgets.QRadioButton(self.MainWidget)
        self.C7Button.setAutoExclusive(False)
        self.C7Button.setObjectName("C7Button")
        self.SingeClampControlGrid.addWidget(self.C7Button, 6, 0, 1, 1, QtCore.Qt.AlignRight)
        self.C6Button = QtWidgets.QRadioButton(self.MainWidget)
        self.C6Button.setAutoExclusive(False)
        self.C6Button.setObjectName("C6Button")
        self.SingeClampControlGrid.addWidget(self.C6Button, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.C5Button = QtWidgets.QRadioButton(self.MainWidget)
        self.C5Button.setAutoExclusive(False)
        self.C5Button.setObjectName("C5Button")
        self.SingeClampControlGrid.addWidget(self.C5Button, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.C4Button = QtWidgets.QRadioButton(self.MainWidget)
        self.C4Button.setAutoExclusive(False)
        self.C4Button.setObjectName("C4Button")
        self.SingeClampControlGrid.addWidget(self.C4Button, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.C3Button = QtWidgets.QRadioButton(self.MainWidget)
        self.C3Button.setAutoExclusive(False)
        self.C3Button.setObjectName("C3Button")
        self.SingeClampControlGrid.addWidget(self.C3Button, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.LabelNameC3 = QtWidgets.QLabel(self.MainWidget)
        self.LabelNameC3.setObjectName("LabelNameC3")
        self.SingeClampControlGrid.addWidget(self.LabelNameC3, 2, 2, 1, 1)
        self.LabelNameC2 = QtWidgets.QLabel(self.MainWidget)
        self.LabelNameC2.setObjectName("LabelNameC2")
        self.SingeClampControlGrid.addWidget(self.LabelNameC2, 1, 2, 1, 1)
        self.LabelNameC1 = QtWidgets.QLabel(self.MainWidget)
        self.LabelNameC1.setObjectName("LabelNameC1")
        self.SingeClampControlGrid.addWidget(self.LabelNameC1, 0, 2, 1, 1)
        self.C1Button = QtWidgets.QRadioButton(self.MainWidget)
        self.C1Button.setAutoExclusive(False)
        self.C1Button.setObjectName("C1Button")
        self.SingeClampControlGrid.addWidget(self.C1Button, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.C2Button = QtWidgets.QRadioButton(self.MainWidget)
        self.C2Button.setAutoExclusive(False)
        self.C2Button.setObjectName("C2Button")
        self.SingeClampControlGrid.addWidget(self.C2Button, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.ClampControlMainLayout.addLayout(self.SingeClampControlGrid)
        self.line_2 = QtWidgets.QFrame(self.MainWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.ClampControlMainLayout.addWidget(self.line_2)
        self.ComandLineLayout = QtWidgets.QHBoxLayout()
        self.ComandLineLayout.setContentsMargins(-1, -1, 10, -1)
        self.ComandLineLayout.setSpacing(0)
        self.ComandLineLayout.setObjectName("ComandLineLayout")
        self.CmdSendButton = QtWidgets.QPushButton(self.MainWidget)
        self.CmdSendButton.setMinimumSize(QtCore.QSize(100, 40))
        self.CmdSendButton.setMaximumSize(QtCore.QSize(100, 40))
        self.CmdSendButton.setObjectName("CmdSendButton")
        self.ComandLineLayout.addWidget(self.CmdSendButton, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmdInput = QtWidgets.QLineEdit(self.MainWidget)
        self.CmdInput.setMinimumSize(QtCore.QSize(350, 30))
        self.CmdInput.setMaximumSize(QtCore.QSize(300, 40))
        self.CmdInput.setObjectName("CmdInput")
        self.ComandLineLayout.addWidget(self.CmdInput, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.ComandLineLayout.setStretch(0, 1)
        self.ComandLineLayout.setStretch(1, 4)
        self.ClampControlMainLayout.addLayout(self.ComandLineLayout)
        self.verticalLayout.addLayout(self.ClampControlMainLayout)
        self.line = QtWidgets.QFrame(self.MainWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.SettingsAndExtraControl = QtWidgets.QGridLayout()
        self.SettingsAndExtraControl.setObjectName("SettingsAndExtraControl")
        self.ReservedCheckBox = QtWidgets.QCheckBox(self.MainWidget)
        self.ReservedCheckBox.setEnabled(False)
        self.ReservedCheckBox.setObjectName("ReservedCheckBox")
        self.SettingsAndExtraControl.addWidget(self.ReservedCheckBox, 2, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_18 = QtWidgets.QFrame(self.MainWidget)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.SettingsAndExtraControl.addWidget(self.line_18, 1, 2, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.MainWidget)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.SettingsAndExtraControl.addWidget(self.line_16, 0, 1, 1, 1)
        self.SyncClamp15CheckBox = QtWidgets.QCheckBox(self.MainWidget)
        self.SyncClamp15CheckBox.setObjectName("SyncClamp15CheckBox")
        self.SettingsAndExtraControl.addWidget(self.SyncClamp15CheckBox, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_17 = QtWidgets.QFrame(self.MainWidget)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.SettingsAndExtraControl.addWidget(self.line_17, 2, 1, 1, 1)
        self.SwitchAllOffButton = QtWidgets.QPushButton(self.MainWidget)
        self.SwitchAllOffButton.setMinimumSize(QtCore.QSize(200, 0))
        self.SwitchAllOffButton.setObjectName("SwitchAllOffButton")
        self.SettingsAndExtraControl.addWidget(self.SwitchAllOffButton, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_19 = QtWidgets.QFrame(self.MainWidget)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.SettingsAndExtraControl.addWidget(self.line_19, 1, 0, 1, 1)
        self.SwitchAllOnButton = QtWidgets.QPushButton(self.MainWidget)
        self.SwitchAllOnButton.setMinimumSize(QtCore.QSize(200, 0))
        self.SwitchAllOnButton.setObjectName("SwitchAllOnButton")
        self.SettingsAndExtraControl.addWidget(self.SwitchAllOnButton, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.SettingsAndExtraControl)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.MainWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 24))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionThere_is_no_help = QtWidgets.QAction(MainWindow)
        self.actionThere_is_no_help.setObjectName("actionThere_is_no_help")
        self.actionConect = QtWidgets.QAction(MainWindow)
        self.actionConect.setObjectName("actionConect")
        self.menuHelp.addAction(self.actionThere_is_no_help)
        self.menuSetting.addAction(self.actionConect)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StatusLabel.setText(_translate("MainWindow", "System Status: Unkownnn"))
        self.LabelNameC4.setText(_translate("MainWindow", "Clamp 30 - Last"))
        self.LabelNameC5.setText(_translate("MainWindow", "Clamp 30 - Crash"))
        self.LabelNameC8.setText(_translate("MainWindow", "Reserved - Not Used"))
        self.LabelNameC6.setText(_translate("MainWindow", "Clamp 15 - Signal"))
        self.LabelNameC7.setText(_translate("MainWindow", "Clamp 15 - Wakeup"))
        self.C8Button.setText(_translate("MainWindow", "Channel 8"))
        self.C7Button.setText(_translate("MainWindow", "Channel 7"))
        self.C6Button.setText(_translate("MainWindow", "Channel 6"))
        self.C5Button.setText(_translate("MainWindow", "Channel 5"))
        self.C4Button.setText(_translate("MainWindow", "Channel 4"))
        self.C3Button.setText(_translate("MainWindow", "Channel 3"))
        self.LabelNameC3.setText(_translate("MainWindow", "Calmp 30 - B"))
        self.LabelNameC2.setText(_translate("MainWindow", "Clamp 30 - G"))
        self.LabelNameC1.setText(_translate("MainWindow", "Clamp 30 - Battery"))
        self.C1Button.setText(_translate("MainWindow", "Channel 1"))
        self.C2Button.setText(_translate("MainWindow", "Channel 2"))
        self.CmdSendButton.setText(_translate("MainWindow", "Send CMD"))
        self.ReservedCheckBox.setText(_translate("MainWindow", "Not Used"))
        self.SyncClamp15CheckBox.setText(_translate("MainWindow", "Sync Clamp 15"))
        self.SwitchAllOffButton.setText(_translate("MainWindow", "All Off"))
        self.SwitchAllOnButton.setText(_translate("MainWindow", "All On"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionThere_is_no_help.setText(_translate("MainWindow", "There is no help"))
        self.actionConect.setText(_translate("MainWindow", "Conect"))
