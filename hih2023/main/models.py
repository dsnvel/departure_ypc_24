from django.db import models
from django.contrib.postgres.fields import ArrayField


from django.contrib.auth.models import User


class UserModel(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    active_events = ArrayField(models.CharField(max_length=100), size=None, blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=30), size=None, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MeetingModel(models.Model):
    # meeting_id = models.AutoField()  # Primary key
    meeting_name = models.CharField(max_length=100)
    begin_date_time = models.DateTimeField()
    place = models.CharField(max_length=100, default='Unknown')
    owner = models.CharField(max_length=100, default='Unknown')
    description = models.TextField()
    remaining_places = models.IntegerField()
    tags = ArrayField(models.CharField(max_length=100), size=None, blank=True, null=True)

    def __str__(self):
        return self.meeting_name


class TagsModel(models.Model):
    # tag_id = models.AutoField()  # Primary key
    name = models.CharField(max_length=100)
    description = models.TextField()
    tag_type = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class DefinedMeeting(models.Model):
    meeting_id = models.CharField(max_length=30, default=-1)
    user_id = models.CharField(max_length=30)

    def __str__(self):
        return self.meeting_id
