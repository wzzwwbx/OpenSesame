# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/general_widget.ui'
#
# Created: Mon Jul  9 13:58:20 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_general_widget(object):
    def setupUi(self, general_widget):
        general_widget.setObjectName(_fromUtf8("general_widget"))
        general_widget.resize(807, 805)
        self.verticalLayout = QtGui.QVBoxLayout(general_widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(general_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.layout_general_properties = QtGui.QGridLayout(self.widget)
        self.layout_general_properties.setMargin(0)
        self.layout_general_properties.setMargin(0)
        self.layout_general_properties.setObjectName(_fromUtf8("layout_general_properties"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layout_general_properties.addWidget(self.label_2, 4, 0, 1, 1)
        self.combobox_backend = QtGui.QComboBox(self.widget)
        self.combobox_backend.setObjectName(_fromUtf8("combobox_backend"))
        self.layout_general_properties.addWidget(self.combobox_backend, 3, 1, 1, 3)
        self.combobox_start = QtGui.QComboBox(self.widget)
        self.combobox_start.setObjectName(_fromUtf8("combobox_start"))
        self.layout_general_properties.addWidget(self.combobox_start, 0, 1, 1, 3)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.layout_general_properties.addWidget(self.label, 0, 0, 1, 1)
        self.spinbox_width = QtGui.QSpinBox(self.widget)
        self.spinbox_width.setMinimum(1)
        self.spinbox_width.setMaximum(10000)
        self.spinbox_width.setObjectName(_fromUtf8("spinbox_width"))
        self.layout_general_properties.addWidget(self.spinbox_width, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.layout_general_properties.addWidget(self.label_4, 4, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.layout_general_properties.addWidget(self.label_8, 3, 0, 1, 1)
        self.spinbox_height = QtGui.QSpinBox(self.widget)
        self.spinbox_height.setMinimum(1)
        self.spinbox_height.setMaximum(10000)
        self.spinbox_height.setObjectName(_fromUtf8("spinbox_height"))
        self.layout_general_properties.addWidget(self.spinbox_height, 5, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.layout_general_properties.addWidget(self.label_5, 5, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layout_general_properties.addWidget(self.label_3, 5, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.group_backend_settings = QtGui.QGroupBox(general_widget)
        self.group_backend_settings.setCheckable(True)
        self.group_backend_settings.setChecked(False)
        self.group_backend_settings.setObjectName(_fromUtf8("group_backend_settings"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.group_backend_settings)
        self.verticalLayout_4.setMargin(4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scrollarea_backend_settings = QtGui.QScrollArea(self.group_backend_settings)
        self.scrollarea_backend_settings.setWidgetResizable(True)
        self.scrollarea_backend_settings.setObjectName(_fromUtf8("scrollarea_backend_settings"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 789, 279))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.group_canvas = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.group_canvas.setObjectName(_fromUtf8("group_canvas"))
        self.layout_canvas = QtGui.QVBoxLayout(self.group_canvas)
        self.layout_canvas.setContentsMargins(0, -1, 0, 0)
        self.layout_canvas.setObjectName(_fromUtf8("layout_canvas"))
        self.label_canvas = QtGui.QLabel(self.group_canvas)
        self.label_canvas.setObjectName(_fromUtf8("label_canvas"))
        self.layout_canvas.addWidget(self.label_canvas)
        self.verticalLayout_7.addWidget(self.group_canvas)
        self.group_keyboard = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.group_keyboard.setObjectName(_fromUtf8("group_keyboard"))
        self.layout_keyboard = QtGui.QVBoxLayout(self.group_keyboard)
        self.layout_keyboard.setContentsMargins(0, -1, 0, 0)
        self.layout_keyboard.setObjectName(_fromUtf8("layout_keyboard"))
        self.label_keyboard = QtGui.QLabel(self.group_keyboard)
        self.label_keyboard.setObjectName(_fromUtf8("label_keyboard"))
        self.layout_keyboard.addWidget(self.label_keyboard)
        self.verticalLayout_7.addWidget(self.group_keyboard)
        self.group_mouse = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.group_mouse.setObjectName(_fromUtf8("group_mouse"))
        self.layout_mouse = QtGui.QVBoxLayout(self.group_mouse)
        self.layout_mouse.setContentsMargins(0, -1, 0, 0)
        self.layout_mouse.setObjectName(_fromUtf8("layout_mouse"))
        self.label_mouse = QtGui.QLabel(self.group_mouse)
        self.label_mouse.setObjectName(_fromUtf8("label_mouse"))
        self.layout_mouse.addWidget(self.label_mouse)
        self.verticalLayout_7.addWidget(self.group_mouse)
        self.group_sampler = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.group_sampler.setObjectName(_fromUtf8("group_sampler"))
        self.layout_sampler = QtGui.QVBoxLayout(self.group_sampler)
        self.layout_sampler.setContentsMargins(0, -1, 0, 0)
        self.layout_sampler.setObjectName(_fromUtf8("layout_sampler"))
        self.label_sampler = QtGui.QLabel(self.group_sampler)
        self.label_sampler.setObjectName(_fromUtf8("label_sampler"))
        self.layout_sampler.addWidget(self.label_sampler)
        self.verticalLayout_7.addWidget(self.group_sampler)
        self.group_synth = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.group_synth.setObjectName(_fromUtf8("group_synth"))
        self.layout_synth = QtGui.QVBoxLayout(self.group_synth)
        self.layout_synth.setContentsMargins(0, -1, 0, 0)
        self.layout_synth.setObjectName(_fromUtf8("layout_synth"))
        self.label_synth = QtGui.QLabel(self.group_synth)
        self.label_synth.setObjectName(_fromUtf8("label_synth"))
        self.layout_synth.addWidget(self.label_synth)
        self.verticalLayout_7.addWidget(self.group_synth)
        self.scrollarea_backend_settings.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollarea_backend_settings)
        self.verticalLayout.addWidget(self.group_backend_settings)
        self.group_script = QtGui.QGroupBox(general_widget)
        self.group_script.setCheckable(True)
        self.group_script.setChecked(False)
        self.group_script.setObjectName(_fromUtf8("group_script"))
        self.layout_script = QtGui.QVBoxLayout(self.group_script)
        self.layout_script.setMargin(4)
        self.layout_script.setObjectName(_fromUtf8("layout_script"))
        self.verticalLayout.addWidget(self.group_script)
        self.spacer = QtGui.QWidget(general_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer.sizePolicy().hasHeightForWidth())
        self.spacer.setSizePolicy(sizePolicy)
        self.spacer.setObjectName(_fromUtf8("spacer"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.spacer)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget_2 = QtGui.QWidget(self.spacer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem = QtGui.QSpacerItem(20, 193, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.frame = QtGui.QFrame(self.widget_2)
        self.frame.setFrameShape(QtGui.QFrame.HLine)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_6.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtGui.QWidget(self.spacer)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_5 = QtGui.QWidget(self.widget_3)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget_4 = QtGui.QWidget(self.widget_5)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_facebook = QtGui.QLabel(self.widget_4)
        self.label_facebook.setObjectName(_fromUtf8("label_facebook"))
        self.horizontalLayout_2.addWidget(self.label_facebook)
        self.label_twitter = QtGui.QLabel(self.widget_4)
        self.label_twitter.setObjectName(_fromUtf8("label_twitter"))
        self.horizontalLayout_2.addWidget(self.label_twitter)
        self.label_website = QtGui.QLabel(self.widget_4)
        self.label_website.setObjectName(_fromUtf8("label_website"))
        self.horizontalLayout_2.addWidget(self.label_website)
        self.label_cogscinl = QtGui.QLabel(self.widget_4)
        self.label_cogscinl.setObjectName(_fromUtf8("label_cogscinl"))
        self.horizontalLayout_2.addWidget(self.label_cogscinl)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_5)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_opensesame = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_opensesame.sizePolicy().hasHeightForWidth())
        self.label_opensesame.setSizePolicy(sizePolicy)
        self.label_opensesame.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_opensesame.setObjectName(_fromUtf8("label_opensesame"))
        self.horizontalLayout.addWidget(self.label_opensesame)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.spacer)

        self.retranslateUi(general_widget)
        QtCore.QMetaObject.connectSlotsByName(general_widget)

    def retranslateUi(self, general_widget):
        general_widget.setWindowTitle(QtGui.QApplication.translate("general_widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("general_widget", "Display width<br />\n"
"<small><i>In pixels</i></small>", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_start.setToolTip(QtGui.QApplication.translate("general_widget", "This is item (typically a sequence) is the starting point for your experiment.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("general_widget", "Entry point<br />\n"
"<small><i>First item to run</i></small>", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_width.setToolTip(QtGui.QApplication.translate("general_widget", "The display resolution (width) in pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_width.setSuffix(QtGui.QApplication.translate("general_widget", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("general_widget", "Default foreground color<br />\n"
"<small><i>E.g., \"white\" or \"#ffffff\"</i></small>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("general_widget", "Back-end<br />\n"
"<small><i>Handles display, sound, and input</i></small>", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_height.setToolTip(QtGui.QApplication.translate("general_widget", "The display resolution (height) in pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_height.setSuffix(QtGui.QApplication.translate("general_widget", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("general_widget", "Default background color<br />\n"
"<small><i>E.g., \"black\" or \"#000000\"</i></small>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("general_widget", "Display height<br />\n"
"<small><i>In pixels</i></small>", None, QtGui.QApplication.UnicodeUTF8))
        self.group_backend_settings.setTitle(QtGui.QApplication.translate("general_widget", "Show back-end settings and info", None, QtGui.QApplication.UnicodeUTF8))
        self.group_canvas.setTitle(QtGui.QApplication.translate("general_widget", "Canvas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_canvas.setText(QtGui.QApplication.translate("general_widget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.group_keyboard.setTitle(QtGui.QApplication.translate("general_widget", "Keyboard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_keyboard.setText(QtGui.QApplication.translate("general_widget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.group_mouse.setTitle(QtGui.QApplication.translate("general_widget", "Mouse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_mouse.setText(QtGui.QApplication.translate("general_widget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.group_sampler.setTitle(QtGui.QApplication.translate("general_widget", "Sampler", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sampler.setText(QtGui.QApplication.translate("general_widget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.group_synth.setTitle(QtGui.QApplication.translate("general_widget", "Synth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_synth.setText(QtGui.QApplication.translate("general_widget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.group_script.setTitle(QtGui.QApplication.translate("general_widget", "Show script editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_facebook.setToolTip(QtGui.QApplication.translate("general_widget", "Visit Facebook page", None, QtGui.QApplication.UnicodeUTF8))
        self.label_facebook.setText(QtGui.QApplication.translate("general_widget", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.label_twitter.setToolTip(QtGui.QApplication.translate("general_widget", "Visit Twitter page", None, QtGui.QApplication.UnicodeUTF8))
        self.label_twitter.setText(QtGui.QApplication.translate("general_widget", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.label_website.setToolTip(QtGui.QApplication.translate("general_widget", "Visit cogsci.nl", None, QtGui.QApplication.UnicodeUTF8))
        self.label_website.setText(QtGui.QApplication.translate("general_widget", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cogscinl.setText(QtGui.QApplication.translate("general_widget", "<html><head/><body><p>COGSCIdotNL // cognitive science and more</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_opensesame.setText(QtGui.QApplication.translate("general_widget", "OpenSesame [version] [codename]\n"
"Copyright Sebastiaan Mathôt (2010-2012)", None, QtGui.QApplication.UnicodeUTF8))

