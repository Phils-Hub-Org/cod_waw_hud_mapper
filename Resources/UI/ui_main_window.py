# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windoweRXfxo.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGraphicsView, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QToolBar, QToolButton, QVBoxLayout, QWidget)
import Resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1387, 720)
        MainWindow.setMinimumSize(QSize(1120, 720))
        MainWindow.setStyleSheet(u"/* QMenuBar */\n"
"QMenuBar {\n"
"    background-color: #2e2e2e;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text */\n"
"    border-bottom: 1px solid #5b5e60;  /* Light gray border for separation */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent; /* Transparent background */\n"
"    padding: 6px 6px;             /* Padding for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"}\n"
"\n"
"QMenuBar::item:selected {          /* Hovered menu item */\n"
"    background-color: #4a90e2;     /* Light blue on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenuBar::item:pressed {           /* Pressed menu item */\n"
"    background-color: #3d78b2;     /* Darker blue on press */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"/* QMenu */\n"
"QMenu {\n"
"    background-color: #2e2e2e;     /* Dark gray background for menus */\n"
"    border: 1px solid #5b5e60;"
                        "     /* Light gray border */\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent; /* Transparent background for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"	padding: 6px;\n"
"    margin-left: 6px;             /* Padding for each menu item */\n"
"}\n"
"\n"
"QMenu::item:selected {             /* Hovered menu item */\n"
"    background-color: #4a90e2;     /* Light blue background on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenu::item:pressed {              /* Pressed menu item */\n"
"    background-color: #3d78b2;     /* Darker blue background on press */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: #5b5e60;     /* Light gray separator between items */\n"
"}\n"
"\n"
"/* QMenu::indicator (checkboxes and radio buttons in menus) */\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    backgrou"
                        "nd-color: #2e2e2e;     /* Dark gray background for indicators */\n"
"    border: 1px solid #5b5e60;     /* Light gray border */\n"
"    border-radius: 2px;            /* Slightly rounded corners */\n"
"}\n"
"\n"
"QMenu::indicator:checked {\n"
"    background-color: #4a90e2;     /* Light blue when checked */\n"
"    border-color: #3d78b2;         /* Darker blue border when checked */\n"
"}\n"
"\n"
"QMenu::indicator:unchecked {\n"
"    background-color: #2e2e2e;     /* Keep the dark gray when unchecked */\n"
"    border-color: #5b5e60;         /* Light gray border when unchecked */\n"
"}\n"
"\n"
"/* QToolBar */\n"
"QToolBar {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    padding: 4px;                   /* Padding inside the toolbar */\n"
"    spacing: 4px;                   /* Spacing between toolbar buttons */\n"
"}\n"
"\n"
"QToolBar::handle {\n"
"    background-color: #5b5e60;      /* Light gray handle for draggable to"
                        "olbars */\n"
"    width: 10px;                    /* Width of the handle */\n"
"	height: 10px;\n"
"    margin: 4px;                    /* Margin around the handle */\n"
"}\n"
"\n"
"QToolBar::separator {\n"
"    background-color: #5b5e60;      /* Light gray for separators */\n"
"    width: 1px;                     /* Thickness of the separator */\n"
"    height: 24px;                   /* Height of the separator */\n"
"    margin: 6px;                    /* Space around the separator */\n"
"}\n"
"\n"
"QToolBar::item {\n"
"    padding: 4px;                   /* Padding for individual toolbar items */\n"
"}\n"
"\n"
"/* QStatusBar */\n"
"QStatusBar {\n"
"    background-color: #2e2e2e;   /* Dark gray background */\n"
"    border-top: 1px solid #5b5e60; /* Light gray top border for separation */\n"
"    color: #ffffff;              /* White text */\n"
"    font-size: 13px;             /* Slightly smaller font for the status bar */\n"
"    padding: 6px;                /* Padding inside the status bar */\n"
"}\n"
"\n"
""
                        "QStatusBar::item {\n"
"    border: none;                /* No border around individual status items */\n"
"    padding: 0px 5px;            /* Padding between status bar items */\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"    color: #ffffff;              /* White text for any QLabel inside the status bar */\n"
"    background-color: transparent; /* Ensure QLabel in status bar matches the bar's background */\n"
"}\n"
"\n"
"QStatusBar::indicator {\n"
"    background-color: #4a90e2;   /* Optional indicator styling, e.g., for icons or status signals */\n"
"    border-radius: 4px;          /* Rounded corners for any indicator elements */\n"
"}\n"
"\n"
"/* Scroll Area Styling (optional) */\n"
"QScrollArea {\n"
"    background-color: transparent; /* Transparent to match the central widget */\n"
"    border: none;                  /* No border */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #3c3f41;    /* Darker gray for scroll bar background */\n"
"    width: 12px;                  /* Scroll bar width *"
                        "/\n"
"    margin: 22px 0 22px 0;        /* Top and bottom margins */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5b5e60;    /* Slightly lighter gray for scroll handle */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;             /* Remove arrows */\n"
"}\n"
"\n"
"/* QLabel */\n"
"QLabel {\n"
"    color: #ffffff;             /* White text */\n"
"}\n"
"\n"
"/* QFrame */\n"
"QFrame {\n"
"    background-color: #2e2e2e;  /* Dark gray for frames */\n"
"}\n"
"\n"
"/* QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #2e2e2e;  /* Dark gray background for input fields */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border when focused */\n"
"    background-color: #333333;  /* Slightly lighter gray on"
                        " focus */\n"
"}\n"
"\n"
"/* QListWidget */\n"
"QListWidget {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    color: #ffffff;                 /* White text */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    padding: 4px;                   /* Padding around the list */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: transparent;  /* Transparent background for items */\n"
"    color: #ffffff;                 /* White text for list items */\n"
"    border: none;                   /* No border for list items */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #4a90e2;      /* Light blue background when selected */\n"
"    color: #ffffff;                 /* Ensure text remains white when selected */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #3d78b2;      /* Darker blue on hover */\n"
"    color: #ffffff;                 /* Ensure text remains white when hovered */\n"
"}\n"
"\n"
"QListWidget::item:focus {\n"
""
                        "    border: 1px solid #4a90e2;      /* Light blue border on focus */\n"
"}\n"
"\n"
"/* QPlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: #2b2b2b;  /* Darker gray background for text area */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 0px;         /* No rounded corners */\n"
"    padding: 10px;              /* Comfortable padding for text input */\n"
"    font-size: 13px;            /* Slightly smaller font */\n"
"    line-height: 1.4;           /* Adjust line spacing for readability */\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border on focus */\n"
"    background-color: #3a3a3a;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QTabWidget */\n"
"QTabWidget::pane {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    border: 1px solid #5b5e60;      /* Light gray border around the pane */\n"
"    padding: 4px;                   /* Pa"
                        "dding inside the pane */\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px;                      /* Space from the left */\n"
"}\n"
"\n"
"/* QTabBar::tab */\n"
"QTabBar::tab {\n"
"    background-color: #3c3f41;      /* Dark gray background for tabs */\n"
"    color: #ffffff;                 /* White text for tabs */\n"
"    border-left: 1px solid #5b5e60;      /* Light gray border around tabs */\n"
"    border-top: 1px solid #5b5e60;\n"
"    border-right: 1px solid #5b5e60;\n"
"    padding: 4px 8px;              /* Padding for each tab */\n"
"    margin-left: 2px;                    /* Slight margin between tabs */\n"
"    margin-right: 2px;\n"
"    border-top-left-radius: 4px;    /* Rounded top corners */\n"
"    border-top-right-radius: 4px;   /* Rounded top corners */\n"
"}\n"
"\n"
"/* Selected tab */\n"
"QTabBar::tab:selected {\n"
"    background-color: #4a90e2;      /* Light blue background for selected tab */\n"
"    color: #ffffff;                 /* White text for selected tab */\n"
"    border-co"
                        "lor: #4a90e2;          /* Blue border for selected tab */\n"
"}\n"
"\n"
"/* Hovered tab */\n"
"QTabBar::tab:hover {\n"
"    background-color: #3d78b2;      /* Darker blue on hover */\n"
"    color: #ffffff;                 /* White text */\n"
"}\n"
"\n"
"/* Disabled tab */\n"
"QTabBar::tab:disabled {\n"
"    background-color: #2e2e2e;      /* Dark gray for disabled tab */\n"
"    color: #777777;                 /* Light gray text for disabled tabs */\n"
"}\n"
"\n"
"/* Focused tab */\n"
"QTabBar::tab:focus {\n"
"    border: 1px solid #4a90e2;      /* Blue border when tab is focused */\n"
"}\n"
"\n"
"/* Tab close button (optional) */\n"
"QTabBar::close-button {\n"
"    /* image: url(close-icon.png);     Replace with your close icon path */\n"
"    subcontrol-position: right;     /* Position the close button on the right */\n"
"    margin: 0 8px 0 0;              /* Spacing for the close button */\n"
"}\n"
"/*\n"
"QTabBar::close-button:hover {\n"
"    image: url(close-icon-hover.png);   Change icon on hover \n"
""
                        "}*/\n"
"\n"
"/* QComboBox */\n"
"QComboBox {\n"
"    background-color: #2e2e2e;       /* Dark gray background */\n"
"    color: #ffffff;                  /* White text */\n"
"    border: 1px solid #5b5e60;       /* Light gray border */\n"
"    border-radius: 4px;              /* Rounded corners */\n"
"    padding-left: 2px;                    /* Padding inside the combo box */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #3a3a3a;       /* Slightly lighter gray on hover */\n"
"    border-color: #4a90e2;           /* Light blue border on hover */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    background-color: #333333;       /* Lighter gray on focus */\n"
"    border-color: #4a90e2;           /* Light blue border on focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;                      /* Width of the drop-down button */\n"
"    background-color: #2e2e2e;        /* Dark gray background for drop-down */\n"
"    b"
                        "order-left: 1px solid #5b5e60;   /* Light gray separator between drop-down button and combo box */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/888EAC-20px/ICONS/888EAC-20px/arrow-down.svg);  /*Replace with your down arrow icon */\n"
"    width: 12px;                         /* Width of the arrow */\n"
"    height: 12px;                        /* Height of the arrow */\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(:/888EAC-20px/ICONS/888EAC-20px/arrow-down.svg); /* Optional: different icon on hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2e2e2e;        /* Dark gray background for drop-down list */\n"
"    color: #ffffff;                   /* White text */\n"
"    border: 1px solid #5b5e60;        /* Light gray border around the list */\n"
"    selection-background-color: #4a90e2;  /* Light blue background for selected item */\n"
"    selection-color: #ffffff;         /* White text for selected item */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView"
                        "::item {\n"
"    background-color: transparent;    /* Transparent background for list items */\n"
"    padding: 6px;                     /* Padding for each item in the list */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #4a90e2;        /* Light blue when an item is selected */\n"
"    color: #ffffff;                   /* White text for selected item */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #3d78b2;        /* Darker blue on hover */\n"
"    color: #ffffff;                   /* White text when hovered */\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: #2e2e2e;        /* Dark gray background when disabled */\n"
"    color: #777777;                   /* Lighter gray text when disabled */\n"
"    border-color: #5b5e60;            /* Keep the light gray border */\n"
"}\n"
"\n"
"/* QPushButton */\n"
"QPushButton {\n"
"    background-color: #3c3f41;  /* Dark gray background */\n"
"    color: #ffffff;             /* Wh"
                        "ite text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"	padding: 0px 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4a90e2;  /* Light blue on hover */\n"
"    border-color: #3d78b2;      /* Darker blue border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3d78b2;  /* Darker blue on press */\n"
"    border-color: #2a5f92;      /* Even darker border when pressed */\n"
"}\n"
"\n"
"/* QCheckBox */\n"
"QCheckBox {\n"
"    color: #ffffff;                 /* White text for checkbox label */\n"
"    spacing: 6px;                   /* Space between checkbox and label */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;                    /* Set the size of the checkbox */\n"
"    height: 14px;\n"
"    background-color: #2e2e2e;      /* Dark gray background for the checkbox */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    border-radius: 2px;             /* Slight round"
                        "ing for modern look */\n"
"}\n"
"\n"
"/* Hovered checkbox */\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #4a90e2;      /* Light blue on hover */\n"
"    border-color: #3d78b2;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"/* Checked checkbox */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #4a90e2;      /* Light blue when checked */\n"
"    border-color: #3d78b2;          /* Darker blue border when checked */\n"
"    image: url(:/checked-icon.png); /* Replace with your checkmark icon if needed */\n"
"}\n"
"\n"
"/* Indeterminate checkbox (for tri-state checkboxes) */\n"
"QCheckBox::indicator:indeterminate {\n"
"    background-color: #4a90e2;      /* Light blue when in indeterminate state */\n"
"    border-color: #3d78b2;          /* Darker blue border */\n"
"    image: url(:/indeterminate-icon.png); /* Replace with your indeterminate icon */\n"
"}\n"
"\n"
"/* Pressed checkbox */\n"
"QCheckBox::indicator:pressed {\n"
"    background-color: #3d78b2;      /* Darker blue on"
                        " press */\n"
"    border-color: #2a5f92;          /* Even darker border when pressed */\n"
"}\n"
"\n"
"/* Disabled checkbox */\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #2e2e2e;      /* Dark gray when disabled */\n"
"    border-color: #5b5e60;          /* Light gray border */\n"
"    color: #777777;                 /* Light gray label when disabled */\n"
"}\n"
"\n"
"/* QRadioButton */\n"
"QRadioButton {\n"
"    color: #ffffff;              /* White text */\n"
"    spacing: 5px;                /* Space between radio button and label */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;                 /* Size of the radio button */\n"
"    height: 14px;\n"
"    background-color: #2e2e2e;   /* Dark gray background for the indicator */\n"
"    border: 1px solid #5b5e60;   /* Light gray border */\n"
"    border-radius: 8px;          /* Circular radio button */\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    background-color: #4a90e2;   /* Light blue on hover */\n"
"    border-"
                        "color: #3d78b2;       /* Darker blue border on hover */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4a90e2;   /* Light blue when checked */\n"
"    border-color: #3d78b2;       /* Darker blue border when checked */\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue on press */\n"
"    border-color: #2a5f92;       /* Even darker border on press */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue when checked and pressed */\n"
"    border-color: #2a5f92;       /* Even darker border when checked and pressed */\n"
"}\n"
"\n"
"/* QToolButton */\n"
"QToolButton {\n"
"    background-color: #3c3f41;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text/icon */\n"
"    border: 1px solid #5b5e60;    /* Light gray border */\n"
"    border-radius: 4px;           /* Rounded corners */\n"
"    padding: 0px 0px;            /* Padding for comfortable button s"
                        "ize */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #4a90e2;    /* Light blue background on hover */\n"
"    border-color: #3d78b2;        /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #3d78b2;    /* Darker blue background on press */\n"
"    border-color: #2a5f92;        /* Even darker border when pressed */\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #3d78b2;    /* Darker blue when checked */\n"
"    border-color: #2a5f92;        /* Border color when checked */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #2e2e2e;    /* Dark gray when disabled */\n"
"    color: #777777;               /* Lighter gray text/icon for disabled state */\n"
"    border-color: #5b5e60;        /* Keep the border color same as normal state */\n"
"}\n"
"\n"
"/* QToolButton::menu-button */\n"
"QToolButton::menu-button {\n"
"    background-color: #3c3f41;      /* Dark gray background for menu button */\n"
"    border: 1px solid #5b5e6"
                        "0;      /* Light gray border for menu button */\n"
"    padding: 4px;                   /* Padding for the menu button */\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"    background-color: #4a90e2;      /* Light blue on hover */\n"
"    border-color: #3d78b2;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton::menu-button:pressed {\n"
"    background-color: #3d78b2;      /* Darker blue on press */\n"
"    border-color: #2a5f92;          /* Even darker border on press */\n"
"}")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* Central Widget */\n"
"#centralwidget {\n"
"    background-color: #1e1e1e;  /* Dark gray background */\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: #1e1e1e;\n"
"	margin: 6px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame {\n"
"    background-color: #2e2e2e;\n"
"	margin: 0px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_10)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.object_inspector = QWidget()
        self.object_inspector.setObjectName(u"object_inspector")
        self.horizontalLayout_2 = QHBoxLayout(self.object_inspector)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.object_inspector)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.frame_2 = QFrame(self.object_inspector)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {padding: 3px;}")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {padding: 3px;}")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.tabWidget.addTab(self.object_inspector, "")
        self.property_editor = QWidget()
        self.property_editor.setObjectName(u"property_editor")
        self.verticalLayout_15 = QVBoxLayout(self.property_editor)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.property_editor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {background-color: #111;}")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_8)

        self.frame_15 = QFrame(self.property_editor)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy1)
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 6, 0, 6)
        self.frame_25 = QFrame(self.frame_15)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_25)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_17.addWidget(self.label_17)

        self.lineEdit_7 = QLineEdit(self.frame_25)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_17.addWidget(self.lineEdit_7)


        self.verticalLayout_12.addWidget(self.frame_25)

        self.frame_24 = QFrame(self.frame_15)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_24)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_16.addWidget(self.label_13)

        self.lineEdit_6 = QLineEdit(self.frame_24)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_16.addWidget(self.lineEdit_6)


        self.verticalLayout_12.addWidget(self.frame_24)

        self.frame_23 = QFrame(self.frame_15)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_23)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_15.addWidget(self.label_16)

        self.lineEdit_5 = QLineEdit(self.frame_23)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_15.addWidget(self.lineEdit_5)


        self.verticalLayout_12.addWidget(self.frame_23)

        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_19)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_12.addWidget(self.label_12)

        self.lineEdit_3 = QLineEdit(self.frame_19)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_12.addWidget(self.lineEdit_3)


        self.verticalLayout_12.addWidget(self.frame_19)


        self.verticalLayout_15.addWidget(self.frame_15)

        self.label_9 = QLabel(self.property_editor)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel {background-color: #111;}")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_9)

        self.frame_20 = QFrame(self.property_editor)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.frame_20.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 6, 0, 6)
        self.frame_28 = QFrame(self.frame_20)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_28)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_20.addWidget(self.label_20)

        self.lineEdit_10 = QLineEdit(self.frame_28)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_20.addWidget(self.lineEdit_10)


        self.verticalLayout_14.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_20)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_29)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_21.addWidget(self.label_21)

        self.lineEdit_11 = QLineEdit(self.frame_29)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_21.addWidget(self.lineEdit_11)


        self.verticalLayout_14.addWidget(self.frame_29)

        self.frame_26 = QFrame(self.frame_20)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_26)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_18.addWidget(self.label_18)

        self.lineEdit_8 = QLineEdit(self.frame_26)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_18.addWidget(self.lineEdit_8)


        self.verticalLayout_14.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_20)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_27)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_19.addWidget(self.label_19)

        self.lineEdit_9 = QLineEdit(self.frame_27)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_19.addWidget(self.lineEdit_9)


        self.verticalLayout_14.addWidget(self.frame_27)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_22)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_14.addWidget(self.label_14)

        self.comboBox = QComboBox(self.frame_22)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.comboBox)


        self.verticalLayout_14.addWidget(self.frame_22)

        self.frame_30 = QFrame(self.frame_20)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_30)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_22.addWidget(self.label_15)

        self.comboBox_2 = QComboBox(self.frame_30)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_22.addWidget(self.comboBox_2)


        self.verticalLayout_14.addWidget(self.frame_30)

        self.frame_18 = QFrame(self.frame_20)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_18)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_11.addWidget(self.label_22)

        self.lineEdit_4 = QLineEdit(self.frame_18)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_11.addWidget(self.lineEdit_4)


        self.verticalLayout_14.addWidget(self.frame_18)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_21)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_13.addWidget(self.label_23)

        self.lineEdit_12 = QLineEdit(self.frame_21)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_13.addWidget(self.lineEdit_12)


        self.verticalLayout_14.addWidget(self.frame_21)

        self.frame_31 = QFrame(self.frame_20)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.comboBox_3 = QComboBox(self.frame_31)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_23.addWidget(self.comboBox_3)

        self.lineEdit_13 = QLineEdit(self.frame_31)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_23.addWidget(self.lineEdit_13)


        self.verticalLayout_14.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_20)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_32)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_24.addWidget(self.label_24)

        self.comboBox_4 = QComboBox(self.frame_32)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy2.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_24.addWidget(self.comboBox_4)


        self.verticalLayout_14.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_20)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_33)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_25.addWidget(self.label_25)

        self.lineEdit_14 = QLineEdit(self.frame_33)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_25.addWidget(self.lineEdit_14)


        self.verticalLayout_14.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_20)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_34)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_26.addWidget(self.label_26)

        self.comboBox_5 = QComboBox(self.frame_34)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy2.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_26.addWidget(self.comboBox_5)


        self.verticalLayout_14.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_20)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_35)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_27.addWidget(self.label_27)

        self.comboBox_6 = QComboBox(self.frame_35)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        sizePolicy2.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy2)

        self.horizontalLayout_27.addWidget(self.comboBox_6)


        self.verticalLayout_14.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_20)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_36)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_28.addWidget(self.label_28)

        self.lineEdit_15 = QLineEdit(self.frame_36)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.horizontalLayout_28.addWidget(self.lineEdit_15)


        self.verticalLayout_14.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_20)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_29.setSpacing(9)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_37)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(57, 0))

        self.horizontalLayout_29.addWidget(self.label_29)

        self.checkBox_14 = QCheckBox(self.frame_37)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.horizontalLayout_29.addWidget(self.checkBox_14)


        self.verticalLayout_14.addWidget(self.frame_37, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_15.addWidget(self.frame_20)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.property_editor, "")
        self.console = QWidget()
        self.console.setObjectName(u"console")
        self.verticalLayout_3 = QVBoxLayout(self.console)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.console)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setTabStopDistance(16.000000000000000)

        self.verticalLayout_3.addWidget(self.plainTextEdit)

        self.tabWidget.addTab(self.console, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.frame_10)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: #2e2e2e;\n"
"	margin: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.graphicsView = QGraphicsView(self.frame)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_5.addWidget(self.graphicsView)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame {\n"
"    background-color: #2e2e2e;\n"
"	margin: 0px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.frame_6)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"")
        self.elements = QWidget()
        self.elements.setObjectName(u"elements")
        self.verticalLayout_7 = QVBoxLayout(self.elements)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.listWidget_2 = QListWidget(self.elements)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_7.addWidget(self.listWidget_2)

        self.tabWidget_2.addTab(self.elements, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_8 = QVBoxLayout(self.settings)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.settings)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {background-color: #111;}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.frame_4 = QFrame(self.settings)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 6, 0, 6)
        self.checkBox = QCheckBox(self.frame_4)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_9.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_4)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_9.addWidget(self.checkBox_2)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.toolButton = QToolButton(self.frame_8)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_3.addWidget(self.toolButton)


        self.verticalLayout_9.addWidget(self.frame_8, 0, Qt.AlignmentFlag.AlignLeft)

        self.checkBox_3 = QCheckBox(self.frame_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_9.addWidget(self.checkBox_3)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.checkBox_4 = QCheckBox(self.frame_9)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_4.addWidget(self.checkBox_4)

        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(3)

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_9.addWidget(self.pushButton_3)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.label_2 = QLabel(self.settings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {background-color: #111;}")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.frame_5 = QFrame(self.settings)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 6, 0, 6)
        self.checkBox_5 = QCheckBox(self.frame_5)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_10.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.frame_5)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_10.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.frame_5)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_10.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.frame_5)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout_10.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.frame_5)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.verticalLayout_10.addWidget(self.checkBox_9)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.radioButton = QRadioButton(self.frame_12)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_6.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_12)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_6.addWidget(self.radioButton_2)


        self.verticalLayout_10.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(74, 0))

        self.horizontalLayout_5.addWidget(self.label_7)

        self.horizontalSpacer = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.radioButton_3 = QRadioButton(self.frame_11)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_5.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.frame_11)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_5.addWidget(self.radioButton_4)


        self.verticalLayout_10.addWidget(self.frame_11)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.label_3 = QLabel(self.settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {background-color: #111;}")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.frame_7 = QFrame(self.settings)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 6, 0, 6)
        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.radioButton_7 = QRadioButton(self.frame_13)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_7.addWidget(self.radioButton_7)

        self.radioButton_6 = QRadioButton(self.frame_13)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_7.addWidget(self.radioButton_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_7)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.radioButton_12 = QRadioButton(self.frame_14)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.horizontalLayout_8.addWidget(self.radioButton_12)

        self.radioButton_9 = QRadioButton(self.frame_14)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_8.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.frame_14)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_8.addWidget(self.radioButton_10)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_13.addWidget(self.frame_14)

        self.pushButton_7 = QPushButton(self.frame_7)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_13.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_7)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_13.addWidget(self.pushButton_8)

        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_13.addWidget(self.pushButton_6)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.tabWidget_2.addTab(self.settings, "")

        self.verticalLayout_6.addWidget(self.tabWidget_2)


        self.horizontalLayout.addWidget(self.frame_6)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(Qt.ToolBarArea.AllToolBarAreas)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1387, 29))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Phils-Hub - WaW Hud Mapper", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.object_inspector), QCoreApplication.translate("MainWindow", u"Object Inspector", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Scene", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_7.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.lineEdit_6.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.lineEdit_5.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.lineEdit_3.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_10.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.lineEdit_11.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.lineEdit_8.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.lineEdit_9.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"H Align", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"HORIZONTAL_ALIGN_LEFT", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"HORIZONTAL_ALIGN_RIGHT", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"V Align", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"VERTICAL_ALIGN_TOP", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"VERTICAL_ALIGN_BOTTOM", None))

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"type", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"forecolor", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"text", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"exp text", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"textfont", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"UI_FONT_NORMAL", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"UI_FONT_BIG", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"UI_FONT_SMALL", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"UI_FONT_BOLD", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"UI_FONT_CONSOLE", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"UI_FONT_OBJECTIVE", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"UI_FONT_MAX", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"textscale", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"textstyle", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"ITEM_TEXTSTYLE_NORMAL", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"ITEM_TEXTSTYLE_BLINK", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"ITEM_TEXTSTYLE_SHADOWED", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"ITEM_TEXTSTYLE_SHADOWEDMORE", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"ITEM_TEXTSTYLE_MONOSPACE", None))

        self.label_27.setText(QCoreApplication.translate("MainWindow", u"textalign", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"ITEM_ALIGN_TOP_LEFT", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"ITEM_ALIGN_TOP_CENTER", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"ITEM_ALIGN_TOP_RIGHT", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"ITEM_ALIGN_MIDDLE_LEFT", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"ITEM_ALIGN_MIDDLE_CENTER", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"ITEM_ALIGN_MIDDLE_RIGHT", None))
        self.comboBox_6.setItemText(6, QCoreApplication.translate("MainWindow", u"ITEM_ALIGN_BOTTOM_LEFT", None))
        self.comboBox_6.setItemText(7, QCoreApplication.translate("MainWindow", u"ITEM_ALIGN_BOTTOM_CENTER", None))
        self.comboBox_6.setItemText(8, QCoreApplication.translate("MainWindow", u"ITEM_ALIGN_BOTTOM_RIGHT", None))

        self.label_28.setText(QCoreApplication.translate("MainWindow", u"visible", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"decoration", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.property_editor), QCoreApplication.translate("MainWindow", u"Property Editor", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Code will output here upon submission", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.console), QCoreApplication.translate("MainWindow", u"Console", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qlistwidgetitem1 = self.listWidget_2.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.elements), QCoreApplication.translate("MainWindow", u"Elements", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Scene", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Background", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Background Image", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Quadrant Grid", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1-50", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Clear Scene", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Open Scene", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save Scene", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Element", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Elem Label", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"X Pos Indicator", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Quadrant Indicator", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Fill Background", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Manipulator Handle", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copy Element", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Start Pos", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Curr Pos", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Resize Area", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Inside", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Outside", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Code", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u".txt", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u".inc", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"Both", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Clear Console", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Generate Code", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Tips", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

