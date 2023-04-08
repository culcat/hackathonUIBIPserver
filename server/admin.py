from django.contrib import admin
from .models import *

admin.site.register(Direction)
admin.site.register(Candidate)
admin.site.register(Status)
admin.site.register(Target)
admin.site.register(Questtion)
admin.site.register(UserAnswer)
admin.site.register(APIKey)