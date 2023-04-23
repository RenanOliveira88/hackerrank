# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lista_alunos = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista_alunos += [[score, name]]

    lista_alunos.sort()
    notas = {nota[0] for nota in lista_alunos}
    lista_nota = [nota for nota in notas]

    menor_nota = 0
    if len(lista_nota) > 1:
        menor_nota = lista_nota[1]
    else:
        menor_nota = lista_nota[0]

    lista_final = []
    for aluno in lista_alunos:
        if aluno[0] == menor_nota:
            lista_final += [[aluno[1], aluno[0]]]

    lista_final.sort()
    for aluno in lista_final:
        print(aluno[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
