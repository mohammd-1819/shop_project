from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Product, Comment, ProductReview


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        return render(request, 'product/product_detail.html', {'product': product})

    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        body = request.POST.get('message')
        review = request.POST.get('review')
        parent_id = request.POST.get('parent_id')
        if review:
            ProductReview.objects.create(text=review, product=product, user=request.user)
        if body:
            Comment.objects.create(text=body, product=product, user=request.user, parent_id=parent_id)

        return render(request, 'product/product_detail.html', {'product': product})


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    paginate_by = 3
    context_object_name = 'products'

    def get_queryset(self):
        request = self.request
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        category = request.GET.get('category')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        queryset = Product.objects.all()

        if colors:
            queryset = queryset.filter(color__title__in=colors).distinct()

        if sizes:
            queryset = queryset.filter(size__title__in=sizes).distinct()

        if category:
            queryset = queryset.filter(category__title__contains=category).distinct()

        if min_price and max_price:
            queryset = queryset.filter(price__lte=max_price, price__gte=min_price).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        request = self.request
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        category = request.GET.get('category')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        context = super(ProductListView, self).get_context_data()
        context['selected_colors'] = colors
        context['selected_category'] = category
        context['selected_sizes'] = sizes
        context['min_price'] = min_price
        context['max_price'] = max_price

        return context


class ProductSearchView(View):
    def get(self, request):
        q = request.GET.get('q')
        products = Product.objects.filter(title__icontains=q)
        paginator = Paginator(products, 2)
        page_number = request.GET.get('page')
        objects_list = paginator.get_page(page_number)
        return render(request, 'product/product_search_result.html', {'products': objects_list})
