# filename: myparser.pe
"""Данный модуль содержит реализацию класса Parser, выполнящего функции 'парсинга' строки текста заявки
на выполнение процедуры обмена монет.
Формат строки - '<Имя> : <Название_монеты_1> [, <Название_монеты_2>, .. <Название_монеты_N>]' .
Логика работы Парсера не защищена от наличия в обрабатываемом потоке данных 'мусорных' символов..."""
class Parser:
    def parsing(self, line):
        """Метод 'парсинг' выполняет 'первичный' разбор строки текста в указанном формате.
        Аргумент метода - ссылка на строку line, содержащую описание лота заявки от коллекционера.
        Метод возвращает ссылку на список строк, соответствующих имени коллекционера и названию монет.
        Данный метод позволяет удалять лишние пробельные символы, которые могут содержаться
        в обрабатываемой строке, описывающей лот заявки коллекционера."""
        listLines = line.split(':')  # Разделение строки на блоки. Символ-разделитель ':' - двоеточие.
        if len(listLines) != 2:  # Если строка содержит не два блока записей, разделенных двоеточием - это ошибка по данным!
            return None
        else:
            res = list()            # Пустая строка для формирования результат
            name = listLines[0]     # Выделяем имя коллекционера - первую запись строки заявки на проведение обмена
            name = name.strip(' ')  # Фильтруем возможный лишние пробелы в начале и в конце записи имени коллекционера
            res.append(name)        # Вставляем в реузльтирующую строку имя коллекционера
            moneys = listLines[1]   # Список строк монет, заявленных коллекционером на процедеру обмена
            # Теперь необходимо строку, содержащую набор записей - названий монет, разделенных запятыми, разбить
            # по символу-разделителю - ',' (запятая).
            moneys = moneys.split(',')
            for money in moneys:     # Цикл обработки строк, содержащих названия монет, возможно, содержащих 'мусор'
                money = money.strip(' ')  # Удаление лишних пробелов в начале и в конце строки, содержащей название монеты
                if len(money) == 0:  # Строка оказалось пуста, состояла только из пробельных символов...
                    continue
                res.append(money)
            return res  # Возвращается список строк, первый элемент - первая строка содержит имя коллекционера,
            # последующие элементы списка содержат строки - "отфильтрованные от пробелов" названия монет.
    # END method Parser.parsing
# END class Parse
# Блок процедур тестирования модуля
if __name__ == '__main__':
    pars = Parser()
    line = "Bob Smith  : 1Rubl, 2ShnedCron , 5Franc , 1Funt, , "
    line = pars.parsing(line)
    print("Result : ", line)
