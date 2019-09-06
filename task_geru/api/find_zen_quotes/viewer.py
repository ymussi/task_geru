from flask_restplus import Resource
from flask import request, jsonify
from task_geru.api import api
import logging
import json


log = logging.getLogger(__name__)

ns = api.namespace(
    'quotes', description='Find Zen Quotes')

@ns.route('/')
class Home(Resource):
    @ns.response(code=400, description="Bad Request")
    # @ns.expect(schemaCadastro, validate=True)
    def get(self):
        """
        Return HOME.
        """

        return res

@ns.route('/quotes')
class AllQuotes(Resource):
    @ns.response(code=400, description="Bad Request")
    # @ns.expect(schemaCadastro, validate=True)
    def get(self):
        """
        Return all QUOTES.
        """

        return res

@ns.route('/quotes/<str:quote>')
class OnlyQuote(Resource):
    @ns.response(code=400, description="Bad Request")
    # @ns.expect(schemaCadastro, validate=True)
    def get(self):
        """
        Return all QUOTES.
        """

        return res

@ns.route('/quotes/random')
class RandomQuotes(Resource):
    @ns.response(code=400, description="Bad Request")
    # @ns.expect(schemaCadastro, validate=True)
    def get(self):
        """
        Return all QUOTES.
        """

        return res