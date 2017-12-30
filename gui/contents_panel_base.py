#coding:utf-8

import wx
import consts
import study_panel

class ContentsPanelBase(wx.Panel):
    """コンテンツパネルクラス基底クラス"""
    def __init__(self,parent,id):
        wx.Panel.__init__(self, parent, id
                          ,pos=(0,consts.Consts.TITLE_SIZE_Y)
                          ,size=(consts.Consts.CONTENTS_SIZE_X,consts.Consts.CONTENTS_SIZE_Y))

        self.parent=parent
        self.next_panel = None
