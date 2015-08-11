# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439252682.593281
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
        their_turn = context.get('their_turn', UNDEFINED)
        my_turn = context.get('my_turn', UNDEFINED)
        your_turn = context.get('your_turn', UNDEFINED)
        finished_games = context.get('finished_games', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        their_turn = context.get('their_turn', UNDEFINED)
        my_turn = context.get('my_turn', UNDEFINED)
        your_turn = context.get('your_turn', UNDEFINED)
        finished_games = context.get('finished_games', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n<button class="btn btn-lg btn-success btn-block"  id="new_game_button">New Game</button>\r\n\r\n')
        if my_turn:
            __M_writer('<div class="panel panel-danger">\r\n    <div class="panel-heading">Your Turn</div>\r\n\r\n    <table class="table table-hover" data-show-header="false">\r\n')
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
            __M_writer('    </table>\r\n</div>\r\n')
        __M_writer('\r\n')
        if your_turn:
            __M_writer('<div class="panel panel-info">\r\n    <div class="panel-heading">Their Turn</div>\r\n    <table class="table table-hover">\r\n')
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
            __M_writer('    </table>\r\n</div>\r\n')
        __M_writer('\r\n')
        if finished_games:
            __M_writer('<div class="panel panel-success">\r\n    <div class="panel-heading">Finished Games</div>\r\n    <table class="table table-hover">\r\n')
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
            __M_writer('    </table>\r\n</div>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "home.html", "filename": "C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/home.html", "line_map": {"134": 79, "135": 80, "136": 80, "137": 82, "138": 82, "139": 85, "140": 88, "141": 89, "142": 90, "143": 93, "144": 94, "145": 95, "146": 95, "147": 95, "148": 95, "149": 97, "150": 98, "151": 99, "152": 100, "153": 102, "154": 104, "27": 0, "38": 1, "167": 115, "48": 4, "179": 125, "180": 126, "181": 126, "182": 128, "183": 128, "184": 132, "185": 135, "58": 4, "59": 9, "60": 10, "61": 14, "62": 15, "63": 16, "64": 16, "65": 16, "66": 16, "67": 18, "79": 28, "80": 29, "92": 39, "93": 40, "94": 40, "95": 42, "96": 42, "97": 43, "98": 43, "99": 46, "100": 49, "101": 50, "102": 51, "103": 54, "104": 55, "105": 56, "106": 56, "107": 56, "108": 56, "109": 58, "121": 68, "122": 69, "191": 185, "166": 114}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
