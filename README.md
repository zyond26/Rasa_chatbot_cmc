## Chatbot hỗ trợ tuyển sinh Đại học Khoa học

## Mở đầu
- Trong phần này tôi sẽ mô tả từng bước cài đặt môi trường cho  mã nguồn mở Rasa.

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
3. Cài đặt `rasa` bằng  `pip install rasa` trong Terminal
4. Khởi tạo `rasa` bằng `rasa init` trong Terminal
5. Cài đặt `underthesea` bằng `pip install underthesea` trong Terminal
6. Cài đặt `django` bằng `pip install django` trong Terminal
7. Cài đặt `ngrok` (https://ngrok.com/download)

## Cách chạy project này
- Bạn phải cài đặt `git` trước khi thực hiện các bước bên dưới:
1. `git clone https://github.com/016886611529a/CHATBOT_TUYENSINH_DHKH.git`
2. Di chuyển đến thư mục chatbot `cd chatbot`
3. `pip install -r requirements.txt`
4. `rasa run actions`
5. `rasa shell`


## Kết nối FB 
- Lưu ý: phải tạo app trong facebook deverlopers trước khi kết nối
1. chạy `ngrok http 5005`
2. chạy `rasa run --endpoints endpoints.yml --credentials credentials.yml`
3. Copy https trong ngrok và chỉnh url gọi lại trong facebook deverlopers


## Chạy chương trình trên web
- chạy `rasa run -m model --enable-api --cors "*"` trong Terminal

## Phản hồi
- Mọi ý kiến phản hồi vui lòng liên hệ (`nguyenngoclongpdl13@gmail.com`hoặc `0772061082`)
## Phiên bản
- v1.0.0

## Tác giả

* **Nguyễn Ngọc Long**
* **Trần Nhơn Tiến**
* **Đoàn Thị Hồng Phước** - *Giáo viên hướng dẫn*


