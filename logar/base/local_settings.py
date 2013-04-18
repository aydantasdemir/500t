DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'logar', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'yemre', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = 's@5-y*s-xdaxvz3wohbwytyq&amp;i$-tb=(r)(j^dyorc-(0+j-d)'

TWITTER_CONSUMER_KEY = "tLvFIkrUBqQK6FXfQldcgQ"
TWITTER_CONSUMER_SECRET = "UIctp6sdZPNZvCo6DQW9rTHr1U6gw0avDJt5quEqWM"

SOCIAL_AUTH_UID_LENGTH = 222
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 200
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 135
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 125


