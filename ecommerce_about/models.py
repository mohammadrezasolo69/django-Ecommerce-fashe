from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=300)
    img = models.ImageField(upload_to='about_us/')
    descriptions_main = models.TextField()
    descriptions_long = models.TextField()

    def __str__(self):
        return self.title
