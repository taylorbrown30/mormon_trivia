# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439159317.758636
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/question.html'
_template_uri = 'question.html'
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
        game_id = context.get('game_id', UNDEFINED)
        question = context.get('question', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        category_id = context.get('category_id', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        game_id = context.get('game_id', UNDEFINED)
        question = context.get('question', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        category_id = context.get('category_id', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n    <div class="well">\r\n        <div style="display: none;" id="answered_correct" class="center-block message"><img src="')
        __M_writer(str( STATIC_URL))
        __M_writer('trivia/media/text-correct.png"></div>\r\n        <div style="display: none;" id="answered_incorrect" class="message"><img src="')
        __M_writer(str( STATIC_URL))
        __M_writer('trivia/media/text-incorrect.png"></div>\r\n\r\n        <h3>')
        __M_writer(str(question.question))
        __M_writer('</h3>\r\n    </div>\r\n\r\n    <h4><button class="answer_button btn btn-lg btn-default btn-block" game_id="')
        __M_writer(str(game_id))
        __M_writer('" id="a" question="')
        __M_writer(str(question.id))
        __M_writer('" category="')
        __M_writer(str(category_id))
        __M_writer('">')
        __M_writer(str(question.answer_a))
        __M_writer('</button></h4>\r\n    <h4><button class="answer_button btn btn-lg btn-default btn-block" game_id="')
        __M_writer(str(game_id))
        __M_writer('" id="b" question="')
        __M_writer(str(question.id))
        __M_writer('" category="')
        __M_writer(str(category_id))
        __M_writer('">')
        __M_writer(str(question.answer_b))
        __M_writer('</button></h4>\r\n    <h4><button class="answer_button btn btn-lg btn-default btn-block" game_id="')
        __M_writer(str(game_id))
        __M_writer('" id="c" question="')
        __M_writer(str(question.id))
        __M_writer('" category="')
        __M_writer(str(category_id))
        __M_writer('">')
        __M_writer(str(question.answer_c))
        __M_writer('</button></h4>\r\n    <h4><button class="answer_button btn btn-lg btn-default btn-block" game_id="')
        __M_writer(str(game_id))
        __M_writer('" id="d" question="')
        __M_writer(str(question.id))
        __M_writer('" category="')
        __M_writer(str(category_id))
        __M_writer('">')
        __M_writer(str(question.answer_d))
        __M_writer('</button></h4>\r\n    <button style="display: none;" class="btn btn-lg btn-success btn-block" id="continue_button" >Continue</button>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "question.html", "filename": "C:\\Users\\Taylor\\Desktop\\mormon_trivia\\trivia\\templates/question.html", "line_map": {"64": 10, "65": 13, "66": 13, "67": 13, "68": 13, "69": 13, "70": 13, "71": 13, "72": 13, "73": 14, "74": 14, "75": 14, "76": 14, "77": 14, "78": 14, "79": 14, "80": 14, "81": 15, "82": 15, "83": 15, "84": 15, "85": 15, "86": 15, "87": 15, "88": 15, "89": 16, "90": 16, "27": 0, "92": 16, "93": 16, "94": 16, "95": 16, "96": 16, "91": 16, "102": 96, "38": 1, "48": 3, "58": 3, "59": 7, "60": 7, "61": 8, "62": 8, "63": 10}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
