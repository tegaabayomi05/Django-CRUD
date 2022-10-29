from django.contrib import admin

from songcrud.musicapp.models import Artiste, Lyric, Song

# Register your models here.

admin.site.register(Artiste)
admin.site.register(Lyric)
admin.site.register(Song)
