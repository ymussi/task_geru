from flask_restplus import Resource
from flask import request, jsonify
from task_geru.api import api
from task_geru.api.find_zen_quotes.controller import Task
import logging
import json


log = logging.getLogger(__name__)

ns = api.namespace(
    '/', description='Find Zen Quotes')

@ns.route('/')
class Home(Resource):
    @ns.response(code=400, description="Bad Request")
    def get(self):
        """
        Return HOME.
        """
        res = 'Desafio Web 1.0'

        return res

@ns.route('/quotes')
class Quotes(Resource):
    @ns.response(code=400, description="Bad Request")
    def get(self):
        """
        Return Quotes.
        """
        res = Task().get_quotes()

        return res

@ns.route('/quotes/<string:quote_number>')
class Quotes(Resource):
    @ns.response(code=400, description="Bad Request")
    def get(self, quote_number):
        """
        Return Only One Quote.
        """
        res = Task().get_only_quote(int(quote_number))

        return res

@ns.route('/quotes/random')
class Quotes(Resource):
    @ns.response(code=400, description="Bad Request")
    def get(self):
        """
        Return Random Quotes.
        """
        res = Task().get_random_quote()

        return res