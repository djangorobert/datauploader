from django.db import models
from django.forms import ModelForm
# Create your models here.
class Submission(models.Model):
    PUBLIC = 'Public'
    PRIVATE = 'Private'

    AUDIENCE = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )
    you = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    filename = models.CharField(max_length=150)
    description = models.CharField(max_length=300, help_text='write a description of file')
    timestamp = models.DateTimeField(auto_now=True)
    audience = models.CharField(max_length=8,
                                choices=AUDIENCE)
    file = models.FileField(upload_to='uploads', null=True, blank=True)

    def __unicode__(self):
        return '%s %s' %(self.filename, self.timestamp)



class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['filename', 'description', 'audience', 'file']

