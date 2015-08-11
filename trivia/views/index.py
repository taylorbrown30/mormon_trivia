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
        return dmp_render_to_response(request, 'index.html', template_vars)
    # user = User.objects.get(username='TaylorBrown')
    auth = user.social_auth.first()
    # print(auth)

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
    finished_games = games.filter(finished=True)
    my_turn =  games.exclude(finished=True).filter(my_turn=True)
    their_turn = games.exclude(finished=True).filter(my_turn=False)

    print("finsied games:", finished_games)
    print("myturn:", my_turn)
    print("thier_turn:", their_turn)

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
    print(id)
    opponent = User.objects.get(social_auth__uid=id)


    g = Game()
    g.player = user
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

    game_id= request.urlparams[0]
    print(game_id)


    game = Game.objects.get(id=game_id)
    opponent_game= game.opponent_game
    print("gasdhfladsfadsklsd", opponent_game)
    opponent = opponent_game.player

    if game.number_right ==3:
        print("Righttttttttttttttttttttttttttttttttttttttttt")
        return win_category(request)

    template_vars = {
        "opponent": opponent,
        "user": user,
        "game_id":game.id,
    }
    return dmp_render_to_response(request, 'category.html', template_vars)

@view_function
def win_category(request):
    user = request.user

    game_id= request.urlparams[0]
    categories = Category.objects.all()

    game = Game.objects.get(id=game_id)
    # game.number_right = 0
    # game.save()

    template_vars = {
        "categories": categories,
        "user": user,
        "game_id":game.id,
    }
    return dmp_render_to_response(request, 'win_category.html', template_vars)



@view_function
def question(request):
    game_id = request.urlparams[0]
    category_id = request.urlparams[1]

    game = Game.objects.get(id=game_id)
    category = Category.objects.get(id=category_id)
    print(category.name, "___________________________")

    total = Question.objects.filter(category__name=category.name).count()
    print(total)
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
    import facebook

    # user = User.objects.get(username='TaylorBrown')
    user = request.user
    auth = user.social_auth.first()
    print(auth)

    joe_token = "CAAHRygMZAE8IBAJFZAjVkvXumfwOAN7u2ZCpQQ4q0DAKzZCk6ZBTEPG3ZBdxEpz75VtLx2YKZCeOrZB6AKDyXe907ZAcUgnBmhZAEYdUyANpPeo8zH3T2gPU35wNqmEKrxQHrZA4VAAdzl2jv959Xn5Vp6B3MGkZBTXZBF147beDsHvDrjCQNkNMSzSKJ"
    graph = facebook.GraphAPI(access_token=auth.extra_data['access_token'])
    # graph = facebook.GraphAPI(access_token=joe_token)


    # friends = graph.get_connections("me", "taggable_friends")
    args = {'fields' : 'id,name,picture' }
    friends = graph.get_object("me/friends", **args)


    # friends = graph.get_connections(id='me', connection_name='friends')
    print(friends)
    # graph.put_object('me', 'feed', message=status.message)
    # status.publish_timestamp = datetime.datetime.now()
    # status.save()
    template_vars = {
        'friends': friends,

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
                game.opponent_game.win_loss = False
                game.opponent_game.finished = True
                game.opponent_game.my_turn=False
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

