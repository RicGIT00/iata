from django.db import models


# Create your models here.


class Vaga(models.Model):
    Tecnologia = 'TECH'
    Advocacia = 'ADV'
    Engenharia = 'ENG'
    Marketing = 'MKT'

    Categorias = ((Tecnologia, 'Tecnologia'),
                  (Advocacia, 'Advocacia'),
                  (Engenharia, 'Engenharia'),
                  (Marketing, 'Marketing')
                  )

    Genero = 'AllIn'
    Afro = 'BayAfro'
    LGBTQ = 'LGBTQ+'
    Deficiente = 'Enable'

    InclusaoTipos = ((Genero, 'AllIn'),
                     (Afro, 'BayAfro'),
                     (LGBTQ, 'LGBTQ+'),
                     (Deficiente, 'Enable')
                     )

    choices_status = ((1, 'Ativa'), (0, 'Desativada'))

    vaga_cargo = models.CharField(max_length=40, verbose_name="Cargo da vaga")
    vaga_descricao = models.TextField(max_length=250, verbose_name="Descrição da vaga")
    vaga_salario = models.FloatField(verbose_name="Salário da vaga")
    nome_categoria = models.CharField(max_length=30, choices=Categorias, verbose_name="Categoria da vaga", null=True)
    nome_tipo_inclusao = models.CharField(max_length=30, choices=InclusaoTipos, verbose_name="Tipo inclusão")
    vaga_status = models.IntegerField(choices=choices_status, verbose_name="Status da vaga")
