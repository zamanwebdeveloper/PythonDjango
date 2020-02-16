from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = "index.html"
	name = "Syed Zaman"
	country = "Bangladesh"
	list = [1,2,3,4,5]

class AboutView(TemplateView):
	template_name = "about.htlml"

	# def get_context_data(self, **kwargs):
 #        context = super().get_context_data(**kwargs)
    
	# 	 	list = [1,2,3,4,5]
	# 	 	context['list'] = list

 #        return context