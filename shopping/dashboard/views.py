from django.shortcuts import render, redirect
from .models import ElectronicItems
from .forms import ElectronicForm
from django.contrib.auth.decorators import login_required


@login_required()
def dashboardView(request):
    return render(request, "dashboard.html")


@login_required()
def add_electronics_items(request):
    form = ElectronicForm()
    if request.method == "POST":
        form = ElectronicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("item")
    template_name = "electronic_form.html"
    context = {"form": form}
    return render(request, template_name, context)


@login_required()
def show_electronics_items(request):
    items = ElectronicItems.objects.all()
    template_name = "items.html"
    context = {"items": items}
    return render(request, template_name, context)
