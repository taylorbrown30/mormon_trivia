# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439073539.253957
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/new_game.html'
_template_uri = 'new_game.html'
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n\r\n        <h3 class="instructions_heading">Choose an opponent</h3>\r\n\r\n    <div class="row">\r\n        <div class="col-xs-5 col-xs-offset-1">\r\n            <td><button  class="btn btn-lg btn-primary btn-block" id="friends_button" >Friends</button></td>\r\n        </div>\r\n        <div class="col-xs-5 ">\r\n                        <td><button  class="btn btn-lg btn-primary btn-block" id="random_button" >Random</button></td>\r\n\r\n        </div>\r\n    </div>\r\n    <table style="width:100%">\r\n        <tr>\r\n\r\n        </tr>\r\n    </table>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"34": 1, "51": 3, "39": 27, "57": 51, "27": 0, "45": 3}, "uri": "new_game.html", "source_encoding": "utf-8", "filename": "C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/new_game.html"}
__M_END_METADATA
"""
