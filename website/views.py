from django.shortcuts import render
from .models import CaseStudy,Service,Testimonial,TeamMember,ContactSubmission,Post
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect


def home_view(request):
    all_services = Service.objects.all()
    # Find the first testimonial marked as 'featured'
    featured_testimonials = Testimonial.objects.filter(is_featured=True).all()

    context = {
        'active_page': 'home',
        'services': all_services,
        'testimonials': featured_testimonials,
    }
    return render(request, 'index.html', context)

def services_view(request):
    all_services = Service.objects.all() # Fetch services
    context = {
        'active_page': 'services',
        'services': all_services, # Add to context
    }
    return render(request, 'services.html', context)

# ... (other views) ...

def about_view(request):
    team_members = TeamMember.objects.all()
    context = {
        'active_page': 'about',
        'team_members': team_members,
    }
    return render(request, 'about.html', context)

def work_view(request):
    # 1. Get all CaseStudy objects from the database.
    #    The .order_by('-id') will show the newest ones first.
    all_case_studies = CaseStudy.objects.order_by('-id')
    
    # 2. Pass the data to the template in the context dictionary.
    context = {
        'active_page': 'work',
        'case_studies': all_case_studies, # The key 'case_studies' is what we'll use in the HTML
    }
    
    return render(request, 'work.html', context)

def contact_view(request):
    if request.method == 'POST':
        # If the form is submitted, process the data
        form = ContactForm(request.POST)
        if form.is_valid():
            # If the data is valid, save it to the database
            form.save()
            
            # Send an email notification (optional, but recommended)
            try:
                subject = f"New Contact Form Submission from {form.cleaned_data['name']}"
                message_body = f"""
                You have received a new message from your website contact form:

                Name: {form.cleaned_data['name']}
                Company: {form.cleaned_data['company']}
                Email: {form.cleaned_data['email']}

                Message:
                {form.cleaned_data['message']}
                """
                send_mail(
                    subject,
                    message_body,
                    settings.DEFAULT_FROM_EMAIL, # The 'from' address
                    ['deepharrysng@gmail.com'], # The 'to' address - CHANGE THIS!
                    fail_silently=False,
                )
            except Exception as e:
                # Handle potential email errors gracefully
                print(f"Error sending email: {e}")
            
            # Add a success message to be displayed on the next page
            messages.success(request, 'Thank you for your message! We will get back to you shortly.')
            
            # Redirect to the same contact page (or a dedicated 'thank you' page)
            return redirect('contact')
    else:
        # If it's a GET request, just display a blank form
        form = ContactForm()

    context = {
        'active_page': 'contact',
        'form': form,
    }
    return render(request, 'contact.html', context)

def post_list_view(request):
    """View to display a list of all blog posts."""
    all_posts = Post.objects.all()
    context = {
        'active_page': 'insights',
        'posts': all_posts
    }
    return render(request, 'post_list.html', context)

def post_detail_view(request, slug):
    """View to display a single blog post."""
    post = Post.objects.get(slug=slug) # Get the specific post by its unique slug
    context = {
        'active_page': 'insights',
        'post': post
    }
    return render(request, 'post_detail.html', context)