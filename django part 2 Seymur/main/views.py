from django.shortcuts import render


def home(request):
    """Render the placeholder landing page."""
    return render(request, "index.html")
