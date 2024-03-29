import datetime
from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from trivia.models import *
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
import facebook

@view_function
def process_request(request):

    user = request.user
    if not user.is_authenticated():
        template_vars = {
            "user": user
        }
        return dmp_render_to_response(request, 'login.html', template_vars)

    auth = user.social_auth.first()

    graph = facebook.GraphAPI(access_token=auth.extra_data['access_token'])

    picture = graph.get_object("me/picture")

    template_vars = {
        'user': user,
        'picture_url': picture["url"],

    }
    return dmp_render_to_response(request, 'index.html', template_vars)

@view_function
def home(request):

    user = request.user
    games = Game.objects.filter(player=user)
    finished_games = games.filter(finished=True)[:10]
    my_turn =  games.exclude(finished=True).filter(my_turn=True)[:10]
    their_turn = games.exclude(finished=True).filter(my_turn=False)[:10]

    print("finsied games:", finished_games)
    print("myturn:", my_turn)
    print("their_turn:", their_turn)

    template_vars = {
        'their_turn': their_turn,
        'my_turn': my_turn,
        "finished_games": finished_games,

    }
    return dmp_render_to_response(request, 'home.html', template_vars)

@view_function
def new_game(request):

    template_vars = {
    }
    return dmp_render_to_response(request, 'new_game.html', template_vars)


@view_function
def create_game(request):
    user = request.user
    if not user.is_authenticated():
        HttpResponseRedirect("/trivia/index")

    id= request.urlparams[0]
    id_number = user.id
    if id:
        opponent = User.objects.get(social_auth__uid=id)
    else:
        # make sure random doesn't pick yourself
        while id_number == user.id:
            count = User.objects.count()
            random_index = randint(0, count - 1)
            opponent = User.objects.all()[random_index]
            id_number = opponent.id

    g = Game()
    g.player = user
    g.my_turn = True
    g.save()

    g2 = Game()
    g2.player = opponent
    g2.save()

    g2.opponent_game =g
    g.opponent_game=g2

    g.save()
    g2.save()

    import json
    data = {'success' : True, 'id' : str(g.id)}
    return HttpResponse( json.dumps( data ) )


@view_function
def category(request):
    user = request.user
    game = Game.objects.get(id=request.urlparams[0])
    opponent_game= game.opponent_game
    opponent = opponent_game.player

    if game.finished or game.my_turn == False:
        return HttpResponseRedirect("/trivia/index")

    if game.number_right ==3:
        print("Righttttttttttttttttttttttttttttttttttttttttt")
        return win_category(request)

    template_vars = {
        "opponent": opponent,
        "user": user,
        "game":game,
    }
    return dmp_render_to_response(request, 'category.html', template_vars)

@view_function
def win_category(request):
    user = request.user
    categories = Category.objects.all()
    game = Game.objects.get(id=request.urlparams[0])

    if game.finished or game.my_turn == False:
        return HttpResponseRedirect("/trivia/index")

    template_vars = {
        "categories": categories,
        "user": user,
        "game": game,
    }
    return dmp_render_to_response(request, 'win_category.html', template_vars)


@view_function
def question(request):
    game = Game.objects.get(id=request.urlparams[0])
    category = Category.objects.get(id=request.urlparams[1])

    if game.finished or game.my_turn == False:
        return HttpResponseRedirect("/trivia/index")

    total = Question.objects.filter(category__name=category.name).count()

    # TODO Try to find a question they haven't had before
    random = randint(0,total-1)
    questions = Question.objects.filter(category__name=category.name)
    question = questions[random]

    # todo fix it so once the question is shown they get it wrong if no answer is received
    template_vars = {
        'question': question,
        'game_id': game.id,
        'category_id': category.id,
    }
    return dmp_render_to_response(request, 'question.html', template_vars)


@view_function
def friends(request):

    from django.contrib.auth.models import User

    user = request.user
    auth = user.social_auth.first()
    print(auth)

    joe_token = "CAAHRygMZAE8IBAJFZAjVkvXumfwOAN7u2ZCpQQ4q0DAKzZCk6ZBTEPG3ZBdxEpz75VtLx2YKZCeOrZB6AKDyXe907ZAcUgnBmhZAEYdUyANpPeo8zH3T2gPU35wNqmEKrxQHrZA4VAAdzl2jv959Xn5Vp6B3MGkZBTXZBF147beDsHvDrjCQNkNMSzSKJ"
    graph = facebook.GraphAPI(access_token=auth.extra_data['access_token'])
    # graph = facebook.GraphAPI(access_token=joe_token)

    args = {'fields' : 'id,name,picture' }
    friends = graph.get_object("me/friends", **args)

    new_friends = []
    for f in friends['data']:
        print(f['id'])
        if User.objects.filter(social_auth__uid=f['id']):
            new_friends.append(f)

    template_vars = {
        'friends': new_friends,
    }
    return dmp_render_to_response(request, 'friends.html', template_vars)


@view_function
def check_answer(request):
    dict = request.GET
    print(dict)
    question_id = dict['question_id']
    answer = dict['answer']
    game_id = dict['game']
    category_id = dict['category']

    game = Game.objects.get(id=game_id)

    q = Question.objects.get(id=question_id)
    if answer == q.correct_answer:
        game.number_right = game.number_right+1
        game.save()
        # Answered 3 right so choose a category to play for
        if game.number_right == 3:
            return HttpResponse('category')
        # Answered category question right so completes that category
        if game.number_right == 4:
            string = "category_"+ category_id
            setattr(game,string,True)
            game.number_right=0
            game.save()

            # Won that game
            if game.category_1 and game.category_2 and game.category_3 and game.category_4:
                game.finished = True
                game.win_loss = True
                game.my_turn=False
                game.finished_date= datetime.datetime.now()
                game.opponent_game.win_loss = False
                game.opponent_game.finished = True
                game.opponent_game.my_turn=False
                game.opponent_game.finished_date= datetime.datetime.now()
                game.opponent_game.save()
                game.save()
                return HttpResponse('won_game')

        return HttpResponse('correct')
    else:
        game.my_turn=False
        game.opponent_game.my_turn=True
        game.opponent_game.save()
        game.number_right=0
        game.current_round=game.current_round+1
        game.save()
        return HttpResponse("incorrect")

    return HttpResponse("error")

