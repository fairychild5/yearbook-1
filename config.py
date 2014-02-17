#encoding: utf-8
import os

SECRET_KEY = 'you_will_never_guess'

# 这是我的本地数据库配置
#SQLALCHEMY_DATABASE_URI = 'mysql://root:hs1019@localhost/yearbook' 
SQLALCHEMY_DATABASE_URI = os.environ['HEROKU_POSTGRESQL_BRONZE_URL']

# upload files setting
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/static/upload')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# default team, user image path
DEFAULT_TEAM_IMG = '../static/img/default_team.png'
DEFAULT_USER_IMG = '../static/img/default_user.jpg'
