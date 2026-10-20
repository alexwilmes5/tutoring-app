from django.views.generic import TemplateView 
from django.contrib.auth import get_user_model

class HomePageView(TemplateView): 
    template_name = "home.html"
    
    # Get data for each user/TA
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = get_user_model().objects.values("username", "course", "name", "day", "hours")
        return context
