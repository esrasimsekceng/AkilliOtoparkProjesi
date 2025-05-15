# 🚗 Akıllı Otopark Sistemi (Raspberry Pi Tabanlı)

Bu proje, Raspberry Pi kullanılarak geliştirilen **akıllı otopark sistemi**dir. Projede çeşitli sensörler ve servo motor ile bir aracın algılanması, park alanı kontrolü, gaz/sıcaklık izleme gibi işlemler gerçekleştirilir.

## 🔧 Kullanılan Donanımlar

- Raspberry Pi 4 (veya uyumlu başka bir model)
- MQ-135 Gaz Sensörü
- DHT11 Sıcaklık ve Nem Sensörü
- Ultrasonik Mesafe Sensörü (HC-SR04)
- IR Sensör
- SG90 Servo Motor
- Breadboard, jumper kablolar

##  Proje Dosyaları

| Dosya Adı             | Açıklama |
|------------------------|---------|
| `Gazsensor.py`         | MQ-135 gaz sensöründen veri okuyarak gaz algılama yapar. |
| `Sicaklik.py`          | DHT11 sensörü ile ortam sıcaklık ve nem bilgisini gösterir. |
| `IR_Servo.py`          | IR sensör ile araç algılandığında servo motor ile kapıyı açar. |
| `servo_ultrasonic.py`  | Ultrasonik sensörle mesafe ölçer ve belirli mesafede kapıyı kontrol eder. |
| `multi_run.py`         | Tüm yukarıdaki betikleri aynı anda çalıştırmak için kullanılır. |

##  Kurulum

1. Raspberry Pi'nize aşağıdaki kütüphaneleri kurun:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install Adafruit_DHT
###  Proje Amacı
Bu proje ile araçların otoparkta tespiti, otomatik kapı açılması, ortamın güvenliğinin artırılması (gaz algılama) ve ortam verilerinin izlenmesi sağlanmıştır. Gerçek dünya uygulamalarına yönelik IoT temelli bir örnek teşkil etmektedir.

#### Notlar
Servo motorlar için yeterli güç sağlandığından emin olun.

GPIO pinleri projenin başında tanımlandığı şekilde bağlandığında sistem sorunsuz çalışır.

Sensörler tozdan ve doğrudan güneş ışığından uzak olmalıdır.