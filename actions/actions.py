from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
from sqlite3 import Error

class ActionRecommend(Action):

    def name(self) -> Text:
        return "action_diemchuan2021"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = DbQueryingMethods.create_connection(db_file="diem2021.db")
        values = tracker.get_slot("major").upper()
        year = int(tracker.get_slot("year"))
        major = "Nganh"

        get_query_results = DbQueryingMethods.get_info_vaccine(conn=conn,major=major,value=values)
        return_text = DbQueryingMethods.rows_info_as_text(get_query_results, year)
        dispatcher.utter_message(text=str(return_text))

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
        return records

    def rows_info_as_text(records, year):
        if len(list(records)) < 1:
            return f"Không có thông tin điểm về ngành này"
        else:
            valid_years = {2021, 2022, 2023, 2024}
            if year in valid_years:
                i_2021 = 3
                year_index = i_2021 + year - 2021
                for result in records:
                    Nganh = result[1]
                    Diem = result[3]
                    return f"Ngành {(result[1])} năm {year} lấy {result[year_index]} điểm."
            else:
                return f"Hiện tại tôi chỉ có điểm từ năm 2021 đến 2024. Xin vui lòng nhập lại"
