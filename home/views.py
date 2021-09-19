from django.shortcuts import render
from .forms import MessageForm
# Create your views here.
from django.views.generic import TemplateView, FormView

class HomeView(FormView):
    template_name = "home/index.html"
    form_class = MessageForm
    success_url='home'
    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.send_message()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

