
import wx
import consts
import study_panel
import contents_panel_base as base

class ListPanel(base.ContentsPanelBase):
    """一覧画面のコンテンツパネルクラス"""
    def __init__(self,parent,id):
        base.ContentsPanelBase.__init__(self, parent, id)

        font = wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)


        listbox = wx.ListBox(self, wx.ID_ANY, choices=self.get_studied_list()
                            , style=wx.LB_SINGLE, pos=(5,5), size=(300,320))


        self.button_del = wx.Button(self, wx.ID_ANY, u"削除", pos=(485,360), size=(90,70))
        self.button_upd = wx.Button(self, wx.ID_ANY, u"修正", pos=(365,360), size=(90,70))
        self.button_return = wx.Button(self, wx.ID_ANY, u"戻る", pos=(245,360), size=(90,70))

        self.Bind(wx.EVT_BUTTON, self.trance_menu,self.button_return)
        self.Bind(wx.EVT_BUTTON, self.del_studied,self.button_del)
        self.Bind(wx.EVT_BUTTON, self.upd_studied,self.button_upd)

    def del_studied(self, evt):
        dialog = wx.MessageDialog(self, '削除します、よろしいですか？', '', style=wx.YES_NO)
        res = dialog.ShowModal()

        if res == wx.ID_YES:
            print("yes")
        elif res == wx.ID_NO:
            print("no")

        dialog.Destroy()

    def upd_studied(self, evt):
        dialog = wx.MessageDialog(self, '修正します、よろしいですか？', '', style=wx.YES_NO)
        res = dialog.ShowModal()

        if res == wx.ID_YES:
            print("yes")
        elif res == wx.ID_NO:
            print("no")

        dialog.Destroy()

    def trance_menu(self, evt):
        self.next_panel = consts.Consts.MENU_ID
        self.parent.trance_panel()

    def get_studied_list(self):
        return ["猫","犬","花"]
