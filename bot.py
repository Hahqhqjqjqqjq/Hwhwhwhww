import telebot,requests
bot=telebot.TeleBot(input('6616243382:AAGjw0a4I_2W4VTm8CXY4nrGnsB2td0_5o0'))
if bot:
	print('The bot has been successfully launched ✅\n Go to your bot and send /start')
	
else:
	exit('Bot Token Undefined ⚠️')
	
@bot.message_handler(commands=['start'])
def start_message(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.add(
       telebot.types.InlineKeyboardButton(
           'Bot Channel Updates', url='t.me/Pythonln'
       )
   )
	user=message.from_user.username
	nam=message.chat.first_name
	bot.send_message(message.chat.id,f'''<strong>
	- ارسل فكرتك لتحويلها الى اداة في بايثون.\n\n Dev -> @Lx0b2 ~ @Pythonln
 </strong>''',
       reply_markup=keyboard,
       parse_mode='html', disable_web_page_preview=True
 )
@bot.message_handler(func=lambda m: True)
def getCo(message):
	tool = message.text+' مع شرح باللغة العربية'
	bot.reply_to(message,f'''<strong>
جاري توليد فكرتك انتظر ....
 </strong>''',
       parse_mode='html', disable_web_page_preview=True
 )
	cookies = {
    'sessionId': '4794c6b0-add6-4469-b055-2921d02cbff1',
    'intercom-id-jlmqxicb': '988acce4-65cf-4502-ac64-65c0e1688ae3',
    'intercom-session-jlmqxicb': '',
    'intercom-device-id-jlmqxicb': 'fc36fc00-2e94-439d-ae4f-52bec50ea617',
}

	headers = {
    'authority': 'www.blackbox.ai',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.blackbox.ai',
    'referer': 'https://www.blackbox.ai/chat/expert-python',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'messages': [
        {
            'id': 'U6TV42y',
            'content': str(tool),
            'role': 'user',
        },
    ],
    'previewToken': None,
    'userId': '00c5d7ab-08d1-4bf3-b334-e2708c68bc0b',
    'codeModelMode': True,
    'agentMode': {},
    'trendingAgentMode': {
        'mode': True,
        'id': 'python',
    },
    'isMicMode': False,
    'userSystemPrompt': None,
    'maxTokens': None,
    'webSearchMode': True,
    'promptUrls': None,
    'isChromeExt': False,
    'githubToken': None,
}

	response = requests.post('https://www.blackbox.ai/api/chat', cookies=cookies, headers=headers, json=json_data)
	bot.reply_to(message,f'''<strong>
# تم توليد فكرتك بنجاح ☑
{response.text}
 </strong>''',
       parse_mode='html', disable_web_page_preview=True
 )
bot.infinity_polling()
