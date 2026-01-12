# --- Import packages ---
import pymysql
import json

class database():
    def __init__(self):
        super().__init__()
        self.user_dict = {}

# --- Connect data ---
    def ConnectData(name:str):
        # Tutaj dodać, że pobiera z lambda, rozwarzyć napisanie tego w lambda 
        pass

# --- Connection --- 
    def Connection(self, u_name:str):
        try:
            login_data = self.user_dict[u_name]
        except:
            self.user_dcict[u_name] = self.ConnectData(u_name)
            login_data = self.user_dict[u_name]

        conn = pymsql.connect(
            host=login_data['host'],
            user=login_data['username'],
            password=login_data['password'],
            database=login_data['database'],
            port=login_data['port'],
            ssl='/'
        )
        return conn

#   --- Get data ---
    def LoginByName(self, u_name:str):
        conn = self.Connection("u_login")
        curs = conn.cursor()
        try:
            curs.execute('CALL login_by_name(%s);', u_name)
            result = cursor.fetchone()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def GetCountries(self):
        conn = self.Connection("u_register")
        curs = conn.cursor()
        try:
            curs.execute('CALL get_countries();')
            result = cursor.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def GetPhonePrefix(self):
        conn = self.Connection("u_register")
        curs = conn.cursor()
        try:
            curs.execute('CALL get_phone_prefix();')
            result = cursor.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def RegisterUser(self, u_data:tuple):
        conn = self.Connection("u_register")
        curs = conn.cursor()
        try:
            curs.execute('CALL get_phone_prefix(%s, %s, %s %s, %s, %s);', u_data)
            
            return result
        finally:
            conn.close()

    def GetNewsContentById(self, c_id:int):
        conn = self.Connection("u_news")
        curs = conn.cursor()
        try:
            curs.execute('CALL get_news_content_by_id(%s);', c_id)
            result = cursor.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
    
    def GetNewsList(self, s_type:str):
        conn = self.Connection("u_news")
        curs = conn.cursor()
        try:
            curs.execute('CALL get_news_list(%s);', s_type)
            result = cursor.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
    
    def UpdateNewsPopularity(self, n_id:int):
        conn = self.Connection("u_news")
        curs = conn.cursor()
        try:
            curs.execute('CALL update_phone_popularity(%s);', n_id)
            result = cursor.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
    
    def GetNewsMain(self):
        conn = self.Connection("u_news")
        curs = conn.cursor()
        try:
            curs.execute('CALL get_news_main();')
            result = cursor.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def SendReport(self, mess:str):
        conn = self.Connection("u_report")
        curs = conn.cursor()
        try:
            curs.execute('CALL send_report(%s);', mess)
            result = cursor.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None




print(database.get_secret())

