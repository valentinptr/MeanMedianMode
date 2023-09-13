def moyenne(list_input):
    somme = 0
    for numb in list_input:
        somme = somme + numb
    return round(somme / len(list_input), 3)


def meadian(list_input):
    list_input.sort()
    if (len(list_input) % 2) == 0:
        return (list_input[int((len(list_input)) / 2) - 1] + list_input[int((len(list_input)) / 2)]) / 2
    else:
        return list_input[int((len(list_input)) / 2)]


def mode(list_input):
    unique = list(set(list_input))
    cnt = []
    for i in range(0, len(unique)):
        cnt.append(list_input.count(unique[i]))
    return unique[cnt.index(max(cnt))]
