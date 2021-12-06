Проект **frog_compass** предназначен для обработки данных, полученных в научных экспериментах
по изучению влияния магнитного поля на сетчатку лягушек. В данных экспериментах проверяется
гипотеза о навигации лягушек под влиянием магнитного поля Земли.

### Скрипт **detrend.py**

Скрипт выполняет вычитание линейного тренда из сигналов.
Линейный тренд строится по точкам с 20 по 90 и с n-50 по n.
В папке raw находятся файлы с сигналами, снятыми с сетчатки.
Файлы с удаленным трендом записываются в папку detrended.

### Скрипт **combine_files.py**

Скрипт объединяет файлы из папки detrended.
В зависимости от выбора пользователя файлы объединяются в один файл out.txt
или в два файла - out1.txt и out2.txt.
В нечетных файлах присутствуют сигналы, снятые при воздействии поля 1.
В четных файлах присутствуют сигналы, снятые при воздействии поля 2.
Значения в выходных файлах разделены табуляцией. Файлы могут быть открыты в Excel.

### Блокнот **approximate.ipynb**

Блокнот выполняет апроксимацию сигнала, определяя коэффициенты экспоненты
```
y = a * exp(-b * x) + c.
```
Входной файл должен находится в папке ./approximation/
Для работы блокнота необходимо в его тексте задать параметры, например:

```
filename = '15.asc'
left = 1.7
right = 12
time_resolution = 0.01
```
где left и right - это отметки времени в секундах, определяющие интервал построения экспоненты;
time_resolution - количество секунд в отсчете.

Запуск - approximate.bat. Откроется окно браузера с блокнотом. 
В папку ./approximate/ записывается файл png с графиками исходного сигнала и экспонентой.
Коэффициенты a, b, c и R-squared выводятся в консоли и в легенде графика.
По окончании работы закрыть вкладку браузера и окно cmd.

### Условия выполнения

Для работы скриптов на компьютере должен быть установлен
[python 3.8.10](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe).
Установка python должна производиться для всех пользователей компьютера в папку program files
(данные параметры указывается во время установки).

Дополнительные пакеты должны быть установлены от имени администратора.
Запустить cmd или powershell от имени администратора, выполнить:
```
pip install natsort
pip install numpy
pip install scipy
pip install matplotlib
pip install jupyter
```