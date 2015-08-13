from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.TextField(blank=True, null=True)
    creation_date= models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.NullBooleanField(default=True)

    def __str__(self):
        return '%s' % (self.name)


class Question(models.Model):
    question = models.TextField()
    answer_a = models.TextField()
    answer_b = models.TextField( blank=True, null=True)
    answer_c = models.TextField( blank=True, null=True)
    answer_d = models.TextField( blank=True, null=True)
    correct_answer = models.TextField()
    number = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    creation_date= models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.NullBooleanField(default=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return '%s' % (self.question)


class Player(models.Model):
    user = models.OneToOneField(User)
    answered_questions = models.ManyToManyField(Question)
    picture_url = models.TextField(blank=True, null=True)

    # username -Required. 30 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.
    # first_name
    # last_name
    # email
    # password
    # groups
    # user_permissions
    # is_staff
    # is_active
    # is_superuser
    # last_login

class Game(models.Model):
    player = models.ForeignKey(User)
    opponent_game = models.ForeignKey('self', null=True)
    my_turn = models.BooleanField(default=False)
    # player2 = models.ForeignKey(User, related_name='player2', blank=True, null=True)
    current_round = models.IntegerField(default=0)
    number_right = models.IntegerField(default=0)
    category_1 = models.BooleanField(default=False)
    category_2 = models.BooleanField(default=False)
    category_3 = models.BooleanField(default=False)
    category_4 = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    win_loss = models.NullBooleanField(null=True)
    finished_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return '%s - %s Round: %s My Turn: %s' % (self.id, self.player.first_name, self.current_round, self.my_turn)


def save_profile(backend, user, response, *args, **kwargs):
    import facebook
    if backend.name == 'facebook':
        # print("_________________________________________________")
        # print(user.social_auth)
        try:
            p= user.player
        except AttributeError:
            graph = facebook.GraphAPI(access_token=response['access_token'])
            # args = {'fields' : 'id,name,picture' }
            # auth = user.social_auth.first()
            result = graph.get_object(response["id"]+"/picture?width=70")
            # print(result)
            url = result['url']
            # print(url)
            p = Player()
            p.picture_url = url
            p.user = user
            p.save()

        # print(user.player.picture_url)
        # user.save()

        #
        # profile = user.get_profile()
        # if profile is None:
        #     profile = Profile(user_id=user.id)
        # profile.gender = response.get('gender')
        # profile.link = response.get('link')
        # profile.timezone = response.get('timezone')
        # profile.save()


from django.contrib import admin

# register any models here
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Player)

