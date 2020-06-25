from django.contrib import admin
from .models import Show, Review, Performer

# Register your models here.

admin.site.register(Show)
admin.site.register(Review)
admin.site.register(Performer)
