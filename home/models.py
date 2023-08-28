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
