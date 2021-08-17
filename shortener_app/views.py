from django.shortcuts import redirect, render

from shortener_app.models import AliasedUrl
from django.views.generic import CreateView
from django.urls import reverse
from shortener_app.forms import AliasedUrlForm
from django.http import HttpResponse


# Create your views here.
def redirect_view(request, alias):
    try:
        aliased_url = AliasedUrl.objects.get(alias=alias)
        return redirect(aliased_url.url)
    except AliasedUrl.DoesNotExist:
        from django.http import Http404
        raise Http404("There is no such alias")


'''
def get_alias(request):
    form = AliasedUrlForm(request.POST or None)
    if form.is_valid():
        my_url = form.cleaned_data["url"]
        AliasedUrl.objects.create(url=my_url)
        return HttpResponse("IT WORKED")
    return render(
        request,
        template_name="create_alias.html",
        context={"form": form}
    )'''


class AliasCreateView(CreateView):
    #form_class = AliasedUrlForm
    model = AliasedUrl
    template_name = 'create_alias.html'
    fields = ['url']

    def get_success_url(self):
        return f"{reverse('create')}?created_alias={self.object.alias}"
