from django.urls import path
from app.views import Home, IndexProjects, ViewProject, Privacy, contact_view, MicrosoftClone

app_name = 'app'

urlpatterns = [
    path('', Home.as_view(),  name="home"),
    path('projects/', IndexProjects.as_view(), name="projects"),
    path('projects/<int:pk>', ViewProject.as_view(), name="project"),
    path('privacy/', Privacy.as_view(), name="privacy"),
    path('contact/', contact_view, name="contact"),
    path('microsoft_clone/', MicrosoftClone.as_view(), name="microsoft_clone")
]
