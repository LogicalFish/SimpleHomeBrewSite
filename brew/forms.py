from django import forms
from .models import Homebrew, Job
from django.core import validators

class createForm(forms.ModelForm):

    jobs = forms.ModelChoiceField(queryset=Job.objects.order_by('name'))
    jobs.label = "Class"

    class Meta:
        model = Homebrew
        exclude = ["user"]
        labels = {
            "title":"Name",
            "summary":"Description",
        }

    # name = forms.CharField(validators=[validators.MaxLengthValidator(26)])
    # summary = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(200)])