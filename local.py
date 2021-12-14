# This is the file you run from your computer. local.py is setup to 
# be what you run when you are running the app on your computer. Main.py 
# is what you would run from a server. The cert.pem and key.pem files enable 
# the app to fake being secure when run on your computer.

from app import app
import os

if __name__ == "__main__":
    
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    
    #app.run(debug="True", ssl_context='adhoc')
    app.run(debug="True", ssl_context=('cert.pem', 'key.pem'))
