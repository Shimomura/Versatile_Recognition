#coding:utf-8

import wx
import consts
import study_panel
import contents_panel_base as base

class MenuPanel(base.ContentsPanelBase):
    """メニュー画面のコンテンツパネルクラス"""
    def __init__(self,parent,id):
        base.ContentsPanelBase.__init__(self, parent, id)

        self.button_study = wx.Button(self, wx.ID_ANY, u"学習する", pos=(150,150), size=(300,100))
        self.buuton_list = wx.Button(self, wx.ID_ANY, u"学習済み一覧", pos=(150,200), size=(300,100))
        self.button_judge = wx.Button(self, wx.ID_ANY, u"識別する", pos=(150,250), size=(300,100))

        self.Bind(wx.EVT_BUTTON, self.trance_study,self.button_study)
        self.Bind(wx.EVT_BUTTON, self.trance_judge,self.button_judge)
        self.Bind(wx.EVT_BUTTON, self.trance_list,self.buuton_list)

        print("complete init")

    def trance_study(self, evt):
        self.next_panel = consts.Consts.STUDY_ID
        self.parent.trance_panel()

    def trance_judge(self, evt):
        self.next_panel = consts.Consts.JUDGE_ID
        self.parent.trance_panel()

    def trance_list(self, evt):
        self.next_panel = consts.Consts.LIST_ID
        self.parent.trance_panel()
