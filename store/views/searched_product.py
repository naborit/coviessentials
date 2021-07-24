from django.shortcuts import render
from store.models.product import Product
from store.models.product import Categories

def searched_products(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        items = Product.objects.filter(name__contains = searched)

        products = None
        categories = Categories.get_all_categories()
        categoryID = request.GET.get('category')
        if (categoryID):
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products();

        return render(request,'searched_product.html',{'searched' : searched ,
                                                       'items' : items,
                                                       'products' : products,
                                                       'categories' : categories})



    #print('welcome: ', request.session.get('name'))
