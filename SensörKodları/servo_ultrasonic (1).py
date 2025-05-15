import RPi.GPIO as GPIO
import time

# Pin Tanımları
TRIG_PIN = 23  # Ultrasonik sensörün TRIG pini
ECHO_PIN = 24  # Ultrasonik sensörün ECHO pini
SERVO_PIN = 18  # Servo motor için pin

# GPIO Ayarları
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Servo Motor PWM
servo = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz frekans
servo.start(0)  # İlk pozisyon

# Kapı Durum Kontrolü
gate_open = False

# Ultrasonik Mesafe Ölçümü
def measure_distance():
    # TRIG sinyalini başlat
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)  # 10 µs TRIG sinyali gönder
    GPIO.output(TRIG_PIN, False)
    
    # ECHO sinyalini bekle
    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        end_time = time.time()
    
    # Zaman farkını mesafeye çevir
    elapsed_time = end_time - start_time
    distance = (elapsed_time * 34300) / 2  # Ses hızını kullanarak mesafeyi hesapla
    return distance

# Kapıyı Açma Fonksiyonu
def open_gate():
    global gate_open
    if not gate_open:  # Kapı zaten açık değilse
        print("Kapı açılıyor...")
        servo.ChangeDutyCycle(7.5)  # Servo motoru 90 dereceye hareket ettir
        gate_open = True
        time.sleep(5)  # Kapı açık kalma süresi
        close_gate()

# Kapıyı Kapatma Fonksiyonu
def close_gate():
    global gate_open
    print("Kapı kapanıyor...")
    servo.ChangeDutyCycle(12.5)  # Servo motoru kapalı pozisyona getir
    gate_open = False
    time.sleep(1)

try:
    while True:
        distance = measure_distance()  # Mesafeyi ölç
        print(f"Ölçülen Mesafe: {distance:.2f} cm")
        
        if distance <= 10:  # 10 cm veya daha yakınsa
            print("Araç tespit edildi. Kapı açılıyor...")
            open_gate()
        else:
            print("Araç algılanmadı.")
        time.sleep(0.5)  # Döngüye kısa bir gecikme ekle

except KeyboardInterrupt:
    print("Program durduruldu.")

finally:
    servo.stop()
    GPIO.cleanup()
