import multiprocessing
import subprocess

# Betik dosyalarını tanımlayın
scripts = [ "servo_ultrasonic.py", "Gazsensor.py", "Sicaklik.py", "IR_Servo.py"]

# Her bir betiği çalıştıracak bir fonksiyon
def run_script(script_name):
    try:
        subprocess.run(["python3", script_name])
    except Exception as e:
        print(f"Betik çalıştırılamadı: {script_name}, Hata: {e}")

# Çoklu iş parçacığı başlatıcı
if __name__ == "__main__":
    processes = []
    for script in scripts:
        p = multiprocessing.Process(target=run_script, args=(script,))
        processes.append(p)
        p.start()

    # Tüm işlemlerin bitmesini bekle
    for p in processes:
        p.join()
