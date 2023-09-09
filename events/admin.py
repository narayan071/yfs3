from django.contrib import admin
from .models import LiveEvents,CorporateWorkshops,PastEvents
# Register your models here.

admin.site.register(LiveEvents)
admin.site.register(CorporateWorkshops)
admin.site.register(PastEvents)
