perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", 
                "Devia para a vítima?", "Já trabalhou com a vítima?"]
sim = 0

print('Responda as seguintes perguntas(use apenas "sim" ou "não" como resposta):')
for pergunta in perguntas:
    resp = input(pergunta)
    if resp.lower() == "sim":
        sim += 1

if sim == 2:
    print("Essa pessoa é suspeita")
elif sim == 3 or sim == 4:
    print("Essa pessoa é cúmplice")
elif sim == 5:
    print("Essa pessoa é o assassino")
else:
    print("Essa pessoa é inocente")