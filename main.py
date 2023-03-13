# constroi as rotas
from flask import Flask
#  json
import json
# from json import JSONEncoder
# conecta com o bd postgresql
import psycopg2

# cria o objeto app do flask
app = Flask(__name__)

# classe de modelo
class Filme(dict):
    def __init__(self, titulo = None, sinopse = None, id = 0):
        self.titulo = titulo
        self.sinopse = sinopse
        self.id = id       
        dict.__init__(self, id=id, titulo=titulo, sinopse=sinopse)    
    
# definicao das rotas
# listar 
@app.route('/')
def index():    
    conn =  psycopg2.connect(dbname="ubots", host="localhost", user="postgres", password="postgres")
    cur = conn.cursor()    
    cur.execute("SELECT * FROM filme")        
    vetFilme = []    
    for f in cur.fetchall():
        filme = Filme(f[1], f[2], f[0])                
        vetFilme.append(filme)      
    cur.close()
    conn.close()
    if(len(vetFilme) > 0):
        return json.dumps(vetFilme, indent=4)
    else:
        return json.dumps({'RESPOSTA': "sem filmes"})   
    
@app.route('/atualizar/<id>/<titulo>/<sinopse>')
def atualizar(id, titulo, sinopse):
    try:
        conn =  psycopg2.connect(dbname="ubots", host="localhost", user="postgres", password="postgres")
        cur = conn.cursor()    
        cur.execute("UPDATE filme SET titulo = %s, sinopse = %s WHERE id = %s;", [titulo, sinopse, int(id)])    
        conn.commit()
        cur.close()
        conn.close()
        return json.dumps({'RESPOSTA': "ok"})
    except:
        return json.dumps({'RESPOSTA': "URL incorreta:atualizar/<id>/<titulo>/<sinopse>"})

@app.route('/criar/<titulo>/<sinopse>')
def criar(titulo, sinopse):
    try:
        conn =  psycopg2.connect(dbname="ubots", host="localhost", user="postgres", password="postgres")
        cur = conn.cursor()    
        cur.execute("insert into filme (titulo, sinopse) values (%s, %s);", [titulo, sinopse])    
        conn.commit()
        cur.close()
        conn.close()        
        return json.dumps({'RESPOSTA': "ok"})
    except:
        return json.dumps({'RESPOSTA': "URL incorreta:criar/<titulo>/<sinopse>"})
       

@app.route('/deletar/<id>')
def deletar(id):
    try:
        conn =  psycopg2.connect(dbname="ubots", host="localhost", user="postgres", password="postgres")
        cur = conn.cursor()    
        cur.execute("BEGIN; DELETE FROM avaliacao WHERE filme_id = %s; DELETE FROM filme WHERE id = %s; COMMIT;", [int(id), int(id)])    
        conn.commit()
        cur.close()
        conn.close()
        return json.dumps({'RESPOSTA': "ok"})
    except:
        return json.dumps({'RESPOSTA': "URL incorreta:deletar/<id>"})
   

@app.route('/avaliar/<id>/<nota>')
def avaliar(id, nota):
    try:
        conn =  psycopg2.connect(dbname="ubots", host="localhost", user="postgres", password="postgres")
        cur = conn.cursor()    
        cur.execute("insert into avaliacao (filme_id, nota) values (%s, %s);", [id, nota])    
        conn.commit()
        cur.close()
        conn.close()
        return json.dumps({'RESPOSTA': "ok"})
    except:
        return json.dumps({'RESPOSTA': "URL incorreta:avaliar/<id>/<nota>"})        

@app.route('/indicar')
def indicar():
    conn =  psycopg2.connect(dbname="ubots", host="localhost", user="postgres", password="postgres")
    cur = conn.cursor()    
    cur.execute("SELECT * FROM filme WHERE id not in (select filme_id from avaliacao) ORDER BY random() limit 1")    
    f = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()    
    if (f is not None):
        filme = Filme(f[1], f[2],f[0])        
        return json.dumps(filme, indent=4)
    return json.dumps({'RESPOSTA': "sem filmes ou todos os filmes cadastrados ja tem uma avaliacao"})

# main
if __name__ == "__main__":
    app.run()