from . import models
from django import forms
from .models import NewChapterApplication, JoinChapterApplication, Event, JoinApplication, AllChapter

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

class JoinChapterForm(forms.ModelForm):
    institution_name = forms.ModelChoiceField(
        queryset=NewChapterApplication.objects.all(),  # Query only the registered institution names
        empty_label=None,  # Prevent an empty label from appearing in the dropdown
        label='Institution Name',  # Label for the field
    )

    class Meta:
        model = JoinChapterApplication  # Use the JoinChapterApplication model
        exclude = ['selected', 'send_email', 'user', 'applied_at', 'is_core', 'is_volunteer']
        help_texts = {
            'institution_name': ('Are you a student? If yes,mention the name of the institute'),
            'city' : ('Enter the location of your institute'),
            'email': ('Mention your emailID here'),
            'experience': ('Do you have any prior volunteering experience with any non-profit organization?'),
            'committed' : ('How many hours can you devote per day?'),
            'reasons_for_chapter': ('Why do you want to join YfS?'),
            'introduction': ('Who introduced you to YFS?'),
            'expertise': ('What are your expertise?'),
            'phone_number': ('Your contact number'),
        }

    def __init__(self, *args, **kwargs):
        super(JoinChapterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            # visible.field.widget.attrs['placeholder'] = visible.field.help_text


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields =['name', 'date', 'description', 'image']
        help_texts = {
            'date': ('(in format yyyy-mm-dd)'),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != 'date':
                visible.field.widget.attrs['class'] = 'form-control'
                    
        # Specify the widget for the date field
        self.fields['date'].widget = forms.DateInput(attrs={'class': 'form-control'})





class JoinForm(forms.ModelForm):

    class Meta:
        model = JoinApplication 
        exclude = ['selected', 'send_email', 'user', 'applied_at']
        help_texts = {
            'city' : ('Enter the location of your institute'),
            'email': ('Mention your emailID here'),
            'experience': ('Do you have any prior volunteering experience with any non-profit organization?'),
            'committed' : ('How many hours can you devote per week?'),
            'reasons_for_chapter': ('Why do you want to join YfS?'),
            'introduction': ('Who introduced you to YFS?'),
            'expertise': ('What are your expertise?'),
            'phone_number': ('Your contact number'),
        }

    def __init__(self, *args, **kwargs):
        super(JoinForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            # visible.field.widget.attrs['placeholder'] = visible.field.help_text



class AllChapterForm(forms.ModelForm):
    class Meta:
        model = AllChapter
        fields = '__all__' 


class AllChapterEditForm(forms.ModelForm):
    class Meta:
        model = AllChapter
        fields = ['institution_name', 'total_members', 'chapter_lead', 'selected', 'logo']
