# This is the file you would run from a server on the internet. local.py is setup to 
# be what you run when you are running the app on your computer.
from app import app
import os

if __name__ == "__main__":
    
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    
    # app.run(debug="True")
    app.run()