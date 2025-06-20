import json
""" Import main news """
from main_news.main_news_structure import Main_news_widget
#_______________________________________________________________________________________________________________________
""" Import main news list """
from main_news_list.main_news_list_structure import Main_news_list_widget
#######################################################################################################################
""" Exit """
def exit():
    pass
#######################################################################################################################
""" Open main news """
def open_main_news(self, id_news):
    self.main_news = Main_news_widget(self, id_news)
#######################################################################################################################
""" Open main news list """
def open_main_news_list(self, news_type_index):
    self.main_news_list = Main_news_list_widget(self, news_type_index)
    self.main_news_list.open_news.connect(lambda val: open_main_news(self, val))
#######################################################################################################################
""" main mid object changed """
def main_mid_object_changed(self):
    self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    _o = self.global_config['mid_object'][0]
    if _o == 'country' or _o == 'market':
        self.bottom_left_chart_button.setHidden(True)
    else:
        self.bottom_left_chart_button.setHidden(False)
    self.mid_object_scroll.setup_widget()
#######################################################################################################################