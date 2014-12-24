from django.contrib import admin
import models
# Register your models here.


class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	
admin.site.register(models.Post)