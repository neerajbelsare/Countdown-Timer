import threading
import time
import platform

from PyQt6.QtCore import QPropertyAnimation, QPoint
from win10toast import ToastNotifier
from PyQt6 import QtCore, QtGui, QtWidgets
from playsound import playsound


class Ui_MainWindow(object):
    def __init__(self):  # Initializing elements
        self.menubar = None
        self.statusbar = None
        self.closeMsgButton = None
        self.closeMsgIcon = None
        self.errorText = None
        self.errorIcon = None
        self.messageContainer = None
        self.msghide = None
        self.msgshow = None
        self.hrsInput = None
        self.secsInput = None
        self.minsInput = None
        self.colon2 = None
        self.colon1 = None
        self.container = None
        self.circularBg = None
        self.circularProgress = None
        self.circularProgressBarBase = None
        self.stopLabel = None
        self.stopButton = None
        self.stopIcon = None
        self.stopFrame = None
        self.startLabel = None
        self.startButton = None
        self.startIcon = None
        self.startFrame = None
        self.resetLabel = None
        self.resetButton = None
        self.resetIcon = None
        self.resetFrame = None
        self.frame = None
        self.title = None
        self.verticalLayout_2 = None
        self.verticalLayoutWidget = None
        self.windowBackground = None
        self.centralwidget = None
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

        # --- WINDOW BACKGROUND ---
        self.windowBackground = QtWidgets.QFrame(self.centralwidget)
        self.windowBackground.setGeometry(QtCore.QRect(9, 9, 776, 581))  # Setting size and position of the
        # window background
        self.windowBackground.setStyleSheet("QFrame {\n"
                                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                            "stop:0 rgba(51, 3, 57, 255), stop:1 rgba(51, 49, 151, 255));    \n "
                                            "}")  # Setting the style elements

        self.windowBackground.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)  # Setting the frame shape
        self.windowBackground.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.windowBackground.setObjectName("windowBackground")

        # --- VERTICAL LAYOUT WIDGET ---
        self.verticalLayoutWidget = QtWidgets.QWidget(self.windowBackground)  # Vertical Layout Widget
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        # --- VERTICAL LAYOUT WIDGET 2 ---
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)    # Vertical Layout Widget 2
        self.verticalLayout_2.setContentsMargins(20, 15, 0, 0)  # Setting margins for the vertical layout
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # --- COUNTDOWN TIMER TITLE ---
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

        # --- PARENT FRAME FOR BUTTONS ---
        self.frame = QtWidgets.QFrame(self.windowBackground)  # Parent Frame for the control buttons
        self.frame.setGeometry(QtCore.QRect(9, 400, 751, 181))  # Setting the size and position
        self.frame.setStyleSheet("QFrame {\n"
                                 "    background-color: transparent;\n"
                                 "}")  # Setting the style elements
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)  # Setting the frame shape
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")  # Setting the object name

        # --- FRAME FOR RESET BUTTON ---
        self.resetFrame = QtWidgets.QFrame(self.frame)  # Frame for the reset button
        self.resetFrame.setGeometry(QtCore.QRect(131, 10, 150, 150))  # Setting the size and position
        self.resetFrame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))  # Setting the cursor
        # shape to pointing hand
        self.resetFrame.setStyleSheet("QFrame {\n"
                                      "    background-color: transparent;\n"
                                      "}")  # Setting the style elements
        self.resetFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)  # Setting the frame shape
        self.resetFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.resetFrame.setObjectName("resetFrame")

        # --- RESET BUTTON ICON ---
        self.resetIcon = QtWidgets.QLabel(self.resetFrame)  # Label for the reset icon
        self.resetIcon.setGeometry(QtCore.QRect(50, 50, 40, 41))  # Setting the size and position
        self.resetIcon.setStyleSheet("QLabel {\n"
                                     "    background-color: transparent;\n"
                                     "}")  # Setting the style elements
        self.resetIcon.setText("")
        self.resetIcon.setPixmap(QtGui.QPixmap("assets/img/Reset.png"))  # Setting the image for the icon
        self.resetIcon.setScaledContents(True)  # Scaled Contents to make the image fit better
        self.resetIcon.setObjectName("resetIcon")

        # --- RESET BUTTON ---
        self.resetButton = QtWidgets.QPushButton(self.resetFrame)   # Reset Button
        self.resetButton.setGeometry(QtCore.QRect(19, 19, 100, 100))    # Setting the size and position
        self.resetButton.setStyleSheet("QPushButton {\n"
                                       "    border-radius: 50px;\n"
                                       "    border: 2px solid rgba(255, 255, 255,0.3);\n"
                                       "    color: white;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    border: 2px solid rgba(255, 255, 255,0.6);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    border: 2px solid rgba(255, 255, 255,0.3);\n"
                                       "}")     # Setting the style elements

        self.resetButton.setText("")
        self.resetButton.setObjectName("resetButton")

        # --- RESET LABEL ---
        self.resetLabel = QtWidgets.QLabel(self.resetFrame)     # Reset Label
        self.resetLabel.setGeometry(QtCore.QRect(44, 130, 49, 16))      # Setting the size and position
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.resetLabel.setFont(font)
        self.resetLabel.setStyleSheet("QLabel {\n"
                                      "    background-color: transparent;\n"
                                      "    color: rgba(255, 255, 255, 0.6);\n"
                                      "}")      # Setting the style elements
        self.resetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resetLabel.setObjectName("resetLabel")

        # --- FRAME FOR START BUTTON ---
        self.startFrame = QtWidgets.QFrame(self.frame)      # Start Frame
        self.startFrame.setGeometry(QtCore.QRect(298, 10, 150, 150))        # Setting the size and position
        self.startFrame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.startFrame.setStyleSheet("QFrame {\n"
                                      "    background-color: transparent;\n"
                                      "}")      # Setting the style elements
        self.startFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)   # Setting the frame shape
        self.startFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.startFrame.setObjectName("startFrame")

        # --- START ICON ---
        self.startIcon = QtWidgets.QLabel(self.startFrame)      # Label for the start icon
        self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))    # Setting the size and position
        self.startIcon.setStyleSheet("QLabel {\n"
                                     "    background-color: transparent;\n"
                                     "}\n"
                                     "QLabel:pressed {\n"
                                     "    transform: scale(0.8);\n"
                                     "}")       # Setting the style elements
        self.startIcon.setText("")
        self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))      # Setting start icon to the label
        self.startIcon.setScaledContents(True)
        self.startIcon.setObjectName("startIcon")

        # --- START BUTTON ---
        self.startButton = QtWidgets.QPushButton(self.startFrame)   # Start Button
        self.startButton.setGeometry(QtCore.QRect(26, 19, 100, 100))    # Setting the size and position
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.startButton.setStyleSheet("QPushButton {\n"
                                       "    border-radius: 50px;\n"
                                       "    background-color: rgba(255, 255, 255,0.3);\n"
                                       "    color: white;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgba(255, 255, 255,0.4);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgba(255, 255, 255,0.2);\n"
                                       "}")     # Setting the style elements
        self.startButton.setText("")
        self.startButton.setObjectName("startButton")

        # --- START LABEL ---
        self.startLabel = QtWidgets.QLabel(self.startFrame)     # Start Label
        self.startLabel.setGeometry(QtCore.QRect(50, 130, 49, 16))      # Setting the size and position
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.startLabel.setFont(font)
        self.startLabel.setStyleSheet("QLabel {\n"
                                      "    background-color: transparent;\n"
                                      "    color: rgba(255, 255, 255, 0.6);\n"
                                      "}")      # Setting the style elements
        self.startLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)       # Setting alignment
        self.startLabel.setObjectName("startLabel")

        # --- STOP FRAME ---
        self.stopFrame = QtWidgets.QFrame(self.frame)       # Parent frame for the stop button
        self.stopFrame.setGeometry(QtCore.QRect(465, 10, 150, 150))     # Setting the size and position
        self.stopFrame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stopFrame.setStyleSheet("QFrame {\n"
                                     "    background-color: transparent;\n"
                                     "}")       # Setting the style elements
        self.stopFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)    # Setting the frame shape
        self.stopFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.stopFrame.setObjectName("stopFrame")

        # --- STOP ICON ---
        self.stopIcon = QtWidgets.QLabel(self.stopFrame)        # Label for the stop icon
        self.stopIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))     # Setting the size and position
        self.stopIcon.setStyleSheet("QLabel {\n"
                                    "    background-color: transparent;\n"
                                    "}")        # Setting the style elements
        self.stopIcon.setText("")
        self.stopIcon.setPixmap(QtGui.QPixmap("assets/img/Stop.png"))   # Setting stop icon to the label
        self.stopIcon.setScaledContents(True)
        self.stopIcon.setObjectName("stopIcon")

        # --- STOP BUTTON ---
        self.stopButton = QtWidgets.QPushButton(self.stopFrame)     # Stop Button
        self.stopButton.setGeometry(QtCore.QRect(29, 19, 100, 100))     # Setting the size and position
        self.stopButton.setStyleSheet("QPushButton {\n"
                                      "    border-radius: 50px;\n"
                                      "    border: 2px solid rgba(255, 255, 255,0.3);\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    border: 2px solid rgba(255, 255, 255,0.6);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    border: 2px solid rgba(255, 255, 255,0.3);\n"
                                      "}")      # Setting the style elements
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")

        # --- STOP LABEL ---
        self.stopLabel = QtWidgets.QLabel(self.stopFrame)   # Stop Label
        self.stopLabel.setGeometry(QtCore.QRect(54, 130, 49, 16))   # Setting the size and position
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.stopLabel.setFont(font)
        self.stopLabel.setStyleSheet("QLabel {\n"
                                     "    background-color: transparent;\n"
                                     "    color: rgba(255, 255, 255, 0.6);\n"
                                     "}")   # Setting the style elements
        self.stopLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stopLabel.setObjectName("stopLabel")

        # --- PROGRESS BAR BASE ---
        self.circularProgressBarBase = QtWidgets.QFrame(self.windowBackground)  # Circular Progress Bar Base
        self.circularProgressBarBase.setGeometry(QtCore.QRect(219, 76, 320, 320))   # Setting the size and position
        self.circularProgressBarBase.setStyleSheet("QFrame {\n"
                                                   "    background-color: transparent;\n"
                                                   "}")     # Setting the style elements
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)      # Setting the frame shape
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")

        # --- CIRCULAR PROGRESS BAR ---
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBarBase)      # Circular Progress Bar
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 300, 300))       # Setting the size and position
        self.circularProgress.setStyleSheet("QFrame {\n"
                                            "    border-radius: 150px;\n"
                                            "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:1.000 "
                                            "rgba(0, 170, 255, 0), stop:1.001 rgba(208, 158, 230, 255));\n "
                                            "}")        # Setting the style elements
        self.circularProgress.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)     # Setting the frame shape
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circularProgress.setObjectName("circularProgress")

        # --- CIRCULAR BACKGROUND ---
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)        # Circular Background
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 300, 300))     # Setting the size and position
        self.circularBg.setStyleSheet("QFrame {\n"
                                      "    border-radius: 150px;\n"
                                      "    background-color: rgba(255, 255, 255, 0.2);\n"
                                      "}")      # Setting the style elements
        self.circularBg.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)       # Setting the frame shape
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circularBg.setObjectName("circularBg")

        # --- PROGRESS BAR CONTAINER ---
        self.container = QtWidgets.QFrame(self.circularProgressBarBase)     # Progress Bar Container
        self.container.setGeometry(QtCore.QRect(20, 20, 280, 280))      # Setting the size and position
        self.container.setStyleSheet("QFrame {\n"
                                     "    border-radius: 140px;\n"
                                     "    background-color: rgb(23, 20, 90);\n"
                                     "}")       # Setting the style elements
        self.container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)    # Setting the frame shape
        self.container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.container.setObjectName("container")

        # --- COLON 1 ---
        self.colon1 = QtWidgets.QLabel(self.container)      # Colon 1
        self.colon1.setGeometry(QtCore.QRect(83, 4, 16, 271))   # Setting the size and position
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(32)
        self.colon1.setFont(font)
        self.colon1.setStyleSheet("QLabel {\n"
                                  "    color: rgba(255, 255, 255, 0.9);\n"
                                  "    background-color: transparent;\n"
                                  "}")      # Setting the style elements
        self.colon1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.colon1.setObjectName("colon1")

        # --- COLON 2 ---
        self.colon2 = QtWidgets.QLabel(self.container)      # Colon 2
        self.colon2.setGeometry(QtCore.QRect(166, 4, 16, 271))      # Setting the size and position
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(32)
        self.colon2.setFont(font)
        self.colon2.setStyleSheet("QLabel { \n"
                                  "    background-color: transparent;\n"
                                  "    color: white;\n"
                                  "}")      # Setting the style elements
        self.colon2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)   # Setting the alignment
        self.colon2.setObjectName("colon2")

        # --- MINUTES INPUT ---
        self.minsInput = QtWidgets.QLineEdit(self.container)    # Minutes Input
        self.minsInput.setGeometry(QtCore.QRect(88, -1, 91, 281))   # Setting the size and position
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        self.minsInput.setFont(font)
        self.minsInput.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 140px;\n"
                                     "    background-color: transparent;\n"
                                     "    color: rgba(255 ,255, 255, 0.9);\n"
                                     "}")   # Setting the size elements
        self.minsInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)    # Setting the alignment
        self.minsInput.setPlaceholderText("00")     # Initial Placeholder Text
        self.minsInput.setObjectName("minsInput")

        # --- SECONDS INPUT ---
        self.secsInput = QtWidgets.QLineEdit(self.container)    # Seconds Input
        self.secsInput.setGeometry(QtCore.QRect(177, -1, 91, 281))      # Setting the size and position
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        self.secsInput.setFont(font)
        self.secsInput.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 140px;\n"
                                     "    background-color: transparent;\n"
                                     "    color: rgba(255 ,255, 255, 0.9);\n"
                                     "}")       # Setting the style elements
        self.secsInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.secsInput.setPlaceholderText("00")     # Initial Placeholder Text
        self.secsInput.setObjectName("secsInput")

        # --- HOURS INPUT ---
        self.hrsInput = QtWidgets.QLineEdit(self.container)     # Hours Input
        self.hrsInput.setGeometry(QtCore.QRect(0, -1, 91, 281))     # Setting the size and position
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        self.hrsInput.setFont(font)
        self.hrsInput.setStyleSheet("QLineEdit {\n"
                                    "    border-radius: 140px;\n"
                                    "    background-color: transparent;\n"
                                    "    color: rgba(255 ,255, 255, 0.9);\n"
                                    "}")    # Setting the style elements
        self.hrsInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)     # Setting the alignment
        self.hrsInput.setPlaceholderText("00")      # Initial Placeholder Text
        self.hrsInput.setObjectName("hrsInput")

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()

        # --- FRAME FOR MESSAGE BOX ---
        self.messageFrame = QtWidgets.QFrame(self.centralwidget)    # Frame for message box
        self.messageFrame.setGeometry(QtCore.QRect(430, -110, 341, 81))     # Setting the size and position
        self.messageFrame.setStyleSheet("")
        self.messageFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)     # Setting the frame shape
        self.messageFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.messageFrame.setObjectName("messageFrame")

        # --- MESSAGE BOX ANIMATIONS ---
        self.msgshow = QPropertyAnimation(self.messageFrame, b"pos")    # Message showing box
        self.msgshow.setEndValue(QPoint(430, 10))   # Setting the end value of the position of the message box
        self.msghide = QPropertyAnimation(self.messageFrame, b"pos")    # Message hiding box
        self.msghide.setEndValue(QPoint(430, -100))     # Setting the end value of the position of the message box

        # --- MESSAGE BOX CONTAINER ---
        self.messageContainer = QtWidgets.QFrame(self.messageFrame)     # Message container
        self.messageContainer.setGeometry(QtCore.QRect(-1, 10, 341, 61))    # Setting the size and position
        self.messageContainer.setStyleSheet("QFrame {\n"
                                            "    background-color: rgba(255, 255, 255, 0.3);\n"
                                            "    border-radius: 15px;\n"
                                            "}")    # Setting the style elements
        self.messageContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.messageContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.messageContainer.setObjectName("messageContainer")

        # --- MESSAGE BOX ERROR ICON ---
        self.errorIcon = QtWidgets.QLabel(self.messageContainer)    # Error icon
        self.errorIcon.setGeometry(QtCore.QRect(16, 14, 32, 32))    # Setting the size and position
        self.errorIcon.setStyleSheet("QLabel {\n"
                                     "    background-color: transparent;\n"
                                     "}    ")   # Setting the style elements
        self.errorIcon.setText("")
        self.errorIcon.setPixmap(QtGui.QPixmap("assets/img/error.png"))     # Setting the error icon to the label
        self.errorIcon.setScaledContents(True)
        self.errorIcon.setObjectName("errorIcon")

        # --- MESSAGE BOX ERROR TEXT ---
        self.errorText = QtWidgets.QLabel(self.messageContainer)    # Error text
        self.errorText.setGeometry(QtCore.QRect(66, 10, 261, 41))   # Setting the size and position
        font = QtGui.QFont()
        font.setBold(True)
        self.errorText.setFont(font)
        self.errorText.setStyleSheet("QFrame {\n"
                                     "    background-color: transparent;\n"
                                     "    color: rgba(255, 255, 255, 0.8)\n"
                                     "}")   # Setting the style elements
        self.errorText.setObjectName("errorText")

        # --- CLOSE MESSAGE ICON ---
        self.closeMsgIcon = QtWidgets.QLabel(self.messageContainer)     # Close message icon
        self.closeMsgIcon.setGeometry(QtCore.QRect(318, 9, 8, 8))   # Setting the size and position
        self.closeMsgIcon.setStyleSheet("QLabel {\n"
                                        "    background-color: transparent;\n"
                                        "}\n"
                                        "")     # Setting the style elements
        self.closeMsgIcon.setText("")
        self.closeMsgIcon.setPixmap(QtGui.QPixmap("assets/img/close.png"))  # Setting close icon to the label
        self.closeMsgIcon.setScaledContents(True)
        self.closeMsgIcon.setObjectName("closeMsgIcon")

        # --- CLOSE MESSAGE BUTTON ---
        self.closeMsgButton = QtWidgets.QPushButton(self.messageContainer)      # Close Message button
        self.closeMsgButton.setGeometry(QtCore.QRect(318, 9, 8, 8))     # Setting the size and position
        self.closeMsgButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))  # Setting the cursor
        # type to pointing hand
        self.closeMsgButton.setStyleSheet("QPushButton {\n"
                                          "    border: none;\n"
                                          "    background-color: transparent;\n"
                                          "}")  # Setting the style elements
        self.closeMsgButton.setText("")
        self.closeMsgButton.setObjectName("closeMsgButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Countdown Timer"))  # Setting the Window Title
        self.title.setText(_translate("MainWindow", "Countdown Timer"))     # Setting the title text
        self.resetLabel.setText(_translate("MainWindow", "Reset"))      # Setting the reset label text
        self.startLabel.setText(_translate("MainWindow", "Start"))      # Setting the start label text
        self.stopLabel.setText(_translate("MainWindow", "Stop"))        # Setting the stop label text
        self.colon1.setText(_translate("MainWindow", ":"))
        self.colon2.setText(_translate("MainWindow", ":"))
        self.startButton.clicked.connect(self.start_clicked)    # Connecting the function to the start button
        self.stopButton.clicked.connect(self.stop_clicked)      # Connecting the function to the stop button
        self.resetButton.clicked.connect(self.reset_clicked)    # Connecting the function to the reset button
        self.closeMsgButton.clicked.connect(self.close_msg_clicked)     # Connecting the function to the close button
        self.errorText.setText(_translate("MainWindow", "An Unknown Error Occurred. Please try again."))    # Setting
        # the error label text

    # --- TIMER STARTING THREAD ---
    def start_thread(self):
        try:
            t = threading.Thread(target=self.start)
            t.start()
        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

    # --- TIMER RESUMING THREAD ---
    def resume_thread(self):
        try:
            t1 = threading.Thread(target=self.resume)
            t1.start()
        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

    # --- TIMER FUNCTIONS ---
    def start(self):
        try:
            # --- TIME CALCULATION ---
            self.stopFrame.setEnabled(True)     # Enabling the stop button
            self.resetFrame.setEnabled(True)    # Enabling the reset button
            self.stop_loop = False

            self.total_secs = self._hrs * 3600 + self._mins * 60 + self._secs   # Calculating total seconds
            self.temp = self.total_secs     # Variable to hold the original value of the total seconds

            # --- CIRCULAR PROGRESS BAR SETUP ---
            self.circularProgress.setStyleSheet("QFrame {\n"
                                                "    border-radius: 150px;\n"
                                                "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, "
                                                "stop:1.000 "
                                                "rgba(0, 170, 255, 0), stop:1.000 rgba(208, 158, 230, 255));\n "
                                                "}")    # Setting the bar to full value

            self.step = 1.001 / self.temp   # To calculate the distance covered by the bar in 1 second
            self.stop_2 = 0.001     # Original value of stop_2 to make it start from full bar

            while self.total_secs > 0 and not self.stop_loop:

                # --- CIRCULAR PROGRESS BAR ANIMATION ---
                self.stop_2 = round(self.stop_2 + self.step, 3)
                self.stop_1 = round(self.stop_2 - 0.001, 3)
                self.circularProgress.setStyleSheet("QFrame {\n"
                                                    "    border-radius: 150px;\n"
                                                    f"    background-color: qconicalgradient(cx:0.5, cy:0.5, "
                                                    f"angle:90, stop:{self.stop_1} rgba(0, 170, 255, 0), "
                                                    f"stop:{self.stop_2} rgba(208, 158, 230, 255));\n "
                                                    "}")    # New stylesheet with updated stop values

                # --- TIME UPDATION ---
                self.total_secs -= 1
                mins, secs = divmod(self.total_secs, 60)    # New value of seconds
                hrs, mins = divmod(mins, 60)    # New value of hours and minutes

                # --- DISABLING INPUT FIELDS ---
                self.hrsInput.setDisabled(True)
                self.minsInput.setDisabled(True)
                self.secsInput.setDisabled(True)

                # --- ASSIGNING AND DISPLAYING THE NEW VALUES OF HOURS, MINUTES, SECONDS ---
                self.hrsInput.setText(str(hrs).zfill(2))
                self.minsInput.setText(str(mins).zfill(2))
                self.secsInput.setText(str(secs).zfill(2))

                time.sleep(1)   # 1 second delay

            if not self.stop_loop:

                # --- ENABLING THE INPUT FIELDS ---
                self.hrsInput.setEnabled(True)
                self.minsInput.setEnabled(True)
                self.secsInput.setEnabled(True)

                # --- UPDATING THE START ICON AND LABEL ---
                self.startLabel.setText("Start")
                self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
                self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))

                playsound('assets/alerts/alert.wav')    # Alert sound

                if platform.system() == 'Windows':  # Toast Notification once the timer is done
                    toast = ToastNotifier()
                    toast.show_toast("Countdown Timer", "Time is Up!", duration=10)

        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

    def pause(self):
        try:
            self.stopFrame.setEnabled(True)     # Enabling the Stop button

            self.stop_loop = True

            self.total_secs = self._hrs * 3600 + self._mins * 60 + self._secs   # Calculating the present value of total
            # seconds.
            mins2, secs2 = divmod(self.total_secs, 60)
            hrs2, mins2 = divmod(mins2, 60)

            # --- ASSIGNING AND DISPLAYING THE TIME VALUES WHEN THE TIMER IS PAUSED ---
            self.hrsInput.setText(str(hrs2).zfill(2))
            self.minsInput.setText(str(mins2).zfill(2))
            self.secsInput.setText(str(secs2).zfill(2))

        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

    def resume(self):
        try:
            # --- ENABLING THE STOP AND RESET BUTTONS ---
            self.stopFrame.setEnabled(True)
            self.resetFrame.setEnabled(True)

            self.stop_loop = False

            self.total_secs = self._hrs * 3600 + self._mins * 60 + self._secs

            while self.total_secs > 0 and not self.stop_loop:

                # --- CIRCULAR PROGRESS BAR ANIMATION ---
                self.stop_2 = round(self.stop_2 + self.step, 3)
                self.stop_1 = round(self.stop_2 - 0.001, 3)
                self.circularProgress.setStyleSheet("QFrame {\n"
                                                    "    border-radius: 150px;\n"
                                                    f"    background-color: qconicalgradient(cx:0.5, cy:0.5, "
                                                    f"angle:90, stop:{self.stop_1} rgba(0, 170, 255, 0), "
                                                    f"stop:{self.stop_2} rgba(208, 158, 230, 255));\n "
                                                    "}")

                # --- TIME UPDATION ---
                self.total_secs -= 1
                mins, secs = divmod(self.total_secs, 60)
                hrs, mins = divmod(mins, 60)

                # --- DISABLING THE INPUT FIELDS ---
                self.hrsInput.setDisabled(True)
                self.minsInput.setDisabled(True)
                self.secsInput.setDisabled(True)

                # --- ASSIGNING AND DISPLAYING THE NEW TIME VALUES ---
                self.hrsInput.setText(str(hrs).zfill(2))
                self.minsInput.setText(str(mins).zfill(2))
                self.secsInput.setText(str(secs).zfill(2))

                time.sleep(1)   # 1 second delay

            if not self.stop_loop:

                # --- ENABLING THE INPUT FIELDS ---
                self.hrsInput.setEnabled(True)
                self.minsInput.setEnabled(True)
                self.secsInput.setEnabled(True)

                # --- UPDATING THE START ICON AND LABEL ---
                self.startLabel.setText("Start")
                self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
                self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))

                playsound('assets/alerts/alert.wav')   # Alert Sound

                if platform.system() == 'Windows':  # Toast Notification once the timer is done
                    toast = ToastNotifier()
                    toast.show_toast("Countdown Timer", "Time is Up!", duration=10)

        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

    def stop(self):
        try:
            self.circularProgress.setStyleSheet("QFrame {\n"
                                                "    border-radius: 150px;\n"
                                                "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, "
                                                "stop:1.000 "
                                                "rgba(0, 170, 255, 0), stop:1.001 rgba(208, 158, 230, 255));\n "
                                                "}")    # Resetting the progress bar to the initial value

            # --- TIME UPDATION ----
            self.stop_loop = True
            mins1, secs1 = divmod(self.temp, 60)
            hrs1, mins1 = divmod(mins1, 60)

            # --- ASSIGNING AND DISPLAYING THE INITIAL TIME VALUES ---
            self.hrsInput.setText(str(hrs1).zfill(2))
            self.minsInput.setText(str(mins1).zfill(2))
            self.secsInput.setText(str(secs1).zfill(2))

            # --- ENABLING THE INPUT FIELDS ---
            self.hrsInput.setEnabled(True)
            self.minsInput.setEnabled(True)
            self.secsInput.setEnabled(True)

            # --- UPDATING THE START ICON AND LABEL ---
            self.startLabel.setText("Start")
            self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
            self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))

        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

    def reset(self):
        try:
            self.circularProgress.setStyleSheet("QFrame {\n"
                                                "    border-radius: 150px;\n"
                                                "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, "
                                                "stop:1.000 "
                                                "rgba(0, 170, 255, 0), stop:1.001 rgba(208, 158, 230, 255));\n "
                                                "}")    # Resetting the progress bar to the initial value

            self.total_secs = 0
            self.stop_loop = True

            # --- RESETTING THE INPUT FIELD VALUES ---
            self.hrsInput.setText("00")
            self.minsInput.setText("00")
            self.secsInput.setText("00")

            # --- ENABLING THE INPUT FIELDS ---
            self.hrsInput.setEnabled(True)
            self.minsInput.setEnabled(True)
            self.secsInput.setEnabled(True)

            # --- UPDATING THE START ICON AND LABEL ---
            self.startLabel.setText("Start")
            self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
            self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))

            self.stopFrame.setDisabled(True)    # Disabling the stop button

        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

    def start_clicked(self):
        try:
            if self.startLabel.text() == "Start":   # If the Start label is 'Start'
                # --- USER INPUT ---
                self._hrs = self.hrsInput.text() or "00"
                self._mins = self.minsInput.text() or "00"
                self._secs = self.secsInput.text() or "00"

                if self._hrs.isdigit() and self._mins.isdigit() and self._secs.isdigit():
                    # --- CHANGING THE START ICON AND LABEL TO PAUSE ---
                    self.startLabel.setText("Pause")
                    self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Pause.png"))
                    self.startIcon.setGeometry(QtCore.QRect(56, 50, 40, 39))

                    self._hrs = int(self._hrs)
                    self._mins = int(self._mins)
                    self._secs = int(self._secs)

                    self.start_thread()     # function call

                else:
                    # --- DISABLING STOP AND RESET BUTTONS ---
                    self.stopFrame.setDisabled(True)
                    self.resetFrame.setDisabled(True)

                    self.errorText.setText("Enter a valid integer value!")
                    self.msgshow.start()    # function call

            elif self.startLabel.text() == 'Pause':     # If the Start label is 'Pause'
                # --- CHANGING THE START ICON AND LABEL TO RESUME ---
                self.startLabel.setText("Resume")
                self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Play.png"))
                self.startIcon.setGeometry(QtCore.QRect(60, 50, 40, 39))

                # --- USER INPUT ---
                self._hrs = int(self.hrsInput.text() or "00")
                self._mins = int(self.minsInput.text() or "00")
                self._secs = int(self.secsInput.text() or "00")

                self.pause()    # function call

            elif self.startLabel.text() == 'Resume':    # If the Start label is 'Resume'
                # --- CHANGING THE START ICON AND LABEL TO PAUSE ---
                self.startLabel.setText("Pause")
                self.startIcon.setPixmap(QtGui.QPixmap("assets/img/Pause.png"))
                self.startIcon.setGeometry(QtCore.QRect(56, 50, 40, 39))

                # --- USER INPUT ---
                self._hrs = int(self.hrsInput.text() or "00")
                self._mins = int(self.minsInput.text() or "00")
                self._secs = int(self.secsInput.text() or "00")

                self.resume_thread()    # function call

        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

    def stop_clicked(self):
        try:
            self.stop()

        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

    def reset_clicked(self):
        try:
            self.reset()

        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

    def close_msg_clicked(self):
        try:
            self.msghide.start()

        except:
            self.errorText.setText("An Unknown Error Occurred. Please try again!")
            self.msgshow.start()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
