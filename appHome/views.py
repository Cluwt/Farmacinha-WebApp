from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Views do DrugRecall:

# View responsável por abrir o Sistema, renderizando a página de Home.
def appHome(request):
    
    # Carrega o template do HTML:
    template = loader.get_template("Home.html")
    
    # Aviso de página recarregada:
    print("Página home foi carregada com sucesso!")

    # Renderiza o template:
    return HttpResponse(template.render())

# View responsável por puxar cookies e renderizar a página de Login.
def appLogin(request):

    # Carrega o template do HTML:
    template = loader.get_template("Login.html")

    # Aviso de página de login carregada:
    print("Página de login foi carregada com sucesso!")

    # Renderiza o template:
    return HttpResponse(template.render())

# View responsável por puxar cookies e renderizar a página de Login.
def appRegister(request):

    # Carrega o template do HTML:
    template = loader.get_template("Register.html")

    # Aviso da página de registro carregada:
    print("Página de registro foi carregada com sucesso!")

    # Renderiza o template:
    return HttpResponse(template.render())

# View responsável por pegar os cookies e renderizar a página de Dashboard.
def appDashboard(request):

    # Carrega o template do HTML:
    template = loader.get_template("Dashboard.html")

    # Aviso da página de dashboard carregada:
    print("Página de dashboard foi carregada com sucesso!")

    # Renderiza o template:
    return HttpResponse(template.render())

# View responsável por pegar os cookies e renderizar a página de DashboardMedicamentos.
def appDashboardMedicamentos(request):

    # Carrega o template do HTML:
    template = loader.get_template("DashboardMedicamentos.html")

    # Aviso da página de dashboard carregada:
    print("Página de dashboard de medicamentos foi carregada com sucesso!")

    # Renderiza o template:
    return HttpResponse(template.render())

# View responsável por pegar os cookies e renderizar a página de DashboardUsuarios.
def appDashboardUsuarios(request):

    # Carrega o template do HTML:
    template = loader.get_template("DashboardUsuarios.html")

    # Aviso da página de dashboard carregada:
    print("Página de dashboard de medicamentos foi carregada com sucesso!")

    # Renderiza o template:
    return HttpResponse(template.render())

# View responsável por pegar os cookies e renderizar a página de DashboardPosts.
def appDashboardPosts(request):

    # Carrega o template do HTML:
    template = loader.get_template("DashboardPosts.html")

    # Aviso da página de dashboard carregada:
    print("Página de dashboard de medicamentos foi carregada com sucesso!")

    # Renderiza o template:
    return HttpResponse(template.render())

# View responsável por pegar os cookies e renderizar a página de DashboardIntegrantes.
def appDashboardIntegrantes(request):

    # Carrega o template do HTML:
    template = loader.get_template("DashboardIntegrantes.html")

    # Aviso da página de dashboard carregada:
    print("Página de dashboard de medicamentos foi carregada com sucesso!")

    # Renderiza o template:
    return HttpResponse(template.render())

# View responsável por renderizar a página de Logout do Sistema.
def appLogout(request):

    # Carrega o template do HTML:
    template = loader.get_template("Logout.html")

    # Aviso da página de dashboard carregada:
    print("Página de logout foi carregada com sucesso!")

    # Renderiza o template:
    return HttpResponse(template.render())