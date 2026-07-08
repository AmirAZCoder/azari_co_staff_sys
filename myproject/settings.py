# 1. در لیست INSTALLED_APPS اپلیکیشن را اضافه کن:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'accounts', # اپلیکیشن مدیریت کاربران
]

# 2. انتهای فایل تنظیمات ریدایرکت‌ها را مشخص کن:
LOGIN_REDIRECT_URL = '/'      # آدرس پیش‌فرض پنل یا ریشه بعد از ورود موفق
LOGOUT_REDIRECT_URL = 'login' # آدرس بازگشت بعد از خروج کاربر

# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DATABASE_NAME',          # نام دیتابیس شما
        'USER': 'DATABASE_USER',          # نام کاربری دیتابیس
        'PASSWORD': 'DATABASE_PASSWORD',  # رمز عبور دیتابیس
        'HOST': 'YOUR_EXTERNAL_HOST_IP',  # آی‌پی یا آدرس هاست خارجی دیتابیس
        'PORT': '5432',                   # پورت پیش‌فرض پستگرس
    }
}
