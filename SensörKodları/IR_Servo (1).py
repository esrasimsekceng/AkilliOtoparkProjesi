import RPi.GPIO as GPIO
import time

# Pin Tanımları
SERVO_PIN = 27
IR_SENSOR_PIN = 4

# GPIO Ayarları
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

# Servo Motor PWM
servo = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz frekans
servo.start(0)  # İlk pozisyon

# Kapı Durum Kontrolü
gate_open = False

# Araç Algılama Süresi
DETECTION_TIME = 0.5 # Algılama için gereken süre (saniye)

def open_gate():
    global gate_open
    if not gate_open:
        print("Kapı açılıyor...")
        servo.ChangeDutyCycle(7)  # Servo motoru 90 dereceye hareket ettir
        gate_open = True
        time.sleep(5)  # Kapı açık kalma süresi
        close_gate()

def close_gate():
    global gate_open
    print("Kapı kapanıyor...")
    servo.ChangeDutyCycle(2.5)  # Servo motoru kapalı pozisyona getir
    gate_open = False
    time.sleep(1)

try:
    while True:
        if GPIO.input(IR_SENSOR_PIN) == GPIO.LOW:  # Araç algılandığında LOW olabilir
            start_time = time.time()
            print("Algılama başladı...")
            while GPIO.input(IR_SENSOR_PIN) == GPIO.LOW:
                if time.time() - start_time >= DETECTION_TIME:
                    print("Araç tespit edildi.")
                    open_gate()
                    break
                time.sleep(1)  # Algılama döngüsüne kısa bir gecikme
        else:
            print("Araç algılanmadı.")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program durduruldu.")

finally:
    if 'servo' in locals():
        servo.stop()
    GPIO.cleanup()
