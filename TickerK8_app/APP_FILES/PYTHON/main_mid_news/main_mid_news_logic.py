""" Import """
import requests
import json
from io import BytesIO
import mysql.connector
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QGridLayout, # Grid layout
    QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
#######################################################################################################################
""" create news widget """
def create_news_widget(self):
    """ Create dafoult variables """
    self.news_button_list = []
    self.news_button_visable = 0
#______________________________________________________________________________________________________________________
    """ Get news """
    connect = mysql.connector.connect( # Create connect with database
        host = "localhost",
        user = "client",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor() # Create cursor
    cursor.execute('SELECT id, json_file FROM news ORDER BY popularity LIMIT 3;')
    news_list = cursor.fetchall()
    for index, data in enumerate(news_list, start=1):
        json_data = json.loads(data[1])
        print(data[0])
        id_news = data[0]
        """ Create objects """
        news_button = QPushButton(self)
        text_label = QLabel(news_button)
#______________________________________________________________________________________________________________________
        """ Set object name """
        news_button.setObjectName(f'news_button_{index}')
        text_label.setObjectName(f'text_label_{index}')
#______________________________________________________________________________________________________________________
        """ Set property """
        news_button.setProperty('class', 'news_button')
        text_label.setProperty('class', 'text_label')
#______________________________________________________________________________________________________________________
        """ Set layout """
        self.main_layout.addWidget(news_button, 10, 0, 80, 100)
#______________________________________________________________________________________________________________________
        """ Set Widget """
        news_button.setHidden(True)
#______________________________________________________________________________________________________________________
        """ Set label """
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setWordWrap(True)
#______________________________________________________________________________________________________________________
        """ Set size """
        news_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        news_button.setFixedSize(int(self.width()*0.775), int(self.height()*1.32))
        text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        text_label.setFixedSize(int(self.width()*0.775), int(self.height()*1.32))
#______________________________________________________________________________________________________________________
        """ Set text """
        text_label.setText(json_data['title'])
#______________________________________________________________________________________________________________________
        """ Set graphics """
        photo = requests.get(json_data["photo"]["original"])
        photo.raise_for_status()
        pix = QPixmap()
        pix.loadFromData(BytesIO(photo.content).read())

        zoomed_pix = pix.scaled(news_button.width(), news_button.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        cropped_pix = zoomed_pix.copy(
            (zoomed_pix.width() - news_button.width()) // 2,
            (zoomed_pix.height() - news_button.height()) // 2,
            news_button.width(),
            news_button.height()
        )
        news_button.setIcon(QIcon(cropped_pix))
        news_button.setIconSize(news_button.size())
#______________________________________________________________________________________________________________________
        """ Set connect function for open """
        news_button.clicked.connect(lambda _, id_news_correct=id_news: self.open_news.emit(id_news_correct))
#______________________________________________________________________________________________________________________
        self.news_button_list.append(news_button)
    self.news_button_list[self.news_button_visable].setHidden(False)
    self.timer.timeout.connect(lambda: news_next(self))
    self.timer.start(5000)
#######################################################################################################################
""" News next """
def news_next(self):
    self.timer.stop()
    self.timer.start(5000)
    self.news_button_list[self.news_button_visable].setHidden(True)
    self.news_button_visable = (self.news_button_visable+1)%len(self.news_button_list)
    self.news_button_list[self.news_button_visable].setHidden(False)
#######################################################################################################################
""" News previous """
def news_previous(self):
    self.timer.stop()
    self.timer.start(5000)
    self.news_button_list[self.news_button_visable].setHidden(True)
    self.news_button_visable = (self.news_button_visable-1)%len(self.news_button_list)
    self.news_button_list[self.news_button_visable].setHidden(False)
#######################################################################################################################
