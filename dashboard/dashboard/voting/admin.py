from django.contrib import admin
from voting.models import Line, Clip, Emotion

# Register your models here.
admin.site.register(Line)
admin.site.register(Clip)
admin.site.register(Emotion)