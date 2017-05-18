import sys
import os
import pandas as pd
from datetime import datetime, date, time
from pandas import DataFrame
from urllib.request import urlopen

df = DataFrame({'id': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
                    'id_1': [24,25,5,6,27,23,26,7,12,13,14,15,16,17,18,19,21,22,8,9,10,1,3,2,4],
                    'name': ["Вінницька", "Волинська", "Дніпропетровська", "Донецька", "Житомирська", "Закарпатська",
                             "Запорізька", "Івано-Франківська", "Київська", "Кіровоградська", "Луганська", "Львівська", "Миколаївська", "Одеська", "Полтавська",
                             "Рівенська", "Сумська", "Тернопільська", "Харківська", "Херсонська", "Хмельницька", "Черкаська", "Чернівецька", "Чернігівська", "Республіка Крим"]})


dt = DataFrame()

def clearScreen():
    clear = lambda: os.system('cls')
    clear()

def DownloadFile(region):
    url="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2017&type=Mean".format(df.id_1[int(region)])
    print(url)
    dt = datetime.now()
    vhi_url = urlopen(url)
    filename = "data/VHI_"+str(df.id_1[int(region)])+"_"+dt.strftime("%d-%m-%Y_%H%M")+".csv"
    out = open(filename, 'wb')
    out.write(vhi_url.read())
    out.close()
    clearFile(filename)

def clearFile(filename):
    f = open(filename).readlines()
    s = f[0].split('<pre>')
    for i in [0, 0, -1]:
        f.pop(i)
    with open(filename, 'w') as F:
        F.writelines(f)
    loadCSV(filename)

def loadCSV(filename):
    print("CSV Load")
    dt = pd.read_csv(filename, index_col=False, names=['year', 'week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI'], sep='[ ,]+',engine='python')
    menu2(dt)

def menu1():
    clearScreen()
    print(df['name'])
    print("----------------------------------------------------------")
    print("Выберете Q что бі закончить программу")
    region = input("Выберете область:")
    if region == 'Q':
        sys.exit()
    if region == 'q':
            sys.exit()

    try:
        i = int(region)
        if i>25: menu1()
    except:
        menu1()

    clearScreen()
    print("Принимаем данные....")
    DownloadFile(region)

def menu2(dt):
    clearScreen()
    print("1 - Отчет: Ряд VHI для області за рік")
    print("2 - Отчет: Ряд VHI за всі ровки для області, єкстремальні посухами")
    print("3 - Отчет: Ряд VHI за всі ровки для області, помірни посухами")
    print("---------------------------------------------------------------------")
    print("Q - Вернуть в предидущее меню")
    a = input("")
    if (a == '1'): menu3(dt)
    elif (a == '2'): menu4(dt)
    elif (a == '3'): menu5(dt)
    elif (a == 'Q'): menu1()
    elif (a == 'q'): menu1()
    else: menu2(dt)

def menu3(dt):
    clearScreen()
    print("Отчет: Ряд VHI для області за рік")
    print("---------------------------------------------------")
    strYear = input("Введите интересующий Вас год или Q что бы вернуться в предидущее меню:\n")
    if strYear=='Q': menu2(dt)
    if strYear == 'Й': menu2(dt)
    if strYear == 'q': menu2(dt)
    if strYear == 'й': menu2(dt)
    try:
        year = int(strYear)
        if (year<1981 or year>2017): menu3(dt)
    except:
        menu3(dt)
    print("Максимальное значение за "+strYear+" год = "+str(dt[dt.year == year].VHI.max()))
    print("Минимальное значение за " + strYear + " год = " + str(dt[dt.year == year].VHI.min()))
    cmd = input()
    if cmd == 'Q': menu2(dt)
    if cmd == 'Й': menu2(dt)
    if cmd == 'q': menu2(dt)
    if cmd == 'й': menu2(dt)


def menu4(dt):
    clearScreen()
    print("Отчет: Ряд VHI за всі ровки для області, єкстремальні посухами\n")
    print("-----------------------------------------------------")
    cmd = input("Укажите минимальное знаение процента (он должен быть меньше 15%):\n")

    try:
        p = int(cmd)
        if (p<=0 or p>=15): menu4(dt)
    except:
        menu4(dt)
    print("Интересующие Вас года:")
    print(dt[(dt.VHI>p) & (dt.VHI<15)].year)
    cmd = input("Для перехода в предидущее меню нажмите Q\n или нажмите 1 для повторения отчета\n")
    if cmd == 'Q': menu2(dt)
    if cmd == 'Й': menu2(dt)
    if cmd == 'q': menu2(dt)
    if cmd == 'й': menu2(dt)
    if cmd == '1': menu4(dt)

def menu5(dt):
    clearScreen()
    print("Отчет: Ряд VHI за всі ровки для області, єкстремальні посухами\n")
    print("-----------------------------------------------------")
    cmd = input("Укажите минимальное знаение процента (он должен быть больше 15% и меньше 35%):\n")
    try:
        p = int(cmd)
        if (p <= 15 or p >= 35): menu4(dt)
    except:
        menu5(dt)
    print("Интересующие Вас года:")
    print(dt[(dt.VHI > p) & (dt.VHI < p)].year)
    cmd = input("Для перехода в предидущее меню нажмите Q\n или нажмите 1 для повторения отчета\n")
    if cmd == 'Q': menu2(dt)
    if cmd == 'Й': menu2(dt)
    if cmd == 'q': menu2(dt)
    if cmd == 'й': menu2(dt)
    if cmd == '1': menu5(dt)

if __name__ == '__main__':
    menu1()

