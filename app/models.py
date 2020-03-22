from django.db import models


class Tag(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class Project(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    picture_URL = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    repo = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return self.title


class Mail(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mail from {self.sender_name} <{self.sender_email}> - Object: {self.subject}"
