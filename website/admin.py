# website/admin.py

from django.contrib import admin
from .models import CaseStudy, Service,TeamMember,Testimonial,ContactSubmission,Post

# We can create a custom admin view to auto-generate the slug
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish_date')
    prepopulated_fields = {'slug': ('title',)} # This is the magic line


# Register your models here.
admin.site.register(CaseStudy)
admin.site.register(Service)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(ContactSubmission)
admin.site.register(Post, PostAdmin)