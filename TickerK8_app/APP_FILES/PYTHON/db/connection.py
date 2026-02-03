# --- Import packages ---
import sqlite3
import pymysql
import json
import requests
import pathlib
from cryptography.fernet import Fernet

class database():
    def __init__(self):
        super().__init__()
        self.user_dict = {}
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.conn = self.Connect_offline_database()

# --- Offline database ---
    def Connect_offline_database(self):
        c = sqlite3.connect(
            database=self.main_path+'/CONFIG/GLOBAL/tickerk8_offline.db'
        )
        return c

    def GetCountries(self):
        r = self.conn.execute('SELECT name FROM country;')
        return [x[0] for x in r.fetchall()]

    def GetPhonePrefix(self):
        r = self.conn.execute('SELECT prefix FROM phone_prefix;')
        return [x[0] for x in r.fetchall()]
    
# --- Online database ---
    def ConnectData(self) -> dict:
        try:
            conf = json.load(open(f'{self.main_path}/PYTHON/db/conf.json', 'r'))
            payload = {
                "token":conf['token'],
                "name":'u_app'
            }
            response = requests.post(conf['url'], json=payload)
            response.raise_for_status()
            cipher = Fernet(conf['key'].encode())
            return json.loads(cipher.decrypt(response.text.encode()))
        except:
            pass

# --- Connection --- 
    def Connection(self):
        try:
            login_data = self.user_dict['u_app']
        except:
            self.user_dict['u_app'] = self.ConnectData()
            login_data = self.user_dict['u_app']
        conn = pymysql.connect(
            host=login_data['host'],
            user=login_data['username'],
            password=login_data['password'],
            database=login_data['database'],
            port=login_data['port'],
            ssl={'ca':f'{self.main_path}/PYTHON/db/rds-combined-ca-bundle.pem'}
        )
        return conn

    def LoginByName(self, u_name:str):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL login_by_name(%s);', (u_name,))
            result = curs.fetchone()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def UpdateLastLogin(self, u_id:str):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL update_last_login(%s);', (u_id))
            result = curs.fetchone()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def RegisterUser(self, u_data:tuple):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute("SET @p_errors = NULL;")
            curs.execute(
                "CALL register_user(%s, %s, %s, %s, %s, %s, @p_errors);",
                u_data
            )
            curs.execute("SELECT @p_errors;")
            errors_json = curs.fetchone()[0]
            if errors_json:
                errors = json.loads(errors_json)
                conn.rollback()
                return errors
            conn.commit()
            return None

        except pymysql.err.OperationalError as e:
            if conn:
                conn.rollback()
                raise 
        except Exception as e:
            if conn:
                conn.rollback()
                raise
        finally:
            if curs:
                curs.close()
                curs = None
            if conn:
                conn.close()
                conn = None
    
    def LoginConfiguration(self, id:str, language:int, theme:str, subscription:int, country:list, market:list, stock:list):
        u_data = '{}'
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute(
                "CALL login_configuration(%s);",
                u_data
            )
            curs.execute
            conn.commit()
            return None
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

#   --- Get data ---
    def GetNewsContentById(self, c_id:int):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL get_news_content_by_id(%s);', (c_id,))
            result = curs.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
    
    def GetNewsList(self, s_type:str):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL get_news_list(%s);', (s_type,))
            result = cursor.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
    
    def UpdateNewsPopularity(self, n_id:int):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL update_phone_popularity(%s);', (n_id,))
            result = cursor.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
    
    def GetNewsMain(self):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL get_news_main();')
            result = curs.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
