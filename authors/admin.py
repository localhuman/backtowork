from django.contrib import admin
from .models import Author
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):

    model = Author
    list_display = ('name','handle','email','can_tweet','interests',)


admin.site.register(Author, AuthorAdmin)