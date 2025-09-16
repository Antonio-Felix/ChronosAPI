from django.db import models

class Client(models.Model):
    TIPO_CHOICES = [
        ("A", "Aluno"),
        ("N", "Nutricionista"),
        ("P", "Personal Trainer"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_tipo_display()})"