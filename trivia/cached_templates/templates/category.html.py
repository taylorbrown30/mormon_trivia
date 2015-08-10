# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439155035.523498
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/category.html'
_template_uri = 'category.html'
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
        opponent = context.get('opponent', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        game_id = context.get('game_id', UNDEFINED)
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
        opponent = context.get('opponent', UNDEFINED)
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        game_id = context.get('game_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="row">\r\n  <div class="col-xs-4"><h3>')
        __M_writer(str(user.get_full_name()))
        __M_writer('</h3></div>\r\n  <div class="col-xs-4"><h3 class="center_text">vs</h3></div>\r\n  <div class="col-xs-4"><h3 class="center_text">')
        __M_writer(str(opponent.get_full_name()))
        __M_writer('</h3></div>\r\n</div>\r\n<div class="row">\r\n  <div class="col-xs-4"><h3 class="center_text"> <i class="fa fa-circle"></i> <i class="fa fa-circle-o"></i> <i class="fa fa-circle-o"></i> <i class="fa fa-circle-o"></i></h3></div>\r\n  <div class="col-xs-4"></div>\r\n  <div class="col-xs-4"><h3 class="center_text"> <i class="fa fa-circle"></i> <i class="fa fa-circle-o"></i> <i class="fa fa-circle-o"></i> <i class="fa fa-circle-o"></i></h3></div>\r\n</div>\r\n<h3 class="center_text">Choose Category</h3>\r\n\r\n<button class="btn btn-lg btn-success btn-block" id="play_button" data-game_id="')
        __M_writer(str(game_id))
        __M_writer('" >Play!</button>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/category.html", "line_map": {"27": 0, "37": 1, "42": 20, "48": 3, "69": 63, "57": 3, "58": 6, "59": 6, "60": 8, "61": 8, "62": 17, "63": 17}, "uri": "category.html"}
__M_END_METADATA
"""
