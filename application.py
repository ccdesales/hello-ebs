from flask import Flask
application = Flask(__name__)


@application.route('/hello')
def hello_world():
    lang = os.getenv('SITE_LANG', 'EN')

    if False and lang == 'DE':
        return 'Hallo, Welt!'

    return 'Hello, World!'


@application.route('/health', methods=['POST', 'GET'])
def health():
    return 'OK'


if __name__ == "__main__":
    application.debug = True
    application.run()
