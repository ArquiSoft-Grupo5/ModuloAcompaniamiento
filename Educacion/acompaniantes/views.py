from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import AcompanianteForm
from .logic.acompaniante_logic import get_acompaniantes, get_acompaniante, create_acompaniante
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def acompaniante_list(request):
    role = getRole(request)
    if role == "Acompaniante":
        acompaniantes = get_acompaniantes()
        context = {
            'acompaniante_list': acompaniantes
        }
        return render(request, 'Acompaniante/acompaniantes.html', context)
    return render(request, 'Acompaniante/acompaniantes.html', context)
    else:
        return HttpResponse("Unauthorized User")
@login_required
def single_acompaniante(request, id=0):
    acompaniante = get_acompaniante(id)
    context = {
        'acompaniante': acompaniante
    }
    return render(request, 'Acompaniante/acompaniante.html', context)

@login_required
def acompaniante_create(request):
    role = getRole(request)
    if role == "Acompaniante":
        if request.method == 'POST':
            form = AcompanianteForm(request.POST)
            if form.is_valid():
                create_acompaniante(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created acompaniante')
                return HttpResponseRedirect(reverse('acompanianteCreate'))
            else:
                print(form.errors)
        else:
            form = AcompanianteForm()

        context = {
            'form': form,
        }
        return render(request, 'Acompaniante/acompanianteCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
