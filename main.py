''' import minerador_IFB
import Telegram_Bot'''
import telepot
import json
import os.path
from funcoes import Funcoes
from minerador_IFB import Minerador
from telegram_bot import Telegram_bot

#atributo global
arquivo_noticias = 'noticias.json'

#instanciando classe de funcoes
f = Funcoes(url = 'https://www.ifb.edu.br/brasilia/noticiasbrasilia',horario= [],imagem=[],titulo=[],descricao=[],link_noticia=[])

#chamando as funcoes da classe e salvando informações da pagina nos atributos
f.soup = f.pegaPagina(f.url)
f.imagem = f.buscarImagem(f.soup)
f.horario = f.buscarHorario(f.soup)
f.titulo = f.buscarTitulo(f.soup)
f.descricao = f.buscarDescricao(f.soup)
f.link = f.buscarLink(f.soup)

#instancia variaveis do minerador
m = Minerador(lista_horario=[],lista_imagem=[],lista_titulo=[],lista_descricao=[],lista_link=[],nome_arquivo='noticias.json', nome_arquivo_tmp='ultima_noticia_minerador.tmp',lista_noticia=[],lista_data=[])

#executa os métodos do minerador
m.organizaNoticia(m.lista_horario,m.lista_imagem,m.lista_titulo,m.lista_descricao,m.lista_link,f)

m.criaDicionario(m.lista_titulo,m.lista_horario,m.lista_descricao,m.lista_imagem,m.lista_link,m.lista_noticia)

m.fazDateTime(m.lista_noticia,m.lista_data)

m.salvaInfo(m.nome_arquivo,m.nome_arquivo_tmp,m.lista_noticia,m.lista_data)

#instanciando bot
t = Telegram_bot(bot = telepot.Bot("830508513:AAFzKIgoWaKkPoDMig3Fa_tCBFKGIGxQogY")
,chat_id = -348118127,channel_id =-1001202036776,lista_chaves =[],lista_data = [],arquivo_tmp = 'ultima_noticia_bot.tmp',noticias=json.loads(open(arquivo_noticias, 'r').read()))

#executando métodos do bot
t.criaChaves(t.noticias,t.lista_chaves)

t.converteDateTime(t.noticias,t.lista_data)

t.enviaMensagem(t.arquivo_tmp,t.noticias,t.lista_chaves,t.bot,t.chat_id,t.lista_data,t.channel_id)

#apaga o arquivo de noticias.json
os.remove(arquivo_noticias)