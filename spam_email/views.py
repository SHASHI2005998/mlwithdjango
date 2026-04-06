from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import Email
from ml_model.predictor import predict_email

class EmailView(CreateView):
    model = Email
    fields = ['email']
    template_name = 'email_form.html'

    def form_valid(self, form):
        text = form.cleaned_data['email']

        result = predict_email(text)

        form.instance.is_spam = bool(result)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('result', kwargs={'pk': self.object.pk})


class ResultView(DetailView):   # 🔥 CHANGE HERE
    model = Email
    template_name = 'result.html'