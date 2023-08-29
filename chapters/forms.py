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
class JoinChapterApplication(models.Model):

    STATES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    applied_at = models.DateTimeField(("Applied at"),auto_now_add=True, blank=True)
    institution_name = models.CharField(max_length=200)
    state = models.CharField(max_length=49, choices = STATES, null=False, default = None)
    city = models.CharField(max_length=100, null = False, default = None)
    first_name = models.CharField(("First Name"), max_length=100, help_text="Enter your first name", null=True)
    last_name = models.CharField(("Last Name"), max_length=100,  help_text="Enter your last name", null=True)
    committed = models.TextField(max_length=250, null=False)
    introduction = models.TextField(max_length=250, default=None)
    experience = models.TextField(max_length=800, default = None)
    expertise = models.TextField(max_length=800, default = None)
    reasons_for_chapter = models.TextField(max_length=600)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=200, primary_key=True, null=False, unique=True)
    selected = models.BooleanField(default=False)
    send_email = models.BooleanField(default=False)

    def __str__(self):
        return "Join School/College Chapter Form: " + self.first_name + ' ' + self.last_name

