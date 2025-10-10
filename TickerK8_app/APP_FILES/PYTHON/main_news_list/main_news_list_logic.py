""" Import """
import mysql
import json
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QPushButton, # Simple button
    QLabel, # Label
    QGridLayout, # Grid layout
    QSizePolicy, # Size policy
    QVBoxLayout, # Vertical layout 
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt, # Qt settings
    QSize, # Size
    QRect # Rect
)
#######################################################################################################################
""" News list main widget """
def news_list_widget(self):
    """ Load user settings """
    user_setting = list(dict(json.load(open(self.main_path+'/CONFIG/GLOBAL/logged_user.json', 'r'))).values())[self.news_type]
    news_type_name = None # Set dafoult
    result = None # Set dafoult
    if self.news_type == 0:
        news_type_name = 'market_id'
    elif self.news_type == 1:
        news_type_name = 'country_id'
    else:
        news_type_name = 'world'
#______________________________________________________________________________________________________________________
    """ Get data """
    connect = mysql.connector.connect(
        host = "localhost",
        user = "client",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor()
    cursor.execute(f'SELECT id, title, date  FROM news WHERE {news_type_name}={user_setting};')
    result = cursor.fetchall()
    cursor.close() # Close cursor
    connect.close() # Close connect 
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.news_list_widget = QWidget(self.news_list_scroll)
    self.news_list_layout = QVBoxLayout(self.news_list_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.news_list_widget.setObjectName('news_list_widget')
#______________________________________________________________________________________________________________________
    """ Set property """
#______________________________________________________________________________________________________________________
    """ Set Layout """
    self.news_list_layout.setSpacing(0)
    self.news_list_layout.setContentsMargins(0,0,0,0)
    self.news_list_widget.setLayout(self.news_list_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.news_list_scroll.setWidget(self.news_list_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
#______________________________________________________________________________________________________________________
    """ Set size """
    self.news_list_widget.setMaximumWidth(self.news_list_scroll.width())
    self.news_list_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Create news """
    for index, rows in enumerate(result, start=0):
        """ Create objects """
        news_button = QPushButton(self.news_list_widget)
        news_layout = QGridLayout(news_button)
        date_label = QLabel(news_button)
        text_label = QLabel(news_button)
#______________________________________________________________________________________________________________________
        """ Set object name """
        news_button.setObjectName(f'news_button_{index}')
        date_label.setObjectName(f'date_label_{index}')
        text_label.setObjectName(f'text_label_{index}')
#______________________________________________________________________________________________________________________
        """ Set property """
        news_button.setProperty('class', 'news_button')
        date_label.setProperty('class', 'date_label')
        text_label.setProperty('class', 'text_label')
#______________________________________________________________________________________________________________________
        """ Set layout """
        news_layout.addWidget(date_label, 0, 0, 100, 25)
        news_layout.addWidget(text_label, 0, 25, 100, 75)
        news_layout.setSpacing(0)
        news_layout.setContentsMargins(0,0,0,0)
        for enc in range(100):
            news_layout.setRowStretch(enc, 1)
            news_layout.setColumnStretch(enc, 1)
        news_button.setLayout(news_layout)
#______________________________________________________________________________________________________________________
        date_label.setAlignment(Qt.AlignCenter)
        date_label.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setAttribute(Qt.WA_TransparentForMouseEvents, True)
#______________________________________________________________________________________________________________________
        """ Set size """
        news_button.setFixedSize(QSize(self.news_list_scroll.width(), self.news_list_scroll.height()//8))
        news_button.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding)
        date_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
        """ Set text """
        date_label.setText(str(rows[2]))
        text_label.setText(str(rows[1]))
        self.news_list_layout.addWidget(news_button)
#______________________________________________________________________________________________________________________
        """ Connect functions """
        news_button.clicked.connect(lambda _, id_news_correct=int(rows[0]): self.open_news.emit(id_news_correct))
#######################################################################################################################
