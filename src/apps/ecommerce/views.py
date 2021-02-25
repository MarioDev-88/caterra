import os
import json

from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, ListView
from django.core.mail import send_mail

import requests

from apps.backoffice.models import Slider, Video, Post, Comment, Propiedad, Agente
from .models import Order, OrderItem
from apps.users.decorators import allowed_users


class HomeView(View):

    template_name = "ecommerce/home.html"

    def dispatch(self, request, *args, **kwargs):
        self.title = "Caterra"
        self.propiedades = Propiedad.objects.all()
        self.sliders = Slider.objects.all()
        self.video = Video.objects.first()

        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        ctx = {"propiedades": self.propiedades, "sliders": self.sliders, "video": self.video}
        return render(request, self.template_name, ctx)


class AboutView(TemplateView):
    template_name = "ecommerce/about-us.html"

class AgentsView(ListView):
    template_name = "ecommerce/agents.html"
    model = Agente

    def get_context_data(self, **kwargs):
        context = super(AgentsView, self).get_context_data(**kwargs)
        context["title"] = "Agentes"
        context["subtitle"] = "Agentes"

        return context

class PropertiesView(ListView):
    template_name = "ecommerce/properties.html"
    model = Propiedad

    def get_context_data(self, **kwargs):
        context = super(PropertiesView, self).get_context_data(**kwargs)
        context["title"] = "Propiedades"
        context["subtitle"] = "Propiedades"

        return context


class PostListView(ListView):
    template_name = "ecommerce/posts-list.html"
    model = Post
    paginate_by = 2


class ContactView(View):
    template_name = "ecommerce/contact.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST["name"])

        send_mail(
            "Mensaje del sitio Caterra",
            request.POST["subject"],
            request.POST["email"],
            ["272f846743-39d2bf@inbox.mailtrap.io"],
            fail_silently=False,
        )

        return HttpResponseRedirect(reverse("ecommerce:contact"))


class ProductsView(View):

    template_name = "ecommerce/products.html"

    def get(self, request):

        page = request.GET.get("page") or 0
        limit = 12
        offset = round(int(page)) * limit

        if not page:
            offset = 0

        url = "{}/productos?offset={}&limit={}".format(
            os.environ.get("AT_URL"), str(offset), str(limit)
        )
        lines_url = "{}/lineas".format(os.environ.get("AT_URL"))
        sublines_url = "{}/sublineas".format(os.environ.get("AT_URL"))

        if request.GET.get("category") and request.GET.get("category") != "":
            url = "{}&linea={}".format(url, request.GET.get("category"))

        if request.GET.get("price") and request.GET.get("price") == "1":
            url = "{}&precio_max={}".format(url, 999)

        if request.GET.get("price") and request.GET.get("price") == "2":
            url = "{}&precio_min={}&precio_max={}".format(url, 1000, 4999)

        if request.GET.get("price") and request.GET.get("price") == "3":
            url = "{}&precio_min={}&precio_max={}".format(url, 5000, 9999)

        if request.GET.get("price") and request.GET.get("price") == "4":
            url = "{}&precio_min={}&precio_max={}".format(url, 10000, 19999)

        if request.GET.get("price") and request.GET.get("price") == "5":
            url = "{}&precio_min={}".format(url, 20000)

        if request.GET.get("subcategory") and request.GET.get("subcategory") != "":
            url = "{}&sublinea={}".format(url, request.GET.get("subcategory"))

        if request.GET.get("q") and request.GET.get("q") != "":
            url = "{}&q={}".format(url, request.GET.get("q"))

        print(url)

        headers = {"Api-Key": os.environ.get("AT_APIKEY")}

        products = requests.get(url, headers=headers)
        lines = requests.get(lines_url, headers=headers)
        sublines = requests.get(sublines_url, headers=headers)

        x = json.loads(products.text)
        lines = json.loads(lines.text)
        sublines = json.loads(sublines.text)
        total = len(x.get("results"))
        pages = total / limit

        if not request.GET.get("category"):
            pages = x.get("count") / limit

        first_pages = range(int(page) - 3, int(page) + 3)
        last_pages = range(round(pages) - 3, round(pages))

        if total < 10:
            pages = 1
            first_pages = range(int(1), int(page))
            last_pages = range(round(pages), round(pages))

        print(page)

        ctx = {
            "products": x,
            "lines": lines,
            "sublines": sublines,
            "total": total,
            "pages": range(0, round(pages + 1)),
            "category": request.GET.get("category") or None,
            "first_pages": first_pages,
            "last_pages": last_pages,
        }

        return render(request, self.template_name, ctx)


class ProductView(View):
    template_name = "ecommerce/product.html"

    def get(self, request, id):
        code = id or None

        headers = {"Api-Key": os.environ.get("AT_APIKEY")}
        url = "{}/productos?codigo={}".format(os.environ.get("AT_URL"), code)

        print(url)

        product = requests.get(url, headers=headers)

        product = json.loads(product.text)

        ctx = {"product": product.get("results")[0]}

        return render(request, self.template_name, ctx)


class CartView(View):
    template_name = "ecommerce/cart.html"

    def get(self, request):
        return render(request, self.template_name)


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class OrderCreate(View):
    template_name = "ecommerce/payment-preview.html"

    def post(self, request):

        # print(request.POST)

        order_total = 0.00
        shipping = 150.00

        for item in request.POST.getlist("products"):
            parsedItem = json.loads(item)
            headers = {"Api-Key": os.environ.get("AT_APIKEY")}
            url = "{}/productos?codigo={}".format(
                os.environ.get("AT_URL"), parsedItem.get("productId")
            )

            product = requests.get(url, headers=headers)

            product = json.loads(product.text)

            product = product.get("results")[0]

            order_total = order_total + product.get("precio")

        print("Total order: {}".format(order_total))
        order = Order.objects.create(
            info_name="{} {}".format(request.POST.get("name"), request.POST.get("lastname")),
            info_business_name=request.POST.get("company"),
            info_address_1=request.POST.get("address"),
            info_address_2=request.POST.get("neighborhood"),
            info_country=request.POST.get("country"),
            info_state=request.POST.get("state"),
            info_city=request.POST.get("city"),
            info_cp=request.POST.get("cp"),
            info_email=request.POST.get("email"),
            info_phone=request.POST.get("phone"),
            info_comments=request.POST.get("comments"),
            owner=request.user,
            total=order_total + shipping,
            status="PENDING"
        )

        for item in request.POST.getlist("products"):
            parsedItem = json.loads(item)
            print(parsedItem)
            OrderItem.objects.create(
                product_id=parsedItem.get("productId"),
                qty=int(parsedItem.get("qty")),
                order_id=order,
            )

        return HttpResponseRedirect(reverse("ecommerce:order_preview", args=[str(order.order_id)]))


def payment_preview(request, pk):
    order = Order.objects.select_related().get(pk=pk)
    order_items = OrderItem.objects.filter(order_id=pk)

    for item in order_items:
        headers = {"Api-Key": os.environ.get("AT_APIKEY")}
        url = "{}/productos?codigo={}".format(os.environ.get("AT_URL"), item.product_id)

        product = requests.get(url, headers=headers)

        product = json.loads(product.text)

        item.admin_info = product.get("results")[0]
    order.items = order_items
    return render(request, "ecommerce/payment-preview.html", {"order": order})


def orders_view(request):
    orders = Order.objects.filter(owner=request.user)

    for order in orders:
        order_items = OrderItem.objects.filter(order_id=order.order_id)

        for item in order_items:
            headers = {"Api-Key": os.environ.get("AT_APIKEY")}
            url = "{}/productos?codigo={}".format(os.environ.get("AT_URL"), item.product_id)

            product = requests.get(url, headers=headers)

            product = json.loads(product.text)

            item.admin_info = product.get("results")[0]
        order.items = order_items

    print(orders)

    return render(request, "ecommerce/orders.html", {"orders": orders})


def single_post_view(request, slug):
    post = Post.objects.select_related().filter(slug=slug).get()
    comments = Comment.objects.filter(post_id=post.id)

    return render(request, "ecommerce/post-single.html", {"post": post, "comments": comments})


def create_comment_view(request, post_id):

    print(request.POST)

    post = Post.objects.get(pk=post_id)
    comment = Comment.objects.create(name=request.POST.get('name'), email=request.POST.get('email'), content=request.POST.get('content'), post=post)

    print(comment)

    return HttpResponseRedirect(reverse("ecommerce:post_single", args=[post.slug]))
