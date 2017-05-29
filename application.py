from flask import Flask
application = Flask(__name__)


@application.route('/hello')
def hello_world():
    return 'Hello, World!'


@application.route('/health', methods=['POST', 'GET'])
def health():
    return 'OK'


if __name__ == "__main__":
    application.debug = True
    application.run()
