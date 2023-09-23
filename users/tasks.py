from users.models import User
from datetime import timedelta, date


def check_active():
    current_date = date.today()
    deactivation_date = current_date - timedelta(days=30)
    users_list = User.objects.filter(last_login__gt=deactivation_date, is_active=True)
    for user in users_list:
        if user.last_login:
            user.is_active = False
