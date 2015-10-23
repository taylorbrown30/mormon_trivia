from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from trivia.models import *
from django.http import HttpResponse
from random import randint

@view_function
def process_request(request):


    # c = Category()
    # c.name = "Book of Mormon"
    # c.save()
    #
    # c1 = Category()
    # c1.name = "Church History"
    # c1.save()
    #
    # c2 = Category()
    # c2.name = "Prophets"
    # c2.save()
    #
    # c3 = Category()
    # c3.name = "Mormon Culture"
    # c3.save()

    import csv
    with open(settings.STATIC_ROOT + '/trivia/media/questions.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        count = 0
        for row in spamreader:
            if count == 0:
                count=count+1
            else:
                que = Question()
                que.question = row[1].strip()
                que.answer_a = row[2].strip()
                que.answer_b = row[3].strip()
                que.answer_c = row[4].strip()
                que.answer_d = row[5].strip()
                que.correct_answer = row[6].strip()
                que.category_id = row[0].strip()
                que.save()

            # for cell in row:
            #     print (cell)



    #
    # que = Question()
    # que.question = "While they were wandering in the wilderness, Nephi broke this metal object."
    # que.answer_a = "Brass Plates"
    # que.answer_b = "He didn't break anything!!!"
    # que.answer_c = "Brazen Serpent"
    # que.answer_d = "Bow"
    # que.correct_answer = "d"
    # que.category_id = 1
    # que.save()
    #
    # que = Question()
    # que.question = "Who is the only woman recorded to have seen the plates and Moroni?"
    # que.answer_a = "Mary Whitmer"
    # que.answer_b = "Emma Smith"
    # que.answer_c = "Lucy Mack Smith"
    # que.answer_d = "Lydia Knight"
    # que.correct_answer = "a"
    # que.category_id = 2
    # que.save()


    return HttpResponse("hi")