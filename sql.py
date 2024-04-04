import psycopg2
conn = psycopg2.connect(
    dbname="trabalho-banco",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute('select *from tempos;')
soma = 0
cont = 0
linhas = cur.fetchall()
for linha in linhas:
    for valor in linha:
        cont += 1
        soma += valor
print(soma)
print(cont)
print(soma/cont)
cur.close()