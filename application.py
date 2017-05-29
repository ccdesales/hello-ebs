from flask import Flask
application = Flask(__name__)


@application.route('/hello')
def hello_world():
    lang = os.getenv('SITE_LANG', 'EN')

    if lang == 'DE':
        return 'Hallo, Welt!'

    return 'Hello, World!'


@application.route('/health', methods=['POST', 'GET'])
def health():
    return 'OK'


@application.route('/send_message/<name>')
def send_message(name='friend'):
    # Get the service resource
    sqs = boto3.resource('sqs', region_name='eu-west-1',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )

    # Get the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName='hello-sqs-queue')
    response = queue.send_message(MessageBody=name)

    return (
        '<p>Message sent: %s!</p>\n'
        'Response: %s'
    ) % (name, response)


if __name__ == "__main__":
    application.debug = True
    application.run()
