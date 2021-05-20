from django.urls import path

# from .views import (
#     HomeView,
#     AboutView,
#     PostListView,
#     ContactView,
#     ProductsView,
#     ProductView,
#     CartView,
#     OrderCreate,
#     payment_preview,
#     orders_view,
#     single_post_view,
#     create_comment_view,
#     AgentsView,
#     AgentProfileView,
#     PropertiesView,
#     PropertyDetailView,
#     DesarrollosView,
# )

from . import views

app_name = "ecommerce"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("acerca-de/", views.AboutView.as_view(), name="about"),
    path("blog/", views.PostListView.as_view(), name="posts_list"),
    path("contacto/", views.ContactView.as_view(), name="contact"),
    path("productos/", views.ProductsView.as_view(), name="products"),
    path("agentes/", views.AgentsView.as_view(), name="agents"),
    path("agentes/<pk>", views.AgentProfileView.as_view(), name="agent_profile"),
    path("propiedades/", views.PropertiesView.as_view(), name="properties"),
    path("propiedades/<pk>", views.PropertyDetailView.as_view(), name="property_detail"),
    path("desarollos/", views.DesarrollosView.as_view(), name="desarrollos"),
    path("desarollos/ambar", views.DesarrollosAmbarView.as_view(), name="desarrollos-ambar"),
    path("desarollos/buenaventura", views.DesarrollosBuenAventuraView.as_view(), name="desarrollos-buenaventura"),
    path("desarollos/hexus", views.DesarrollosHexusView.as_view(), name="desarrollos-hexus"),
    path("desarollos/kinobay", views.DesarrollosKinoBayView.as_view(), name="desarrollos-kinobay"),
    path("desarollos/playas", views.DesarrollosPlayasView.as_view(), name="desarrollos-playas"),
    path("desarollos/puntodelmar", views.DesarrollosPuntaView.as_view(), name="desarrollos-punta"),
    path("desarollos/rancho", views.DesarrollosRanchoView.as_view(), name="desarrollos-rancho"),
    path("desarollos/upday", views.DesarrollosUpdayView.as_view(), name="desarrollos-upday"),
    path("productos/<str:id>", views.ProductView.as_view(), name="product"),
    path("carrito/", views.CartView.as_view(), name="cart"),
    path("pago/", views.OrderCreate.as_view(), name="payment_preview"),
    path("payment/<str:pk>", views.payment_preview, name="order_preview"),
    path("pedidos/", views.orders_view, name="orders"),
    path("blog/<str:slug>", views.single_post_view, name="post_single"),
    path("comment/<int:post_id>", views.create_comment_view, name="comment"),
]
