from django.shortcuts import render
from django.views.generic import TemplateView

#Create your views here. 


class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)


#About view

class AboutPageView(TemplateView):
	template_name = 'about.html'

	#projects view 

class ProjectsPageView(TemplateView):
	template_name = 'projects.html' 