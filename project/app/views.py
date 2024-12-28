from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Product, Orders
from .forms import OrdersForm


class BookListView(ListView):


    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self, *args, **kwargs):
        product = self.request.GET.get('title')
        if product:
            product = Product.objects.filter(title=product)
        else:
            product = Product.objects.all()
        return product


class BookCreateView(CreateView):
    model = Product
    template_name = 'book_form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Product
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book-list')


class BookUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')


class BookDetailView(DetailView):
    model = Product
    template_name = 'book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['smile'] = ('🙉')
        return context


def buy(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
    form = OrdersForm()
    return render(request, 'orders.html', context={'form': form})


def orders(request):
    orders = Orders.objects.all()
    return render(request, 'all_orders.html', context={'orders': orders})
