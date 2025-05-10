from django.contrib import admin
from .models import Vote,Post
# Register your models here.


# class PostAdmin(admin.ModelAdmin):
#     list_display  = ('title','url')

admin.site.register(Vote)
admin.site.register(Post,)


