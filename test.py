from git import Repo
import os
from os import listdir
from os.path import isfile, join

repo_dir = os.path.dirname(os.path.realpath(__file__)) 
repo = Repo(repo_dir)
file_list = [f for f in listdir(repo_dir) if isfile(join(repo_dir, f))] 

commit_message = 'Test GitPython'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
