import os

from django.http import HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from main.models import MeetingModel, UserModel, TagsModel, DefinedMeeting
from internal.services.service import ExecutionService


def index(request: HttpRequest):
    template = 'main/index.html'

    data = {'user': None,
            'meetings_tags': None}

    meetings = list(MeetingModel.objects.all().order_by('begin_date_time').values())
    user = list(UserModel.objects.filter(login='test_2').values())[0]

    service = ExecutionService()

    user_tags = user['tags']
    meetings_tags = service.get_meetings_by_tags(user_tags, list(TagsModel.objects.all().values()), meetings)

    data['user'] = user
    data['meetings_tags'] = meetings_tags
    print(meetings_tags)

    return render(request, template, context=data)


def test(request: HttpRequest):
    '''# Users
    UserModel.objects.create(login='test_1', password='1234', role='guest', active_events=[0, 1, 2],
                              tags=[0, 1, 2])
    UserModel.objects.create(login='test_2', password='1234', role='guest', active_events=[0],
                              tags=[2])
    UserModel.objects.create(login='test_3', password='1234', role='guest', active_events=[1, 2],
                              tags=[0, 2])

    # Meetings
    MeetingModel.objects.create(meeting_name='meeting_1', begin_date_time='2024-11-20 00:00:00',
                         description='description meeting 1', remaining_places='5',
                         tags=[0, 1, 2])
    MeetingModel.objects.create(meeting_name='meeting_2', begin_date_time='2024-11-21 00:00:00',
                         description='description meeting 2', remaining_places='2',
                         tags=[2])
    MeetingModel.objects.create(meeting_name='meeting_3', begin_date_time='2024-11-22 00:00:00',
                         description='description meeting 3', remaining_places='1',
                         tags=[0, 2])

    # Tags
    TagsModel.objects.create(name='#sport', description='sport meetings', tag_type='base', color='red')
    TagsModel.objects.create(name='#science', description='science meetings', tag_type='base', color='yellow')
    TagsModel.objects.create(name='#it', description='it meetings', tag_type='base', color='blue')'''
'''
    # DefinedMeeting
    DefinedMeeting.objects.create(meeting_id=0, user_id=0)
    DefinedMeeting.objects.create(meeting_id=1, user_id=1)
    DefinedMeeting.objects.create(meeting_id=2, user_id=2)

    print("IS OKEY!")'''


def profile_detail():
    pass


def registration_view():
    pass
