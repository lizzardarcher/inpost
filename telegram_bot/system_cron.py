import os
import time


def crutching():
    os.system('chmod 777 -R /var/www/html/black-dashboard-django-new/core/static/media/')

    # files = os.listdir('/var/www/html/mysite1/slivki_bot/static/images')
    #
    # for file in files:
    #     if '.session' in file:
    #         os.system('cp -n ' + '/var/www/html/mysite1/slivki_bot/static/images/' + file + ' /var/www/html/mysite1/')
    #         print(file, ' copied to /var/www/html/mysite1/')
    #
    #         os.system('chmod 777 -R /var/www/html/mysite1/')
    #
    #         os.system('rm ' + '/var/www/html/mysite1/slivki_bot/static/images/' + file)
    #         print(file, ' deleted from /var/www/html/mysite1/')


while True:
    try:
        crutching()
        time.sleep(15)
    except:
        time.sleep(15)