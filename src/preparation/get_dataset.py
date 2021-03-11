import os
from git import Repo

folders = os.listdir()

if 'data' in folders:
    if os.path.isdir('data/raw/emotion_portuguese_database'):
        print('You already have a folder called emotion_portuguese_database')
    else:
        repo_dir = 'data/raw/emotion_portuguese_database'
        git_url = 'git@github.com:TulioChiodi/emotion_portuguese_database.git'
        Repo.clone_from(git_url, repo_dir)
        print('Dataset downloaded successfully')
else:
    mydir = os.getcwd()
    print('Make sure you are in the root directory of the repository')
    print(f'Current directory: {mydir}')
