# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDial, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QSplitter, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1242, 655)
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        iconThemeName = u"edit-find-replace"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.picture = QLabel(self.centralwidget)
        self.picture.setObjectName(u"picture")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.picture.sizePolicy().hasHeightForWidth())
        self.picture.setSizePolicy(sizePolicy1)
        self.picture.setMinimumSize(QSize(0, 0))
        self.picture.setBaseSize(QSize(0, 0))
        self.picture.setMouseTracking(True)
        self.picture.setFrameShape(QFrame.StyledPanel)
        self.picture.setFrameShadow(QFrame.Sunken)
        self.picture.setLineWidth(1)
        self.picture.setMidLineWidth(0)
        self.picture.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.picture.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.picture)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loca_in = QPushButton(self.groupBox)
        self.loca_in.setObjectName(u"loca_in")
        self.loca_in.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        iconThemeName = u"document-open"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.loca_in.setIcon(icon1)

        self.verticalLayout.addWidget(self.loca_in)

        self.umiste = QPlainTextEdit(self.groupBox)
        self.umiste.setObjectName(u"umiste")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.umiste.sizePolicy().hasHeightForWidth())
        self.umiste.setSizePolicy(sizePolicy3)
        self.umiste.setMinimumSize(QSize(0, 10))
        self.umiste.setBaseSize(QSize(0, 10))

        self.verticalLayout.addWidget(self.umiste)

        self.with_next = QCheckBox(self.groupBox)
        self.with_next.setObjectName(u"with_next")
        self.with_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.with_next.setChecked(False)

        self.verticalLayout.addWidget(self.with_next)

        self.loader = QPushButton(self.groupBox)
        self.loader.setObjectName(u"loader")
        self.loader.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        iconThemeName = u"image-x-generic"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.loader.setIcon(icon2)

        self.verticalLayout.addWidget(self.loader)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.last = QPushButton(self.groupBox)
        self.last.setObjectName(u"last")
        self.last.setMinimumSize(QSize(0, 50))
        self.last.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        iconThemeName = u"go-previous"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.last.setIcon(icon3)

        self.horizontalLayout.addWidget(self.last)

        self.next = QPushButton(self.groupBox)
        self.next.setObjectName(u"next")
        self.next.setEnabled(True)
        self.next.setMinimumSize(QSize(0, 50))
        self.next.setCursor(QCursor(Qt.PointingHandCursor))
        self.next.setAutoFillBackground(False)
        icon4 = QIcon()
        iconThemeName = u"go-next"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.next.setIcon(icon4)
        self.next.setFlat(False)

        self.horizontalLayout.addWidget(self.next)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.loca_out = QPushButton(self.groupBox_2)
        self.loca_out.setObjectName(u"loca_out")
        self.loca_out.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        iconThemeName = u"folder-open"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.loca_out.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.loca_out)

        self.umiste_out = QPlainTextEdit(self.groupBox_2)
        self.umiste_out.setObjectName(u"umiste_out")
        sizePolicy3.setHeightForWidth(self.umiste_out.sizePolicy().hasHeightForWidth())
        self.umiste_out.setSizePolicy(sizePolicy3)
        self.umiste_out.setMinimumSize(QSize(0, 10))
        self.umiste_out.setBaseSize(QSize(0, 10))

        self.verticalLayout_2.addWidget(self.umiste_out)

        self.rewrite = QCheckBox(self.groupBox_2)
        self.rewrite.setObjectName(u"rewrite")
        self.rewrite.setCursor(QCursor(Qt.PointingHandCursor))
        self.rewrite.setMouseTracking(True)

        self.verticalLayout_2.addWidget(self.rewrite)

        self.saver = QPushButton(self.groupBox_2)
        self.saver.setObjectName(u"saver")
        self.saver.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.saver.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.saver)

        self.reload = QPushButton(self.groupBox_2)
        self.reload.setObjectName(u"reload")
        self.reload.setMinimumSize(QSize(0, 50))
        self.reload.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        iconThemeName = u"document-revert"
        if QIcon.hasThemeIcon(iconThemeName):
            icon7 = QIcon.fromTheme(iconThemeName)
        else:
            icon7.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.reload.setIcon(icon7)

        self.verticalLayout_2.addWidget(self.reload)

        self.splitter.addWidget(self.groupBox_2)
        self.groupBox_3 = QGroupBox(self.splitter)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.marker = QPushButton(self.groupBox_3)
        self.marker.setObjectName(u"marker")
        self.marker.setCursor(QCursor(Qt.PointingHandCursor))
        self.marker.setIcon(icon)
        self.marker.setCheckable(True)

        self.verticalLayout_9.addWidget(self.marker)

        self.tabWidget = QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dial_2 = QDial(self.groupBox_5)
        self.dial_2.setObjectName(u"dial_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.dial_2.sizePolicy().hasHeightForWidth())
        self.dial_2.setSizePolicy(sizePolicy4)
        self.dial_2.setMinimum(1)
        self.dial_2.setMaximum(11)
        self.dial_2.setSingleStep(1)
        self.dial_2.setValue(6)

        self.verticalLayout_5.addWidget(self.dial_2)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.dial = QDial(self.groupBox_6)
        self.dial.setObjectName(u"dial")
        sizePolicy4.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy4)
        self.dial.setMinimum(1)
        self.dial.setMaximum(39)
        self.dial.setValue(20)

        self.verticalLayout_4.addWidget(self.dial)


        self.horizontalLayout_2.addWidget(self.groupBox_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy2.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy2)
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.slider2 = QSlider(self.groupBox_7)
        self.slider2.setObjectName(u"slider2")
        self.slider2.setCursor(QCursor(Qt.ArrowCursor))
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(8)
        self.slider2.setValue(2)
        self.slider2.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.slider2)


        self.verticalLayout_8.addWidget(self.groupBox_7)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.invert = QCheckBox(self.tab_2)
        self.invert.setObjectName(u"invert")
        self.invert.setCursor(QCursor(Qt.PointingHandCursor))
        self.invert.setChecked(True)

        self.verticalLayout_11.addWidget(self.invert)

        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horiz = QPushButton(self.groupBox_8)
        self.horiz.setObjectName(u"horiz")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.horiz.sizePolicy().hasHeightForWidth())
        self.horiz.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.horiz, 1, 1, 1, 1)

        self.verti = QPushButton(self.groupBox_8)
        self.verti.setObjectName(u"verti")
        sizePolicy5.setHeightForWidth(self.verti.sizePolicy().hasHeightForWidth())
        self.verti.setSizePolicy(sizePolicy5)
        self.verti.setMinimumSize(QSize(0, 35))
        self.verti.setBaseSize(QSize(0, 50))

        self.gridLayout.addWidget(self.verti, 1, 2, 1, 1)

        self.counter = QPushButton(self.groupBox_8)
        self.counter.setObjectName(u"counter")
        sizePolicy5.setHeightForWidth(self.counter.sizePolicy().hasHeightForWidth())
        self.counter.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.counter, 0, 1, 1, 1)

        self.clock = QPushButton(self.groupBox_8)
        self.clock.setObjectName(u"clock")
        sizePolicy5.setHeightForWidth(self.clock.sizePolicy().hasHeightForWidth())
        self.clock.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.clock, 0, 2, 1, 1)


        self.verticalLayout_11.addWidget(self.groupBox_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ingroup = QSpinBox(self.tab_2)
        self.ingroup.setObjectName(u"ingroup")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ingroup.sizePolicy().hasHeightForWidth())
        self.ingroup.setSizePolicy(sizePolicy6)
        self.ingroup.setMinimum(1)
        self.ingroup.setMaximum(15)
        self.ingroup.setSingleStep(1)
        self.ingroup.setValue(2)

        self.horizontalLayout_3.addWidget(self.ingroup)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.splitter.addWidget(self.groupBox_3)
        self.groupBox_4 = QGroupBox(self.splitter)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.info = QTextBrowser(self.groupBox_4)
        self.info.setObjectName(u"info")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy7)
        self.info.setMinimumSize(QSize(200, 0))
        self.info.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_10.addWidget(self.info)

        self.splitter.addWidget(self.groupBox_4)

        self.verticalLayout_3.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.loca_in, self.umiste)
        QWidget.setTabOrder(self.umiste, self.with_next)
        QWidget.setTabOrder(self.with_next, self.loader)
        QWidget.setTabOrder(self.loader, self.next)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.picture.setToolTip(QCoreApplication.translate("MainWindow", u"hlavn\u00ed vokno pro opr\u00e1ski\n"
"(funguje tady Ctrl+Z btw.)", None))
#endif // QT_CONFIG(tooltip)
        self.picture.setText("")
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("MainWindow", u"tady se \u0159e\u0161\u00ed v\u0161echno ohledn\u011b vstupn\u00edch dat", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Vstup", None))
#if QT_CONFIG(tooltip)
        self.loca_in.setToolTip(QCoreApplication.translate("MainWindow", u"klasick\u00fd v\u00fdb\u011br souboru prohl\u00ed\u017ee\u010dem", None))
#endif // QT_CONFIG(tooltip)
        self.loca_in.setText(QCoreApplication.translate("MainWindow", u"Vybrat soubor", None))
#if QT_CONFIG(tooltip)
        self.umiste.setToolTip(QCoreApplication.translate("MainWindow", u"nebo i mo\u017enost p\u0159\u00edm\u00e9ho zad\u00e1n\u00ed adresy, je-li libo", None))
#endif // QT_CONFIG(tooltip)
        self.umiste.setPlainText(QCoreApplication.translate("MainWindow", u"/home/vachaj11/Documents/python/klik/test.npy", None))
#if QT_CONFIG(tooltip)
        self.with_next.setToolTip(QCoreApplication.translate("MainWindow", u"mo\u017enost automatick\u00e9ho ukl\u00e1d\u00e1n\u00ed pro speedrunnery", None))
#endif // QT_CONFIG(tooltip)
        self.with_next.setText(QCoreApplication.translate("MainWindow", u"ulo\u017eit s na\u010dten\u00edm dal\u0161\u00edho souboru", None))
#if QT_CONFIG(tooltip)
        self.loader.setToolTip(QCoreApplication.translate("MainWindow", u"na\u010dte soubor z v\u00fd\u0161e uveden\u00e9 adresy\n"
"(alias Control + R)", None))
#endif // QT_CONFIG(tooltip)
        self.loader.setText(QCoreApplication.translate("MainWindow", u"Na\u010d\u00edst(znovu)", None))
#if QT_CONFIG(tooltip)
        self.last.setToolTip(QCoreApplication.translate("MainWindow", u"na\u010dte dle n\u00e1zvu p\u0159edchoz\u00ed soubor\n"
"(pokud teda n\u011bjak\u00fd je)\n"
"(alias Control + A)", None))
#endif // QT_CONFIG(tooltip)
        self.last.setText(QCoreApplication.translate("MainWindow", u"P\u0159ede\u0161l\u00fd\n"
" soubor", None))
#if QT_CONFIG(tooltip)
        self.next.setToolTip(QCoreApplication.translate("MainWindow", u"na\u010dte dle n\u00e1zvu n\u00e1sleduj\u00edc\u00ed soubor\n"
"(pokud teda n\u011bjak\u00fd je)\n"
"(alias Control + D)", None))
#endif // QT_CONFIG(tooltip)
        self.next.setText(QCoreApplication.translate("MainWindow", u"Dal\u0161\u00ed\n"
"soubor", None))
#if QT_CONFIG(tooltip)
        self.groupBox_2.setToolTip(QCoreApplication.translate("MainWindow", u"kam se sypou naklikan\u00e1 data:", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"V\u00fdstup", None))
#if QT_CONFIG(tooltip)
        self.loca_out.setToolTip(QCoreApplication.translate("MainWindow", u"prohl\u00ed\u017ee\u010d soubor\u016f, klasika", None))
#endif // QT_CONFIG(tooltip)
        self.loca_out.setText(QCoreApplication.translate("MainWindow", u"Vybrat um\u00edst\u011bn\u00ed", None))
#if QT_CONFIG(tooltip)
        self.umiste_out.setToolTip(QCoreApplication.translate("MainWindow", u"ok\u00fdnko pro superusery", None))
#endif // QT_CONFIG(tooltip)
        self.umiste_out.setPlainText(QCoreApplication.translate("MainWindow", u"/home/vachaj11/Documents/python/klik/out", None))
#if QT_CONFIG(tooltip)
        self.rewrite.setToolTip(QCoreApplication.translate("MainWindow", u"d\u011bl\u00e1, co m\u00e1 v popisu pr\u00e1ce", None))
#endif // QT_CONFIG(tooltip)
        self.rewrite.setText(QCoreApplication.translate("MainWindow", u"p\u0159episovat ji\u017e ulo\u017een\u00e1 data", None))
#if QT_CONFIG(tooltip)
        self.saver.setToolTip(QCoreApplication.translate("MainWindow", u"v\u011bt\u0161inou ulo\u017e\u00ed naklikan\u00e1 data\n"
"(alias Control + S)", None))
#endif // QT_CONFIG(tooltip)
        self.saver.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit", None))
#if QT_CONFIG(tooltip)
        self.reload.setToolTip(QCoreApplication.translate("MainWindow", u"umo\u017e\u0148uje na\u010d\u00edst a nav\u00e1zat na d\u0159\u00edv\u011bj\u0161\u00ed pr\u00e1ci, nebo ji t\u0159eba zkontrolovat\n"
"(nen\u00ed mo\u017en\u00e9 aktivovat, kdy\u017e \u017e\u00e1dn\u00e1 d\u0159\u00edv\u011bj\u0161\u00ed pr\u00e1ce nen\u00ed)", None))
#endif // QT_CONFIG(tooltip)
        self.reload.setText(QCoreApplication.translate("MainWindow", u"Znovu na\u010d\u00edst d\u0159\u00edve ulo\u017een\u00e1 data\n"
"(p\u0159id\u00e1 k aktu\u00e1ln\u011b zobrazen\u00fdm datum)", None))
#if QT_CONFIG(tooltip)
        self.groupBox_3.setToolTip(QCoreApplication.translate("MainWindow", u"kone\u010dn\u011b to zaj\u00edmav\u00fd - klik\u00e1n\u00ed", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Ozna\u010dov\u00e1n\u00ed", None))
#if QT_CONFIG(tooltip)
        self.marker.setToolTip(QCoreApplication.translate("MainWindow", u"zapne klikac\u00ed m\u00f3d\n"
"(v retrospektiv\u011b celkem zbyte\u010dn\u00e1 funkce)\n"
"(net\u0159eba vyp\u00ednat)", None))
#endif // QT_CONFIG(tooltip)
        self.marker.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00edt ozna\u010dovat", None))
#if QT_CONFIG(tooltip)
        self.groupBox_5.setToolTip(QCoreApplication.translate("MainWindow", u"tady se h\u00fdbe s kontrastem", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Kontrast", None))
#if QT_CONFIG(tooltip)
        self.groupBox_6.setToolTip(QCoreApplication.translate("MainWindow", u"a tady s jasem", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Jas", None))
#if QT_CONFIG(tooltip)
        self.groupBox_7.setToolTip(QCoreApplication.translate("MainWindow", u"umo\u017en\u00ed vybrat jednu z mnoha colormap\n"
" moje obl\u00edben\u00e1 je mo\u017enost 3", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Zbarven\u00ed", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Barevn\u00e9 zobrazen\u00ed", None))
#if QT_CONFIG(tooltip)
        self.invert.setToolTip(QCoreApplication.translate("MainWindow", u"zm\u011bn\u00ed den v noc a noc v den", None))
#endif // QT_CONFIG(tooltip)
        self.invert.setText(QCoreApplication.translate("MainWindow", u"Invertovat hodnoty", None))
#if QT_CONFIG(tooltip)
        self.groupBox_8.setToolTip(QCoreApplication.translate("MainWindow", u"zde se v\u0161e p\u0159evrac\u00ed a rotuje", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Transformace", None))
#if QT_CONFIG(tooltip)
        self.horiz.setToolTip(QCoreApplication.translate("MainWindow", u"zrcadlit horizont\u00e1ln\u011b", None))
#endif // QT_CONFIG(tooltip)
        self.horiz.setText(QCoreApplication.translate("MainWindow", u"|", None))
#if QT_CONFIG(tooltip)
        self.verti.setToolTip(QCoreApplication.translate("MainWindow", u"zrcadlit vertik\u00e1ln\u011b", None))
#endif // QT_CONFIG(tooltip)
        self.verti.setText(QCoreApplication.translate("MainWindow", u"\u2015", None))
#if QT_CONFIG(tooltip)
        self.counter.setToolTip(QCoreApplication.translate("MainWindow", u"oto\u010dit proti sm\u011bru hodinov\u00fdch ru\u010di\u010dek", None))
#endif // QT_CONFIG(tooltip)
        self.counter.setText(QCoreApplication.translate("MainWindow", u"\u2b6f", None))
#if QT_CONFIG(tooltip)
        self.clock.setToolTip(QCoreApplication.translate("MainWindow", u"oto\u010dit po sm\u011bru hodinov\u00fdch ru\u010di\u010dek", None))
#endif // QT_CONFIG(tooltip)
        self.clock.setText(QCoreApplication.translate("MainWindow", u"\u2b6e", None))
#if QT_CONFIG(tooltip)
        self.ingroup.setToolTip(QCoreApplication.translate("MainWindow", u"pro zobecn\u011bn\u00ed funk\u010dnosti je mo\u017en\u00e9 nastavit po\u010det bod\u016f", None))
#endif // QT_CONFIG(tooltip)
        self.ingroup.setSuffix("")
        self.ingroup.setPrefix("")
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"pro zobecn\u011bn\u00ed funk\u010dnosti je mo\u017en\u00e9 nastavit po\u010det bod\u016f", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"po\u010det bod\u016f ve skupin\u011b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Ostatn\u00ed", None))
#if QT_CONFIG(tooltip)
        self.groupBox_4.setToolTip(QCoreApplication.translate("MainWindow", u"mal\u00fd n\u00e1hled do my\u0161lenkov\u00fdch proces\u016f programu", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Konzole", None))
#if QT_CONFIG(tooltip)
        self.info.setToolTip(QCoreApplication.translate("MainWindow", u"zde se poslu\u0161n\u011b hl\u00e1s\u00ed v\u0161echno d\u011bn\u00ed v pozad\u00ed\n"
"(ale trochu Pot\u011bmkinovsky jen tehdy, kdy\u017e to b\u011b\u017e\u00ed, jak m\u00e1,\n"
" jinak je t\u0159eba sledovat Pythonovskou konzoli)", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

