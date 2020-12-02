from django.shortcuts import render

# Create your views here.
def hashtag(request):
	return render(request, "hashtag.html", {})