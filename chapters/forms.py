from . import models
from django import forms

class NewChapterForm(forms.ModelForm):
    class Meta:
        model = models.NewChapterApplication
        exclude = ['selected', 'send_email', 'user', 'applied_at']
        help_texts = {
            'institution_name': ('Enter the name of the institute'),
            'email': ('Mention your emailID here'),
            'year': ('Which year/standard are you in currently'),
            'define_sdg': ('Define sustainable development goals in your own words. Do not write more than 50 words.'),
            'shown_leadership': ('Do you have any leadership experience ?'),
            'leadership_experience': ('Let us know about your leadership experiences if any'),
            'community_service': ('Describe about any of your community service(s) if any'),
            'reasons_for_chapter': ('Why do you want to start a YfS Chapter in your college'),
            'chapter_recognition': ('Do you want your chapter to be recognised by the official administration of your college'),
            'plans_for_chapter': ('What are your plans for your college chapter of YfS'),
            'phone': ('Your contact number'),
            'hours': ('How many hours can you give to YfS per week'),
            'queries': ('Let us know if you have any queries for us'),
        }

    def __init__(self, *args, **kwargs):
        super(NewChapterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            # visible.field.widget.attrs['placeholder'] = visible.field.help_text
