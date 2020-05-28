#!/usr/bin/python3

import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

# matplotlib.use('Qt4Agg')

# Seances CC normales
la_poly = {
    '2018-05-20': 4,
    '2018-06-10': 6,
    '2018-07-08': 4,
    '2018-07-29': 1,
    '2018-08-19': 1,
    '2018-09-06': 0,
    '2018-10-25': 0,
    '2018-11-22': 2,
    '2019-01-24': 1,
    '2019-04-25': 0
}
# Autres seances (reunions STs, ASTP)
la_poly_plus = {
    '2018-09-20': 2,
    '2018-10-11': 8,
    '2018-11-29': 2
}

dates = list(la_poly.keys())
dates_x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
num_lapoly = list(la_poly.values())

dates_plus = list(la_poly_plus.keys())
dates_plus_x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates_plus]
num_lapoly_plus = list(la_poly_plus.values())

x_fit = mdates.date2num(dates_x)
z4 = np.polyfit(x_fit, num_lapoly, 1)
p4 = np.poly1d(z4)
xx = np.linspace(x_fit.min(), x_fit.max(), 100)
dd = mdates.num2date(xx)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.plot(dates_x, num_lapoly, label='instances CA, CC')
plt.plot(dates_plus_x, num_lapoly_plus, label='autres (STs, ASTP)')
plt.plot(dd, p4(xx), ':g', label='deg 1')
plt.gcf().autofmt_xdate()
plt.legend(fontsize=20)
plt.xticks(dates_x + dates_plus_x)
# plt.ylim((0, max(num_lapoly + num_lapoly_plus) + 1))
plt.xlabel('date d\'une instance', fontsize=25)
plt.ylabel('nombre d\'infractions', fontsize=25)
plt.title('Infractions -- norme d\'utilisation du nom officiel', fontsize=30)
plt.grid()
plt.show()
