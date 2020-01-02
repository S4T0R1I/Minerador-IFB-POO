# -*- coding: utf-8 -*-
import json
import os.path
from datetime import datetime
from funcoes import Funcoes as f
class Minerador(f):


	def __init__(self,lista_horario,lista_imagem,lista_titulo,lista_descricao,lista_link,nome_arquivo,nome_arquivo_tmp,lista_noticia,lista_data):
		self.lista_horario = lista_horario
		self.lista_imagem = lista_imagem
		self.lista_titulo = lista_titulo
		self.lista_imagem = lista_imagem
		self.lista_descricao = lista_descricao
		self.lista_link = lista_link
		self.nome_arquivo = nome_arquivo
		self.nome_arquivo_tmp = nome_arquivo_tmp
		self.lista_noticia = lista_noticia
		self.lista_data = lista_data

	def organizaNoticia(self,lista_horario,lista_imagem,lista_titulo,lista_descricao,lista_link,f):
		for i in range(0, len(f.horario)):
			lista_horario.append(f.horario[i].strip())
			lista_imagem.append(f.imagem[i])
			lista_titulo.append(f.titulo[i])
			lista_descricao.append(f.descricao[i])
			lista_link.append(f.link[i])

	def criaDicionario(self,lista_titulo,lista_horario,lista_descricao,lista_imagem,lista_link,lista_noticia):
		for i in range(0, len(lista_titulo)):
			noticia = {
				lista_horario[i] : (lista_titulo[i],
									lista_descricao[i],
									lista_imagem[i],
									lista_link[i])
			}
			self.lista_noticia.append(noticia)
		return lista_noticia



		# Converte todas as datas das notícias resgatadas nessa execução de str para datetime
	def fazDateTime(self,lista_noticia,lista_data):
		for i in range(len(lista_noticia)):
			data_hora = list(self.lista_noticia[i].keys())[0]
			data_hora = datetime.strptime(data_hora, '%d/%m/%y  %Hh%M')
			lista_data.append(data_hora)

	#salva informações coletadas em um arquivo json
	def salvaInfo(self,nome_arquivo,nome_arquivo_tmp,lista_noticia,lista_data):
		if (os.path.exists(nome_arquivo)):
			arquivo_json = open(nome_arquivo, 'r')
			dados_json = json.loads(arquivo_json.read())
			arquivo_json.close()

			arquivo_tmp = open(nome_arquivo_tmp,'r')
			ultima_data = datetime.strptime(arquivo_tmp.read(), '%d/%m/%y  %Hh%M')
			arquivo_tmp.close()
		
			for i in range(len(lista_data)-1, -1, -1):
				data_hora = lista_data[i]
				if data_hora > ultima_data:
					#Salvar essa notícia
					dados_json.insert(0,lista_noticia[i])
			
			dados_json_new = json.dumps(dados_json, ensure_ascii=False, indent = 2)
			arquivo = open(nome_arquivo,'w')
			arquivo.write(dados_json_new)
			arquivo.close()
		else:
			for x in range(len(lista_data)-1, -1, -1):
				i = x
			dados_json = json.dumps(lista_noticia, ensure_ascii=False, indent = 2)
			arquivo = open(nome_arquivo,'w')
			arquivo.write(dados_json)
			arquivo.close()
		arquivo_tmp = open(nome_arquivo_tmp,'w')
		arquivo_tmp.write(list(lista_noticia[i].keys())[0])
		arquivo_tmp.close()