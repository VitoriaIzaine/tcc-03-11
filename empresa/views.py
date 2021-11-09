from django.shortcuts import render

def principal(request):
    return render(request, 'empresa/principal.html')

def cadastrar_empresa(request):
    # validando se veio de um formulario POST
    if request.method != 'POST':
        return render(request, 'empresa/cadastrar.html')
    # obtendo os dados do form
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    senha = request.POST.get('senha')

    if not email or not usuario or not nome or not sobrenome or not senha:
        messages.add_message(request, messages.WARNING, 'Todos os campos são obrigatórios')
        return render(request, 'empresa/cadastrar.html')

    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.WARNING, 'email inválido')
        return render(request, 'empresa/cadastrar.html')

    if len(senha)<6:
       messages.add_message(request, messages.WARNING, 'Senha deve ter no mínimo 6 caracter')
       return render(request, 'empresa/cadastrar.html')

    if User.objects.filter(username=usuario).exists():
       messages.add_message(request, messages.WARNING, 'Usuário já existe')
       return render(request, 'empresa/cadastrar.html')

    if User.objects.filter(email=email).exists():
       messages.add_message(request, messages.WARNING, 'e-mail já existe')
       return render(request, 'empresa/cadastrar.html')

    user = User.objects.create_user(
        username=usuario,
        email=email,
        first_name=nome,
        last_name=sobrenome,
        password=senha
    )
    messages.add_message(request, messages.SUCCESS, 'Cadastrado com sucesso')
    user.save()
    return redirect('login')

