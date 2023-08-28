from .models import Feedback
from django.forms import ModelForm


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ['time']

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.label:
                visible.field.widget.attrs['class'] = 'form-control border border-success'
