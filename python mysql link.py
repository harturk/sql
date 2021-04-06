"""
This code was one of the first i've made it. I spent some of time learning about SQL in order to do it, so is
a dirty code. Havent worked on it anymore. But i'll leave it there to guide if anyone is starting too.
"""
import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='teste1',
    )
print("Conectado")

mycursor1_2 = banco.cursor(buffered=True)
mycursor1_2.execute("SELECT pergunta_texto from perguntas")
pgt = mycursor1_2.fetchall()
mycursor2_1 = banco.cursor(buffered=True)
mycursor2_1.execute("SELECT alternativas_texto from alternativas")
alt_txt = mycursor2_1.fetchall()
mycursor2_2 = banco.cursor(buffered=True)
mycursor2_2.execute("SELECT alternativas_id from alternativas")
alt_id = mycursor2_2.fetchall()
mycursor3_1 = banco.cursor(buffered=True)
mycursor3_1.execute("SELECT * from respostas")
choice = mycursor3_1.fetchone()
res = 0
val = []
mycursor = banco.cursor(buffered=True)
mycursor.execute("SELECT * from respostas")
sql = "INSERT INTO respostas(pgt_ID,escolha) VALUES(%s,%s)"
mycursor.execute("TRUNCATE TABLE respostas")
banco.commit()
for i in range(len(pgt)):
    if i == 0:
        print(pgt[i])
        for j in range(i*4, i*4+4):
            print(f"Digite {alt_id[j]} para {alt_txt[j]}")
        while res not in (1, 2, 3, 4):
            res = int(input(f"Digite um valor válido entre {i * 4 + 1} e {i * 4 + 4}: >>> "))
        val.append(i)
        val.append(res)
        print(val)
        mycursor.execute(sql, val)
    if i == 1:
        val.clear()
        print(pgt[i])
        for j in range(i*4, i*4+4):
            print(f"Digite {alt_id[j]} para {alt_txt[j]}")
        while res not in (5,6,7,8):
            res = int(input(f"Digite um valor válido entre {i * 4 + 1} e {i * 4 + 4}: >>> "))
        val.append(i)
        val.append(res)
        print(val)
        mycursor.execute(sql, val)
    if i == 2:
        val.clear()
        print(pgt[i])
        for j in range(i*4, i*4+4):
            print(f"Digite {alt_id[j]} para {alt_txt[j]}")
        while res not in (9,10,11,12):
            res = int(input(f"Digite um valor válido entre {i * 4 + 1} e {i * 4 + 4}: >>> "))
        val.append(i)
        val.append(res)
        print(val)
        mycursor.execute(sql, val)
    if i == 3:
        val.clear()
        print(pgt[i])
        for j in range(i*4, i*4+4):
            print(f"Digite {alt_id[j]} para {alt_txt[j]}")
        while res not in (13,14,15,16):
            res = int(input(f"Digite um valor válido entre {i * 4 + 1} e {i * 4 + 4}: >>> "))
        val.append(i)
        val.append(res)
        print(val)
        mycursor.execute(sql, val)
