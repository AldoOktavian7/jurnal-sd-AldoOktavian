import os
import time

user_name = os.getenv('APP_USER', 'Guest')
app_env = os.getenv('APP_ENV', 'development')

if __name__ == "__main__":
    print(f"Halo {user_name}! Aplikasi ini berjalan di dalam kontainer Docker.")
    print(f"Environment saat ini: {app_env}")
    
    print("Kontainer standby. Menunggu perintah...")
    # Loop ini menjaga agar kontainer tetap hidup terus di latar belakang
    while True:
        time.sleep(3600)