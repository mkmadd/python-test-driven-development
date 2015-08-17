from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

# MKM: added key and port variables
KEY = '../../mkmadd-key-pair-aws-useast.pem'
PORT = '2244'

def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            '-i{}'.format(KEY),    # add key for ssh authentication
            '--port={}'.format(PORT),   # add non-22 port
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()

def reset_database(host):
    subprocess.check_call(
        [
            'fab',
            '-i{}'.format(KEY),    # add key for ssh authentication
            '--port={}'.format(PORT),   # add non-22 port
            'reset_database',
            '--host={}'.format(host),
        ],
        cwd=THIS_FOLDER
    )
