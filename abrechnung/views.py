from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Rechnung
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import RechnungForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

@login_required
def rechnung_list(request):
    rechnungen = Rechnung.objects.all()
    return render(request, 'abrechnung/rechnung_list.html', {'rechnungen': rechnungen})

@login_required
def rechnung_delete(request, pk):
    instance = get_object_or_404(Rechnung, pk=pk)
    instance.delete()
    return HttpResponseRedirect('/abrechnung/abrechnungen/')

@login_required
def rechnung_new(request):
    if request.method == "POST":
        form = RechnungForm(request.POST)
        if form.is_valid():
            Rechnung = form.save(commit=False)
            Rechnung.author = request.user
            Rechnung.save()
            return redirect('rechnung_list')
    else:
        form = RechnungForm()
    return render(request, 'abrechnung/rechnung_edit.html', {'form': form})