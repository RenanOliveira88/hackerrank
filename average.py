if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    soma_nota = 0
    lista_notas = []
    try:
        lista_notas = student_marks[query_name]
    except:
        print('nome informado não consta na lista.')

    for nota in lista_notas:
        soma_nota += nota

    average_score = soma_nota/len(lista_notas)
    print('{:.2f}'.format(average_score))