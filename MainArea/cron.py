from background_task import background
from django.contrib.auth.models import User

@background(schedule=1, queue='my-queue')
def WorkerChecker(user_id):
    # lookup user by id and send them a message
    print("Das ist der Crontab")
    #user = User.objects.get(pk=user_id)
    #user.email_user('Here is a notification', 'You have been notified')
