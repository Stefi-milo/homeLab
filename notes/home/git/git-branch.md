# Creating new branch
git branch lifemetric

# Switching to the branch
git checkout lifemetric


**LetterMeaning : **

D Deleted
M Modified
A Added
R Renamed
C Copied
? Untracked



# Pushing the new branch to repository
git push --set-upstream origin lifemetric

# Pushing to that branch
git push origin lifemetric

# Pushing changes from branch to master
git checkout main
git pull origin main
git merge lifemetric
git push origin main
