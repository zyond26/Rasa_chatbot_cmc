from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

DATABASE =[" chào hỏi ",
            "tạm biệt",
            " xác nhận ",
            " từ chối ",
            "thông tin trường",
            "chương trình đào tạo",
            "tuyển sinh",
            "học phí",
            "học bổng",
            "chi tiết học bổng",
            "thông tin liên hệ",
            "cơ sở vật chất",
            "cảm ơn",
            "hỏi bot",
            "thời gian nhập học",
            "giảng viên",
            "sinh viên",
            "tên trường",
            "điểm chuẩn",
            "cơ hội việc làm",
            "đối tác",
            "thư viện",
            "chuyên ngành công nghệ",
            "chuyên ngành công nghệ thông tin",
            "chi tiết ngành công nghệ thông tin",
            "chuyên ngành khoa học máy tính",
            "chi tiết khoa học máy tính",
            "chuyên ngành điện tử viễn thông ",
            "chi tiết điện tử viễn thông",
            "chuyên ngành thiết kế đồ họa",
            "chi tiết thiết kế đồ họa",
            "chuyên ngành quản trị kinh doanh",
            "chi tiết quản trị kinh doanh",
            "chuyên ngành ngôn ngữ",
            "chi tiết ngôn ngữ",
            "ngành ngôn ngữ hàn",
            "ngành ngôn ngữ nhật",
            "phòng học",
            "câu lạc bộ",
            "clb bóng đá",
            "clb bóng chuyền",
            "clb bóng rổ",
            "clb cầu lông",
            "clb event",
            "clb english",
            "clb dance",
            "quà nhập học",
            "điểm rèn luyện",
            "đồng phục",
            "ký túc xá",
            "hỗ trợ học tập",
            "thông tin giáo trình",
            "xét học lại",
            "câu hỏi thường gặp",
            "nội quy" ]
            

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

