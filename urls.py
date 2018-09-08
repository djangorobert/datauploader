from django.conf.urls import url

from datauploader.views import UploadFileView, SubmissionListView
from datauploader import views
urlpatterns = [



    url(r'^upload/$', UploadFileView.as_view(), name='upload'),
    url(r'^list/$', SubmissionListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)\$', views.SubmissionDetailView.as_view(), name='detail'),
    url(r'^submitted/$', views.submitted, name='submitted'),

]