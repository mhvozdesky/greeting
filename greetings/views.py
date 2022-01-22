from django.views.generic.edit import FormView
from .forms import VisitorForm
from django.views.generic import TemplateView


class Greetings(FormView):
    form_class = VisitorForm
    template_name = 'greetings/index.html'

# class Greetings(TemplateView):
#     template_name = 'greetings/index.html'
