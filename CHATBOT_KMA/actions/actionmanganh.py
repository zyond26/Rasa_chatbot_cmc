from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
from sqlite3 import Error

class ActionRecommend(Action):

    def name(self) -> Text:
        return "action_Manganh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = DbQueryingMethods.create_connection(db_file="diem2021.db")
        print("Connected to the database.")
        if conn is None:
            print("Failed to connect to the database.")
        values = tracker.get_slot("major").upper()
        major = "Nganh"

        get_query_results = DbQueryingMethods.get_info_vaccine(conn=conn,major=major,value=values)
        return_text = DbQueryingMethods.rows_info_as_text(get_query_results)
        dispatcher.utter_message(text=str(return_text))
        print(f"Truy vấn: Nganh = {values}")

        return

class DbQueryingMethods:

    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def get_info_vaccine(conn,major,value):
        c = conn.cursor()
        c.execute(f'''select * from diem2021
                  where {major}="{value}"''')
        records = c.fetchall()
        print(f"Kết quả truy vấn: {records}")
        return records

    def rows_info_as_text(records):
        if len(list(records)) < 1:
            return f"Không có thông tin mã ngành về ngành này. Bạn có nhập sai gì không? Hãy nhập lại"
        else:
            for result in records:
                print(result)
                Nganh = result[1]
                Ma = result[0]
                return f" {(result[0])} là mã ngành của ngành {result[1]} ."