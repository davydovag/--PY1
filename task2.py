def get_count_char(str_):
    new_str = main_str.lower()# TODO посчитать количество каждой буквы в строке в аргументе str_


    sym_dict = {}

    for sym in new_str:
        if  sym.isalpha():
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1


    return sym_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))



def get_abc(dict_):
    total_count = sum(get_count_char(main_str).values())
    abc_dict = {}
    for sym, count in get_count_char(main_str).items():
        count /= total_count
        count *= 100
        abc_dict[sym] = count


    return abc_dict


#print(get_abc(get_count_char(main_str)))ount_char(main_str))