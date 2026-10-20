from django.views.generic import TemplateView 
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from accounts.forms import AvailabilityForm

# Class based homepage view
class HomePageView(TemplateView): 
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = get_user_model().objects.values(
            "username",
            "course",
            "name",
            "day",
            "hours",
        )

        if self.request.user.is_authenticated:
            context["availability_form"] = AvailabilityForm(
                instance=self.request.user
            )

        return context
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        form = AvailabilityForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("home")

        context = self.get_context_data(**kwargs)
        context["availability_form"] = form
        return self.render_to_response(context)

# Class based view for TA pages
class TAProfileView(TemplateView):
    template_name = "pages/ta_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ta"] = get_object_or_404(
            get_user_model(),
            name=self.kwargs["name"],
        )
        return context