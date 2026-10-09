BUỔI THỰC HÀNH 1: LẬP TRÌNH PYTHON VỚI MQTT

**1. MÔI TRƯỜNG**

- Python 3.x
- Thư viện paho-mqtt phiên bản 2.0 trở lên

Cài đặt thư viện:

```bash
python -m pip install "paho-mqtt>=2.0"
```

**2. MQTT BROKER**

Bài 1:
- Broker: broker.emqx.io
- Port: 1883
- Topic: iot/lab/message

Bài 2:
- Broker: test.mosquitto.org
- Port: 1883
- Topic: iot/lab/sensor/data

Bài 3:
- Broker: test.mosquitto.org
- Port: 1883
- Command Topic: iot/lab/light01/cmd
- Status Topic: iot/lab/light01/status

**3. CÁCH CHẠY CHƯƠNG TRÌNH**

**BÀI 1: GỬI VÀ NHẬN THÔNG ĐIỆP MQTT**

Terminal 1:
```bash
python subscriber_bai1.py
```

Terminal 2:
```bash
python publisher_bai1.py
```

Kết quả: Publisher gửi thông điệp chứa họ tên, mã sinh viên và nội dung chào mừng mỗi 2 giây. Subscriber hiển thị topic, payload và thời gian nhận.

Dừng chương trình: Nhấn `Ctrl + C` tại Terminal của Publisher hoặc Subscriber để dừng chương trình tương ứng.

**BÀI 2: MÔ PHỎNG CẢM BIẾN NHIỆT ĐỘ VÀ ĐỘ ẨM**

Terminal 1:
```bash
python monitor_subscriber_bai2.py
```

Terminal 2:
```bash
python sensor_publisher_bai2.py
```

Kết quả: Publisher mô phỏng hai cảm biến `sensor01` và `sensor02`, gửi dữ liệu JSON mỗi 3 giây. Subscriber hiển thị nhiệt độ, độ ẩm và cảnh báo khi nhiệt độ lớn hơn 35°C hoặc độ ẩm nhỏ hơn 40%.

Dừng chương trình: Nhấn `Ctrl + C` tại Terminal của Sensor Publisher để dừng gửi dữ liệu. Monitor Subscriber vẫn tiếp tục chờ dữ liệu mới. Nhấn `Ctrl + C` tại Terminal của Monitor để dừng chương trình giám sát.

**BÀI 3: ĐIỀU KHIỂN ĐÈN THÔNG MINH**

Terminal 1:
```bash
python device_bai3.py
```

Terminal 2:
```bash
python controller_bai3.py
```

Nhập lệnh trong Controller:
- `ON`: Bật đèn.
- `OFF`: Tắt đèn.
- `EXIT`: Thoát Controller.

Kết quả: Device nhận lệnh điều khiển, cập nhật trạng thái đèn và gửi phản hồi dưới dạng JSON về Controller.

Dừng chương trình: Nhập `EXIT` để thoát Controller. Nhấn `Ctrl + C` tại Terminal của Device để dừng thiết bị.

**4. KẾT LUẬN**

Hoàn thành ba bài thực hành:
- Gửi và nhận thông điệp qua giao thức MQTT.
- Mô phỏng cảm biến nhiệt độ, độ ẩm và cảnh báo theo ngưỡng.
- Điều khiển đèn thông minh và nhận phản hồi trạng thái.