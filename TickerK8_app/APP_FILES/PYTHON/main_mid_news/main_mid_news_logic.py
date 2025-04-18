""" Import """
import mysql.connector
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QLineEdit, # Simple line edit
    QStackedWidget, # Stacked widget
    QGridLayout, # Grid layout
    QVBoxLayout # Vertical layout 
)
from PyQt5.QtCore import Qt
#######################################################################################################################
""" create news widget """
def create_news_widgets(self):
    """ Create dafoult variables """
    news_list = list # Create news list
    user_markets = [1] # Get user markets
    user_countries = [1] # Get user countries 
#______________________________________________________________________________________________________________________
    """ Get news """
    connect = mysql.connector.connect( # Create connect with database
        host = "localhost",
        user = "client",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor() # Create cursor
    cursor.execute('SELECT title, date FROM news ORDER BY date LIMIT 3;')
    news_list.append(cursor.fetchall())

    #for market_id in user_markets: # Add news to news list
    #    cursor.execute(f'SELECT title, date, popularity FROM news WHERE market_id like{market_id} ORDER BY date LIMIT 3;')
    #    news_list.append(cursor.fetchall()) # Add data of news to list 
    #for country_id in user_countries:
    #    cursor.execute(f'SELECT title, date, popularity FROM news WHERE country_id like{country_id} ORDER BY date LIMIT 3;')
    #    news_list.append(cursor.fetchall()) # Add data of news to list
    # Tutaj dla świata jak baze ogrne i dane etc.
#______________________________________________________________________________________________________________________
    widget = QWidget(self)
    layout = QVBoxLayout(wigdet)
#______________________________________________________________________________________________________________________
    for news_data in news_list:
        button = QPushButton(widget)
        self.layout.addWidget(button)
        #button.setIcon(QIcon())
        button.clicked.connect()



