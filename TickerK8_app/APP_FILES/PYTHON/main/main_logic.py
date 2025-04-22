""" Import main news """
from main_news.main_news_structure import Main_news_widget
""" Open main news """
def open_main_news(self, id_news):
    self.main_news = Main_news_widget(self, id_news)