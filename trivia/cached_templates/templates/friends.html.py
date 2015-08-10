# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439080548.264082
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/friends.html'
_template_uri = 'friends.html'
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
        friends = context.get('friends', UNDEFINED)
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
        friends = context.get('friends', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n<div class="panel panel-success">\r\n    <div class="panel-heading">Choose a friend</div>\r\n    <table class="table table-hover" id="friends_table">\r\n')
        for f in friends['data']:
            __M_writer('        <tr>\r\n            <td><img src="')
            __M_writer(str(f['picture']['data']['url']))
            __M_writer('" class="profile_pics"></td>\r\n            <td>')
            __M_writer(str(f['name']))
            __M_writer('</td>\r\n            <td><button  class="btn btn-success play_friend_button" id="')
            __M_writer(str(f['id']))
            __M_writer('" >Play!</button></td>\r\n        </tr>\r\n')
        __M_writer('\r\n    </table>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/friends.html", "line_map": {"35": 1, "68": 62, "40": 20, "46": 3, "59": 12, "53": 3, "54": 9, "55": 10, "56": 11, "57": 11, "58": 12, "27": 0, "60": 13, "61": 13, "62": 16}, "uri": "friends.html"}
__M_END_METADATA
"""
