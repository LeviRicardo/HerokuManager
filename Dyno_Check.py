import os
import telebot
from time import sleep, ctime
from threading import Thread as th
from dotenv import load_dotenv

#Lê o arquivo contendo as informações sobre os dynos e checa apenas a primeira linha ( que é onde fica armazenada a informação sobre dynos restants), retornando uma lista com o tempo restante dividido em horas e minutos e a porcentagem de tempo restante. 
def check_dynos():
	o = open("Dynos.log", "r")
	dynos = (o.readlines())[0]
	o.close()
	dynos = (dynos.split(" "))[-3:]
	final = []
	for i in dynos:
		final.append(i.strip())
	return(final)

#Usa a cli do Heroku para criar um log com as informações de Dyno
def get_dynos():
	os.system("heroku ps -a ultimatespelltome > Dynos.log")
	os.system(f"echo '\n\n\t{ctime()}' >> Dynos.log")

#
def valuate_dynos(lista_dos_dynos):
	porcentagem = (lista_dos_dynos[-1])[1:-2]
	if int(porcentagem) <=20:#Valor para que o telegram avise que os dynos estão acabando
		return True
	else:
		return False

#Manda a mensagem sobre o tempo de dyno restante
def message_me():
	meu_id = 592950370	#meu id no telegram
	while True:
		get_dynos()
		dynos_left = (check_dynos())
		dynos_time = " ".join(dynos_left)
		if valuate_dynos(dynos_left) == True:
			bot.send_message(meu_id, (f"Você tem {dynos_time} restantes"))
		else:
			pass
		sleep(43200)

#pega o token no .env
load_dotenv()
token = os.getenv("Tele_Token")

#Conecta o bot ao telegram
bot = telebot.TeleBot(token, parse_mode=None)

#inicia a função. Como é uma função pode ser usado com threading no futuro
message_me()
