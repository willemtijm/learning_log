from django.conf.urls import url
from . import views

app_name = 'learning_log'

urlpatterns = [
    # Home page
    url(r'^$',  views.index, name='index'),
    #Show all topics
    url(r'^topics/$',  views.topics, name='topics'),
    #Detail pages
    url(r'^topics/(?P<topic_id>\d+)',  views.topic, name='topic'),
    
]