from django.conf.urls import url  
from . import views


urlpatterns = [
	url(r'^index/$', views.HomePageView.as_view(), name='index'),
	url(r'^about/$', views.AboutPageView.as_view(), name='about'),
	url(r'^projects/$', views.ProjectsPageView.as_view(), name='projects'),

]
