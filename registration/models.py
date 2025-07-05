from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('Outro', 'Outro')])
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pendente', 'Pendente'), ('Confirmada', 'Confirmada')],
        default='Pendente'
    )

    def __str__(self):
        return self.name