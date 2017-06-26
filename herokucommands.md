
to install heroku CLI


sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install heroku



to log into heroku

heroku login



select the correct heroku git repository

heroku git:remote -a gitclone


to update files to heroku git repository

git add . 
git commit -am "uploading notes and CLI foundation"
git push heroku master






github
git init
git add .
git commit -m "First commit"
git remote add origin https://github.com/jnw216/gitclone.git
git remote -v
git push -u origin master
