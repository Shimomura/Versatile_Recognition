#coding:utf-8

import wx
import sys
import menu_panel
import study_panel
import judge_panel
import list_panel
import consts


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,"AITraner",size=(600,600))

        #　タイトル部分作成
        self.panel_title=wx.Panel(self, pos=(0,0), size=(600,150))
        self.panel_title.SetBackgroundColour('#4169e1')
        title = wx.StaticText(self.panel_title, wx.ID_ANY, u"汎用画像認識学習装置", pos=(100,50), size=(400,100))
        font = wx.Font(40, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        title.SetFont(font)

        self.next_panel = None

        self.now_panel = menu_panel.MenuPanel(self,wx.ID_ANY)

    def trance_panel(self):
        if self.now_panel is None:
            print("現在画面の取得エラー")
            sys.exit()

        switch = self.now_panel.next_panel
        self.now_panel.Hide()
        self.now_panel = None

        if switch == consts.Consts.STUDY_ID:
            self.now_panel = study_panel.StudyPanel(self,wx.ID_ANY)
        elif switch == consts.Consts.JUDGE_ID:
            self.now_panel = judge_panel.JudgePanel(self,wx.ID_ANY)
        elif switch == consts.Consts.LIST_ID:
            self.now_panel = list_panel.ListPanel(self,wx.ID_ANY)
        else:
            self.now_panel = menu_panel.MenuPanel(self,wx.ID_ANY)



if __name__ == '__main__':
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
