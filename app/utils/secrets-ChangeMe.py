# The purpose of this file is to hold sensitive information that you don't want to 
# post publicly to GitHub.  This file is excluded from being sent to github by .gitignore

def getSecrets():
    secrets = {
        'MAIL_PASSWORD':'<password to gmail account>',
        'MAIL_USERNAME':'<gmail account>',
        'MONGO_HOST':'mongodb+srv://<db admin user>:<db admin user pw>@cluster0.8m0v1.mongodb.net/<db name>?retryWrites=true&w=majority',
        'MONGO_DB_NAME':'capstone'
        }
    return secrets