from django.contrib import admin
from .models import NewChapterApplication, JoinChapterApplication, Event, JoinApplication
# Register your models here.


admin.site.register(NewChapterApplication)
admin.site.register(JoinChapterApplication)
admin.site.register(JoinApplication)
admin.site.register(Event)