import os
import sys

"""
You need to have a valid SSH key added to your GitHub account
This key serves as a fingerprint and password authentication is skipped while pushing code

For running LazyGit -
3 system arguements are required
First one has to be file name ie lazy_git.py
Second one has to be checkout_directory 
Third one has to be local repo_name
"""

#Keywords
git_remote_command = 'git remote set-url origin git@github.com:'
slash = "/"
git = ".git"

#Edit the 2 keywords below
git_username = 'mayank26saxena' #Replace with your user name here
git_reponame = 'LazyGit' #Replace with repo name which you have used on github

#URL for configuring push access using ssh
url = git_remote_command + git_username + slash + git_reponame + git

def main():
    if len(sys.argv) != 3 :
        print 'Enter 3 arguements'
    else :
        checkout_dir = sys.argv[1]
        repo_name = sys.argv[2]
        commit_msg = raw_input('Write your commit message: ')

	#Path to local repository
        path =  checkout_dir + '/' + repo_name + '/'
        
        os.chdir('%s' %path)

        os.system('pwd')
        
	#Check whether git has been initialised in directory
        n = os.system('git rev-parse')
        print n 
        
	#If n == 0 git has been initialised already	
	#If n != 0 initialise git and add remote repo URL
        if n != 0 :
            os.system('pwd')
            os.system('git init')
            os.system('git remote add origin https://github.com/' + git_username + slash + git_reponame + git)
            os.system(url)
            
        txt = """#!/bin/sh

GIT_WORK_TREE = %s git checkout -f""" % path

	#Run git add, commit, push
        os.system('git add -A')
        os.system('git commit -m \'' + commit_msg + '\'')
        os.system('git push origin master')

if __name__ == "__main__" :
    main()
