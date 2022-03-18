# The purpose of this file is to hold sensitive information that you don't want to 
# post publicly to GitHub.  This file is excluded from being sent to github by .gitignore

def getSecrets():
    secrets = {
        'MAIL_PASSWORD':'<password_to_gmail_account>',
        'MAIL_USERNAME':'<gmail_address>',
        'MONGO_HOST':'mongodb+srv://admin:bulldogs@cluster0.vp6an.mongodb.net/Capstone?retryWrites=true&w=majority',
        'MONGO_DB_NAME':'Capstone'
        }
    return secrets
