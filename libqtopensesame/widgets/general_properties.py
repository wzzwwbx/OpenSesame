#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame import debug
from PyQt4 import QtCore, QtGui
from libopensesame import misc
from libqtopensesame.misc import _
import libopensesame.exceptions
from libqtopensesame.ui import general_widget_ui
from libqtopensesame.widgets import color_edit, inline_editor, header_widget
from libqtopensesame.items import experiment
from libqtopensesame.misc import config
import openexp.backend_info
import sip

class general_properties(QtGui.QWidget):

	"""The QWidget for the general properties tab"""

	backend_format = "%s [%s]"

	def __init__(self, parent=None):

		"""
		Constructor

		Keywords arguments:
		parent -- the parent QWidget
		"""

		self.main_window = parent
		QtGui.QWidget.__init__(self)

		# Set the header, with the icon, label and script button
		self.header_widget = general_header_widget(self, \
			self.main_window.experiment)
		button_help = QtGui.QPushButton(self.main_window.experiment.icon( \
			"help"), "")
		button_help.setIconSize(QtCore.QSize(16, 16))
		button_help.clicked.connect( \
			self.main_window.ui.tabwidget.open_general_help)
		button_help.setToolTip(_("Tell me more about OpenSesame!"))
		header_hbox = QtGui.QHBoxLayout()
		header_hbox.addWidget(self.main_window.experiment.label_image( \
			"experiment"))
		header_hbox.addWidget(self.header_widget)
		header_hbox.addStretch()
		header_hbox.addWidget(button_help)
		header_hbox.setContentsMargins(0, 0, 0, 0)
		header_widget = QtGui.QWidget()
		header_widget.setLayout(header_hbox)

		# The rest of the controls from the UI file
		w = QtGui.QWidget()
		self.ui = general_widget_ui.Ui_general_widget()
		self.ui.setupUi(w)
		self.main_window.theme.apply_theme(self)

		# Initialize the color and font widgets
		self.ui.edit_foreground.initialize(self.main_window.experiment)
		self.ui.edit_background.initialize(self.main_window.experiment)
		QtCore.QObject.connect(self.ui.edit_foreground, QtCore.SIGNAL( \
			"set_color"), self.apply_changes)
		QtCore.QObject.connect(self.ui.edit_background, QtCore.SIGNAL( \
			"set_color"), self.apply_changes)
		self.ui.widget_font.initialize(self.main_window.experiment)
		QtCore.QObject.connect(self.ui.widget_font, QtCore.SIGNAL( \
			"font_changed"), self.apply_changes)

		# Connect the rest
		self.ui.spinbox_width.editingFinished.connect(self.apply_changes)
		self.ui.spinbox_height.editingFinished.connect(self.apply_changes)
		self.ui.button_script_editor.clicked.connect( \
			self.main_window.ui.tabwidget.open_general_script)
		self.ui.button_backend_settings.clicked.connect( \
			self.main_window.ui.tabwidget.open_backend_settings)

		# Set the backend combobox
		for backend in openexp.backend_info.backend_list:
			desc = openexp.backend_info.backend_list[backend]["description"]
			icon = openexp.backend_info.backend_list[backend]["icon"]
			self.ui.combobox_backend.addItem(self.main_window.theme.qicon( \
				icon), self.backend_format % (backend, desc))
		self.ui.combobox_backend.currentIndexChanged.connect(self.apply_changes)

		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(header_widget)
		vbox.addWidget(w)

		self.setLayout(vbox)
		self.tab_name = '__general_properties__'
		self.on_activate = self.refresh

	def set_header_label(self):

		"""
		Set the general header based on the experiment title and description
		"""

		self.header_widget.edit_name.setText(self.main_window.experiment.title)
		self.header_widget.label_name.setText( \
			"<font size='5'><b>%s</b> - Experiment</font>&nbsp;&nbsp;&nbsp;<font color='gray'><i>Click to edit</i></font>" \
			% self.main_window.experiment.title)
		self.header_widget.edit_desc.setText(self.main_window.experiment.description)
		self.header_widget.label_desc.setText(self.main_window.experiment.description)

	def apply_changes(self):

		"""Apply changes to the general tab"""

		# Skip if the general tab is locked and lock it otherwise
		if self.lock:
			return
		self.lock = True

		debug.msg()
		rebuild_item_tree = False
		self.main_window.set_busy(True)
		# Set the title and the description
		title = self.main_window.experiment.sanitize( \
			self.header_widget.edit_name.text())
		self.main_window.experiment.set("title", title)
		desc = self.main_window.experiment.sanitize( \
			self.header_widget.edit_desc.text())
		self.main_window.experiment.set("description", desc)

		# Set the backend
		if self.ui.combobox_backend.isEnabled():
			i = self.ui.combobox_backend.currentIndex()
			backend = openexp.backend_info.backend_list.values()[i]
			self.main_window.experiment.set("canvas_backend", \
				backend["canvas"])
			self.main_window.experiment.set("keyboard_backend", \
				backend["keyboard"])
			self.main_window.experiment.set("mouse_backend", \
				backend["mouse"])
			self.main_window.experiment.set("sampler_backend", \
				backend["sampler"])
			self.main_window.experiment.set("synth_backend", \
				backend["synth"])
		else:
			debug.msg( \
				'not setting back-end, because a custom backend is selected')

		# Set the display width
		width = self.ui.spinbox_width.value()
		if self.main_window.experiment.get("width") != width:
			self.main_window.update_resolution(width, \
				self.main_window.experiment.get("height"))

		# Set the display height
		height = self.ui.spinbox_height.value()
		if self.main_window.experiment.get("height") != height:
			self.main_window.update_resolution( \
				self.main_window.experiment.get("width"), height)

		# Set the foreground color
		foreground = self.main_window.experiment.sanitize( \
			self.ui.edit_foreground.text())
		refs = []
		try:
			refs = self.main_window.experiment.get_refs(foreground)
			self.main_window.experiment.color_check(foreground)
		except Exception as e:
			if refs == []:
				self.main_window.experiment.notify(e)
				foreground = self.main_window.experiment.get("foreground")
				self.ui.edit_foreground.setText(foreground)
		self.main_window.experiment.set("foreground", foreground)

		# Set the background color
		background = self.main_window.experiment.sanitize( \
			self.ui.edit_background.text())
		refs = []
		try:
			refs = self.main_window.experiment.get_refs(background)
			self.main_window.experiment.color_check(background)
		except Exception as e:
			if refs == []:
				self.main_window.experiment.notify(e)
				background = self.main_window.experiment.get("background")
				self.ui.edit_background.setText(background)
		self.main_window.experiment.set("background", foreground)
		self.main_window.experiment.set("background", background)

		# Set the font
		self.main_window.experiment.set('font_family', \
			self.ui.widget_font.family)
		self.main_window.experiment.set('font_size', \
			self.ui.widget_font.size)
		self.main_window.experiment.set('font_italic', \
			self.ui.widget_font.italic)
		self.main_window.experiment.set('font_bold', \
			self.ui.widget_font.bold)

		# Refresh the interface and unlock the general tab
		self.main_window.refresh()
		self.lock = False
		self.main_window.set_busy(False)

	def refresh(self):

		"""Update the controls of the general tab"""

		debug.msg()

		# Lock the general tab to prevent a recursive loop
		self.lock = True

		# Set the header containing the titel etc
		self.set_header_label()

		# Select the backend
		backend = openexp.backend_info.match(self.main_window.experiment)
		if backend == "custom":
			self.ui.combobox_backend.setDisabled(True)
		else:
			self.ui.combobox_backend.setDisabled(False)
			desc = openexp.backend_info.backend_list[backend]["description"]
			i = self.ui.combobox_backend.findText(self.backend_format \
				% (backend, desc))
			self.ui.combobox_backend.setCurrentIndex(i)

		# Set the resolution
		try:
			self.ui.spinbox_width.setValue(int( \
				self.main_window.experiment.width))
			self.ui.spinbox_height.setValue(int( \
				self.main_window.experiment.height))
		except:
			self.main_window.experiment.notify( \
				_("Failed to parse the resolution. Expecting positive numeric values."))

		# Set the colors
		self.ui.edit_foreground.setText(self.main_window.experiment.unistr( \
			self.main_window.experiment.foreground))
		self.ui.edit_background.setText(self.main_window.experiment.unistr( \
			self.main_window.experiment.background))

		# Set the font
		self.ui.widget_font.initialize(self.main_window.experiment)

		# Release the general tab
		self.lock = False

class general_header_widget(header_widget.header_widget):

	"""
	The widget containing the clickable title and description of the experiment
	"""

	def __init__(self, general_tab, item):

		"""
		Constructor

		Arguments:
		item -- the experiment
		"""

		header_widget.header_widget.__init__(self, item)
		self.general_tab = general_tab
		self.label_name.setText( \
			"<font size='5'><b>%s</b> - Experiment</font>&nbsp;&nbsp;&nbsp;<font color='gray'><i>Click to edit</i></font>" \
			% self.item.get("title", _eval=False))

	def restore_name(self):

		"""Apply the name change, hide the editable title and show the label"""

		self.general_tab.apply_changes()
		self.label_name.setText( \
			"<font size='5'><b>%s</b> - Experiment</font>&nbsp;&nbsp;&nbsp;<font color='gray'><i>Click to edit</i></font>" \
			% self.item.get("title", _eval=False))
		self.label_name.show()
		self.edit_name.setText(self.item.get("title", _eval=False))
		self.edit_name.hide()

	def restore_desc(self):

		"""
		Apply the description change, hide the editable description and show the label
		"""

		self.general_tab.apply_changes()
		self.label_desc.setText(self.item.get("description", _eval=False))
		self.label_desc.show()
		self.edit_desc.setText(self.item.get("description", _eval=False))
		self.edit_desc.hide()
