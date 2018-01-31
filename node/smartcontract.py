
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

    score = 0
    success, failed = {'value': 0, 'files':[]}, {'value': 0, 'files':[]}
    compensation = 0
    for filePath, reward in files:
        print(filePath, reward)
        my_file = os.path.join(THIS_FOLDER, repo_dir+filePath)
        logger.info("running doctest for {}".format(my_file))
        os.system('python -m doctest -v {}'.format(my_file))
        try:
            f = subprocess.check_output('python -m doctest -v {}'.format(my_file),
                    stderr=subprocess.STDOUT,
                    shell=True)
            score += 1
            success['files'].append(filePath)
            success['value'] += reward
        except subprocess.CalledProcessError:
            logger.info("unit tests do not pass")
            failed['files'].append(filePath)
            failed['value'] += reward

    print(success, failed)
    logger.info("passed {}/{} tests...".format(score, len(files)))
    debrief(logger, success, failed)
    teardown(logger, repo_dir)

def debrief(log, success, failed):
    """Log which projects remain"""
    log.info("client awarded {}, successfully implemented {}".format(
        success['value'], ', '.join(success['files'])
    ))
    log.info("{} were not successfully implemented, bounty of {} remains".format(
         ', '.join(failed['files']), failed['value']
    ))
    
def safe_send(log, value, address):
    """Send reward to user."""
    log.info("sending {} to {}".format(value, address))


def teardown(log, repo_dir):
    log.info("removing dir from repo")
    os.system('rm -rf {}'.format(repo_dir))

if __name__ == '__main__':
    logger()
    config = {'git_url': 'https://github.com/r-x-c/opus',
              'repo_dir' : 'client_dir',
              'files' : [('/git/hw2_python.py', .023), ('/git/file.py', .05)]}

    monitor_progress(config['git_url'], config['repo_dir'], config['files'])
 