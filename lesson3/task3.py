# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.


def thesaurus(*args):
    empl_vocabl = {}
    for names in args:
        empl_vocabl.setdefault(names[0], [])
        empl_vocabl[names[0]].append(names)
    return empl_vocabl


vocabl = thesaurus("Иван", "Мария", "Петр", "Илья")
for i in vocabl:
    print(i, vocabl[i])
