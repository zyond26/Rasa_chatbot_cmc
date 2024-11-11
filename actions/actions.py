from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

DATABASE =[" chào hỏi ",
            "tạm biệt",   
            "thông tin trường",
            "chương trình đào tạo",
            "tuyển sinh",
            "xét tuyển điểm thi thpt",
            "xét tuyển học bạ",
            "học phí",
            "học bổng",
            "Duy trì học bổng",
            "thông tin liên hệ",
            "cơ sở vật chất",
            "cảm ơn",
            "hỏi bot",
            "thời gian nhập học",
            "giảng viên",
            "số lượng sinh viên",
            "tên trường",
            "điểm chuẩn",
            "điểm chuẩn năm 2022",
            "điểm chuẩn năm 2023",
            "điểm chuẩn năm 2024",
            "cơ hội việc làm",
            "đối tác",
            "chuyên ngành công nghệ",
            "ngành công nghệ thông tin",          
            "ngành khoa học máy tính",
            "ngành điện tử viễn thông ",
            "việc làm ngành công nghệ thông tin",
            "việc làm ngành khoa học máy tính",
            "việc làm ngành điện tử viễn thông",
            "ngành thiết kế đồ họa",
            "ngành quản trị kinh doanh",
            "ngành ngôn ngữ",
            "ngành ngôn ngữ hàn",
            "ngành ngôn ngữ nhật",
            "thư viện",
            "phòng học",
            " phòng lab",
            "câu lạc bộ",
            "clb lập trình",
            "clb bóng đá",
            "clb bóng chuyền",
            "clb bóng rổ",
            "clb cầu lông",
            "clb tiếng anh",
            "clb tiếng hàn",
            "clb tiếng nhật",
            "clb nhảy",
            "quà nhập học",
            "điểm rèn luyện", 
            "ký túc xá",
            "hỗ trợ học tập",
            "học lại",
            "câu hỏi thường gặp",
            "nội quy",
            ]
            

class ActionRecommend(Action):
    def name(self) -> Text:
        return "action_recommend"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        suggest = []

        for i in range(2):
            suggest_number = random.randrange(len(DATABASE))
            suggest.append(DATABASE[suggest_number])

        dispatcher.utter_message(
            text="Tôi nghĩ bạn nên hỏi về chủ đề '{}' hoặc bên cạnh có cũng có thể là chủ đề '{}'".format(suggest[0],suggest[1])
        )

        return []

