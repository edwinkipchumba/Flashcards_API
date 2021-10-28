from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    # api
    # url(r'^api/subjects/$', views.Subject.as_view()), # list of subjects
    url(r'^api/subjects/$', views.SubjectList.as_view()), # list of subjects
    url(r'^api/subjects/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view()), # single subject
    url(r'^api/notes/$', views.Notes.as_view()), # list of notes
    url(r'^api/notes/(?P<pk>[0-9]+)/$', views.NotesDetail.as_view()), # single note
    url(r'^api/profiles/$', views.Profile.as_view()), # list of profiles
    url(r'^api/profiles/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()), # single profile
    url(r'^api/users/$', views.Users.as_view()), # list of users
    url(r'^api/users/create/$', views.UserCreate.as_view()), # create user
    url(r'^api/auth/login/$', views.loginUser.as_view()), # login user
    url(r'^api/auth/logout/$', views.logoutUser.as_view()), # logout user
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)