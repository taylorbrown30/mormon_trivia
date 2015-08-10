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

from django.contrib import admin

# register any models here
admin.site.register(Question)
admin.site.register(Category)

