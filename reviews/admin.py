from django.contrib import admin

# Register your models here.
from reviews.models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'rating', 'author')
    list_filter = ('rating',)

admin.site.register(Review, ReviewAdmin)
