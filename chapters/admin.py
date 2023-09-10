from django.contrib import admin
from .models import NewChapterApplication, JoinChapterApplication, Event, JoinApplication, AllChapter
# Register your models here.


admin.site.register(NewChapterApplication)
admin.site.register(JoinChapterApplication)
admin.site.register(JoinApplication)
admin.site.register(Event)
admin.site.register(AllChapter)