from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings

# Create your models here.
class NewChapterApplication(models.Model):

    CHAPTER_RECOGNITION = [
        ('Y', 'Yes'),
        ('N', 'No'),
        ('M', 'Maybe'),
    ]

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

    SHOWN_LEADERSHIP = [
        (True, 'Yes'),
        (False, 'No'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    applied_at = models.DateTimeField(("Applied at"),auto_now_add=True, blank=True)
    institution_name = models.CharField(max_length=200, primary_key=True)
    state = models.CharField(max_length=49, choices = STATES, null=False, default = None)
    city = models.CharField(max_length=100, null = False, default = None)
    first_name = models.CharField(("First Name"), max_length=100, help_text="Enter your first name", null=True)
    last_name = models.CharField(("Last Name"), max_length=100,  help_text="Enter your last name", null=True)
    define_sdg = models.TextField(max_length=250, null=False)
    service = models.TextField(max_length=550, default=None)
    committed = models.TextField(max_length=800, default = None)
    reason_for_chapter = models.TextField(max_length=600)
    chapter_recognition = models.CharField(max_length=5, choices=CHAPTER_RECOGNITION, default='Y')
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=200, null=False, unique=True)
    website = models.CharField(max_length=200, null=True),
    queries = models.CharField(max_length=800)
    selected = models.BooleanField(default=False)
    send_email = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     if self.send_email == True:
    #         if self.selected == True:
    #             mail_body = "Congratulations! and welcome to YfS India, we hope hope to see you in the team ASAP. You have got this magical link to join the group. Caution: Do not share it with anyone."
    #             sendmail("Congratulations! you have have made it to YfS", mail_body, self.name, self.email, "https://wap.me/7008380000/")
    #         else:
    #             mail_body = "Your dreams are endless, and we hope to see you at a better place in the coming days. Sadly, you did not fulfill all the requirements for YfS, but we want you to prove us wrong and show your dedication towards the betterment of the environment."
    #             sendmail("Great things comes to those who don't quit!", mail_body, self.name, self.email, None)

    #     super().save(*args, **kwargs)

    def __str__(self):
        return "New Chapter Form: " + self.institution_name

class AllChapter(models.Model):
    institution_name = models.CharField(max_length=220)
    total_members = models.IntegerField(null=False, default=0)
    chapter_lead = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    established_on = models.DateField(("Chapter Estd. On"),auto_now_add=True)
    def __str__(self):
        return f"{self.institution_name}"
