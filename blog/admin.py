from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author_id','title', 'slug', 'author', 'publish','Status')
    list_filter = ('Status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author')
    
  
    
