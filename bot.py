
import asyncio
import datetime
import telegram
import pytz

# استبدال "TOKEN" بتوكن البوت الخاص بك
bot = telegram.Bot(token="7122754136:AAE-8mr83R7_O8w0R5bJIxEsYIKE3VlD1FU")

# استبدال "CHANNEL_ID" بمعرف القناة الذي تريد تحديث وصفها
channel_id = "@UU_Le2"

# إضافة النص الثابت هنا
description = """• كل مايخص المجال موجود هنا 
شروحات لبرامج ارقام وهميه
جميع حلول الواتساب
وثغرات فك وحول لجميع منصات التواصل الاجتماعي"""

async def update_channel_description():
    while True:
        try:
            # الحصول على التاريخ والوقت الحالي بتوقيت مصر
            tz = pytz.timezone( Asia/Yemen )
            now = datetime.datetime.now(tz)
            current_date = now.strftime("%d/%m/%Y")
            current_time = now.strftime("%H:%M:%S")

            # تحديث وصف القناة بالتاريخ والوقت الحالي والنص الثابت
            description_with_time = f"{description}\n\n🗓| التاريخ :  {current_date}\n⏱| الوقت : {current_time}"
            await bot.setChatDescription(chat_id=channel_id, description=description_with_time)

        except telegram.TelegramError as e:
            print(f"An error occurred: {e}")

        # انتظر لمدة 60 ثانية قبل تحديث وصف القناة مرة أخرى
        await asyncio.sleep(60)

# تشغيل الدالة الزمنية بشكل دائم باستخدام asyncio
if __name__ ==  __main__ :
    loop = asyncio.get_event_loop()
    loop.create_task(update_channel_description())
    loop.run_forever()
