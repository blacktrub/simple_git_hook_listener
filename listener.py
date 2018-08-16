import os
import subprocess
import configparser

from bottle import route, run

PATH = os.path.dirname(os.path.abspath(__file__))
TOKEN = None


@route('/deploy/<token>')
def view(token):
    if token != TOKEN:
        return 'no ok', 403

    subprocess.Popen(os.path.join(PATH, 'deploy.sh'), shell=True)
    return 'ok', 200


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(os.path.join(PATH, 'config.ini'))
    port = config['settings']['port']
    TOKEN = config['settings']['token']

    run(host='localhost', port=port)
