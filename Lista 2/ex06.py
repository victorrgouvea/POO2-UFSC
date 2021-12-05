medias = []
for i in range(10):
    notas = [float(x) for x in input("Digite as 4 notas do aluno separadas por vírgula:").split(",")]
    media = 0
    for nota in notas:
        media += nota
    medias.append(media/len(notas))

acima_da_media = 0
for media in medias:
    if media >= 7:
        acima_da_media += 1

print("O número de alunos com média maior ou igual a 7.0 é:", acima_da_media)