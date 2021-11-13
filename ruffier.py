txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''
нет данных для такого возраста'''
txt_res = [] 
txt_res.append('''низкая. 
Срочно обратитесь к врачу!''')
txt_res.append('''удовлетворительная. 
Обратитесь к врачу!''')
txt_res.append('''средняя. 
Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''
выше среднего''')
txt_res.append('''
высокая''')


def ruffier_index(P1, P2, P3):
    index = ((4 * (P1 + P2 + P3)) - 200) / 10
    return index


def neud_level(age):
    norm_age = (min(age, 15) - 7) // 2
    result = 21 - norm_age * 1.5

    return result

    

def ruffier_result(index, level):

    if index >= level:
        return 0

    level -= 4

    if index >= level:
        return 1

    level -= 5

    if index >= level:
        return 2

    level -= 5.5

    if index >= level:

        return 3

    return 4

