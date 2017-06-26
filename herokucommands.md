
to install heroku CLI


sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get install heroku



to log into heroku

heroku login



select the correct heroku git repository

heroku git:remote -a jnw216


to update files to heroku git repository

git add . 
git commit -am "uploading notes and CLI foundation"
git push heroku master

