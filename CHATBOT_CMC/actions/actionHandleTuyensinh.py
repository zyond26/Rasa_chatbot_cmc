from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHandleTuyenSinh(Action):

    def name(self) -> Text:
        return "action_handle_tuyen_sinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Lấy giá trị của slot 'year'
        int_year = int(tracker.get_slot("year"))
        valid_years = {2021, 2022, 2023, 2024}
        # Xử lý logic dựa trên giá trị của 'year'
        if int_year in valid_years:
            if int_year == 2021:
                dispatcher.utter_message(text="Thông tin tuyển sinh cho năm 2021",
                                         image="https://i.imgur.com/P9e43lQ.jpeg")
            elif int_year == 2022:
                dispatcher.utter_message(text="Thông tin tuyển sinh cho năm 2022",
                                         image="https://i.imgur.com/RzdAZNE.jpeg")
            elif int_year == 2023:
                dispatcher.utter_message(text="Thông tin tuyển sinh cho năm 2023",
                                         image="https://i.imgur.com/gMWznIY.png")
            elif int_year == 2024:
                dispatcher.utter_message(text="Thông tin tuyển sinh cho năm 2024",
                                         image="https://i.imgur.com/jMXQwbp.jpeg")
        else:
            dispatcher.utter_message(text="Xin lỗi, tôi chỉ có thông tin từ năm 2021 đến 2024. Vui lòng nhập lại!")

        return []
