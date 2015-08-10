# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439072957.236789
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['content', 'navbar']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        picture_url = context.get('picture_url', UNDEFINED)
        def navbar():
            return render_navbar(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar'):
            context['self'].navbar(**pageargs)
        

        __M_writer('\r\n')
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
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid"><div class="loading loader"></div>\r\n    <div class="row">\r\n        <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2 col-lg-6 col-lg-offset-3">\r\n\r\n\r\n\r\n            <div class="panel panel-default">\r\n\r\n                <div class="panel-body" id="game_panel">\r\n                    <div class="loader loader_wheel">Loading...</div>\r\n                    <div id="panel_contents">\r\n\r\n                    </div>\r\n                    </div>\r\n                </div>\r\n\r\n        </div>\r\n    </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        picture_url = context.get('picture_url', UNDEFINED)
        def navbar():
            return render_navbar(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div  id="top_bar">\r\n    <div class="container-fluid">\r\n        <div class="row">\r\n            <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2 col-lg-6 col-lg-offset-3">\r\n\r\n                <a class="top_bar_item_left" href="trivia"><img alt="Brand" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('trivia/media/logo.svg" id="brand_image"></a>\r\n                <p class="top_bar_item_left" id="app_title"><a href="trivia" id="app_title_link">Mormon Trivia</a></p>\r\n\r\n')
        if user.is_authenticated():
            __M_writer('\r\n                    <div class="dropdown top_bar_item_right top_bar_text">\r\n                        <a id="name_link" href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">')
            __M_writer(str( user.get_full_name()))
            __M_writer(' <span class="caret"></span></a>\r\n                        <ul class="dropdown-menu">\r\n                            <li></li>\r\n                            <li><a href="#">Help</a></li>\r\n                            <li><a href="#">Account</a></li>\r\n                            <li role="separator" class="divider"></li>\r\n                            <li><a href="/logout/?next=')
            __M_writer(str( request.path ))
            __M_writer('">Logout</a></li>\r\n\r\n                        </ul>\r\n                    </div>\r\n                 <a class="top_bar_item_right"></a><img src="')
            __M_writer(str(picture_url))
            __M_writer('" id="profile_pic"></a>\r\n\r\n')
        else:
            __M_writer('\r\n                <p class="top_bar_item_right top_bar_text"><a href="/login/facebook/?next=')
            __M_writer(str( request.path ))
            __M_writer('">Login with Facebook</a></p>\r\n\r\n')
        __M_writer('            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"67": 2, "77": 2, "78": 8, "79": 8, "80": 11, "81": 12, "82": 14, "83": 14, "84": 20, "85": 20, "86": 24, "87": 24, "88": 26, "89": 27, "90": 28, "91": 28, "92": 31, "98": 92, "27": 0, "40": 1, "45": 36, "55": 37, "61": 37}, "uri": "index.html", "source_encoding": "utf-8", "filename": "C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/index.html"}
__M_END_METADATA
"""
