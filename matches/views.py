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


