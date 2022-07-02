from django.db import models

# Create your models here.

STATUS_CHOICES = [('active', 'Active'), ('blocked', 'Blocked')]

class Book(models.Model):
    guest_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Name")
    from_email = models.EmailField(max_length=50, null=False, blank=False, verbose_name="from_email")
    content = models.TextField(max_length=3000, verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new', verbose_name='Status')


    def __str__(self):
        return f"{self.pk}, {self.guest_name}, {self.from_email}, {self.content}, {self.status}"


    class Meta:
        db_table = "note"
        verbose_name = "Entry"
        verbose_name_plural = "Entryses"