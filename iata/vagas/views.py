from django.shortcuts import render, redirect

from .models import Vaga


# Create your views here.


def vacanciesJob(request):
    vagas = Vaga.objects.all()

    return render(request, 'jobs-rh.html', {'vagas': vagas})


def createJobVacancy(request):
    if request.method == 'POST':
        cargo = request.POST['job_name']
        salario = request.POST['job_salary']
        categoria = request.POST['job_category']
        tipo = request.POST['job_type']
        status = request.POST['job_status']
        descricao = request.POST['job_description']

        vaga = Vaga(vaga_cargo=cargo, vaga_descricao=descricao, vaga_salario=salario, nome_categoria=categoria,
                    nome_tipo_inclusao=tipo, vaga_status=status)

        vaga.save()
        print("Vaga criada !")
        return redirect("jobs-rh")
    else:
        return render(request, 'job-form.html')
