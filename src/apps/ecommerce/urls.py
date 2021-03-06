from django.urls import path

from .views import (
    HomeView,
    AboutView,
    PostListView,
    ContactView,
    ProductsView,
    ProductView,
    CartView,
    OrderCreate,
    payment_preview,
    orders_view,
    single_post_view,
    create_comment_view,
    AgentsView,
    AgentProfileView,
    PropertiesView,
    PropertyDetailView,
)

app_name = "ecommerce"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("acerca-de/", AboutView.as_view(), name="about"),
    path("blog/", PostListView.as_view(), name="posts_list"),
    path("contacto/", ContactView.as_view(), name="contact"),
    path("productos/", ProductsView.as_view(), name="products"),
    path("agentes/", AgentsView.as_view(), name="agents"),
    path("agentes/<pk>", AgentProfileView.as_view(), name="agent_profile"),
    path("propiedades/", PropertiesView.as_view(), name="properties"),
    path("propiedades/<pk>", PropertyDetailView.as_view(), name="property_detail"),
    path("productos/<str:id>", ProductView.as_view(), name="product"),
    path("carrito/", CartView.as_view(), name="cart"),
    path("pago/", OrderCreate.as_view(), name="payment_preview"),
    path("payment/<str:pk>", payment_preview, name="order_preview"),
    path("pedidos/", orders_view, name="orders"),
    path("blog/<str:slug>", single_post_view, name="post_single"),
    path("comment/<int:post_id>", create_comment_view, name="comment")
]
