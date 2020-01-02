import os.path
from time import sleep
from datetime import datetime

class Telegram_bot:

#variaveis
	def __init__(self,bot,chat_id,channel_id,lista_chaves,lista_data,arquivo_tmp,noticias):
		self.bot = bot
		self.chat_id = chat_id
		self.channel_id = channel_id
		self.lista_chaves = lista_chaves
		self.lista_data = lista_data
		self.arquivo_tmp = arquivo_tmp
		self.noticias = noticias
		
	def criaChaves(self,noticias,lista_chaves):
		for i in range(len(noticias)):
			chave = list(noticias[i].keys())[0]
			lista_chaves.append(chave)
		
	def converteDateTime(self,noticias,lista_data):
		for i in range(len(noticias)):
			data_hora = list(noticias[i].keys())[0]
			data_hora = datetime.strptime(data_hora, '%d/%m/%y  %Hh%M')
			lista_data.append(data_hora)
	
	#formata a notícia para se tornar uma mensagem
	'''noticia = (noticias[i][lista_chaves[i]])
	mensagem ="_{0}_ \n*{1}* \n\n{2}\n\n [.]({3}).\n {4}\n".format(lista_chaves[i],noticia[0],noticia[1],noticia[2],noticia[3])'''

	#se o arquivo existe envia noticias novas e atualiza o arquivo
	def enviaMensagem(self, arquivo_tmp,noticias,lista_chaves,bot,chat_id,lista_data,channel_id):
		if (os.path.exists(arquivo_tmp)):

			arquivo_tmp = open(arquivo_tmp,'r')
			ultima_data = datetime.strptime(arquivo_tmp.read(), '%d/%m/%y  %Hh%M')
			arquivo_tmp.close()

			for i in range(len(noticias)-1, -1, -1):
				print(i)
				
				noticia = (noticias[i][lista_chaves[i]])
				mensagem ="_{0}_ \n*{1}* \n\n{2}\n\n [.]({3}).\n {4}\n".format(lista_chaves[i],noticia[0],noticia[1],noticia[2],noticia[3])
				data_hora = lista_data[i]

				if data_hora > ultima_data:
					bot.sendMessage(chat_id, 
													mensagem,
													parse_mode = "markdown")
					bot.sendMessage(channel_id, 
													mensagem, 
													parse_mode = "markdown")			
				sleep(1)
		#se o arquivo não existe, ele envia as noticias no canal e cria o arquivo com a data da ultima noticia enviada
		else:	
			for i in range(len(noticias)-1, -1, -1):	
				noticia = (noticias[i][lista_chaves[i]])
				mensagem ="_{0}_ \n*{1}* \n\n{2}\n\n [.]({3}).\n {4}\n".format(lista_chaves[i],noticia[0],noticia[1],noticia[2],noticia[3])
				
				bot.sendMessage(chat_id, 
												mensagem,
												parse_mode = "markdown")
				bot.sendMessage(channel_id, 
												mensagem, 
												parse_mode = "markdown")
			sleep(1)
			
		file_tmp = open(arquivo_tmp,'w')
		file_tmp.write(list(noticias[i].keys())[0])
		file_tmp.close()

