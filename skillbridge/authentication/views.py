from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import FormularioLogin

# Create your views here.
class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        context = {'login_form': FormularioLogin()}
        return render(request, 'login.html', context)

    def post(self, request):
        usuario = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']   
        )
        if usuario is not None:
            login(request, usuario)
            return redirect('index_privado')
        else:
            context = {'error': 'Usuario no encontrado', 'login_form': FormularioLogin()}
            return render(request, 'login.html', context)

@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')