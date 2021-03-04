from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .models import Slider, Video, Post, Propiedad
from .forms import SliderForm, VideoForm, PostForm, PropiedadForm
from apps.users.decorators import allowed_users
from apps.users.models import User, Admin, Editor, Agente
from apps.users.forms import CustomUserCreationForm, CustomUserChangeForm, UserCreationForm, UserForm, AgenteForm
from apps.ecommerce.models import Order


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class DasboardView(TemplateView):
    template_name = "backoffice/dashboard.html"


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class SliderListView(ListView):
    template_name = "backoffice/sliders/list.html"
    model = Slider

    def get_context_data(self, **kwargs):
        context = super(SliderListView, self).get_context_data(**kwargs)
        context["title"] = "Sliders"
        context["subtitle"] = "Sliders"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class SliderCreateView(CreateView):
    template_name = "backoffice/sliders/create.html"
    model = Slider
    form_class = SliderForm
    success_url = reverse_lazy("backoffice:sliders")

    def get_context_data(self, **kwargs):
        context = super(SliderCreateView, self).get_context_data(**kwargs)
        context["title"] = "Nuevo Slider"
        context["subtitle"] = "Nuevo Slider"

        return context

    def form_valid(self, form):
        form.is_valid()
        return super().form_valid(form)


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class SliderUpdateView(UpdateView):
    template_name = "backoffice/sliders/update.html"
    form_class = SliderForm
    model = Slider
    success_url = reverse_lazy("backoffice:sliders")

    def get_context_data(self, **kwargs):
        context = super(SliderUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Actualizar Slider"
        context["subtitle"] = "Actualizar Slider"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class SliderDeleteView(DeleteView):
    template_name = "backoffice/sliders/slider_confirm_delete.html"
    model = Slider
    success_url = reverse_lazy("backoffice:sliders")


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class VideoUpdateView(UpdateView):
    template_name = "backoffice/video/update.html"
    form_class = VideoForm
    model = Video
    success_url = reverse_lazy("backoffice:video")

    def get_object(self):
        video = Video.objects.first()

        return video

    def get_context_data(self, **kwargs):
        context = super(VideoUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Video"
        context["subtitle"] = "Actualizar Video"

        return context

@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class PostListView(ListView):
    template_name = "backoffice/posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["title"] = "Blog"
        context["subtitle"] = "Blog"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class PostCreateView(CreateView):
    template_name = "backoffice/posts/create.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("backoffice:posts")

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context["title"] = "Nuevo post"
        context["subtitle"] = "Nuevo post"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class PostUpdateView(UpdateView):
    template_name = "backoffice/posts/update.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("backoffice:posts")

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Actualizar post"
        context["subtitle"] = "Actualizar post"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class PostDeleteView(DeleteView):
    template_name = "backoffice/posts/post-confirm-delete.html"
    model = Post
    success_url = reverse_lazy("backoffice:posts")



@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class UserListView(ListView):
    model = User
    template_name = "backoffice/users/list.html"

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context["title"] = "Usuarios"
        context["subtitle"] = "Usuarios"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class EditorUserListView(ListView):
    model = Editor
    template_name = "backoffice/users/list.html"

    def get_context_data(self, **kwargs):
        context = super(EditorUserListView, self).get_context_data(**kwargs)
        context["title"] = "Usuarios editores"
        context["subtitle"] = "Usuarios editores"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class AgenteUserListView(ListView):
    model = Agente
    template_name = "backoffice/users/list.html"

    def get_context_data(self, **kwargs):
        context = super(AgenteUserListView, self).get_context_data(**kwargs)
        context["title"] = "Usuarios agentes"
        context["subtitle"] = "Usuarios agemtes"

        return context

@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class AdminListView(ListView):
    template_name = "backoffice/users/list.html"
    model = Admin
    login_url = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminListView, self).get_context_data(**kwargs)
        context["title"] = "Usuarios administradores"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class UserDetailView(DetailView):
    template_name = "backoffice/users/details.html"
    model = User
    login_url = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        return super(UserDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["title"] = "Detalles de usuario"

        return context



def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        agente_form = AgenteForm(request.POST, request.FILES)

        if form.is_valid() and agente_form.is_valid():
            user = form.save()
            agente = agente_form.save(commit=False)
            agente.user = user
            agente.save()


            return redirect("backoffice:users_editors")
    
    else:
        form = CustomUserCreationForm()
        agente_form = AgenteForm()
    
    context = {'form' : form, 'agente_form':agente_form, 'title':'Nuevo Usuario', 'subtitle':'Nuevo usuario'}
    return render(request, 'backoffice/users/create.html', context)


class UserCreateView(CreateView):
    template_name = "backoffice/users/create.html"
    model = User
    form_class = CustomUserCreationForm
    agente_form = AgenteForm
    success_url = reverse_lazy("backoffice:users_editors")

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context["title"] = "Nuevo usuario"
        context["subtitle"] = "Nuevo usuario"
        context["agente_form"] = AgenteForm

        return context



class UserUpdateView(UpdateView):
    template_name = "backoffice/users/update.html"
    model = User
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("backoffice:users_editors")

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Actualizar usuario"
        context["subtitle"] = "Actualizar usuario"

        return context


class UserDeleteView(DeleteView):
    template_name = "backoffice/users/user-confirm-delete.html"
    model = User
    success_url = reverse_lazy("backoffice:users_editors")




























# Propiedades
@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class PropiedadListView(ListView):
    template_name = "backoffice/propiedades/list.html"
    model = Propiedad

    def get_context_data(self, **kwargs):
        context = super(PropiedadListView, self).get_context_data(**kwargs)
        context["title"] = "Propiedades"
        context["subtitle"] = "Propiedades"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class PropiedadCreateView(CreateView):
    template_name = "backoffice/propiedades/create.html"
    model = Propiedad
    form_class = PropiedadForm
    success_url = reverse_lazy("backoffice:propiedades")

    def get_context_data(self, **kwargs):
        context = super(PropiedadCreateView, self).get_context_data(**kwargs)
        context["title"] = "Nueva Propiedad"
        context["subtitle"] = "Nueva Propiedad"

        return context

@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class PropiedadDeleteView(DeleteView):
    template_name = "backoffice/propiedades/confirm-delete.html"
    model = Propiedad
    success_url = reverse_lazy("backoffice:propiedades")

@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class PropiedadUpdateView(UpdateView):
    template_name = "backoffice/propiedades/update.html"
    model = Propiedad
    form_class = PropiedadForm
    success_url = reverse_lazy("backoffice:propiedades")

    def get_context_data(self, **kwargs):
        context = super(PropiedadUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Actualizar propiedad"
        context["subtitle"] = "Actualizar propiedad"

        return context

#Agentes
@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class AgenteListView(ListView):
    template_name = "backoffice/agentes/list.html"
    model = Agente

    def get_context_data(self, **kwargs):
        context = super(AgenteListView, self).get_context_data(**kwargs)
        context["title"] = "Agentes"
        context["subtitle"] = "Agentes"

        return context

@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class AgenteCreateView(CreateView):
    template_name = "backoffice/agentes/create.html"
    model = Agente
    form_class = AgenteForm
    success_url = reverse_lazy("backoffice:agentes")

    def get_context_data(self, **kwargs):
        context = super(AgenteCreateView, self).get_context_data(**kwargs)
        context["title"] = "Nuevo Agente"
        context["subtitle"] = "Nuevo Agente"

        return context

def register_agente(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # form.initial['type'] = [2]
        agente_form = AgenteForm(request.POST, request.FILES)

        if form.is_valid() and agente_form.is_valid():
            user = form.save()
            agente = agente_form.save(commit=False)
            agente.user = user
            agente.save()


            return redirect("backoffice:agentes")
    
    else:
        form = CustomUserCreationForm()
        agente_form = AgenteForm()
    
    context = {'form' : form, 'agente_form':agente_form, 'title':'Nuevo agente', 'subtitle':'Nuevo agente'}
    return render(request, 'backoffice/agentes/create.html', context)


@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class AgenteDeleteView(DeleteView):
    template_name = "backoffice/agentes/confirm-delete.html"
    model = Agente
    success_url = reverse_lazy("backoffice:agentes")

@method_decorator(allowed_users(allowed_roles=["ADMIN", "AGENTE", "EDITOR"]), name="dispatch")
class AgenteUpdateView(UpdateView):
    template_name = "backoffice/agentes/update.html"
    model = Agente
    form_class = AgenteForm
    success_url = reverse_lazy("backoffice:agentes")

    def get_context_data(self, **kwargs):
        context = super(AgenteUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Actualizar agente"
        context["subtitle"] = "Actualizar agente"

        return context