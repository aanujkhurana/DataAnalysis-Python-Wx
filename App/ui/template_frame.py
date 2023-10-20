# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-370-gc831f1f7)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"New South Wales Department of Transportation", pos = wx.DefaultPosition, size = wx.Size( 1200,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"MOTOR VECHILE TRAFFIC ANALYTICS TOOL", wx.Point( -1,-1 ), wx.Size( -1,34 ), 0 )
		self.m_staticText15.Wrap( 0 )

		self.m_staticText15.SetFont( wx.Font( 26, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hiragino Sans GB" ) )
		self.m_staticText15.SetForegroundColour( wx.Colour( 128, 0, 2 ) )
		self.m_staticText15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer2.Add( self.m_staticText15, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.Point( 0,0 ), wx.Size( 1200,800 ), 0|wx.BORDER_SIMPLE )
		self.m_notebook2.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_notebook2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_notebook2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.info = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.info.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )
		self.info.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		main = wx.BoxSizer( wx.VERTICAL )

		dateSelector = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self.info, wx.ID_ANY, u"Enter Date:", wx.DefaultPosition, wx.Size( 120,20 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		dateSelector.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.info, wx.ID_ANY, u"FROM", wx.DefaultPosition, wx.Size( 40,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		dateSelector.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_datePicker_start = wx.adv.DatePickerCtrl( self.info, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 140,-1 ), wx.adv.DP_DROPDOWN|wx.BORDER_THEME )
		self.m_datePicker_start.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )
		self.m_datePicker_start.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		dateSelector.Add( self.m_datePicker_start, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.info, wx.ID_ANY, u"TO", wx.DefaultPosition, wx.Size( 20,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		dateSelector.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_datePicker_end = wx.adv.DatePickerCtrl( self.info, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 140,-1 ), wx.adv.DP_DROPDOWN|wx.BORDER_THEME )
		self.m_datePicker_end.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )
		self.m_datePicker_end.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_datePicker_end.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		dateSelector.Add( self.m_datePicker_end, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button1 = wx.Button( self.info, wx.ID_ANY, u"FIND", wx.Point( 0,0 ), wx.Size( 300,40 ), 0 )

		self.m_button1.SetDefault()

		self.m_button1.SetBitmapMargins( wx.Size( 100,30 ) )
		self.m_button1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		dateSelector.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL|wx.LEFT|wx.RIGHT, 5 )

		self.m_button3 = wx.Button( self.info, wx.ID_ANY, u"Reset", wx.Point( 0,0 ), wx.Size( 200,40 ), 0 )

		self.m_button3.SetBitmapMargins( wx.Size( 100,30 ) )
		self.m_button3.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_button3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		dateSelector.Add( self.m_button3, 0, wx.ALL, 5 )


		main.Add( dateSelector, 0, wx.EXPAND, 5 )

		filterSelector = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self.info, wx.ID_ANY, u"Filters:", wx.DefaultPosition, wx.Size( 120,20 ), wx.ALIGN_RIGHT )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		filterSelector.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_comboBox1Choices = [ u"None", u"LEGISLATION", u"SECTION_CLAUSE", u"OFFENCE_CODE", u"LOCATION_CODE", u"SPEED_BAND", u"CAMERA_TYPE", u"LOCATION_DETAILS" ]
		self.m_comboBox1 = wx.ComboBox( self.info, wx.ID_ANY, u"OFFENCE_CODE", wx.DefaultPosition, wx.Size( 200,30 ), m_comboBox1Choices, wx.CB_DROPDOWN|wx.CB_READONLY|wx.CB_SIMPLE|wx.TE_PROCESS_ENTER )
		self.m_comboBox1.SetSelection( 3 )
		self.m_comboBox1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )

		filterSelector.Add( self.m_comboBox1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_comboText = wx.TextCtrl( self.info, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 470,-1 ), 0|wx.BORDER_SIMPLE )
		self.m_comboText.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )
		self.m_comboText.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		filterSelector.Add( self.m_comboText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button2 = wx.Button( self.info, wx.ID_ANY, u"Filter", wx.Point( 0,0 ), wx.Size( 200,40 ), 0 )

		self.m_button2.SetBitmapMargins( wx.Size( 100,30 ) )
		self.m_button2.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_button2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		filterSelector.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL|wx.LEFT|wx.RIGHT, 5 )


		main.Add( filterSelector, 0, 0, 5 )

		self.m_grid1 = wx.grid.Grid( self.info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC )

		# Grid
		self.m_grid1.CreateGrid( 50, 50 )
		self.m_grid1.EnableEditing( False )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 10, 10 )

		# Columns
		self.m_grid1.SetColSize( 0, 41 )
		self.m_grid1.SetColSize( 1, 41 )
		self.m_grid1.SetColSize( 2, 42 )
		self.m_grid1.SetColSize( 3, 42 )
		self.m_grid1.SetColSize( 4, 40 )
		self.m_grid1.SetColSize( 5, 40 )
		self.m_grid1.SetColSize( 6, 42 )
		self.m_grid1.SetColSize( 7, 42 )
		self.m_grid1.SetColSize( 8, 36 )
		self.m_grid1.SetColSize( 9, 39 )
		self.m_grid1.SetColSize( 10, 40 )
		self.m_grid1.SetColSize( 11, 39 )
		self.m_grid1.SetColSize( 12, 44 )
		self.m_grid1.SetColSize( 13, 43 )
		self.m_grid1.SetColSize( 14, 42 )
		self.m_grid1.AutoSizeColumns()
		self.m_grid1.EnableDragColMove( True )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.SetRowSize( 0, 22 )
		self.m_grid1.SetRowSize( 1, 23 )
		self.m_grid1.SetRowSize( 2, 22 )
		self.m_grid1.SetRowSize( 3, 22 )
		self.m_grid1.SetRowSize( 4, 22 )
		self.m_grid1.SetRowSize( 5, 22 )
		self.m_grid1.SetRowSize( 6, 22 )
		self.m_grid1.SetRowSize( 7, 22 )
		self.m_grid1.SetRowSize( 8, 22 )
		self.m_grid1.SetRowSize( 9, 22 )
		self.m_grid1.SetRowSize( 10, 22 )
		self.m_grid1.SetRowSize( 11, 22 )
		self.m_grid1.SetRowSize( 12, 22 )
		self.m_grid1.SetRowSize( 13, 22 )
		self.m_grid1.SetRowSize( 14, 22 )
		self.m_grid1.SetRowSize( 15, 22 )
		self.m_grid1.SetRowSize( 16, 22 )
		self.m_grid1.SetRowSize( 17, 22 )
		self.m_grid1.SetRowSize( 18, 22 )
		self.m_grid1.SetRowSize( 19, 22 )
		self.m_grid1.AutoSizeRows()
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid1.SetLabelBackgroundColour( wx.Colour( 15, 128, 255 ) )
		self.m_grid1.SetLabelFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )
		self.m_grid1.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		# Cell Defaults
		self.m_grid1.SetDefaultCellFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )

		main.Add( self.m_grid1, 0, 0, 10 )


		self.info.SetSizer( main )
		self.info.Layout()
		main.Fit( self.info )
		self.m_notebook2.AddPage( self.info, u"Find Cases", True )
		self.search = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		filterSelector1 = wx.BoxSizer( wx.VERTICAL )

		dateSelector1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self.search, wx.ID_ANY, u"Enter Date:", wx.DefaultPosition, wx.Size( 120,20 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		dateSelector1.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self.search, wx.ID_ANY, u"FROM", wx.DefaultPosition, wx.Size( 40,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		dateSelector1.Add( self.m_staticText22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_datePicker_start1 = wx.adv.DatePickerCtrl( self.search, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 140,-1 ), wx.adv.DP_DROPDOWN|wx.BORDER_THEME )
		self.m_datePicker_start1.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )
		self.m_datePicker_start1.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		dateSelector1.Add( self.m_datePicker_start1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self.search, wx.ID_ANY, u"TO", wx.DefaultPosition, wx.Size( 20,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		dateSelector1.Add( self.m_staticText32, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_datePicker_end1 = wx.adv.DatePickerCtrl( self.search, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 140,-1 ), wx.adv.DP_DROPDOWN|wx.BORDER_THEME )
		self.m_datePicker_end1.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )
		self.m_datePicker_end1.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_datePicker_end1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		dateSelector1.Add( self.m_datePicker_end1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		filterSelector1.Add( dateSelector1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_offence = wx.StaticText( self.search, wx.ID_ANY, u"Search Offence Description", wx.DefaultPosition, wx.Size( -1,20 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText_offence.Wrap( -1 )

		self.m_staticText_offence.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		bSizer31.Add( self.m_staticText_offence, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self.search, wx.ID_ANY, u"Search for any keyword(s) or type anything below to find related records", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_SLANT, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText16.SetForegroundColour( wx.Colour( 15, 128, 255 ) )

		bSizer31.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.BOTTOM, 5 )

		self.m_search_text = wx.TextCtrl( self.search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,60 ), wx.TE_MULTILINE|wx.BORDER_SIMPLE )
		self.m_search_text.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )
		self.m_search_text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer31.Add( self.m_search_text, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button_offence = wx.Button( self.search, wx.ID_ANY, u"Find", wx.Point( -1,-1 ), wx.Size( 400,40 ), wx.BORDER_NONE )

		self.m_button_offence.SetDefault()

		self.m_button_offence.SetBitmapMargins( wx.Size( 100,30 ) )
		self.m_button_offence.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_button_offence.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button_offence.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer31.Add( self.m_button_offence, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_grid_offence = wx.grid.Grid( self.search, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_STATIC )

		# Grid
		self.m_grid_offence.CreateGrid( 25, 20 )
		self.m_grid_offence.EnableEditing( False )
		self.m_grid_offence.EnableGridLines( True )
		self.m_grid_offence.SetGridLineColour( wx.Colour( 15, 128, 255 ) )
		self.m_grid_offence.EnableDragGridSize( True )
		self.m_grid_offence.SetMargins( 10, 40 )

		# Columns
		self.m_grid_offence.SetColSize( 0, 41 )
		self.m_grid_offence.SetColSize( 1, 41 )
		self.m_grid_offence.SetColSize( 2, 42 )
		self.m_grid_offence.SetColSize( 3, 42 )
		self.m_grid_offence.SetColSize( 4, 40 )
		self.m_grid_offence.SetColSize( 5, 40 )
		self.m_grid_offence.SetColSize( 6, 42 )
		self.m_grid_offence.SetColSize( 7, 42 )
		self.m_grid_offence.SetColSize( 8, 36 )
		self.m_grid_offence.SetColSize( 9, 39 )
		self.m_grid_offence.SetColSize( 10, 40 )
		self.m_grid_offence.SetColSize( 11, 39 )
		self.m_grid_offence.SetColSize( 12, 44 )
		self.m_grid_offence.SetColSize( 13, 43 )
		self.m_grid_offence.SetColSize( 14, 42 )
		self.m_grid_offence.EnableDragColMove( True )
		self.m_grid_offence.EnableDragColSize( True )
		self.m_grid_offence.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
		self.m_grid_offence.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid_offence.SetRowSize( 0, 23 )
		self.m_grid_offence.SetRowSize( 1, 23 )
		self.m_grid_offence.SetRowSize( 2, 22 )
		self.m_grid_offence.SetRowSize( 3, 22 )
		self.m_grid_offence.SetRowSize( 4, 22 )
		self.m_grid_offence.SetRowSize( 5, 22 )
		self.m_grid_offence.SetRowSize( 6, 22 )
		self.m_grid_offence.SetRowSize( 7, 22 )
		self.m_grid_offence.SetRowSize( 8, 22 )
		self.m_grid_offence.SetRowSize( 9, 22 )
		self.m_grid_offence.SetRowSize( 10, 22 )
		self.m_grid_offence.SetRowSize( 11, 22 )
		self.m_grid_offence.SetRowSize( 12, 22 )
		self.m_grid_offence.SetRowSize( 13, 22 )
		self.m_grid_offence.SetRowSize( 14, 22 )
		self.m_grid_offence.SetRowSize( 15, 22 )
		self.m_grid_offence.SetRowSize( 16, 22 )
		self.m_grid_offence.SetRowSize( 17, 22 )
		self.m_grid_offence.SetRowSize( 18, 22 )
		self.m_grid_offence.SetRowSize( 19, 22 )
		self.m_grid_offence.SetRowSize( 20, 18 )
		self.m_grid_offence.SetRowSize( 21, 18 )
		self.m_grid_offence.SetRowSize( 22, 18 )
		self.m_grid_offence.SetRowSize( 23, 18 )
		self.m_grid_offence.SetRowSize( 24, 18 )
		self.m_grid_offence.EnableDragRowSize( True )
		self.m_grid_offence.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
		self.m_grid_offence.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid_offence.SetLabelBackgroundColour( wx.Colour( 15, 128, 255 ) )
		self.m_grid_offence.SetLabelFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )
		self.m_grid_offence.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		# Cell Defaults
		self.m_grid_offence.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid_offence.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )

		bSizer31.Add( self.m_grid_offence, 0, wx.ALL, 5 )


		filterSelector1.Add( bSizer31, 1, wx.EXPAND, 5 )


		self.search.SetSizer( filterSelector1 )
		self.search.Layout()
		filterSelector1.Fit( self.search )
		self.m_notebook2.AddPage( self.search, u"Search Offence", False )
		self.graphs = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		filters = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText41 = wx.StaticText( self.graphs, wx.ID_ANY, u"Chart Type:", wx.DefaultPosition, wx.Size( 120,20 ), wx.ALIGN_RIGHT )
		self.m_staticText41.Wrap( -1 )

		self.m_staticText41.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_staticText41.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		filters.Add( self.m_staticText41, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_comboBox_graphChoices = [ u"PenaltyCasesAnalysis", u"LocationAnalysis", u"CameraAnalysis", u"SeasonalAnalysis", u"HeatMap" ]
		self.m_comboBox_graph = wx.ComboBox( self.graphs, wx.ID_ANY, u"HeatMap Chart", wx.DefaultPosition, wx.Size( 170,30 ), m_comboBox_graphChoices, wx.CB_DROPDOWN|wx.CB_READONLY|wx.CB_SIMPLE|wx.TE_PROCESS_ENTER )
		self.m_comboBox_graph.SetSelection( 3 )
		self.m_comboBox_graph.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )

		filters.Add( self.m_comboBox_graph, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.graphs, wx.ID_ANY, u"FROM", wx.DefaultPosition, wx.Size( 40,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		filters.Add( self.m_staticText21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_datePicker_graph_start = wx.adv.DatePickerCtrl( self.graphs, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 140,-1 ), wx.adv.DP_DROPDOWN|wx.BORDER_THEME )
		self.m_datePicker_graph_start.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )
		self.m_datePicker_graph_start.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		filters.Add( self.m_datePicker_graph_start, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self.graphs, wx.ID_ANY, u"TO", wx.DefaultPosition, wx.Size( 20,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		filters.Add( self.m_staticText31, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_datePicker_graph_end = wx.adv.DatePickerCtrl( self.graphs, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 140,-1 ), wx.adv.DP_DROPDOWN|wx.BORDER_THEME )
		self.m_datePicker_graph_end.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )
		self.m_datePicker_graph_end.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_datePicker_graph_end.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		filters.Add( self.m_datePicker_graph_end, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button_graph = wx.Button( self.graphs, wx.ID_ANY, u"Generate", wx.Point( 0,0 ), wx.Size( 200,40 ), 0 )

		self.m_button_graph.SetBitmapMargins( wx.Size( 100,30 ) )
		self.m_button_graph.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_button_graph.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		filters.Add( self.m_button_graph, 0, wx.ALIGN_CENTER|wx.ALL|wx.LEFT|wx.RIGHT, 5 )

		self.m_button_export = wx.Button( self.graphs, wx.ID_ANY, u"Export", wx.Point( 0,0 ), wx.Size( 200,40 ), 0 )

		self.m_button_export.SetBitmapMargins( wx.Size( 100,30 ) )
		self.m_button_export.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_button_export.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		filters.Add( self.m_button_export, 0, wx.ALL, 5 )


		bSizer28.Add( filters, 1, wx.EXPAND, 5 )

		graphPanel = wx.BoxSizer( wx.VERTICAL )

		self.m_panel = wx.Panel( self.graphs, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,1000 ), wx.BORDER_RAISED )
		graphPanel.Add( self.m_panel, 1, wx.EXPAND, 5 )


		bSizer28.Add( graphPanel, 1, wx.EXPAND, 5 )


		self.graphs.SetSizer( bSizer28 )
		self.graphs.Layout()
		bSizer28.Fit( self.graphs )
		self.m_notebook2.AddPage( self.graphs, u"Generate Graphs", False )
		self.report = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		dateSelector2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self.report, wx.ID_ANY, u"Enter Date:", wx.DefaultPosition, wx.Size( 120,20 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		dateSelector2.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.report, wx.ID_ANY, u"FROM", wx.DefaultPosition, wx.Size( 40,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText23.Wrap( -1 )

		self.m_staticText23.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		dateSelector2.Add( self.m_staticText23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_datePicker_rstart = wx.adv.DatePickerCtrl( self.report, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 140,-1 ), wx.adv.DP_DROPDOWN|wx.BORDER_THEME )
		self.m_datePicker_rstart.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )
		self.m_datePicker_rstart.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		dateSelector2.Add( self.m_datePicker_rstart, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self.report, wx.ID_ANY, u"TO", wx.DefaultPosition, wx.Size( 20,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		dateSelector2.Add( self.m_staticText33, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_datePicker_rend = wx.adv.DatePickerCtrl( self.report, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 140,-1 ), wx.adv.DP_DROPDOWN|wx.BORDER_THEME )
		self.m_datePicker_rend.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )
		self.m_datePicker_rend.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_datePicker_rend.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		dateSelector2.Add( self.m_datePicker_rend, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText411 = wx.StaticText( self.report, wx.ID_ANY, u"Chart Type:", wx.DefaultPosition, wx.Size( 120,20 ), wx.ALIGN_RIGHT )
		self.m_staticText411.Wrap( -1 )

		self.m_staticText411.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_staticText411.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		dateSelector2.Add( self.m_staticText411, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )

		m_comboBox_graph1Choices = [ u"BarGraph", u"PieChart", u"LineGraph", u"StackPlot" ]
		self.m_comboBox_graph1 = wx.ComboBox( self.report, wx.ID_ANY, u"LineGraph", wx.DefaultPosition, wx.Size( 140,30 ), m_comboBox_graph1Choices, wx.CB_DROPDOWN|wx.CB_READONLY|wx.CB_SIMPLE|wx.TE_PROCESS_ENTER )
		self.m_comboBox_graph1.SetSelection( 2 )
		self.m_comboBox_graph1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )

		dateSelector2.Add( self.m_comboBox_graph1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button_r = wx.Button( self.report, wx.ID_ANY, u"Generate", wx.Point( 0,0 ), wx.Size( 300,40 ), 0 )

		self.m_button_r.SetBitmapMargins( wx.Size( 100,30 ) )
		self.m_button_r.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_button_r.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		dateSelector2.Add( self.m_button_r, 0, wx.ALIGN_CENTER|wx.ALL|wx.LEFT, 5 )


		bSizer11.Add( dateSelector2, 0, wx.EXPAND, 5 )

		bSizer74 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText20 = wx.StaticText( self.report, wx.ID_ANY, u" Speed-Related Violations", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_staticText20.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		bSizer16.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_grid_r1 = wx.grid.Grid( self.report, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC )

		# Grid
		self.m_grid_r1.CreateGrid( 10, 2 )
		self.m_grid_r1.EnableEditing( False )
		self.m_grid_r1.EnableGridLines( True )
		self.m_grid_r1.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_grid_r1.EnableDragGridSize( False )
		self.m_grid_r1.SetMargins( 10, 10 )

		# Columns
		self.m_grid_r1.SetColSize( 0, 260 )
		self.m_grid_r1.SetColSize( 1, 75 )
		self.m_grid_r1.EnableDragColMove( False )
		self.m_grid_r1.EnableDragColSize( False )
		self.m_grid_r1.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
		self.m_grid_r1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid_r1.SetRowSize( 0, 40 )
		self.m_grid_r1.AutoSizeRows()
		self.m_grid_r1.EnableDragRowSize( False )
		self.m_grid_r1.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
		self.m_grid_r1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid_r1.SetLabelBackgroundColour( wx.Colour( 128, 0, 2 ) )
		self.m_grid_r1.SetLabelFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )
		self.m_grid_r1.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		# Cell Defaults
		self.m_grid_r1.SetDefaultCellFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )
		self.m_grid_r1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
		self.m_grid_r1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )

		bSizer16.Add( self.m_grid_r1, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 20 )


		bSizer15.Add( bSizer16, 0, 0, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText211 = wx.StaticText( self.report, wx.ID_ANY, u"Top Locations with Max Penalty Cases", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		self.m_staticText211.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_staticText211.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		bSizer17.Add( self.m_staticText211, 0, wx.ALL, 5 )

		self.m_grid_r2 = wx.grid.Grid( self.report, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC )

		# Grid
		self.m_grid_r2.CreateGrid( 10, 2 )
		self.m_grid_r2.EnableEditing( False )
		self.m_grid_r2.EnableGridLines( True )
		self.m_grid_r2.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_grid_r2.EnableDragGridSize( False )
		self.m_grid_r2.SetMargins( 10, 10 )

		# Columns
		self.m_grid_r2.SetColSize( 0, 380 )
		self.m_grid_r2.SetColSize( 1, 80 )
		self.m_grid_r2.EnableDragColMove( False )
		self.m_grid_r2.EnableDragColSize( False )
		self.m_grid_r2.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
		self.m_grid_r2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid_r2.SetRowSize( 0, 40 )
		self.m_grid_r2.AutoSizeRows()
		self.m_grid_r2.EnableDragRowSize( False )
		self.m_grid_r2.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
		self.m_grid_r2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid_r2.SetLabelBackgroundColour( wx.Colour( 128, 0, 2 ) )
		self.m_grid_r2.SetLabelFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )
		self.m_grid_r2.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		# Cell Defaults
		self.m_grid_r2.SetDefaultCellFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_MEDIUM, False, "Helvetica Neue" ) )
		self.m_grid_r2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
		self.m_grid_r2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )

		bSizer17.Add( self.m_grid_r2, 0, wx.LEFT, 20 )


		bSizer15.Add( bSizer17, 0, wx.EXPAND, 5 )


		bSizer74.Add( bSizer15, 0, 0, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel14 = wx.Panel( self.report, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer161.Add( self.m_panel14, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer151.Add( bSizer161, 1, wx.EXPAND, 5 )

		bSizer171 = wx.BoxSizer( wx.VERTICAL )


		bSizer151.Add( bSizer171, 1, wx.EXPAND, 5 )


		bSizer74.Add( bSizer151, 1, wx.EXPAND, 5 )


		bSizer11.Add( bSizer74, 1, wx.EXPAND, 5 )


		self.report.SetSizer( bSizer11 )
		self.report.Layout()
		bSizer11.Fit( self.report )
		self.m_notebook2.AddPage( self.report, u"Get Report", False )
		self.MC = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_mobilecase = wx.Button( self.MC, wx.ID_ANY, u"CLICK HERE FOR MOBILE CASES ANALYSIS REPORT", wx.Point( -1,-1 ), wx.Size( 400,40 ), wx.BORDER_NONE )

		self.m_button_mobilecase.SetDefault()

		self.m_button_mobilecase.SetBitmapMargins( wx.Size( 100,30 ) )
		self.m_button_mobilecase.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_button_mobilecase.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button_mobilecase.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer44.Add( self.m_button_mobilecase, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer192 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2012 = wx.StaticText( self.MC, wx.ID_ANY, u"Mobile Phone Usage Offenses Trend Over Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2012.Wrap( -1 )

		self.m_staticText2012.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_staticText2012.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		bSizer192.Add( self.m_staticText2012, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.MC, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,200 ), wx.TE_LEFT|wx.TE_READONLY )
		self.m_textCtrl1.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		bSizer192.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer211.Add( bSizer192, 1, wx.EXPAND, 5 )

		bSizer1912 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText20112 = wx.StaticText( self.MC, wx.ID_ANY, u"Mobile Phone Cases Offense Code Counts:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20112.Wrap( -1 )

		self.m_staticText20112.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_staticText20112.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		bSizer1912.Add( self.m_staticText20112, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.MC, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_LEFT|wx.TE_READONLY )
		self.m_textCtrl2.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		bSizer1912.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer211.Add( bSizer1912, 1, wx.EXPAND, 5 )

		bSizer19111 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText201111 = wx.StaticText( self.MC, wx.ID_ANY, u"Amount Collected in each year from MobileCases:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201111.Wrap( -1 )

		self.m_staticText201111.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_staticText201111.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		bSizer19111.Add( self.m_staticText201111, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.MC, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_LEFT|wx.TE_READONLY )
		self.m_textCtrl3.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )

		bSizer19111.Add( self.m_textCtrl3, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer211.Add( bSizer19111, 1, wx.EXPAND, 5 )


		bSizer44.Add( bSizer211, 1, wx.EXPAND, 5 )

		bSizer2111 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer1921 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel9 = wx.Panel( self.MC, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,600 ), wx.TAB_TRAVERSAL )
		self.m_panel9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1921.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer2111.Add( bSizer1921, 1, wx.EXPAND, 5 )


		bSizer44.Add( bSizer2111, 1, wx.EXPAND, 5 )


		self.MC.SetSizer( bSizer44 )
		self.MC.Layout()
		bSizer44.Fit( self.MC )
		self.m_notebook2.AddPage( self.MC, u"Mobile Cases", False )

		bSizer2.Add( self.m_notebook2, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


