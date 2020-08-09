from django.contrib import admin

# Register your models here.
from .models import Policy, Answer

admin.site.register(Policy)
admin.site.register(Answer)
