
import git
import subprocess
import logging
import os
import sys


def logger():
    """Build logger format."""
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=FORMAT)

def monitor_progress(git_url, repo_dir, files):
    """Check progress on dog test"""
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    # logger.warning('Protocol problem: %s', 'connection reset', extra=d)
    logger = logging.getLogger('tcpserver')

    if os.path.isdir("./{}".format(repo_dir)):
        logger.info("updating dir for latest version")
        g = git.cmd.Git(repo_dir)
        g.pull()
    else:
        logger.info("downloading dir from website")
        git.Repo.clone_from(git_url, repo_dir)
    # print(os.path.exists("/home/el/myfle.txt"))
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

    for f in files:
        my_file = os.path.join(THIS_FOLDER, repo_dir+f)
        print(my_file)
        os.system('python -m doctest -v {}'.format(my_file))
    my_file = os.path.join(THIS_FOLDER, '{}/git/file.py'.format(repo_dir))
    print(my_file)


    # result = subprocess.check_output(['python {}'.format(my_file)])
    # print(result)
    # teardown(logger, repo_dir)


def teardown(logger, repo_dir):
    logger.info("removing dir from repo")
    os.system('rm -rf {}'.format(repo_dir))

if __name__ == '__main__':
    logger()
    config = {'git_url': 'https://github.com/r-x-c/opus',
              'repo_dir' : 'client_dir',
              'files' : ['/git/hw2_python.py', '/git/file.py']}

    monitor_progress(config['git_url'], config['repo_dir'], config['files'])
 