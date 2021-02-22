from django.urls import path


from .views import (
    DasboardView,
    SliderListView,
    SliderCreateView,
    SliderUpdateView,
    SliderDeleteView,
    VideoUpdateView,
    MonthOfferListView,
    MonthOfferCreateView,
    MonthOfferUpdateView,
    MonthOfferDeleteView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    EditorUserListView,
    AdminListView,
    SellerListView,
    UserDeleteView,
    UserDetailView,
    UserUpdateView,
    UserCreateView,
    OrderListView,
    OrderDetailView,
    OrderDeleteView
)

app_name = "backoffice"

urlpatterns = [
    path("sliders", SliderListView.as_view(), name="sliders"),
    path("sliders/crear", SliderCreateView.as_view(), name="sliders_create"),
    path("sliders/<int:pk>/actualizar", SliderUpdateView.as_view(), name="sliders_update"),
    path("sliders/<int:pk>/delete", SliderDeleteView.as_view(), name="sliders_delete"),
    path("video/", VideoUpdateView.as_view(), name="video"),
    path("ofertas/", MonthOfferListView.as_view(), name="offers"),
    path("ofertas/crear", MonthOfferCreateView.as_view(), name="offers_create"),
    path("ofertas/<int:pk>/actualizar", MonthOfferUpdateView.as_view(), name="offers_edit"),
    path("ofertas/<int:pk>/delete", MonthOfferDeleteView.as_view(), name="offers_delete"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/crear", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/actualizar", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("usuarios/editores", EditorUserListView.as_view(), name="users_editors"),
    path("usuarios/vendedores", SellerListView.as_view(), name="users_sellers"),
    path("usuarios/administradores", AdminListView.as_view(), name="users_admins"),
    path("usuarios/<int:pk>/delete", UserDeleteView.as_view(), name="users_delete"),
    path("usuarios/<int:pk>", UserDetailView.as_view(), name="users_details"),
    path("usuarios/<int:pk>/actualizar", UserUpdateView.as_view(), name="users_update"),
    path("usuarios/crear", UserCreateView.as_view(), name="users_create"),
    path("pedidos/", OrderListView.as_view(), name="orders_list"),
    path("pedidos/<str:pk>", OrderDetailView.as_view(), name="order_details"),
    path("pedidos/<str:pk>/delete", OrderDeleteView.as_view(), name="order_delete"),
    path("", DasboardView.as_view(), name="dashboard"),
]
