from datetime import date


def validar_datanasc(data):
    try:
        data = data.strip().split('/')
        data = [int(c) for c in data]
    except:
        return False

    if len(data) == 3:
        if 0 < data[0] <= 31 and 0 < data[1] <= 12 and (date.today().year - 120) < data[2] <= date.today().year:
            if data[0] > 29 and data[1] == 2:
                return False
            elif data[0] == 31 and data[1] in [4, 6, 9, 11]:
                return False
            else:
                return True
        else:
            return False
    else:
        return False


def formatar_data(data):
    data = data.split('/')
    data = [int(c) for c in data]
    data = date(day=data[0], month=data[1], year=data[2])
    return data


def calcular_idade(datanasc):
    if isinstance(datanasc, str):
        datanasc = formatar_data(datanasc)

    idade_apos_aniversario = date.today().year - datanasc.year

    if datanasc.month > date.today().month:
        return idade_apos_aniversario - 1
    elif datanasc.month == date.today().month:
        if datanasc.day > date.today().day:
            return idade_apos_aniversario - 1
        else:
            return idade_apos_aniversario
    else:
        return idade_apos_aniversario
