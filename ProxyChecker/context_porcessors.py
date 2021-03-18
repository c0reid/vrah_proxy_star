# https://stackoverflow.com/questions/37982412/django-login-from-in-modal-window
from background_task import background
from ProxyChecker.src.checker import checkPROXY_DB
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
defcol = "\033[0m"




def add_my_login_form(request):
    return {
        'login_form': LoginForm(),
    }


#def ProxyWorker(request):
#    checkPROXY_DB(request)
    return print("der Context Proxy worker is starting!")


@background(schedule=10, queue='Proxy-valid')
def notify_user():
    # lookup user by id and send them a message
    #user = User.objects.get(pk=user_id)
    print(blue+"Bachground task from django with schedule")
    #user.email_user('Here is a notification', 'You have been notified')
