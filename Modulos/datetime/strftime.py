# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime

# fmt = "%d/%m/%Y"
# fmt = "%d/%m/%Y %H:%M"
fmt = "%d/%m/%Y %H:%M:%S"
data = datetime.strptime("2022-12-13 07:59:23", "%Y-%m-%d %H:%M:%S")
print(data.strftime(fmt))
print(data.strftime("%Y"))  # ano em str
print(data.year)  # ano em int
