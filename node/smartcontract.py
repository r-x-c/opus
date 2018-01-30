
# from git import Repo
import git
import subprocess
import logging
import os
import sys


def logger():
    """Build logger format."""
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=FORMAT)

def monitor_progress(git_url, repo_dir):
    """Check progress on dog test"""
    logger = logging.getLogger('tcpserver')
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    # logger.warning('Protocol problem: %s', 'connection reset', extra=d)

    if os.path.isdir("./{}".format(repo_dir)):
        logger.info("updating dir for latest version")
        g = git.cmd.Git(repo_dir)
        g.pull()
    else:
        logger.info("downloading dir from website")
        Repo.clone_from(git_url, repo_dir)
    # print(os.path.exists("/home/el/myfle.txt"))
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

    my_file = os.path.join(THIS_FOLDER, '{}/git/file.py'.format(repo_dir))
    print(my_file)

    os.system('python {}'.format(my_file))
    os.system('python -m doctest -v {}'.format(my_file))

    # result = subprocess.check_output(['python {}'.format(my_file)])
    # print(result)

if __name__ == '__main__':
    logger()
    git_url, repo_dir = "https://github.com/r-x-c/opus", "client_dir"
    monitor_progress(git_url, repo_dir)
 