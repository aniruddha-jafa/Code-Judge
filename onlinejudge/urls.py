from . import views
from django.conf.urls import url


urlpatterns = [
   url(r'^$', views.index, name="index"),
   url(r'^signup/$', views.signup, name="signup"),
   url(r'^login/$', views.login, name="login"),
   url(r'^problemset/$', views.problemset, name="problemset")
   
]
