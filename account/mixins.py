from operator import imod
from django.http import Http404

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['title', 'slug', 'author', 'category', 'description', 'thumbnail', 'publish', 'status']

        elif request.user.is_author:
            self.fields = ['title', 'slug', 'category', 'description', 'thumbnail', 'publish']

        else:
            raise Http404("you can't access to this page !")
        
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit = False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        
        return super().form_valid(form)