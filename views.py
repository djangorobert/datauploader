from django.shortcuts import render
from datauploader.models import SubmissionForm
from django.views.generic import CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from .models import Submission



class UploadFileView(CreateView):
    form_class = SubmissionForm
    success_url = reverse_lazy('submitted')
    template_name = 'datauploader/upload.html'



class SubmissionListView(ListView):
    model = Submission

    def get_context_data(self, **kwargs):
        context = super(SubmissionListView, self).get_context_data(**kwargs)
        context['subs'] = Submission.objects.all()
        return context

class SubmissionDetailView(DetailView):
    model = Submission
    def get_context_data(self, **kwargs):
        context = super(SubmissionDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def submitted(request):
    templates = 'datauploader/submitted.html'
    context = {}
    return render(request, templates, context)
