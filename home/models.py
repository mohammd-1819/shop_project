from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    subject = models.CharField(max_length=70)
    text = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'contact us message'
        verbose_name_plural = 'contact us messages'


