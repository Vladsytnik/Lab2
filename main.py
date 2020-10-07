import random


# глобальная переменная-словарь, куда записывается шифр
dic_of_shifr = dict()
globals = 0

# Класс источник данных
class Data_Source:


    def Body(array_of_text):
        elements_sorted = Coder.Count_Of_Symbols(array_of_text)  # функция создания сортированного словаря с частотой букв
        dict_with_probability = Coder.Probability_of_Symbols(array_of_text)        # словарь с вероятностями
        print(f'Буквы и их вероятности до слияние: {dict_with_probability}')

        merge = Coder.Merge_Symbols_And_Probabaility(dict_with_probability) # слияние

        if len(elements_sorted) == 0:   #если ничего не ввели
            print("Вы ничего не ввели :(")
            exit()
        print(f'Буквы и их вероятность после слияния: {elements_sorted}')
        # print(f'Буквы и их вероятность: {elem_with_probability}')
        if len(elements_sorted) > 1:
            if len(elements_sorted) % 2 != 0:  # если нечетное кол-ва символов
               # print('Получилось нечетное кол-во символов в самом начале!')
                Coder.Function_Of_Difference_List_In_Massive_NECHENT(elements_sorted)

                for i in dic_of_shifr.keys():
                    dic_of_shifr[i] = "".join(reversed(dic_of_shifr[i]))

                print(dic_of_shifr)
            else:
                Coder.Function_Of_Difference_List_In_Massive(elements_sorted)  # функция разделения листа на два массива
                for i in dic_of_shifr.keys():
                    dic_of_shifr[i] = "".join(reversed(dic_of_shifr[i]))
                print(dic_of_shifr)
        elif len(elements_sorted) == 1:
            for i in elements_sorted.keys():
                dic_of_shifr[i] = 0
            print(dic_of_shifr)







class Coder:

    # функция создания сортированного словаря с частотой букв   --  работает
    def Count_Of_Symbols(massive):
        dictionary = dict()
        for word in massive:
            for letters in word:
                if letters not in dictionary:
                    dictionary[letters] = 1
                else:
                    dictionary[letters] += 1
        # Сортировка словаря по значению по убыванию!
        elements_sorted = {k: dictionary[k] for k in sorted(dictionary, key=dictionary.get, reverse=True)}
        return (elements_sorted)




    def toFixed(numObj, digits=0):      # функция ограничивающая знаки после запятой
        return f"{numObj:.{digits}f}"



    # функция, создающая словарь из символов и вероятности символа
    def Probability_of_Symbols(massive):
        print(f'кол-во всего символов: {len(massive)}')
        dictionary = dict()
        for word in massive:
            for letters in word:
                if letters not in dictionary:
                    dictionary[letters] = 1
                else:
                    dictionary[letters] += 1

        for values in dictionary:
            dictionary[values] = Coder.toFixed( dictionary[values] / len(dictionary) , 4)

        # Сортировка словаря по значению по убыванию!
        elements_sorted = {k: dictionary[k] for k in sorted(dictionary, key=dictionary.get, reverse=True)}
        return (elements_sorted)
    # Вызов функции



    #TODO: функция, реализующая блочное кодирование, то есть слияние символов и перемножение вероятностей.
    def Merge_Symbols_And_Probabaility(initial_dict):
        new_dict = dict()

        for elem_at_initial_dict in initial_dict:   # идем по элементам(символам) начального словаря.
            for elem2_at_initial_dict in initial_dict:
                temp_var = elem_at_initial_dict + elem2_at_initial_dict
                new_dict[temp_var] = Coder.toFixed(float(initial_dict[elem2_at_initial_dict]) * float(initial_dict[elem_at_initial_dict]) , 4 )

        for i in new_dict:      #преобразуем в строку
            new_dict[i] = float(new_dict[i])
        # отсортируем словарь:
        elements_sorted = {k: new_dict[k] for k in sorted(new_dict, key=new_dict.get, reverse=True)}
        print(f'Словарь для блочного кодирования: {elements_sorted}')
        return new_dict


    # функция разделения словаря на два массива для четного
    def Function_Of_Difference_List_In_Massive(start_list):  # ф-я готова
        mas_of_key = []
        mas_of_values = []
        i = 0
        for key in start_list:  # создаем массив ключей из списка    --  работает
            mas_of_key.append(key)
            ++i
        for values in start_list.values():  # создаем массив значений из списка  --  работает
            mas_of_values.append(values)
        Coder.Function_Of_Cut_Massive(mas_of_key, mas_of_values)

    # функция разделения листа на два массива для НЕЧЕТНОГО кол-ва
    def Function_Of_Difference_List_In_Massive_NECHENT(start_list):  # ф-я готова
        mas_of_key = []
        mas_of_values = []
        i = 0
        for key in start_list:  # создаем массив ключей из списка    --  работает
            mas_of_key.append(key)
            ++i
        for values in start_list.values():  # создаем массив значений из списка  --  работает
            mas_of_values.append(values)
        Coder.Function_Of_Cut_Massive_NECHETN(mas_of_key, mas_of_values)

    # Функция работы с первым уровнем(верхним) дерева для четного кол-ва символов
    def Function_Of_Cut_Massive(mas_of_key, mas_of_values):
        if len(mas_of_values) % 2 == 0:
            # todo dic_of_shifr = dict()   # словарь шифрования
            k = 0
            l = len(mas_of_values)
            # for i in mas_of_values.count():
            while k < len(mas_of_values):
                # print(mas_of_values[l-2:l])
                current_mas = mas_of_values[l - 2:l]  # берем по две буквы
                current_mas_key = mas_of_key[l - 2:l]
                if current_mas[0] >= current_mas[1]:  # если все нормально
                    if current_mas[0] not in dic_of_shifr:
                        dic_of_shifr[current_mas_key[0]] = str(0)
                    else:
                        dic_of_shifr[current_mas_key[0]] += str(0)
                    if current_mas[1] not in dic_of_shifr:
                        dic_of_shifr[current_mas_key[1]] = str(1)
                    else:
                        dic_of_shifr[current_mas_key[1]] += str(1)

                else:
                    if current_mas[0] not in dic_of_shifr:
                        dic_of_shifr[current_mas_key[0]] = str(1)
                    else:
                        dic_of_shifr[current_mas_key[0]] += str(1)
                    if current_mas[1] not in dic_of_shifr:
                        dic_of_shifr[current_mas_key[1]] = str(0)
                    else:
                        dic_of_shifr[current_mas_key[1]] += str(0)
                l -= 2
                k += 2
                # дальше нужно слить буквы и суммировать попарно цифры
            Coder.Down_In_Tree(mas_of_key, mas_of_values, dic_of_shifr)  # идем вниз дереа, сливая буквы и цифры
            # print("dic_of_shifr: ", dic_of_shifr)
        else:
            print('Получилось нечетная длина фразы в функции Function_Of_Cut_Massive')

    # Функция работы с первым уровнем(верхним) дерева для НЕЧЕТНОГО кол-ва символов
    def Function_Of_Cut_Massive_NECHETN(mas_of_key, mas_of_values):
        if len(mas_of_values) % 2 != 0:
            # todo dic_of_shifr = dict()   # словарь шифрования
            k = 0
            l = len(mas_of_values)
            # for i in mas_of_values.count():
            while k < len(mas_of_values):
                if l > 1:
                    # print(mas_of_values[l-2:l])
                    current_mas = mas_of_values[l - 2:l]  # берем по две буквы
                    current_mas_key = mas_of_key[l - 2:l]
                    if current_mas[0] >= current_mas[1]:  # если все нормально
                        if current_mas[0] not in dic_of_shifr:
                            dic_of_shifr[current_mas_key[0]] = str(0)
                        else:
                            dic_of_shifr[current_mas_key[0]] += str(0)
                        if current_mas[1] not in dic_of_shifr:
                            dic_of_shifr[current_mas_key[1]] = str(1)
                        else:
                            dic_of_shifr[current_mas_key[1]] += str(1)

                    else:
                        if current_mas[0] not in dic_of_shifr:
                            dic_of_shifr[current_mas_key[0]] = str(1)
                        else:
                            dic_of_shifr[current_mas_key[0]] += str(1)
                        if current_mas[1] not in dic_of_shifr:
                            dic_of_shifr[current_mas_key[1]] = str(0)
                        else:
                            dic_of_shifr[current_mas_key[1]] += str(0)
                    l -= 2
                    k += 2
                else:
                    current_mas = mas_of_key[0]  # берем первую букву
                    dic_of_shifr[current_mas] = ""
                    break
                # дальше нужно слить буквы и суммировать попарно цифры
            Coder.Down_In_Tree_NECHETN(mas_of_key, mas_of_values, dic_of_shifr)  # идем вниз дереа, сливая буквы и цифры
            # print("dic_of_shifr: ", dic_of_shifr)
        else:
            print('Получилось нечетная длина фразы в функции Function_Of_Cut_Massive')

    # Функция, работающая со всеми строками дерева, кроме первой(сливающая буквы и суммирующая цифры в том числе)
    # для четного кол-ва символов
    def Down_In_Tree(mas_of_key, mas_of_values,
                     dic_of_shifr):  # todo исправить ошибку тут - надо идти через каждые 2 элемента
        # слияние:
        mas_of_key_sl = Coder.Sliyanie_Bukv(mas_of_key)
        mas_of_values_sl = Coder.Sliyanie_Cifr(mas_of_values)
        first_num = 0
        first_key = ''
        if len(mas_of_key_sl) % 2 == 0 or len(mas_of_key_sl) == 1:
            if len(mas_of_values_sl) >= 2:
                for key_elem in range(0, len(mas_of_key_sl), 2):
                    # if first_num != 0:
                    if mas_of_values_sl[key_elem] >= mas_of_values_sl[key_elem + 1]:  # если все нормально
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(0)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(1)
                    else:
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(1)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(0)
                # first_num = mas_of_values_sl[key_elem-1]
                # first_key = mas_of_key_sl[key_elem-1]
                # continue
                #  first_num = mas_of_values_sl[key_elem]
                #  first_key = mas_of_key_sl[key_elem]
                Coder.Down_In_Tree(mas_of_key_sl, mas_of_values_sl, dic_of_shifr)
            # print(dic_of_shifr)
        else:
            #print('Получилось нечетная длина фразы в функции Down_In_Tree')
            Coder.Down_In_Tree_Only_Body_NECHETN(mas_of_key_sl, mas_of_values_sl, dic_of_shifr)

    def Down_In_Tree_Only_Body(mas_of_key_sl, mas_of_values_sl, dic_of_shifr):
        # слияние:
        first_num = 0
        first_key = ''
        if len(mas_of_key_sl) % 2 == 0 or len(mas_of_key_sl) == 1:
            if len(mas_of_values_sl) >= 2:
                for key_elem in range(0, len(mas_of_key_sl), 2):
                    # if first_num != 0:
                    if mas_of_values_sl[key_elem] >= mas_of_values_sl[key_elem + 1]:  # если все нормально
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(0)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(1)
                    else:
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(1)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(0)
                # first_num = mas_of_values_sl[key_elem-1]
                # first_key = mas_of_key_sl[key_elem-1]
                # continue
                #  first_num = mas_of_values_sl[key_elem]
                #  first_key = mas_of_key_sl[key_elem]
                Coder.Down_In_Tree(mas_of_key_sl, mas_of_values_sl, dic_of_shifr)
        # print(dic_of_shifr)
        else:
            #print('Получилось нечетная длина фразы в функции Down_In_Tree')
            Coder.Down_In_Tree_Only_Body_NECHETN()

    def Down_In_Tree_Only_Body_NECHETN(mas_of_key_sl, mas_of_values_sl, dic_of_shifr):
        # слияние:
        first_num = 0
        first_key = ''
        if len(mas_of_key_sl) % 2 == 0 or len(mas_of_key_sl) == 1:  # если четное кол-во
            if len(mas_of_values_sl) >= 2:
                for key_elem in range(0, len(mas_of_key_sl), 2):
                    # if first_num != 0:
                    if mas_of_values_sl[key_elem] >= mas_of_values_sl[key_elem + 1]:  # если все нормально
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(0)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(1)
                    else:
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(1)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(0)
                Coder.Down_In_Tree(mas_of_key_sl, mas_of_values_sl, dic_of_shifr)
        # print(dic_of_shifr)
        else:  # если нечетное все равно кол-во
            h = 0
            #print('Получилось нечетная длина фразы в функции Down_In_Tree')
            if len(mas_of_values_sl) >= 2:  # не надо трогать (для рекурсии)
                for key_elem in range(1, len(mas_of_key_sl), 2):
                    # if first_num != 0:
                    if mas_of_values_sl[key_elem] >= mas_of_values_sl[key_elem + 1]:  # если все нормально
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(0)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(1)
                    else:
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(1)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(0)
                Coder.Down_In_Tree_NECHETN(mas_of_key_sl, mas_of_values_sl, dic_of_shifr)
        #  print(dic_of_shifr)

    # Функция, работающая со всеми строками дерева, кроме первой(сливающая буквы и суммирующая цифры в том числе)
    # для НЕЧЕТНОГО кол-ва символов
    def Down_In_Tree_NECHETN(mas_of_key, mas_of_values, dic_of_shifr):
        # слияние:
        mas_of_key_sl = Coder.Sliyanie_Bukv_NECHETN(mas_of_key)
        mas_of_values_sl = Coder.Sliyanie_Cifr_NECHETN(mas_of_values)
        first_num = 0
        first_key = ''
        if len(mas_of_key_sl) % 2 == 0 or len(mas_of_key_sl) == 1:  # если четное кол-во
            if len(mas_of_values_sl) >= 2:
                for key_elem in range(0, len(mas_of_key_sl), 2):
                    # if first_num != 0:
                    if mas_of_values_sl[key_elem] >= mas_of_values_sl[key_elem + 1]:  # если все нормально
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(0)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(1)
                    else:
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(1)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(0)
                Coder.Down_In_Tree(mas_of_key_sl, mas_of_values_sl, dic_of_shifr)
        #  print(dic_of_shifr)
        else:  # если нечетное все равно кол-во
            h = 0
           # print('Получилось нечетная длина фразы в функции Down_In_Tree')
            if len(mas_of_values_sl) >= 2:  # не надо трогать (для рекурсии)
                for key_elem in range(1, len(mas_of_key_sl), 2):
                    # if first_num != 0:
                    if mas_of_values_sl[key_elem] >= mas_of_values_sl[key_elem + 1]:  # если все нормально
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(0)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(1)
                    else:
                        for temp in mas_of_key_sl[key_elem]:  # иду по буквам элемента
                            dic_of_shifr[temp] += str(1)
                        for temp in mas_of_key_sl[key_elem + 1]:
                            dic_of_shifr[temp] += str(0)
                Coder.Down_In_Tree_NECHETN(mas_of_key_sl, mas_of_values_sl, dic_of_shifr)
        #  print(dic_of_shifr)

    def Sliyanie_Bukv(massive_of_key):
        final_mas = []
        l = len(massive_of_key)
        k = 0
        while k < len(massive_of_key):
            temp_mas_of_connect_2_keys = str(massive_of_key[k]) + str(massive_of_key[k + 1])
            final_mas.append(temp_mas_of_connect_2_keys)
            k += 2
        return final_mas

    def Sliyanie_Bukv_NECHETN(massive_of_key):  # нужно идти с конца и в самом конце инвертировать массив
        final_mas = []
        l = len(massive_of_key)
        k = 0
        while l > 1:
            temp_mas_of_connect_2_keys = str(massive_of_key[l - 2]) + str(massive_of_key[l - 1])  # слияние двух букв
            final_mas.append(temp_mas_of_connect_2_keys)
            l -= 2
        if l == 1:
            final_mas.append(massive_of_key[0])
            final_mas.reverse()
        return final_mas

    def Sliyanie_Cifr(mas_of_values):
        final_mas = []
        l = len(mas_of_values)
        k = 0
        while k < len(mas_of_values):
            temp_mas_of_connect_2_keys = mas_of_values[k] + mas_of_values[k + 1]
            final_mas.append(temp_mas_of_connect_2_keys)
            k += 2
        return final_mas

    def Sliyanie_Cifr_NECHETN(mas_of_values):
        final_mas = []
        l = len(mas_of_values)
        k = 0
        while l > 1:
            temp_mas_of_connect_2_keys = mas_of_values[l - 2] + mas_of_values[l - 1]  # слияние двух цифр
            final_mas.append(temp_mas_of_connect_2_keys)
            l -= 2
        if l == 1:
            final_mas.append(mas_of_values[0])
            final_mas.reverse()
        return final_mas

    #   функция, кодирующая сообщение в двоичные символы
    def Shifrator(array_of_text, dic_of_shifr):
        encoded=""
        for i in range (len(array_of_text)):
            encoded+=dic_of_shifr[array_of_text[i]]
        print(f'Закодированная строка: {encoded}')
        return(encoded)







# Класс отправителя
class Sender:

    def Body(dictionary, encoded):
        Reciever.Body(dictionary, encoded)







# Класс Получателя
class Reciever:
    def Body(dictionary, mas_of_binary_code):
        Decoder.Decode(dictionary, mas_of_binary_code)







# Класс дешифратора
class Decoder:

    def Decode(dictionary, mas_of_binary_code):

        temp=""
        decoded=""
        for i in range(len(mas_of_binary_code)):
            temp+=mas_of_binary_code[i]
            for k in dictionary.keys():
                if temp==dictionary[k]:
                    decoded+=k
                    temp=""
        print(f'Раскодированная строка: {decoded}')
        f = open('/Users/vladsytnik/Desktop/fileRESULT.txt', 'w')
        f.write(decoded)


def Fun(k):
    return k-0.36




# Функция, считаюшие кол-во бит, кол-во единиц и нулей
def Count(mas_of_byte):
    count = 0
    count_of_0 = 0
    count_of_1 = 0
    for i in mas_of_byte:
        count += 1
        if i == '0':
            count_of_0 += 1
        elif i == '1':
            count_of_1 += 1
    print(f'Количество бит: {count}')
    print(f'Количество единиц: {count_of_1}')
    print(f'Количество нулей: {count_of_0}')






# Функция, считающая среднее кол-во двоичных символов на букву
def Average(dic_of_shifr):
    sum = 0
    for dict_element in dic_of_shifr:
        sum += len(dic_of_shifr[dict_element])
    final = sum / len(dic_of_shifr)
    globals = Fun(final)
    print(f'Среднее кол-во двоичных символов на букву: {final}')
    print(f'Среднее кол-во двоичных символов на букву при блочном кодировании: {globals}')
    print(f'Получаем, что при блочном кодировании среднее кол-во двоичных символов на {final-globals} меньше')





def Noise(encoded):
    new_encoded_mas = ''
    #TODO: ошибка
    probability = 5                           # вероятность, меньше которой будет инвертироватья двоичный сивол

    for binary_elem in encoded:
        rand_num = random.randrange(0, 100, 1)  # генерируем случайно число от 0 до 1
        if rand_num < probability:              # если попадается вероятность ошибки
            if binary_elem == '0':
                new_encoded_mas += '1'
            elif binary_elem == '1':
                new_encoded_mas += '0'
        elif rand_num >= probability:             # если НЕ попадается вероятность ошибки
            new_encoded_mas += binary_elem


    count = 0
    for i in range(len(encoded)-1):
        if encoded[i] != new_encoded_mas[i]:
            count += 1
    print(f'Вероятность ошибки: {probability}%')
    print(f'Инвертировано: {count} двоичных символов')

    return new_encoded_mas


#________________________________________________ТЕЛО ПРОГРАММЫ____________________________________________________

#точка входа в программу
answer = input("Чтение из файла(0) / терминала(1)?" + '\n')
if answer == '1':
    array_of_text = input("Введите текст" + '\n')
    print(f'Введенный вами текст: {array_of_text}')
    Data_Source.Body(array_of_text)
    encoded = Coder.Shifrator(array_of_text, dic_of_shifr)  # зашифрованное сообщение

    # добавим шум
    encoded = Noise(encoded)

    Count(encoded)
    Average(dic_of_shifr)
    Sender.Body(dic_of_shifr, encoded)
    #Reciever.(dic_of_shifr, mas_of_binary_code)
else:
    file = open('/Users/vladsytnik/Desktop/fileINPUT.txt', 'r')
    array_of_text = file.read()
    print(f'Текст из файла: {array_of_text}')
    Data_Source.Body(array_of_text)
    encoded = Coder.Shifrator(array_of_text, dic_of_shifr)  # зашифрованное сообщение
    Count(encoded)
    Average(dic_of_shifr)
    Sender.Body(dic_of_shifr, encoded)
    # Reciever.(dic_of_shifr, mas_of_binary_code)
    f = open('/Users/vladsytnik/Desktop/fileOUTPUT.txt', 'w')
    f.write(encoded)


