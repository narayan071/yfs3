from . import models
from django import forms

class NewChapterForm(forms.ModelForm):
    class Meta:
        model = models.NewChapterApplication
        exclude = ['selected', 'send_email', 'user', 'applied_at']
        help_texts = {
            'institution_name': ('Enter the name of the institute'),
            'city' : ('Enter the location of your institute'),
            'email': ('Mention your emailID here'),
            'define_sdg': ('Define sustainable development goals in your own words. Do not write more than 50 words.'),
            'service': (' List some potential activities, events, or projects your chapter might organize to promote sustainability.'),
            'committed' : (' How committed are you to managing and sustaining the chapter over the long term?'),
            'reasons_for_chapter': ('Why do you want to start a YfS Chapter in your college'),
            'plans_for_chapter': ('How committed are you to managing and sustaining the chapter over the long term?'),
            'chapter_recognition': ('Do you want your chapter to be recognised by the official administration of your college'),
            'phone': ('Your contact number'),
            'queries': ('Let us know if you have any queries for us'),
            'website': ('Enter the link to your chapter website(if available)'),
        }

    def __init__(self, *args, **kwargs):
        super(NewChapterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            # visible.field.widget.attrs['placeholder'] = visible.field.help_text
