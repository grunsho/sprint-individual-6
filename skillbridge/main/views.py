from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import RegistroUsuariosForm, RegistroUsuarioStaffForm

# Create your views here.

def index(request):
    return render(request, 'landing.html')

def es_mod(user):
    return user.groups.filter(name='Moderadores').exists()

class UsuariosView(TemplateView):
    template_name = 'usuarios.html'
    
    def get(self, request):
        usuarios = User.objects.all()
        context = {'usuarios': usuarios}
        return render(request, 'usuarios.html', context)

class RegistroUsuariosView(View):
    def get(self, request):
        form = RegistroUsuariosForm()
        context = {'form': form}
        return render(request, 'registro_usuarios.html', context)

    def post(self, request):
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            try:
                usuario = User.objects.create_user(
                    username = request.POST['username'],
                    password = request.POST['password1'],
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    email = request.POST['email']
                )
                usuario.save()
                login(request, usuario)
                return redirect('login')
            except Exception:
                context = {'form': form, 'error': 'El nombre de usuario ya existe'}
                return render(request, 'registro_usuarios.html', context)
        else:
            context = {'form': form }
            return render(request, "registro_usuarios.html", context)

@method_decorator(user_passes_test(es_mod), name='dispatch')
class RegistroUsuarioStaffView(View):
    forma = RegistroUsuarioStaffForm
    def get(self, request):
        form = self.forma()
        return render(request, 'registro_usuarios_staff.html', {'form': form})

    def post(self, request):
        form = self.forma(request.POST)
        if form.is_valid():
            grupo = form.cleaned_data['groups']
            usuario = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1'],
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
            )
            usuario.save()
            usuario.groups.add(grupo)
            grupo_usuario = usuario.groups.first()
            return render(request, 'registro_usuarios_staff.html', {'form': self.forma(), 
                                                                'exito': f'Usuario creado con exito para {usuario.first_name} {usuario.last_name}',
                                                                'usuario_nuevo' : usuario.username,
                                                                'usuario_grupo' : grupo_usuario,
                                                                'usuario_email' : usuario.email})
        return render(request, 'registro_usuarios_staff.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class PrivateIndexView(TemplateView):
    template_name = 'index_privado.html'
    
    def get(self, request):
        return render(request, 'index_privado.html')

    def post(self, request):
        return render(request, 'index_privado.html')