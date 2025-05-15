import time
import RPi.GPIO as GPIO

# Gaz sensörü GPIO bağlantısı
GAS_SENSOR_PIN = 17  # MQ-135'in bağlı olduğu GPIO pini

# GPIO yapılandırması
GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_SENSOR_PIN, GPIO.IN)

# Gaz sensöründen veri alma fonksiyonu
def read_gas_level():
    gas_value = GPIO.input(GAS_SENSOR_PIN)
    return gas_value  # 1: Gaz algılandı, 0: Gaz algılanmadı

# Gaz durumunu ekrana yazdıran fonksiyon
def display_gas_data():
    gas_status = read_gas_level()
    print(f"Gaz Durumu: {'Algılanmadı' if gas_status else 'Algındı'}")

# Ana döngü
try:
    print("MQ-135 Gaz Sensörü İzleme Başlatıldı...")
    while True:
        display_gas_data()  # Gaz durumunu ekrana yazdır
        time.sleep(2)  # Her 2 saniyede bir sensör durumu kontrol edilir
except KeyboardInterrupt:
    print("Program sonlandırıldı.")
    GPIO.cleanup()

