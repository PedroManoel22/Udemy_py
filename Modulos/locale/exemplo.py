# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

import calendar
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
# mudamos o locale para o padrão do sistema operacional
print(calendar.calendar(2002))

print(locale.getlocale())  # como saber o locale da máquina
