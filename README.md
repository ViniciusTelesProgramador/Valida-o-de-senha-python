# Validar-senha-python


Este código é um sistema simples de validação de senha em Python. Aqui está uma breve descrição de como ele funciona:

O código começa importando os módulos os e re. O módulo os é usado para limpar a tela do terminal, enquanto o módulo re é usado para realizar validações com expressões regulares.

Em seguida, é definida a lista login_senha, que será usada para armazenar as senhas cadastradas pelos usuários.

A função mostrarMenu1() é definida para exibir o menu principal do sistema.

A função cadastrar_senha() é definida para permitir que os usuários cadastrem uma senha. Ele realiza a validação da senha, garantindo que ela tenha pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais. O usuário tem até 3 tentativas para cadastrar uma senha válida.

Em seguida, entra em um loop infinito que exibe o menu principal e solicita que o usuário escolha uma opção. Dependendo da opção selecionada, o código executa ações diferentes:

Se o usuário escolher a opção 1 (LOGIN), ele será solicitado a digitar sua senha. Se a senha estiver na lista de senhas cadastradas, ele será autenticado com sucesso. Caso contrário, uma mensagem de senha incorreta será exibida.

Se o usuário escolher a opção 2 (CADASTRAR), ele será levado ao processo de cadastro de senha utilizando a função cadastrar_senha(). Se a senha for cadastrada com sucesso, ela será adicionada à lista de senhas cadastradas.

Se o usuário escolher qualquer outra opção, uma mensagem de opção inválida será exibida.

O loop continua até que o usuário escolha a opção de sair do programa.

Em resumo, este código implementa um sistema básico de autenticação com a capacidade de cadastrar novas senhas.
