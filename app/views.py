from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.urls import reverse
from django.shortcuts import redirect
from app.models import Project, Mail
from app.forms import MailForm
from app.service import send_mails


def contact_view(request):
    form = MailForm(request.POST)
    if not form.is_valid():
        return redirect("app:home")

    sender_name = form.cleaned_data['sender_name']
    sender_email = form.cleaned_data['sender_email']
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']

    mail_params = Mail.objects.create(
        sender_name=sender_name,
        sender_email=sender_email,
        subject=subject,
        message=message
    )

    print(mail_params)
    # send_mails(mail_params)

    return redirect("app:home")


class Home(ListView):
    model = Project
    template_name = "home.html"


class IndexProjects(ListView):
    model = Project
    template_name = "index.html"


class ViewProject(DetailView):
    model = Project
    template_name = "view.html"


class Privacy(TemplateView):
    template_name = "privacy.html"
