from django.conf.urls import url
from django.contrib import admin
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.register, name="register"),
    url(r'^user_login/$', views.user_login, name="user_login")
]
