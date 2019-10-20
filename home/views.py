# Create your views here.
from django.utils import timezone
from django.views import generic
from .models import Category, Product


class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Category.objects.all()


class DetailView(generic.DetailView):
    template_name = 'product.html'
    model = Category

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Category.objects.all()
