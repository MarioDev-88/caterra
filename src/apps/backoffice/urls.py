from django.urls import path


from .views import (
    DasboardView,
    SliderListView,
    SliderCreateView,
    SliderUpdateView,
    SliderDeleteView,
    VideoUpdateView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    # EditorUserListView,
    # AgenteUserListView,
    # AdminListView,
    UserListView,
    UserDeleteView,
    UserDetailView,
    UserUpdateView,
    register_user,
    # UserCreateView,
    PropiedadListView,
    PropiedadCreateView,
    PropiedadDeleteView,
    PropiedadUpdateView,
    AgenteListView,
    register_agente,
    AgenteDetailView,
    AgenteDeleteView,
    AgenteUpdateView,
)

app_name = "backoffice"

urlpatterns = [
    path("sliders", SliderListView.as_view(), name="sliders"),
    path("sliders/crear", SliderCreateView.as_view(), name="sliders_create"),
    path("sliders/<int:pk>/actualizar", SliderUpdateView.as_view(), name="sliders_update"),
    path("sliders/<int:pk>/delete", SliderDeleteView.as_view(), name="sliders_delete"),
    path("video/", VideoUpdateView.as_view(), name="video"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/crear", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/actualizar", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("usuarios", UserListView.as_view(), name="users"),
    # path("usuarios/agentes", AgenteUserListView.as_view(), name="users_agentes"),
    # path("usuarios/administradores", AdminListView.as_view(), name="users_admins"),
    path("usuarios/<int:pk>/delete", UserDeleteView.as_view(), name="users_delete"),
    path("usuarios/<int:pk>", UserDetailView.as_view(), name="users_details"),
    path("usuarios/<int:pk>/actualizar", UserUpdateView.as_view(), name="users_update"),
    path("usuarios/crear", register_user, name="users_create"),
    path("propiedades/", PropiedadListView.as_view(), name="propiedades"),
    path("propiedades/crear", PropiedadCreateView.as_view(), name="propiedades_create"),
    path("propiedades/<int:pk>/delete", PropiedadDeleteView.as_view(), name="propiedades_delete"),
    path("propiedades/<int:pk>/actualizar", PropiedadUpdateView.as_view(), name="propiedades_update"),
    path("agentes/", AgenteListView.as_view(), name="agentes"),
    path("agentes/crear",register_agente, name="agentes_create"),
    path("agentes/<int:pk>/delete", AgenteDeleteView.as_view(), name="agentes_delete"),
    path("agentes/<int:pk>", AgenteDetailView.as_view(), name="agentes_details"),
    path("agentes/<int:pk>/actualizar", AgenteUpdateView.as_view(), name="agentes_update"),
    path("", DasboardView.as_view(), name="dashboard"),
]
