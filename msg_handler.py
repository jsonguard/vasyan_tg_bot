@bot.message_handler(content_types=['text'])
def send_echo(message):
	
	#mesg = message.text
	mesg = message.text.lower()  # чтобы не проверять несколько вариантов, давай проверять строку в lowercase
	
	#count_users = bot.get_chat_members_count(message.chat.id)
	
	#if ((mesg.find("ы") != -1)):
	#	bot.send_message(message.chat.id, count_users)
	
	# пусть все полежат тут пока, а так надо найти функцию в API, которая будет возвращать список участников чата
	users_list = ["@Акакий", "@OneFake", "@michele_giardino", "@rarity_meow", "@json_guard",
				"@vikabubley", "@ManifoldP", "@supermishkin3000", "@dura40k", "@postpashka"]
	top_phrases = ["Дрисня какая-то выпала. Не скажу.", "СУАА", "Один хуй жопа"]

	who_search_result = mesg.find("кто сегодня")  # вернёт нам индекс строки, с которого начинается нужная нам подстрока
	who_length = len("кто сегодня")

	if who_search_result != -1:
		z = random.randint(0, len(users_list)-1)  # проверим, кто счастливчиком стал

		# mesg[z:z+who_length] - тут берём подстроку от z+who_length-ого элемента включительно и до конца строки
		bot.send_message(message.chat.id, users_list[z]+' сегодня '+mesg[z+who_length:])

	"""if (mesg.find("кто сегодня") != -1) or (mesg.find("Кто сегодня") != -1):
		z=random.randint(1,10)
		if z==1:
			bot.send_message(message.chat.id, "@Акакий"+mesg[3:])
		elif z==2:
			bot.send_message(message.chat.id, "@OneFake"+mesg[3:])
		elif z==3:	
			bot.send_message(message.chat.id, "@michele_giardino"+mesg[3:])
		elif z==4:
			bot.send_message(message.chat.id, "@rarity_meow"+mesg[3:])
		elif z==5:	
			bot.send_message(message.chat.id, "@json_guard"+mesg[3:])
		elif z==6:
			bot.send_message(message.chat.id, "@vikabubley"+mesg[3:])
		elif z==7:	
			bot.send_message(message.chat.id, "@ManifoldP"+mesg[3:])
		elif z==8:
			bot.send_message(message.chat.id, "@supermishkin3000"+mesg[3:])
		elif z==9:	
			bot.send_message(message.chat.id, "@dura40k"+mesg[3:])
		elif z==10:
			bot.send_message(message.chat.id, "@postpashka"+mesg[3:])"""


		#bot.send_message(message.chat.id, "Ты"+mesg[3:])

	elif mesg.find("какой васян") != -1:
		bot.send_message(message.chat.id, "С претензией :)")
	
	elif mesg.find("васян") == 0:  # проверим, начинается ли сообщения с васяна; если да, то считаем, что к нему обратились
		bot.send_message(message.chat.id, "Чё нада?")
	
	elif ((mesg.find("топ фраза") != -1) or (mesg.find("топ фразу") != -1)):
		i = random.randint(0, len(top_phrases)-1)

		bot.send_message(message.chat.id, top_phrases[i])
		"""if i==0:
			bot.send_message(message.chat.id, "Хуйня какая-то выпала. Не скажу.")
		elif i==1:
			bot.send_message(message.chat.id, "СУАА")
		elif i==2:	
			bot.send_message(message.chat.id, "Один хуй жопа")"""


bot.polling( none_stop = True)
