from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from .models import Note
from .forms import NoteForm

def home(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NoteForm()
    notes = Note.objects.all()
    return render(request, "home.html", {"form": form, "notes": notes})