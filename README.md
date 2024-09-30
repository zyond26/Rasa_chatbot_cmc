## Chatbot hỗ trợ tuyển sinh đại học cmc

## Mở đầu

- Trong phần này tôi sẽ mô tả từng bước cài đặt môi trường cho mã nguồn mở Rasa.

## Những phần cần phải cài đặt

```
python
pycharm
rasa
underthesea
ngrok
django
....
```

## Cài đặt thiết lập

1. Cài đặt `python` phiên bản >= 3.7 (https://www.python.org/downloads/release/python-370/)
2. Cài đặt `pycharm` (https://www.jetbrains.com/pycharm/download/#section=windows)
3. Cài đặt `rasa` bằng `pip install rasa` trong Terminal
4. Khởi tạo `rasa` bằng `rasa init` trong Terminal
5. Cài đặt `underthesea` bằng `pip install underthesea` trong Terminal
6. Cài đặt `django` bằng `pip install django` trong Terminal
7. Cài đặt `ngrok` (https://ngrok.com/download)

## Cách chạy project này

1. bạn hãy git clone git này về : " https://github.com/zyond26/AI_project.git "
2. `pip install -r requirements.txt`
3. `rasa run actions`
4. `rasa shell`

## Chạy chương trình trên web

- chạy `rasa run -enable-api --cors "*"` trong Terminal
- sau đó mở file main.html và test chatbot
