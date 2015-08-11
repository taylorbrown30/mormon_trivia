# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439256992.461639
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['navbar', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def navbar():
            return render_navbar(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n<head>\r\n    <meta charset="utf-8">\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1">\r\n\r\n    <title>Mormon Trivia!</title>\r\n\r\n')
        __M_writer('    <script type="text/javascript">if (window.location.hash == \'#_=_\')window.location.hash = \'\';</script>\r\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('trivia/scripts/jquery.min.js"></script>\r\n\r\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('trivia/scripts/bootstrap.min.js"></script>\r\n    <!-- History.js -->\r\n    <script src="//browserstate.github.io/history.js/scripts/bundled/html4+html5/jquery.history.js"></script>\r\n\r\n    <link href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('trivia/styles/bootstrap.min.css" rel="stylesheet">\r\n    <link href=\'http://fonts.googleapis.com/css?family=Rammetto+One\' rel=\'stylesheet\' type=\'text/css\'>\r\n')
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


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "filename": "C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/base.htm", "line_map": {"64": 36, "70": 36, "76": 39, "16": 4, "18": 0, "88": 82, "30": 2, "31": 4, "32": 5, "36": 5, "37": 18, "38": 19, "39": 19, "40": 21, "41": 21, "42": 25, "43": 25, "44": 28, "45": 28, "46": 28, "51": 38, "82": 39, "56": 41, "57": 45, "58": 45}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
