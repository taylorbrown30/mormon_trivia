# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439164968.075396
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/home.html'
_template_uri = 'home.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        my_turn = context.get('my_turn', UNDEFINED)
        their_turn = context.get('their_turn', UNDEFINED)
        finished_games = context.get('finished_games', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        my_turn = context.get('my_turn', UNDEFINED)
        their_turn = context.get('their_turn', UNDEFINED)
        finished_games = context.get('finished_games', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n<button class="btn btn-lg btn-success btn-block"  id="new_game_button">New Game</button>\r\n\r\n<div class="panel panel-danger">\r\n    <div class="panel-heading">Your Turn</div>\r\n\r\n    <table class="table table-hover" data-show-header="false">\r\n')
        for g in my_turn:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str(g.opponent_game.player.get_full_name()))
            __M_writer('<br/>Round ')
            __M_writer(str(g.current_round))
            __M_writer('</td>\r\n                <td class="score_td you_td">\r\n                    ')

            i = 0
            if g.category_1:
              i += 1
            if g.category_2:
                  i += 1
            if g.category_3:
                  i += 1
            if g.category_4:
                  i += 1
                                
            
            __M_writer('\r\n                    ')

            x = 0
            if g.opponent_game.category_1:
              x += 1
            if g.opponent_game.category_2:
                  x += 1
            if g.opponent_game.category_3:
                  x += 1
            if g.opponent_game.category_4:
                  x += 1
                                
            
            __M_writer('\r\n                    You <br/>')
            __M_writer(str(i))
            __M_writer('\r\n                </td>\r\n                <td class="score_td ">Opponent <br/>')
            __M_writer(str(x))
            __M_writer('</td>\r\n                <td><button  class="btn btn-success play_game_button" id="')
            __M_writer(str(g.id))
            __M_writer('" >Play!</button></td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n</div>\r\n<div class="panel panel-info">\r\n    <div class="panel-heading">Their Turn</div>\r\n    <table class="table table-hover">\r\n')
        for g in their_turn:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str(g.opponent_game.player.get_full_name()))
            __M_writer('<br/>Round ')
            __M_writer(str(g.current_round))
            __M_writer('</td>\r\n                <td class="score_td you_td">\r\n                    ')

            i = 0
            if g.category_1:
              i += 1
            if g.category_2:
                  i += 1
            if g.category_3:
                  i += 1
            if g.category_4:
                  i += 1
                                
            
            __M_writer('\r\n                    ')

            x = 0
            if g.opponent_game.category_1:
              x += 1
            if g.opponent_game.category_2:
                  x += 1
            if g.opponent_game.category_3:
                  x += 1
            if g.opponent_game.category_4:
                  x += 1
                                
            
            __M_writer('\r\n                    You <br/>')
            __M_writer(str(i))
            __M_writer('\r\n                </td>\r\n                <td class="score_td ">Opponent <br/>')
            __M_writer(str(x))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n</div>\r\n<div class="panel panel-success">\r\n    <div class="panel-heading">Finished Games</div>\r\n    <table class="table table-hover">\r\n')
        for g in finished_games:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str(g.opponent_game.player.get_full_name()))
            __M_writer('<br/>Round ')
            __M_writer(str(g.current_round))
            __M_writer('</td>\r\n                <td>\r\n')
            if g.win_loss:
                __M_writer('                        You Won!\r\n')
            else:
                __M_writer('                        You Lost!\r\n')
            __M_writer('                </td>\r\n                <td class="score_td you_td">\r\n                    ')

            i = 0
            if g.category_1:
              i += 1
            if g.category_2:
                  i += 1
            if g.category_3:
                  i += 1
            if g.category_4:
                  i += 1
                                
            
            __M_writer('\r\n                    ')

            x = 0
            if g.opponent_game.category_1:
              x += 1
            if g.opponent_game.category_2:
                  x += 1
            if g.opponent_game.category_3:
                  x += 1
            if g.opponent_game.category_4:
                  x += 1
                                
            
            __M_writer('\r\n                   You <br/>')
            __M_writer(str(i))
            __M_writer('\r\n                </td>\r\n                <td class="score_td ">Opponent <br/>')
            __M_writer(str(x))
            __M_writer('</td>\r\n\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "home.html", "filename": "C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/home.html", "line_map": {"128": 76, "129": 76, "130": 78, "131": 78, "132": 81, "133": 86, "134": 87, "135": 88, "136": 88, "137": 88, "138": 88, "139": 90, "140": 91, "141": 92, "142": 93, "143": 95, "144": 97, "27": 0, "156": 107, "157": 108, "37": 1, "169": 118, "170": 119, "171": 119, "172": 121, "173": 121, "174": 125, "47": 4, "180": 174, "56": 4, "57": 13, "58": 14, "59": 15, "60": 15, "61": 15, "62": 15, "63": 17, "75": 27, "76": 28, "88": 38, "89": 39, "90": 39, "91": 41, "92": 41, "93": 42, "94": 42, "95": 45, "96": 50, "97": 51, "98": 52, "99": 52, "100": 52, "101": 52, "102": 54, "114": 64, "115": 65, "127": 75}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
