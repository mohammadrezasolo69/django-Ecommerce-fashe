from django.db import models


class ContactUs(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField(null=True)
    send = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

