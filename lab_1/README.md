# Lab 1

1. I have run `git clone git@github.com:dhdhxji/lpnu_devops_course.git` to get a local copy of the repository from remote (this Github repo).
2. to get the last commit hash I used the git hist command (alias of git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short). The previous hash is aa87f7f
3. Changes do not appear in the `master` branch because they stored in a separated `branching` branch and did not merge yet.
4. To create a new branch git br "branching" was used (alias of git branch). To go over a newly-created branch I have used a git co branching (alias for git checkout). 
5. Merge conflict has appeared because both changes in `README.md` was in a single place of separated branches (have shared ancestor but these commit objects are different), so, git has no idea how to deal with and transfers control to us.
6. Some changes from GitHub web editor
7. To retrieve changes from the remote I have used the `git pull origin master` command.