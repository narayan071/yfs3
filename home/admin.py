from django.contrib import admin
from .models import Feedback, num_counts, what_we_do
# Register your models here.


admin.site.register(Feedback)
admin.site.register(num_counts)
admin.site.register(what_we_do)