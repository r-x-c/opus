
from git import Repo
import subprocess
import logging
import os

def logger():
    FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)


def monitor_progress(git_url, repo_dir):
    logger = logging.getLogger('tcpserver')
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    # logger.warning('Protocol problem: %s', 'connection reset', extra=d)

    if os.path.isdir("./client_dir"):
        logger.info("updating dir for latest version")
        g = git.cmd.Git(repo_dir)
        g.pull()
    else:
        logger.info("downloading dir from website")
        Repo.clone_from(git_url, repo_dir)
    # print(os.path.exists("/home/el/myfile.txt"))
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    result.stdout

if __name__ == '__main__':
    logger()
    git_url, repo_dir = "https://github.com/r-x-c/opus", "client_dir"
    monitor_progress(git_url, repo_dir)
 