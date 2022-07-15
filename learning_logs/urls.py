from django.conf.urls import url
from . import views

app_name = 'learning_log'

urlpatterns = [
    # Home page
    url(r'^$',  views.index, name='index'),
    #Show all topics
    url(r'^topics/$',  views.topics, name='topics'),
    
]