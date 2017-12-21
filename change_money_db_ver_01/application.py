# filename: application.py
"""Модуль определяет атрибуты и методы класса Application, определяющего бизнес-логику приложения"""
from offert import *
from demand import *
import copy
class Application:
    """Класс Application отвечает за реализацию бизнес-логики приложения.
    С данным классам связаны ресурсы: две ссылки на файлы, содержащие данные о заявках коллекционеров на проведение
    процедуры обмена монет, файл предложений и файл требований. При разработке класса использована агрегация, то есть
    определение в качестве атрибут объектов других классов: Demand и Offert."""
    def __init__(self):
        """Конструктор класса Application"""
        self.offertFileName = str()  # Ссылка на строку, содержащую имя файла 'предложения' на обмен
        self.demandFileName = str()  # Ссылка на строку, содержащую имя файла 'спроса' на обмен
        self.offerts = []  #  Список 'Предложений' в формате [str(<Название_монеты>),str(<Имя_коллекционера>)]
        self.demands =[]    #  Список 'Спроса'(т.е. 'Требований') в формате [str(<Название_монеты>),str(<Имя_коллекционера>)]
        self.trade =[]  # Результирующий список, содержащий данные по процедуре обмена монетами между коллекционерами
        self.offertFileStatus = False  # Данные переменные испольуются для выполнения проверки возможности открыть
        self.demandFileStatus = False  # указанные файлы, содержащие описание лотов 'Спроса' и 'Предложения'
        self.possibleExchanges = [] # Список содержащий возможные обмены
    # END constructor class Application

    def setTrade(self, offertFileName, demandFileName):
        """Данный метод отвечает за выполнение процедуры инициализации данных лотов 'Спроса' и 'Предложений'."""
        with open(offertFileName, mode="r", encoding="cp1251") as offertFile:
            self.offerts.clear()  # Очитска списка 'Предложений' при подготовке к новой процедуре обмена
            for line in offertFile:  # В цикле перебираются строки текста открытого файла
                self.offerts.append(line.rstrip('\n'))  # В конце строки нужно удалить символ '\n'
            # END circle - Конец цикла, из файла прочитаны все строки.
        # END - Конец блока менеджера контекста. Файл атоматически гарантированно закрыт
        with open(demandFileName, mode='r', encoding='cp1251') as demandFile:
            self.demands.clear()  # Очитска списка 'Спроса' при подготовке к новой процедуре обмена
            for line in demandFile:  # В цикле перебираются строки текста открытого файла
                self.demands.append(line.rstrip('\n'))  # В конце строки нужно удалить символ '\n'
            # END circle - Конец цикла, из файла прочитаны все строки.
        # END - Конец блока менеджера контекста. Файл атоматически гарантированно закрыт
        # В случае успешного выполнения данных блоков операций будут сформированы списки строк 'Спроса' и 'Предложения'
        # Теперь необходимо обработать списки строк заявок
        obj = Offert()  # создание локального объекта - экземпляра класса 'Предложение'
        obj.setOffert(self.offerts)
        obj.make()
        self.offerts = obj.listOfferts
        obj = Demand()  # создание локального объекта - экземпляра класса 'Спрос'
        obj.setDemand(self.demands)
        obj.make()
        self.demands = obj.listDemands
        num = 0
        statusDemand = False  # статус заявки типа 'Спрос': она 'удовлетворена' (True) или 'не удовлетворена' (False)
        # Цикл добавления каждому лоту заявки типа 'Спрос' нового поля - статус заявки. Первоначально все завяки
        # не удовлетворены.
        for i in self.demands:
            i.append(False)
    # END method Application.setTrade()

    def exchange(self):
        i=0
        """Данный метод отвечает за выполнение процедуры обмена монетами между коллекционерами,
        заявленными в лотах 'Спроса' и 'Предложения'."""
        self.trade.clear()  # Предварительная очистка списка 'Сделок'
        copyOfferts = copy.copy(self.offerts)  # создание поверхностной копии списка лотов 'Предложения'
        copyDemands = copy.copy(self.demands)  # создание повержностной копии списка лотов 'Спроса'
        # При определении ввозможности сделки сначало анализируется 'Предложение'. Последовательно выполняется
        # цикл передора элементов списка 'Спрос'. Если сделак по обмену возможна - имеются нужные монеты в лотах
        # 'Спрос' и 'Предложение', в список self.trade заносится информация обоих участников сделки
        for bidOffert in copyOfferts:
            for bidDemand in copyDemands:
                if bidOffert[0] == bidDemand[0]:  # Названия момент в лотах 'Спроса' и 'Предложения' совпадают
                    if bidDemand[2] == True:
                        continue  # Данная заявка уже удовлетворена. Переходим к следующей итерации цикла
                    self.possibleExchanges.append([bidOffert[0], bidOffert[1], bidDemand[1]])
                    line = bidOffert[0] + ' ' + bidOffert[1] + ' -> ' + bidDemand[1]  # Строка - описание сделки
                    print("Возможная продажа : ",line)
                    # Ура! Возможен обмен. В данной программе не рассматривается процедера 'Аукциона' среди желающих
                    #  получить нужную монету. Выполняется первый встретившийся вариант обмена
                    # После выполнения сделки лот удовлетворенной заявки 'Спроса' должен быть удален из списка
                    bidDemand[2] = True
                    i+=1
        i = len(self.possibleExchanges)
        print("\n")
        for k in range(i-1):
            c = k + 1
            seller1 = self.possibleExchanges[k][1]
            buyer1 = self.possibleExchanges[k][2]
            while c<i:
                seller2 = self.possibleExchanges[c][1]
                buyer2 = self.possibleExchanges[c][2]
                if seller1 == buyer2 and self.possibleExchanges[k][0] != "0":
                    if buyer1 == seller2 and self.possibleExchanges[c][0] != "0":
                        line = (self.possibleExchanges[k][1] + ' <-> ' + self.possibleExchanges[k][2] + ' : ' + self.possibleExchanges[k][0] + ' <-> ' + self.possibleExchanges[c][0]) # Строка - описание сделки
                        currency1 = self.possibleExchanges[k][0]
                        currency2 = self.possibleExchanges[c][0]
                        for g in range(len(self.possibleExchanges)):
                            if self.possibleExchanges[g][1] == self.possibleExchanges[k][1] and self.possibleExchanges[g][0] == currency1:
                                self.possibleExchanges[g][0] = "0"
                            if self.possibleExchanges[g][2] == self.possibleExchanges[k][1] and self.possibleExchanges[g][0] == currency2:
                                self.possibleExchanges[g][0] = "0"
                                
                        for g in range(len(self.possibleExchanges)):
                            if self.possibleExchanges[g][1] == self.possibleExchanges[k][2] and self.possibleExchanges[g][0] == currency2:
                                self.possibleExchanges[g][0] = "0"
                            if self.possibleExchanges[g][2] == self.possibleExchanges[k][2] and self.possibleExchanges[g][0] == currency1:
                                self.possibleExchanges[g][0] = "0"
                        print("Сделка : ",line)
                        self.trade.append(line)
                c += 1

    # END method Application.exchanhe() 

    def run(self):
        """Метод, определяющий последовательность вызова других методов класса"""
        print("======================================================================\n"
              "= Автоматизированная торговая площадка ===============================\n"
              "= Сессия - выполнение процедуры обмена монет между коллекционерами   =\n"
              "======================================================================")
        _offertFileName = input("Введите имя файла 'Предложений' : ")
        _demandFileName = input("Введите имя файла 'Спроса' : ")
        self.setTrade(_offertFileName,_demandFileName)
        self.exchange()
# END class Application

# Блок предварительного тестирования модуля и реализованных в нем процедур
if __name__ == '__main__':
    app = Application()
    app.run()
