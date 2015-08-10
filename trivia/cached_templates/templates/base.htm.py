# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439074308.040334
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['content', 'navbar']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def navbar():
            return render_navbar(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n<head>\r\n\r\n    <title>Mormon Trivia!</title>\r\n\r\n')
        __M_writer('    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('trivia/scripts/jquery.min.js"></script>\r\n\r\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('trivia/scripts/bootstrap.min.js"></script>\r\n    <!-- History.js -->\r\n    <script src="//browserstate.github.io/history.js/scripts/bundled/html4+html5/jquery.history.js"></script>\r\n\r\n    <link href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('trivia/styles/bootstrap.min.css" rel="stylesheet">\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n\r\n</head>\r\n<body>\r\n\r\n<header>\r\n</header>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar'):
            context['self'].navbar(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\nSite content goes here in sub-templates.\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar():
            return render_navbar(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 34, "70": 34, "76": 31, "16": 4, "18": 0, "88": 82, "30": 2, "31": 4, "32": 5, "36": 5, "37": 15, "38": 15, "39": 15, "40": 17, "41": 17, "42": 21, "43": 21, "44": 23, "45": 23, "46": 23, "51": 33, "82": 31, "56": 36, "57": 40, "58": 40}, "uri": "base.htm", "source_encoding": "utf-8", "filename": "C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/base.htm"}
__M_END_METADATA
"""
