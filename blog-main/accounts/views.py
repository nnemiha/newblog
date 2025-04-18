from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        if not User.objects.filter(is_superuser=True).exists():
            user = self.object
            user.is_superuser = True
            user.is_staff = True
            user.save()
        return response

