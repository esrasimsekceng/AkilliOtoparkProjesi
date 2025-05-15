import Adafruit_DHT
import time

# DHT11 Sensörü Tanımı
sensor = Adafruit_DHT.DHT11
pin = 5  # DHT11'in bağlı olduğu GPIO pini

while True:
    # Sensörden sıcaklık ve nem değerlerini oku
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        print(f"Sıcaklık: {temperature:.1f}C  Nem: {humidity:.1f}%")
    else:
        print("Veri okuma başarısız. Sensör bağlantılarını kontrol edin.")
    
    time.sleep(5)  # 5 saniye bekle

