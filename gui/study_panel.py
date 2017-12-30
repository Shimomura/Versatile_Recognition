
import wx
import consts
import study_panel
import contents_panel_base as base

class StudyPanel(base.ContentsPanelBase):
    """学習画面のコンテンツパネルクラス"""
    def __init__(self,parent,id):
        base.ContentsPanelBase.__init__(self, parent, id)

        font = wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        name_label = wx.StaticText(self, wx.ID_ANY, u"学習名", pos=(10,10), size=(400,50))
        name_label.SetFont(font)

        name_text = wx.TextCtrl(self, wx.ID_ANY, pos=(10,35), size=(450,30))
        name_text.SetFont(font)


        dir_label = wx.StaticText(self, wx.ID_ANY, u"学習サンプルフォルダ", pos=(10,90), size=(400,50))
        dir_label.SetFont(font)

        name_text = wx.TextCtrl(self, wx.ID_ANY, pos=(10,115), size=(450,30))
        name_text.SetFont(font)

        self.button_study = wx.Button(self, wx.ID_ANY, u"フォルダ選択", pos=(465,110), size=(110,40))

        self.button_start = wx.Button(self, wx.ID_ANY, u"学習開始", pos=(485,360), size=(90,70))
        self.button_return = wx.Button(self, wx.ID_ANY, u"戻る", pos=(365,360), size=(90,70))

        self.Bind(wx.EVT_BUTTON, self.trance_menu,self.button_return)
        self.Bind(wx.EVT_BUTTON, self.start_study,self.button_start)

    def start_study(self, evt):
        dialog = wx.MessageDialog(self, '学習中...', '', style=wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def trance_menu(self, evt):
        self.next_panel = consts.Consts.MENU_ID
        self.parent.trance_panel()
