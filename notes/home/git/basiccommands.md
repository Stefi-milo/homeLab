
```sh
cat /etc/os-release

sudo apt-get install git -y

git version

git show

  (show various types of objects)

git branch

  (to list, create or delete branches)

git pull

  (copies changes from a remote repository directly into your working directory)

git pull --rebase

  (there will be one linear commit line, no side branch commit history)

git rebase --abord

  (if you get merge conflict, do it and git pull after to fix the conflict)

git fetch

  (only copies changes into your local Git repo, GIT MERGE to pull it to Work repo)

  (to download locally OBJECTS like commits, files ext from another repo, to see others work)
  
git init

  (to initialize new repo, or start a working area)

git init --bare

  (start bare new empty repo)

git help

git add .

  (adding changes to STAGING DIR )

git config user.email sarah@example.com

git config user.name sarah

echo notes.txt >> .gitignore .

  (.gitignore tells git which file or folder to ignore in repo)

git commit -i -m "Increase time from 400 to 500" .

  (-i -m to add and commit in one step)

git log
	(commit 00c95d977e25671a30bfbd0c58d3be78e628d192 (HEAD -> master)
	
git log --oneline
	(to display log in one line)

git log --name-only
	(It will also list the changed files)

git log -n 3
	(to view last 3 commits)

BRANCH - means a pointer to the the specific git commit

git checkout -b /story/frog

	(it creates and switch to the newly created branch)

git checkout
	(switching bwetween branches)

git commit --amend
	(it will in text editor allow you to edit the commited message)

git log --graph 
	(to see previous commit history along with the branch they were committed on)
	
```
