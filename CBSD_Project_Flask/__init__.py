from flask import Flask

app = Flask(__name__) #Create an instance of a flask object

app.config['SECRET_KEY']='cop4814' #Password you need for page cookies

from CBSD_Project_Flask import routes  #Import routes from webapp