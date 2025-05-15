from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
import requests

user_questions = {}

class ActionCheckQuestions(Action):
    def name(self):
        return "action_check_questions"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        user_questions[user_id] = user_questions.get(user_id, 0) + 1
        if user_questions[user_id] >= 2:
            dispatcher.utter_message("می‌تونید با همراه‌ساز همکاری کنید و ۴۰٪ سود از معاملات دریافت کنید. علاقه‌مندید؟")
        return []

class ActionAskUserInfo(Action):
    def name(self):
        return "action_ask_user_info"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("لطفاً نام کامل و شماره تماس خود را وارد کنید:")
        return []

class ActionStoreUserInfo(Action):
    def name(self):
        return "action_store_user_info"

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        requests.post("https://api.telegram.org/botYOUR_BOT_TOKEN/sendMessage", data={
            "chat_id": "@poshtibanihamrahsaz",
            "text": f"اطلاعات نماینده جدید:
{message}"
        })
        dispatcher.utter_message("ثبت شد! حالا مشخصات اولین مشتری خود را وارد کنید:")
        return []

class ActionGenerateReferralCode(Action):
    def name(self):
        return "action_generate_referral_code"

    def run(self, dispatcher, tracker, domain):
        text = tracker.latest_message.get('text')
        # نمونه ساده برای ساخت کد ارجاع
        date = datetime.now().strftime("%y%m%d")
        ref_code = f"REF{date}-R1"
        requests.post("https://api.telegram.org/botYOUR_BOT_TOKEN/sendMessage", data={
            "chat_id": "@poshtibanihamrahsaz",
            "text": f"مشتری جدید معرفی شده:
{text}
کد ارجاع: {ref_code}"
        })
        dispatcher.utter_message(f"مشتری شما ثبت شد. کد ارجاع شما: {ref_code}")
        return []