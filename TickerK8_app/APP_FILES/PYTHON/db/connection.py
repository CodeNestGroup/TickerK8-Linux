# --- Import packages ---
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
    
# --- Connect data ---
    def ConnectData(self, user:str) -> dict:
        try:
            conf = json.load(open(f'{self.main_path}/PYTHON/db/conf.json', 'r'))
            payload = {
                "token":conf['token'],
                "name":user
            }
            response = requests.post(conf['url'], json=payload)
            response.raise_for_status()
            cipher = Fernet(conf['key'].encode())
            return json.loads(cipher.decrypt(response.text.encode()))
        except:
            pass

# --- Connection --- 
    def Connection(self, u_name:str):
        try:
            login_data = self.user_dict[u_name]
        except:
            self.user_dict[u_name] = self.ConnectData(u_name)
            login_data = self.user_dict[u_name]
        conn = pymysql.connect(
            host=login_data['host'],
            user=login_data['username'],
            password=login_data['password'],
            database=login_data['database'],
            port=login_data['port'],
            ssl={'ca':f'{self.main_path}/PYTHON/db/rds-combined-ca-bundle.pem'}
        )
        return conn

#   --- Get data ---
    def LoginByName(self, u_name:str):
        conn = self.Connection("u_login")
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

    def GetCountries(self):
        conn = self.Connection("u_register")
        curs = conn.cursor()
        try:
            curs.execute('CALL get_countries();')
            result = curs.fetchall()
            return [x[0] for x in result]
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
            result = curs.fetchall()
            return [x[0] for x in result]
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def RegisterUser(self, u_data:tuple):
        conn = self.Connection("u_register")
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

    def GetNewsContentById(self, c_id:int):
        conn = self.Connection("u_news")
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
        conn = self.Connection("u_news")
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
        conn = self.Connection("u_news")
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
        conn = self.Connection("u_news")
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
