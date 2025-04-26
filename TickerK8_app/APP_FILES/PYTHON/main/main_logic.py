""" Import main news """
from main_news.main_news_structure import Main_news_widget
#_______________________________________________________________________________________________________________________
""" Import main news list """
from main_news_list.main_news_list_structure import Main_news_list_widget
########################################################################################################################
""" Open main news """
def open_main_news(self, id_news):
    self.main_news = Main_news_widget(self, id_news)
#######################################################################################################################
""" Open main news list """
def open_main_news_list(self, news_type_index):
    self.main_news_list = Main_news_list_widget(self, news_type_index)
    #self.main_news_list.open_news.connect(lambda val: open_main_news(self, val))
    self.main_news_list.open_news.connect(lambda val: print(val))
#######################################################################################################################
