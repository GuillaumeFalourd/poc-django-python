from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(PostAdmin, self).get_changeform_initial_data(request)
        get_data['created_by'] = request.user.pk
        return get_data

admin.site.register(Post, PostAdmin)
