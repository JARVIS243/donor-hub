from django.contrib import admin
from .models import Donor, BloodRequest, ContactMessage

admin.site.register(Donor)
admin.site.register(BloodRequest)
admin.site.register(ContactMessage)