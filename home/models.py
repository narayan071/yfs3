import datetime
from django.db import models
# from django.utils.text import truncatechars

class Feedback(models.Model):
    name = models.CharField(max_length=80, null=True)
    email = models.EmailField(max_length=200, null=True)
    feedback = models.TextField(null=False)
    time = models.DateTimeField("Time submitted", default=datetime.datetime.now, blank=True, null=True)

    # @property
    # def short_feedback(self):
    #     return truncatechars(self.feedback, 100)

    def __str__(self):
        return str(self.email)

class num_counts(models.Model):
    trees = models.IntegerField(default = 157)
    beaches = models.IntegerField(default = 4)
    projects = models.IntegerField(default = 25)
    plastic = models.IntegerField(default = 250)

class what_we_do(models.Model):
    name = models.CharField(max_length=100, default=None, null=False)
    details = models.TextField()
    image = models.ImageField(upload_to="what_do", default=None, null=False)
    url = models.URLField(max_length=200)
    date_created = models.DateField(default=datetime.datetime.now, blank = True, null=True)