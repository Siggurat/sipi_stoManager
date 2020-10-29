class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

    SECRET_KEY = 'super secret key'
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = "sha256_crypt"

    # !!!
    # Uncomment it if you want to use Mail
    # !!!

    # MAIL_SERVER = 'localhost'
    # MAIL_PORT = 25
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True
    # MAIL_USERNAME = 'example@example.com'
    # MAIL_PASSWORD = '**************'
    # MAIL_DEFAULT_SENDER = 'example@example.com'


