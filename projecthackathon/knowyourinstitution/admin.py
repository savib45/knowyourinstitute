from django.contrib import admin

from .models import UserProfile
from .models import Review
from .models import College

admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(College)
