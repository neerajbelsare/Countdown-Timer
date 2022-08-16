import threading
import time
import platform

from PyQt6.QtCore import QPropertyAnimation, QPoint
from win10toast import ToastNotifier
from PyQt6 import QtCore, QtGui, QtWidgets
from playsound import playsound


class Ui_MainWindow(object):
    def __init__(self):
        self.stop_1 = None
        self.stop_2 = None
        self.step = None
        self.messageFrame = None
        self.temp = None
        self.total_secs = None
        self._hrs = None
        self._mins = None
        self._secs = None
        self.stop_loop = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.windowBackground = QtWidgets.QFrame(self.centralwidget)
        self.windowBackground.setGeometry(QtCore.QRect(9, 9, 776, 581))
        self.windowBackground.setStyleSheet("QFrame {\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(51, 3, 57, 255), stop:1 rgba(51, 49, 151, 255));    \n"
                                            "}")
        self.windowBackground.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.windowBackground.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.windowBackground.setObjectName("windowBackground")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.windowBackground)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(20, 15, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("QLabel {\n"
                                 "    background-color: transparent;\n"
                                 "    color: white;\n"
                                 "}")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.frame = QtWidgets.QFrame(self.windowBackground)
        self.frame.setGeometry(QtCore.QRect(9, 400, 751, 181))
        self.frame.setStyleSheet("QFrame {\n"
                                 "    background-color: transparent;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.resetFrame = QtWidgets.QFrame(self.frame)
        self.resetFrame.setGeometry(QtCore.QRect(131, 10, 150, 150))
        self.resetFrame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.resetFrame.setStyleSheet("QFrame {\n"
                                      "    background-color: transparent;\n"
                                      "}")
        self.resetFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.resetFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.resetFrame.setObjectName("resetFrame")
        self.resetIcon = QtWidgets.QLabel(self.resetFrame)
        self.resetIcon.setGeometry(QtCore.QRect(50, 50, 40, 41))
        self.resetIcon.setStyleSheet("QLabel {\n"
                                     "    background-color: transparent;\n"
                                     "    display: block;\n"
                                     "}")
        self.resetIcon.setText("")
        self.resetIcon.setPixmap(QtGui.QPixmap("assets/img/Reset.png"))
        self.resetIcon.setScaledContents(True)
        self.resetIcon.setObjectName("resetIcon")
        self.resetButton = QtWidgets.QPushButton(self.resetFrame)
        self.resetButton.setGeometry(QtCore.QRect(19, 19, 100, 100))
        self.resetButton.setStyleSheet("QPushButton {\n"
                                       "    border-radius: 50px;\n"
                                       "    border: 2px solid rgba(255, 255, 255,0.3);\n"
                                       "    color: white;\n"
                                       "    transition: 0.2s all;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    transition: 0.2s all;\n"
                                       "    border: 2px solid rgba(255, 255, 255,0.6);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    border: 2px solid rgba(255, 255, 255,0.3);\n"
                                       "}")
        self.resetButton.setText("")
        self.resetButton.setObjectName("resetButton")
        self.resetLabel = QtWidgets.QLabel(self.resetFrame)
        self.resetLabel.setGeometry(QtCore.QRect(44, 130, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.resetLabel.setFont(font)
        self.resetLabel.setStyleSheet("QLabel {\n"
                                      "    background-color: transparent;\n"
                                      "    color: rgba(255, 255, 255, 0.6);\n"
                                      "}")
        self.resetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resetLabel.setObjectName("resetLabel")
        self.startFrame = QtWidgets.QFrame(self.frame)
        self.startFrame.setGeometry(QtCore.QRect(298, 10, 150, 150))
        self.startFrame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.startFrame.setStyleSheet("QFrame {\n"
                                      "    background-color: transparent;\n"
                                      "}")
        self.startFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.startFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.startFrame.setObjectName("startFrame")
        self.startIcon = QtWidgets.QLabel(self.startFrame)
        self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))
        self.startIcon.setStyleSheet("QLabel {\n"
                                     "    background-color: transparent;\n"
                                     "    display: inline-block;\n"
                                     "}\n"
                                     "QLabel:pressed {\n"
                                     "    transform: scale(0.8);\n"
                                     "}")
        self.startIcon.setText("")
        self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
        self.startIcon.setScaledContents(True)
        self.startIcon.setObjectName("startIcon")
        self.startButton = QtWidgets.QPushButton(self.startFrame)
        self.startButton.setGeometry(QtCore.QRect(26, 19, 100, 100))
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.startButton.setStyleSheet("QPushButton {\n"
                                       "    border-radius: 50px;\n"
                                       "    background-color: rgba(255, 255, 255,0.3);\n"
                                       "    color: white;\n"
                                       "    transition: 0.2s all;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgba(255, 255, 255,0.4);\n"
                                       "    transition: 0.2s all;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgba(255, 255, 255,0.2);\n"
                                       "}")
        self.startButton.setText("")
        self.startButton.setObjectName("startButton")
        self.startLabel = QtWidgets.QLabel(self.startFrame)
        self.startLabel.setGeometry(QtCore.QRect(50, 130, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.startLabel.setFont(font)
        self.startLabel.setStyleSheet("QLabel {\n"
                                      "    background-color: transparent;\n"
                                      "    color: rgba(255, 255, 255, 0.6);\n"
                                      "}")
        self.startLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.startLabel.setObjectName("startLabel")
        self.stopFrame = QtWidgets.QFrame(self.frame)
        self.stopFrame.setGeometry(QtCore.QRect(465, 10, 150, 150))
        self.stopFrame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stopFrame.setStyleSheet("QFrame {\n"
                                     "    background-color: transparent;\n"
                                     "}")
        self.stopFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.stopFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.stopFrame.setObjectName("stopFrame")
        self.stopIcon = QtWidgets.QLabel(self.stopFrame)
        self.stopIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))
        self.stopIcon.setStyleSheet("QLabel {\n"
                                    "    background-color: transparent;\n"
                                    "    display: block;\n"
                                    "}")
        self.stopIcon.setText("")
        self.stopIcon.setPixmap(QtGui.QPixmap("assets/img/Stop.png"))
        self.stopIcon.setScaledContents(True)
        self.stopIcon.setObjectName("stopIcon")
        self.stopButton = QtWidgets.QPushButton(self.stopFrame)
        self.stopButton.setGeometry(QtCore.QRect(29, 19, 100, 100))
        self.stopButton.setStyleSheet("QPushButton {\n"
                                      "    border-radius: 50px;\n"
                                      "    border: 2px solid rgba(255, 255, 255,0.3);\n"
                                      "    color: white;\n"
                                      "    transition: 0.2s all;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    transition: 0.2s all;\n"
                                      "    border: 2px solid rgba(255, 255, 255,0.6);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    border: 2px solid rgba(255, 255, 255,0.3);\n"
                                      "}")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.stopLabel = QtWidgets.QLabel(self.stopFrame)
        self.stopLabel.setGeometry(QtCore.QRect(54, 130, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.stopLabel.setFont(font)
        self.stopLabel.setStyleSheet("QLabel {\n"
                                     "    background-color: transparent;\n"
                                     "    color: rgba(255, 255, 255, 0.6);\n"
                                     "}")
        self.stopLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stopLabel.setObjectName("stopLabel")
        self.circularProgressBarBase = QtWidgets.QFrame(self.windowBackground)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(219, 76, 320, 320))
        self.circularProgressBarBase.setStyleSheet("QFrame {\n"
                                                   "    background-color: transparent;\n"
                                                   "}")
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet("QFrame {\n"
                                            "    border-radius: 150px;\n"
                                            "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:1.000 rgba(0, 170, 255, 0), stop:1.001 rgba(208, 158, 230, 255));\n"
                                            "}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet("QFrame {\n"
                                      "    border-radius: 150px;\n"
                                      "    background-color: rgba(255, 255, 255, 0.2);\n"
                                      "}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(self.circularProgressBarBase)
        self.container.setGeometry(QtCore.QRect(20, 20, 280, 280))
        self.container.setStyleSheet("QFrame {\n"
                                     "    border-radius: 140px;\n"
                                     "    background-color: rgb(23, 20, 90);\n"
                                     "}")
        self.container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.container.setObjectName("container")
        self.colon1 = QtWidgets.QLabel(self.container)
        self.colon1.setGeometry(QtCore.QRect(83, 4, 16, 271))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(32)
        self.colon1.setFont(font)
        self.colon1.setStyleSheet("QLabel {\n"
                                  "    color: rgba(255, 255, 255, 0.9);\n"
                                  "    background-color: transparent;\n"
                                  "}")
        self.colon1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.colon1.setObjectName("colon1")
        self.colon2 = QtWidgets.QLabel(self.container)
        self.colon2.setGeometry(QtCore.QRect(166, 4, 16, 271))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(32)
        self.colon2.setFont(font)
        self.colon2.setStyleSheet("QLabel { \n"
                                  "    background-color: transparent;\n"
                                  "    color: white;\n"
                                  "}")
        self.colon2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.colon2.setObjectName("colon2")
        self.minsInput = QtWidgets.QLineEdit(self.container)
        self.minsInput.setGeometry(QtCore.QRect(88, -1, 91, 281))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        self.minsInput.setFont(font)
        self.minsInput.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 140px;\n"
                                     "    background-color: transparent;\n"
                                     "    color: rgba(255 ,255, 255, 0.9);\n"
                                     "}")
        self.minsInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.minsInput.setPlaceholderText("00")
        self.minsInput.setObjectName("minsInput")
        self.secsInput = QtWidgets.QLineEdit(self.container)
        self.secsInput.setGeometry(QtCore.QRect(177, -1, 91, 281))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        self.secsInput.setFont(font)
        self.secsInput.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 140px;\n"
                                     "    background-color: transparent;\n"
                                     "    color: rgba(255 ,255, 255, 0.9);\n"
                                     "}")
        self.secsInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.secsInput.setPlaceholderText("00")
        self.secsInput.setObjectName("secsInput")
        self.hrsInput = QtWidgets.QLineEdit(self.container)
        self.hrsInput.setGeometry(QtCore.QRect(0, -1, 91, 281))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        self.hrsInput.setFont(font)
        self.hrsInput.setStyleSheet("QLineEdit {\n"
                                    "    border-radius: 140px;\n"
                                    "    background-color: transparent;\n"
                                    "    color: rgba(255 ,255, 255, 0.9);\n"
                                    "}")
        self.hrsInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hrsInput.setPlaceholderText("00")
        self.hrsInput.setObjectName("hrsInput")
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()

        self.messageFrame = QtWidgets.QFrame(self.centralwidget)
        self.messageFrame.setGeometry(QtCore.QRect(430, -110, 341, 81))
        self.messageFrame.setStyleSheet("")
        self.messageFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.messageFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.messageFrame.setObjectName("messageFrame")
        self.msgshow = QPropertyAnimation(self.messageFrame, b"pos")
        self.msgshow.setEndValue(QPoint(430, 10))
        self.msghide = QPropertyAnimation(self.messageFrame, b"pos")
        self.msghide.setEndValue(QPoint(430, -100))

        self.messageContainer = QtWidgets.QFrame(self.messageFrame)
        self.messageContainer.setGeometry(QtCore.QRect(-1, 10, 341, 61))
        self.messageContainer.setStyleSheet("QFrame {\n"
                                            "    background-color: rgba(255, 255, 255, 0.3);\n"
                                            "    border-radius: 15px;\n"
                                            "}")
        self.messageContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.messageContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.messageContainer.setObjectName("messageContainer")
        self.errorIcon = QtWidgets.QLabel(self.messageContainer)
        self.errorIcon.setGeometry(QtCore.QRect(16, 14, 32, 32))
        self.errorIcon.setStyleSheet("QLabel {\n"
                                     "    background-color: transparent;\n"
                                     "}    ")
        self.errorIcon.setText("")
        self.errorIcon.setPixmap(QtGui.QPixmap("assets/img/error.png"))
        self.errorIcon.setScaledContents(True)
        self.errorIcon.setObjectName("errorIcon")
        self.errorText = QtWidgets.QLabel(self.messageContainer)
        self.errorText.setGeometry(QtCore.QRect(66, 10, 261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.errorText.setFont(font)
        self.errorText.setStyleSheet("QFrame {\n"
                                     "    background-color: transparent;\n"
                                     "    color: rgba(255, 255, 255, 0.8)\n"
                                     "}")
        self.errorText.setObjectName("errorText")
        self.closeMsgIcon = QtWidgets.QLabel(self.messageContainer)
        self.closeMsgIcon.setGeometry(QtCore.QRect(318, 9, 8, 8))
        self.closeMsgIcon.setStyleSheet("QLabel {\n"
                                        "    background-color: transparent;\n"
                                        "}\n"
                                        "")
        self.closeMsgIcon.setText("")
        self.closeMsgIcon.setPixmap(QtGui.QPixmap("assets/img/close.png"))
        self.closeMsgIcon.setScaledContents(True)
        self.closeMsgIcon.setObjectName("closeMsgIcon")

        self.closeMsgButton = QtWidgets.QPushButton(self.messageContainer)
        self.closeMsgButton.setGeometry(QtCore.QRect(318, 9, 8, 8))
        self.closeMsgButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.closeMsgButton.setStyleSheet("QPushButton {\n"
                                          "    border: none;\n"
                                          "    background-color: transparent;\n"
                                          "}")
        self.closeMsgButton.setText("")
        self.closeMsgButton.setObjectName("closeMsgButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Countdown Timer"))
        self.title.setText(_translate("MainWindow", "Countdown Timer"))
        self.resetLabel.setText(_translate("MainWindow", "Reset"))
        self.startLabel.setText(_translate("MainWindow", "Start"))
        self.stopLabel.setText(_translate("MainWindow", "Stop"))
        self.colon1.setText(_translate("MainWindow", ":"))
        self.colon2.setText(_translate("MainWindow", ":"))
        self.startButton.clicked.connect(self.start_clicked)
        self.stopButton.clicked.connect(self.stop_clicked)
        self.resetButton.clicked.connect(self.reset_clicked)
        self.closeMsgButton.clicked.connect(self.close_msg_clicked)
        self.errorText.setText(_translate("MainWindow", "An Unknown Error Occurred. Please try again."))

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    def resume_thread(self):
        t1 = threading.Thread(target=self.resume)
        t1.start()

    def start(self):
        self.stopFrame.setEnabled(True)
        self.resetFrame.setEnabled(True)
        self.stop_loop = False
        self.total_secs = self._hrs * 3600 + self._mins * 60 + self._secs
        self.temp = self.total_secs

        self.circularProgress.setStyleSheet("QFrame {\n"
                                            "    border-radius: 150px;\n"
                                            "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:1.000 rgba(0, 170, 255, 0), stop:1.000 rgba(208, 158, 230, 255));\n"
                                            "}")
        
        self.step = 1.001 / self.temp
        self.stop_2 = 0.001

        while self.total_secs > 0 and not self.stop_loop:
            self.stop_2 = round(self.stop_2 + self.step, 3)
            self.stop_1 = round(self.stop_2 - 0.001, 3)
            self.circularProgress.setStyleSheet("QFrame {\n"
                                                "    border-radius: 150px;\n"
                                                f"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{self.stop_1} rgba(0, 170, 255, 0), stop:{self.stop_2} rgba(208, 158, 230, 255));\n"
                                                "}")

            self.total_secs -= 1
            mins, secs = divmod(self.total_secs, 60)
            hrs, mins = divmod(mins, 60)

            self.hrsInput.setDisabled(True)
            self.minsInput.setDisabled(True)
            self.secsInput.setDisabled(True)

            self.hrsInput.setText(str(hrs).zfill(2))
            self.minsInput.setText(str(mins).zfill(2))
            self.secsInput.setText(str(secs).zfill(2))

            time.sleep(1)

        if not self.stop_loop:
            self.hrsInput.setEnabled(True)
            self.minsInput.setEnabled(True)
            self.secsInput.setEnabled(True)

            self.startLabel.setText("Start")
            self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
            self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))

            playsound('assets/alerts/alert1.mp3')

            if platform.system() == 'Windows':
                toast = ToastNotifier()
                toast.show_toast("Countdown Timer", "Time is Up!", duration=10)

    def pause(self):
        self.stopFrame.setEnabled(True)
        self.stop_loop = True
        self.total_secs = self._hrs * 3600 + self._mins * 60 + self._secs
        mins2, secs2 = divmod(self.total_secs, 60)
        hrs2, mins2 = divmod(mins2, 60)

        self.hrsInput.setText(str(hrs2).zfill(2))
        self.minsInput.setText(str(mins2).zfill(2))
        self.secsInput.setText(str(secs2).zfill(2))

    def resume(self):
        self.stopFrame.setEnabled(True)
        self.resetFrame.setEnabled(True)
        self.stop_loop = False
        self.total_secs = self._hrs * 3600 + self._mins * 60 + self._secs

        while self.total_secs > 0 and not self.stop_loop:
            self.stop_2 = round(self.stop_2 + self.step, 3)
            self.stop_1 = round(self.stop_2 - 0.001, 3)

            self.circularProgress.setStyleSheet("QFrame {\n"
                                                "    border-radius: 150px;\n"
                                                f"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{self.stop_1} rgba(0, 170, 255, 0), stop:{self.stop_2} rgba(208, 158, 230, 255));\n"
                                                "}")

            self.total_secs -= 1
            mins, secs = divmod(self.total_secs, 60)
            hrs, mins = divmod(mins, 60)

            self.hrsInput.setDisabled(True)
            self.minsInput.setDisabled(True)
            self.secsInput.setDisabled(True)

            self.hrsInput.setText(str(hrs).zfill(2))
            self.minsInput.setText(str(mins).zfill(2))
            self.secsInput.setText(str(secs).zfill(2))

            time.sleep(1)

        if not self.stop_loop:
            self.hrsInput.setEnabled(True)
            self.minsInput.setEnabled(True)
            self.secsInput.setEnabled(True)

            self.startLabel.setText("Start")
            self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
            self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))

            playsound('assets/alerts/alert1.mp3')

            if platform.system() == 'Windows':
                toast = ToastNotifier()
                toast.show_toast("Countdown Timer", "Time is Up!", duration=10)

    def stop(self):
        self.stop_loop = True
        mins1, secs1 = divmod(self.temp, 60)
        hrs1, mins1 = divmod(mins1, 60)

        self.hrsInput.setText(str(hrs1).zfill(2))
        self.minsInput.setText(str(mins1).zfill(2))
        self.secsInput.setText(str(secs1).zfill(2))

        self.hrsInput.setEnabled(True)
        self.minsInput.setEnabled(True)
        self.secsInput.setEnabled(True)

        self.startLabel.setText("Start")
        self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
        self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))

    def reset(self):
        self.total_secs = 0
        self.stop_loop = True

        self.hrsInput.setText("00")
        self.minsInput.setText("00")
        self.secsInput.setText("00")

        self.hrsInput.setEnabled(True)
        self.minsInput.setEnabled(True)
        self.secsInput.setEnabled(True)

        self.startLabel.setText("Start")
        self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
        self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))

        self.stopFrame.setDisabled(True)

    def start_clicked(self):
        if self.startLabel.text() == "Start":
            self._hrs = self.hrsInput.text() or "00"
            self._mins = self.minsInput.text() or "00"
            self._secs = self.secsInput.text() or "00"

            if self._hrs.isdigit() and self._mins.isdigit() and self._secs.isdigit():
                self.startLabel.setText("Pause")
                self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Pause.png"))
                self.startIcon.setGeometry(QtCore.QRect(56, 50, 40, 39))
                self._hrs = int(self._hrs)
                self._mins = int(self._mins)
                self._secs = int(self._secs)

                self.start_thread()

            else:
                self.stopFrame.setDisabled(True)
                self.resetFrame.setDisabled(True)
                self.errorText.setText("Enter a valid integer value!")
                self.msgshow.start()

        elif self.startLabel.text() == 'Pause':
            self.startLabel.setText("Resume")
            self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
            self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))

            self._hrs = int(self.hrsInput.text() or "00")
            self._mins = int(self.minsInput.text() or "00")
            self._secs = int(self.secsInput.text() or "00")

            self.pause()

        elif self.startLabel.text() == 'Resume':
            self.startLabel.setText("Pause")
            self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Pause.png"))
            self.startIcon.setGeometry(QtCore.QRect(56, 50, 40, 39))

            self._hrs = int(self.hrsInput.text() or "00")
            self._mins = int(self.minsInput.text() or "00")
            self._secs = int(self.secsInput.text() or "00")

            self.resume_thread()

    def stop_clicked(self):
        self.stop()

    def reset_clicked(self):
        self.reset()

    def close_msg_clicked(self):
        self.msghide.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
