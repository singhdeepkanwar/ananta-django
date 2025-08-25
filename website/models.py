# website/models.py

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class CaseStudy(models.Model):
    # e.g., "Logistics & Supply Chain"
    tag = models.CharField(max_length=100)
    
    # e.g., "Optimized Fleet Routing for Global Shipper"
    title = models.CharField(max_length=200)

    # An image file that you can upload from the admin panel
    image = models.ImageField(upload_to='case_studies/')

    # Longer text fields for the main content
    challenge = models.TextField()
    solution = models.TextField()
    
    # We'll store the list of results as a single block of text
    results = models.TextField(help_text="List each result on a new line.")

    # This is how the object will be named in the admin panel
    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Storing the SVG path or class name is often better than the whole SVG
    icon_svg_path = models.TextField(blank=True, help_text="Paste the SVG <path> data here.")
    # For more detailed lists on the services page
    key_benefits = models.TextField(blank=True, help_text="List each benefit on a new line.")

    def __str__(self):
        return self.title
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    headshot = models.ImageField(upload_to='team/')
    # For ordering members on the page
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

# website/models.py

class Testimonial(models.Model):
    quote = models.TextField()
    author_name = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100)
    # Making the image optional
    author_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    # To show only one featured testimonial on the homepage
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f'"{self.quote[:30]}..." - {self.author_name}'

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True) # Optional field
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} on {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    # The 'slug' is the URL-friendly version of the title
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=100) # Or ForeignKey to a User model
    
    # Use RichTextField instead of a normal TextField for the body
    body = RichTextField()
    
    publish_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # An optional image for the post listing
    featured_image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    class Meta:
        ordering = ['-publish_date'] # Show newest posts first

    def __str__(self):
        return self.title