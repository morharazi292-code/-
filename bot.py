import requests
import time
from bs4 import BeautifulSoup # سنحتاج هذه المكتبة لقراءة الأزرار

USERNAME = "chikc"
PASSWORD = "00000000"
BASE_URL = "https://vara.e-sim.org"

def start_bot():
    session = requests.Session()
    # إضافة User-Agent لتبدو كمتصفح حقيقي 100%
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })

    print(f"🚀 بدء المهمة للحساب: {USERNAME}")

    # 1. تسجيل الدخول
    login_page = session.get(f"{BASE_URL}/login.html")
    login_data = {'login': USERNAME, 'password': PASSWORD}
    response = session.post(f"{BASE_URL}/login.html", data=login_data)
    
    if "logout.html" in response.text:
        print("✅ تم تسجيل الدخول بنجاح!")
        
        # 2. تنفيذ العمل (Work)
        print("🛠️ جاري محاولة العمل...")
        # نفتح صفحة العمل أولاً لجلب أي رموز حماية
        work_page = session.get(f"{BASE_URL}/work.html")
        # إرسال طلب العمل
        session.post(f"{BASE_URL}/work.html", data={'work': 'Work'})
        
        time.sleep(3) # انتظار بسيط

        # 3. تنفيذ التدريب (Train)
        print("💪 جاري محاولة التدريب...")
        train_page = session.get(f"{BASE_URL}/train.html")
        # إرسال طلب التدريب
        session.post(f"{BASE_URL}/train.html", data={'train': 'Train'})
        
        print("🏁 انتهت المحاولة. تفقد الحساب الآن!")
    else:
        print("❌ فشل تسجيل الدخول. تأكد من البيانات.")

if __name__ == "__main__":
    start_bot()
