import requests
import time
import random

USERNAME = "chikc"
PASSWORD = "00000000"
BASE_URL = "https://vara.e-sim.org"

def start_bot():
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    print(f"🔄 محاولة تسجيل الدخول لـ {USERNAME}...")

    try:
        # تسجيل الدخول
        login_res = session.post(f"{BASE_URL}/login.html", data={'login': USERNAME, 'password': PASSWORD})
        
        if "logout.html" in login_res.text:
            print("✅ تم تسجيل الدخول!")
            time.sleep(5)
            
            # العمل
            session.post(f"{BASE_URL}/work.html", data={'work': 'Work'})
            print("🛠️ تم ضغط زر العمل")
            
            time.sleep(5)
            
            # التدريب
            session.post(f"{BASE_URL}/train.html", data={'train': 'Train'})
            print("💪 تم ضغط زر التدريب")
        else:
            print("❌ فشل الدخول (تأكد من البيانات)")
    except:
        print("⚠️ حدث خطأ في الاتصال")

if __name__ == "__main__":
    start_bot()
