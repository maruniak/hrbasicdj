from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    birthday = models.DateField(verbose_name="Birthday")
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name="Organization"
    )
    photo = models.ImageField(
        upload_to='employee_photos/',
        blank=True,    # фото необязательно
        null=True,
        verbose_name="Photo"
    )

    def __str__(self):
        return f"{self.name} ({self.organization.name})"
