pip install Django

pip install djangorestframework


在项目的settings.py中，加入下面的代码

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # os.path.join(APP_PATH, '/dj_news_classification/static').replace('\\', '/'),
    os.path.join(BASE_DIR, 'static'),
)


ALLOWED_HOSTS = ['*']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], // 这样TEMPLATES中的html才能用
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework' //用该框架的话，加入
]# Based_Django_WechatApp_news_classification
