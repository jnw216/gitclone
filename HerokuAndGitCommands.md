
# Install Heroku CLI
* sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
* curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
* sudo apt-get update
* sudo apt-get install heroku



# Log into Heroku
* heroku login

# Select the correct Heroku git repository
* heroku git:remote -a gitclone


# Update files to Heroku git repository
* git add . 
* git commit -am "uploading notes and CLI foundation"
* git push heroku master

# Remote Migration
* heroku config --app APPNAME
* heroku config:set APP_SETTINGS=config.ProductionConfig --app APPNAME
* heroku run python manage.py db init --app APPNAME
* heroku run python manage.py db upgrmigrate ade --app APPNAME
* heroku run python manage.py db upgrade --app APPNAME

# Github Basics
* git init
* git add .
* git commit -m "First commit"
* git remote add origin https://github.com/jnw216/gitclone.git
* git remote -v
## Add to GitHub
* git add .
* git commit -m "First commit"
* git push -u origin master
## Remove from GitHub
* git rm -r --cached FolderName
* git commit -m "Removed folder from repo"
* git push origin master


