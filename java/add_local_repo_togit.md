
## Add a New Remote To Your Git Repo
```
# init git in local repo
git init
git add .
git commit -m "first commit"
# create a remote repo and add remote url to local repo
git branch -M main
git remote add origin <remote_repo_url> # https://github.com/AkhilATC/django-learn-app.git
git push -u origin main

```
