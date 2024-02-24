
def main():
    password = os.getenv('EMAIL_PASSWORD')
    email = os.getenv('EMAIL_HOST_USER')
    print(password)
    print(email)
    
if __name__=='__main__':
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    application = get_wsgi_application()
    main()