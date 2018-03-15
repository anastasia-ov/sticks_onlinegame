from django.shortcuts import render
from random import randint
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.

def main_view(request):
    s = request.session
    s['win'] = 0
    s['lose'] = 0
    s['start_game'] = True
    return render(request, 'main.html')


def start_view(request):
    s = request.session
    if s['start_game']:
        s['sticks_total'] = 21
        return render(request, 'start.html',
                      context=dict(sticks_total=s['sticks_total'],
                                   start_game=s['start_game'],
                                   win=s['win'],
                                   lose=s['lose']))
    else:
        return render(request, 'start.html',
                      context=dict(sticks_total=s['sticks_in_game'],
                                   start_game=s['start_game'],
                                   win=s['win'],
                                   lose=s['lose'],
                                   player1_taken=s['player1_taken'],
                                   sticks_pl1=s['sticks_in_game_2'],
                                   player2_taken=s['player2_taken'],
                                   sticks_pl2=s['sticks_total']))


def take_view(request, sticks_taken):
    s = request.session
    s['player1_taken'] = sticks_taken
    s['sticks_in_game'] = s['sticks_total']
    s['sticks_in_game_2'] = None
    s['player2_taken'] = None
    s['start_game'] = False

    if 1 <= s['player1_taken'] <= 3:
        if s['player1_taken'] <= s['sticks_in_game']:
            s['sticks_total'] -= s['player1_taken']
            if s['sticks_total'] == 0:
                s['lose'] += 1
                s['start_game'] = True
                return HttpResponseRedirect(reverse('lose'))
            elif s['sticks_total'] == 1:
                s['win'] += 1
                s['start_game'] = True
                return HttpResponseRedirect(reverse('win'))

            s['player2_taken'] = randint(1, 3)
            while s['player2_taken'] > s['sticks_total']:
                s['player2_taken'] = randint(1,3)

            s['sticks_in_game_2'] = s['sticks_total']
            s['sticks_total'] -= s['player2_taken']

            if s['sticks_total'] == 0:
                s['win'] += 1
                s['start_game'] = True
                return HttpResponseRedirect(reverse('win'))
            elif s['sticks_total'] == 1:
                s['lose'] += 1
                s['start_game'] = True
                return HttpResponseRedirect(reverse('lose'))
        else:
            return HttpResponseRedirect(reverse('more_sticks'))
    else:
        return HttpResponseRedirect(reverse('bad_sticks'))
    
    return HttpResponseRedirect(reverse('start_game'))


def bad_sticks_view(request):
    s = request.session
    return render(request, 'bad_sticks.html',
                  context=dict(sticks_total=s['sticks_total'],
                               win=s['win'],
                               lose=s['lose']))


def more_sticks_view(request):
    s = request.session
    return render(request, 'more_sticks.html',
                  context=dict(sticks_total=s['sticks_total'],
                               win=s['win'],
                               lose=s['lose']))


def win_view(request):
    s = request.session
    try:
        if s['sticks_total'] == 0:
            return render(request, 'win.html',
                          context=dict(taken=s['player2_taken'],
                                       sticks_total=s['sticks_in_game_2'],
                                       sticks=s['sticks_total']))
        elif s['sticks_total'] == 1:
            return render(request, 'win.html',
                          context=dict(taken=s['player1_taken'],
                                       sticks_total=s['sticks_in_game'],
                                       sticks=s['sticks_total']))
        else:
            return HttpResponseRedirect(reverse('start_game'))
    except KeyError:
        return HttpResponseRedirect(reverse('please'))


def lose_view(request):
    s = request.session
    try:
        if s['sticks_total'] == 0:
            return render(request, 'lose.html',
                          context=dict(taken=s['player1_taken'],
                                       sticks_total=s['sticks_in_game'],
                                       sticks=s['sticks_total']))
        elif s['sticks_total'] == 1:
            return render(request, 'lose.html',
                          context=dict(taken=s['player2_taken'],
                                       sticks_total=s['sticks_in_game_2'],
                                       sticks=s['sticks_total']))
        else:
            return HttpResponseRedirect(reverse('start_game'))
    except KeyError:
        return HttpResponseRedirect(reverse('please'))


def please_start(request):
    return render(request, 'please_start_game.html')