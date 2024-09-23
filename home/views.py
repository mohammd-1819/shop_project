from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from product.models import Product
from blog.models import Post
from .forms import ContactUsForm
from .models import ContactUs

class HomeView(View):
    def get(self, request):
        featured_products = Product.objects.all()[:3]
        new_product = Product.objects.all().order_by('-created_at')[:4]
        inspired_products = Product.objects.all()[:4]
        latest_blogs = Post.objects.all().order_by('-created_at')[:3]
        return render(request, 'home/home.html', {'featured_products': featured_products, 'new_products': new_product,
                                                  'inspired_products': inspired_products, 'latest_blogs': latest_blogs})


class ContactUsView(FormView):
    template_name = 'home/contact.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form_data = form.cleaned_data
        ContactUs.objects.create(**form_data)

        return super().form_valid(form)



