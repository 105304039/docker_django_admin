# from django.contrib.auth.management.commands import createsuperuser
# from django.core.management import CommandError
from django.contrib.auth.models import User
import argparse



# from django.contrib.auth import get_user_model

if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    parser = argparse.ArgumentParser(description="Change superuser's password",\
                                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--username", help="Superuser name")
    parser.add_argument("-p", "--password", help="Superuser password")
    args = parser.parse_args()
    config = vars(args)
    super_user = User.objects.get(username=config["username"])
    super_user.set_password(config["password"])
    super_user.save()
    