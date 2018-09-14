from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import PostModel
from .forms import PostModelForm

def post_model_list_view(request):
	qs = PostModel.objects.all()
	template = "blog/list-view.html"
	context={
		"object_list": qs
	}
	return render(request, template, context)

def post_model_create_view(request):
	template="blog/create-view.html"
	form = PostModelForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		context = {
			"form": PostModelForm()
		}
	return render(request, template, context)

def post_model_detail_view(request, id=None):
	obj = get_object_or_404(PostModel, id=id)
	context = {
		"object": obj
	}
	template = "blog/detail-view.html"
	return render(request, template, context)