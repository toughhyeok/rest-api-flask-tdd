"""
Hello API Controller
"""
from flask_restx import (
    Resource,
    Namespace,
)


ns_hello = Namespace('Hello')


@ns_hello.route('')
class HelloGet(Resource):

    def get(self):
        """Get string Hello"""

        return "Hello!"
