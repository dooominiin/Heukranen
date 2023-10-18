import numpy as np

class dr:                      
    def lookup(value, lookup_table):
        # Finde den Index des nächsten kleineren Werts in der Lookup-Tabelle
        index = 0
        while index < len(lookup_table) - 2 and value > lookup_table[index][0]:
            index += 1
        # Extrahiere die Werte der nächsten beiden Punkte
        x0, y0 = lookup_table[index]
        if index > len(lookup_table)-1:
            index = len(lookup_table)-2
        x1, y1 = lookup_table[index + 1]
        # Lineare Interpolation zwischen den beiden Punkten
        interpolated_value = y0 + (y1 - y0) * (value - x0) / (x1 - x0)
        return interpolated_value
    
lookup_table = [
            (0,4.21197388614424462),
            (5400000,202.058449644594873),
            (10800000,398.271812926794325),
            (16200000,591.12460920663932),
            (21600000,778.940186344151243),
            (27000000,960.380591160864469),
            (32400000,1134.24639678983294),
            (37800000,1299.33859080336583),
            (43200000,1496.94847074355403),
            (48600000,1994.91364226592555)
            ]


ist = np.array([9 ,522 ,1176, 1400, 1485])
soll = np.array([15 ,623 ,1328, 1668 ,2020])


mess = ist/2*(2**16)
for m in mess:
    print(dr.lookup(m,lookup_table))
