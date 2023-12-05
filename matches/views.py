from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Match
from .forms import MatchForm


def get_matches(request):
    """
    Get all matches
    """
    matches = Match.objects.all()
    template = "matches/matches.html"
    context = {
        "matches": matches,
    }
    return render(request, template, context)


def add_match(request):
    """
    Function to add a new match - if superuser
    """
    if not request.user.is_superuser:
        messages.error(request, "Not authorised. Please try again.")
        return redirect(reverse(get_matches))
    # is superuser - proceed
    form = MatchForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Match added!")
            return redirect(reverse(get_matches))
        messages.error(request, "Error - please try again")
    template = "matches/add_match.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


