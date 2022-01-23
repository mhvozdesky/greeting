from django.views.generic.edit import FormView
from .forms import VisitorForm
from django.urls import reverse_lazy
from .models import Visitor
from django.shortcuts import render
from django.views.generic.list import ListView


class Greetings(FormView):
    form_class = VisitorForm
    template_name = 'greetings/index.html'
    success_url = reverse_lazy("greetings")

    def form_valid(self, form):
        possible_list = Visitor.objects.filter(name=form.cleaned_data['name'],
                                               surname=form.cleaned_data['surname'])

        if len(possible_list) == 0:
            form.save()
            return render(self.request, 'greetings/hello.html', context={
                'name': form.cleaned_data['name']})
        else:
            return render(self.request, 'greetings/our_ friend.html', context={
                'name': form.cleaned_data['name']})


class AllGuests(ListView):
    model = Visitor
    paginate_by = 5
    template_name = 'greetings/list_all.html'
