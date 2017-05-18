import sys
import json
from spyre import server
import pandas as pd
from datetime import datetime, date, time
from pandas import DataFrame
from urllib.request import urlopen
import numpy as np
from matplotlib import pyplot as plt

class SimpleApp(server.App):
    title = "Выберите область"

    inputs = [{"input_type": 'dropdown',
               "label": 'Область',
               "options": [ {"label": "Вінницька",         "value":24},
                            {"label": "Волинська",         "value":25},
                            {"label": "Дніпропетровська",  "value":5},
                            {"label": "Донецька",          "value":6},
                            {"label": "Житомирська",       "value":27},
                            {"label": "Закарпатська",      "value":23},
                            {"label": "Запорізька",        "value":26},
                            {"label": "Івано-Франківська", "value":7},
                            {"label": "Київська",          "value":12},
                            {"label": "Кіровоградська",    "value":13},
                            {"label": "Луганська",         "value":14},
                            {"label": "Львівська",         "value":15},
                            {"label": "Миколаївська",      "value":16},
                            {"label": "Одеська",	       "value":17},
                            {"label": "Полтавська",        "value":18},
                            {"label": "Рівенська",         "value":19},
                            {"label": "Сумська",           "value":21},
                            {"label": "Тернопільська",     "value":22},
                            {"label": "Харківська",        "value":8},
                            {"label": "Херсонська",        "value":9},
                            {"label": "Хмельницька",       "value":10},
                            {"label": "Черкаська",         "value":1},
                            {"label": "Чернівецька",       "value":3},
                            {"label": "Чернігівська",      "value":2},
                            {"label": "Республіка Крим",   "value":4}],
                "variable_name": 'ticker'},
              {
                  "input_type": 'dropdown',
                  "label": 'Минимальный год',
                  "options": [
                      {"label": "1980", "value": 1980},
                      {"label": "1981", "value": 1981},
                      {"label": "1982", "value": 1982},
                      {"label": "1983", "value": 1983},
                      {"label": "1984", "value": 1984},
                      {"label": "1985", "value": 1985},
                      {"label": "1986", "value": 1986},
                      {"label": "1987", "value": 1987},
                      {"label": "1988", "value": 1988},
                      {"label": "1989", "value": 1989},
                      {"label": "1990", "value": 1990},
                      {"label": "1991", "value": 1991},
                      {"label": "1992", "value": 1992},
                      {"label": "1993", "value": 1993},
                      {"label": "1994", "value": 1994},
                      {"label": "1995", "value": 1995},
                      {"label": "1996", "value": 1996},
                      {"label": "1997", "value": 1997},
                      {"label": "1998", "value": 1998},
                      {"label": "1999", "value": 1999},
                      {"label": "2000", "value": 2000},
                      {"label": "2001", "value": 2001},
                      {"label": "2002", "value": 2002},
                      {"label": "2003", "value": 2003},
                      {"label": "2004", "value": 2004},
                      {"label": "2005", "value": 2005},
                      {"label": "2006", "value": 2006},
                      {"label": "2007", "value": 2007},
                      {"label": "2008", "value": 2008},
                      {"label": "2009", "value": 2009},
                      {"label": "2010", "value": 2010},
                      {"label": "2011", "value": 2011},
                      {"label": "2012", "value": 2012},
                      {"label": "2013", "value": 2013},
                      {"label": "2014", "value": 2014},
                      {"label": "2015", "value": 2015},
                      {"label": "2016", "value": 2016},
                      {"label": "2017", "value": 2017}
                  ],
                  "variable_name": 'dmin'
              },
              {
                  "input_type": 'dropdown',
                  "label": 'Максимальный год',
                  "options": [
                      {"label": "1980", "value": 1980},
                      {"label": "1981", "value": 1981},
                      {"label": "1982", "value": 1982},
                      {"label": "1983", "value": 1983},
                      {"label": "1984", "value": 1984},
                      {"label": "1985", "value": 1985},
                      {"label": "1986", "value": 1986},
                      {"label": "1987", "value": 1987},
                      {"label": "1988", "value": 1988},
                      {"label": "1989", "value": 1989},
                      {"label": "1990", "value": 1990},
                      {"label": "1991", "value": 1991},
                      {"label": "1992", "value": 1992},
                      {"label": "1993", "value": 1993},
                      {"label": "1994", "value": 1994},
                      {"label": "1995", "value": 1995},
                      {"label": "1996", "value": 1996},
                      {"label": "1997", "value": 1997},
                      {"label": "1998", "value": 1998},
                      {"label": "1999", "value": 1999},
                      {"label": "2000", "value": 2000},
                      {"label": "2001", "value": 2001},
                      {"label": "2002", "value": 2002},
                      {"label": "2003", "value": 2003},
                      {"label": "2004", "value": 2004},
                      {"label": "2005", "value": 2005},
                      {"label": "2006", "value": 2006},
                      {"label": "2007", "value": 2007},
                      {"label": "2008", "value": 2008},
                      {"label": "2009", "value": 2009},
                      {"label": "2010", "value": 2010},
                      {"label": "2011", "value": 2011},
                      {"label": "2012", "value": 2012},
                      {"label": "2013", "value": 2013},
                      {"label": "2014", "value": 2014},
                      {"label": "2015", "value": 2015},
                      {"label": "2016", "value": 2016},
                      {"label": "2017", "value": 2017}
                  ],
                  "variable_name": 'dmax',
                  "action_id": "plot"
              }]

    outputs = [{"output_type": "plot",
                "output_id": "plot",
                "on_page_load": False}]

    def getData(self, params):
        ticker = params['ticker']
        url = 'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2017&type=Mean'.format(ticker)
        filename = "data/VHI_" + str(params['ticker']) + "_" + datetime.now().strftime("%d-%m-%Y_%H%M") + ".csv"
        vhi_url = urlopen(url)
        out = open(filename, 'wb')
        out.write(vhi_url.read())
        out.close()
        f = open(filename).readlines()
        s = f[0].split('<pre>')
        for i in [0, 0, -1]:
            f.pop(i)
        with open(filename, 'w') as F:
            F.writelines(f)
        dt = pd.read_csv(filename, index_col=False, names=['year', 'week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI'],
                         sep='[ ,]+', engine='python')
        return dt[(dt.year >= int(params['dmin'])) & (dt.year <= int(params['dmax']))]

    def getPlot(self, params):
        print("ticket: "+params['ticker']+" dmin: "+params['dmin']+" dmax: "+params['dmax'])
        df = self.getData(params)
        plt_object = df.set_index('year').drop(['week'],axis=1).drop(['SMN'],axis=1).drop(['SMT'],axis=1).plot()
        fig = plt_object.get_figure()
        return fig


if __name__ == "__main__":
    app = SimpleApp()
    app.launch(port=8888)
