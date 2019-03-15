from django.conf.urls import url
from . import views

urlpatterns=[
    url('^photos/$',views.welcome,name = 'welcome'),
]


