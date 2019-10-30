from django.db import models
from datetime import datetime

# Create your models here.

"""
Link to the Field overwiew:
    https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
Some Fields have requirements, but not all
"""

# To get access to the models via the shell, type the following:
#   from userinfo.models import UserInfo
#   UserInfo.objects.get(id=1)
#-> This will display your first object stored in the database
#   Since there is no output format defined, the output will be:
#       <UserInfo: UserInfo object (1)>


class UserInfo(models.Model):
    name     = models.CharField(max_length=120) # max_length = required
    age      = models.DecimalField(decimal_places=0, max_digits=3)
    date     = models.DateTimeField(default=datetime.now, blank=True)
    # blank=True, null=True -> if someone writes no comment, its still fine
    #   blank has to do with how its rendered
    #   null has to do with the database
    comments = models.TextField(blank=False, null=False)
    # Features are documented in https://www.youtube.com/watch?v=F5mRW0jo-U4
    #   view the part "Change a Model"
    # Features are made to add new table columns, without deleting the database
    #   still run 'makemigrations' and 'migrate'
    featured = models.BooleanField(default=True) # null=True, default=True

