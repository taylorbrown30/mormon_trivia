# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439156669.900314
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/win_category.html'
_template_uri = 'win_category.html'
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
        categories = context.get('categories', UNDEFINED)
        game_id = context.get('game_id', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        categories = context.get('categories', UNDEFINED)
        game_id = context.get('game_id', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h3 class="center_text">Choose what to play!</h3>\r\n\r\n<div class="row">\r\n    <div class="col-xs-6">\r\n        <button class="btn btn-lg btn-success btn-block category_button" id="')
        __M_writer(str(categories[0].id))
        __M_writer('" data-game_id="')
        __M_writer(str(game_id))
        __M_writer('"><span class="glyphicon glyphicon-book" aria-hidden="true"></span> ')
        __M_writer(str(categories[0].name))
        __M_writer('</button>\r\n    </div>\r\n    <div class="col-xs-6">\r\n        <button class="btn btn-lg btn-success btn-block category_button" id="')
        __M_writer(str(categories[1].id))
        __M_writer('" data-game_id="')
        __M_writer(str(game_id))
        __M_writer('">')
        __M_writer(str(categories[1].name))
        __M_writer('</button>\r\n    </div>\r\n</div>\r\n<div class="row">\r\n    <div class="col-xs-6">\r\n        <button class="btn btn-lg btn-success btn-block category_button" id="')
        __M_writer(str(categories[2].id))
        __M_writer('" data-game_id="')
        __M_writer(str(game_id))
        __M_writer('">')
        __M_writer(str(categories[2].name))
        __M_writer('</button>\r\n    </div>\r\n    <div class="col-xs-6">\r\n        <button class="btn btn-lg btn-success btn-block category_button" id="')
        __M_writer(str(categories[3].id))
        __M_writer('" data-game_id="')
        __M_writer(str(game_id))
        __M_writer('">')
        __M_writer(str(categories[3].name))
        __M_writer('</button>\r\n    </div>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/win_category.html", "line_map": {"64": 12, "65": 12, "66": 12, "67": 12, "68": 17, "69": 17, "70": 17, "71": 17, "72": 17, "73": 17, "74": 20, "75": 20, "76": 20, "77": 20, "78": 20, "79": 20, "85": 79, "27": 0, "36": 1, "41": 25, "47": 3, "55": 3, "56": 9, "57": 9, "58": 9, "59": 9, "60": 9, "61": 9, "62": 12, "63": 12}, "uri": "win_category.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
