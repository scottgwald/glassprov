from django.contrib import admin
from voting.models import Line, Clip, Emotion, PledgeBreak1, PartyQuirk, PartyQuirk2, PartyQuirk3, Location

# Register your models here.
admin.site.register(Line)
admin.site.register(Clip)
admin.site.register(Emotion)
admin.site.register(PledgeBreak1)
admin.site.register(PartyQuirk)
admin.site.register(PartyQuirk2)
admin.site.register(PartyQuirk3)
admin.site.register(Location)