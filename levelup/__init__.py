import os
from flask import Flask

def create_app(test_config=None):

    # create and configure the first app here
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'levelup.sqlite'))

    if test_config is None:
        # load instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedir(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'hello, world!'

    return app