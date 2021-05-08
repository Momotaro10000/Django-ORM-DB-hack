from datacenter.models import Schoolkid,Mark,Lesson,Chastisement,Commendation
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
import random


def get_kid_account(kid_name):
    try:
        kid = Schoolkid.objects.filter(full_name__contains=kid_name).get()
        return kid
    except ObjectDoesNotExist:
        print('Такого ученика {} в списке нет! Проверь, правильно ли написано имя.'.format(kid_name))
        return None
    except MultipleObjectsReturned:
        print('Учеников с именем {} слишком много, укажи полное имя.'.format(kid_name))
        return None


def fix_marks(kid_name):
    kid = get_kid_account(kid_name)
    if not kid:
        return None
    bad_marks = Mark.objects.filter(schoolkid=kid,points__in=[2, 3])
    for mark in bad_marks:
        mark.points = '5'
        mark.save()


def remove_chastisements(kid_name):
    kid = get_kid_account(kid_name)
    if not kid:
        return None
    chas = Chastisement.objects.filter(schoolkid=kid)
    chas.delete()


def create_commendation(kid_name,subject):
    commendations = [ 
        'Молодец!', 
        'Отлично!', 
        'Хорошо!', 
        'Гораздо лучше, чем ожидалось!', 
        'Великолепно!', 
        'Прекрасно!', 
        'Сказано здорово – просто и ясно!', 
        'Очень хороший ответ!', 
        'Талантливо!', 
        'Уже существенно лучше!', 
        'Потрясающе!', 
        'Замечательно!', 
        'Прекрасное начало!', 
        'Так держать!', 
        'Ты на верном пути!', 
        'Здорово!', 
        'Это как раз то, что нужно!', 
        'Я тобой горжусь!', 
        'С каждым разом у тебя получается всё лучше!', 
        'Мы с тобой не зря поработали!', 
        'Я вижу, как ты стараешься!', 
        'Ты растешь над собой!', 
        'Теперь у тебя точно все получится!', 
    ]
    kid = get_kid_account(kid_name)
    if not kid:
        return None
    try: 
        lessons = Lesson.objects.filter(year_of_study=kid.year_of_study,group_letter=kid.group_letter,subject__title=subject).order_by('date')
        needed_lesson = lessons[0]
        Commendation.objects.create(text=random.choice(commendations),created=needed_lesson.date,schoolkid=kid,subject=needed_lesson.subject,teacher=needed_lesson.teacher)
    except ObjectDoesNotExist:
        print('Предмета {} в списке нет! Кажется, в названии предмета ошибка.'.format(subject))
        return None