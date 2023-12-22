import os
import git
from datetime import datetime
import subprocess
import logging

logging.basicConfig(filename='git_operations.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def get_branches(remote_url):
    command = ["git", "ls-remote", "--heads", remote_url]
    result = subprocess.check_output(command, text=True)
    branches = [line.split("\t")[-1].split("/")[-1] for line in result.splitlines()]
    return branches


def clone_or_update_repo(repo_url, path_to_folder, branch):
    if os.path.exists(path_to_folder):
        logging.info(f"Updating repository: {path_to_folder}")
        repo = git.Repo(path_to_folder)
        origin = repo.remotes.origin
        origin.fetch()
        repo.head.reset(index=True, working_tree=True)
        origin.pull()
    else:
        logging.info(f"Cloning repository: {repo_url} to {path_to_folder}")
        git.Repo.clone_from(repo_url, path_to_folder, branch=branch)


def create_timestamp_file(repo_folder, branch):
    timestamp = datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
    filename = f"{timestamp}_{branch}.txt"
    file_path = os.path.join(repo_folder, filename)

    with open(file_path, 'w') as file:
        file.write(f"Timestamp: {timestamp}\nRepository: {repo_folder}\nBranch: {branch}")

    logging.info(f"Created timestamp file: {file_path}")


def upload_file_to_repo(repo_folder, branch):
    repo = git.Repo(repo_folder)
    index = repo.index
    index.add(['*.txt'])
    index.commit(f"Add timestamp file for branch {branch}")
    origin = repo.remotes.origin
    origin.push()

    logging.info(f"Uploaded timestamp file for branch {branch} to repository: {repo_folder}")


def process_repositories(repo_url_list):
    for repo_url in repo_url_list:
        repo_name = os.path.basename(repo_url.rstrip('.git'))
        branches = get_branches(repo_url)
        for branch in branches:
            path_to_folder = f"{repo_name}/{branch}"
            clone_or_update_repo(repo_url, path_to_folder, branch)
            create_timestamp_file(path_to_folder, branch)
            upload_file_to_repo(path_to_folder, branch)


if __name__ == "__main__":
    repositories = ['https://github.com/TestTaskGitHub/First-Repository.git',
                    'https://github.com/TestTaskGitHub/Second-Repository.git',
                    'https://github.com/TestTaskGitHub/Third-Repository.git']

    logging.info("Logging started")
    process_repositories(repositories)
    logging.info("End of logging")
