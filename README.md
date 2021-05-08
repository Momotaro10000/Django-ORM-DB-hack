# Взламываем школьный [дневник](https//:github.com/devmanorg/e-diary/tree/master/)



Родители обещали крутой подарок за хорошую успеваемость, а с оценками беда? Нет времени грустить! Качай скрипт, и начнется магия...

_Внимание! При частом использовании вызывает зависимость и вероятность потерять все. Использовать осознанно._



## Как использовать?



Надеюсь, база данных с оценками у тебя? Без нее ничего не получиться, тебе придется добывать ее самостоятельно.

Как только получишь базу, запускай консоль Django:
```python
python manage.py shell
```

Сохраняй файл со скриптами magic_scripts.py в папку с файлом manage.py и запускай его в консоль:
```python
from magic_scripts import *
```


## Волшебные функции



1. "Починить оценки".
На ввод функция принимает имя ученика, меняет двойки и тройки на пятерки. Лучше знать точно имя и фамилию, иначе есть шанс исправить оценки не тому. Сначала введи фамилию, затем - имя.
```python
fix_marks('Фролов Иван')
```
На исполнение скрипту нужно какое-то время - оценок много.


2. "Прилежный ученик". 
Как по волшебству исчезнут все замечания от учителей. На ввод функция принимает имя ученика.
```python
remove_chastisements('Фролов Иван')
```
_Cледи за правильным вводом имени ('Фамилия Имя')_


3. "Учительская любовь". 
Функция сама от имени учителя пишет тебе похвалу, нужно лишь ввести имя ученика и предмет:
```python
create_commendation('Фролов Иван','Математика')
```

Похвала появляется за последний урок по указанному тобой предмету, так что не больше одной похвалы за урок! И ты уж постарайся написать название предмета без ошибок.



## На что еще способен скрипт?



Если у тебя есть хороший друг, ему тоже можно подсобить. Скрипт можно использовать сколько угодно, главное - не попадись!




_Скрипт написан в учебных целях для курса Django-ORM на [devman](https//:dvmn.org/)._
