console.log("==============================================")
console.log("          SEJA BEM-VINDO À NOSSA LOJA1!         ")
console.log("==============================================")
console.log("Estamos felizes em ter você aqui!")
console.log("Esperamos que você encontre tudo o que precisa.")
console.log("==============================================")

const readline = require('readline');
const fs = require('fs');

let usuarios = [];
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function registrarUsuario() {
  rl.question('Digite seu nome: ', (nome) => {
    rl.question('Digite seu email: ', (email) => {
      let emailExistente = usuarios.find((usuario) => usuario.email === email);
      if (emailExistente) {
        console.log('Email já cadastrado. Tente novamente.');
        registrarUsuario();
      } else {
        rl.question('Digite sua senha: ', (senha) => {
          rl.question('Confirme sua senha: ', (confirmarSenha) => {
            if (senha === confirmarSenha) {
              let usuario = { nome, email, senha };
              usuarios.push(usuario);
              console.log('Usuário registrado com sucesso!');

              // Salvar registro em um arquivo TXT
              fs.appendFile('registros.txt', `Nome: ${nome}\nEmail: ${email}\nSenha: ${senha}\n\n`, (err) => {
                if (err) {
                  console.error(err);
                }
              });

              mostrarMenu();

            } else {
              console.log('Senhas não conferem.');
              registrarUsuario();
            }
          });
        });
      }
    });
  });
}

function fazerLogin() {
  rl.question('Digite seu email: ', (email) => {
    rl.question('Digite sua senha: ', (senha) => {
      let usuario = usuarios.find((usuario) => usuario.email === email && usuario.senha === senha);
      if (usuario) {
        console.log('Login realizado com sucesso!');
        mostrarMenu();
      } else {
        console.log('Email ou senha incorretos.');
        fazerLogin();
      }
    });
  });
}

function mostrarMenu() {
  console.log('Menu:');
  console.log('1. Registrar');
  console.log('2. Login');
  console.log('3. Sair');

  rl.question('Digite sua opção: ', (opcao) => {
    switch (opcao) {
      case '1':
        registrarUsuario();
        break;
      case '2':
        fazerLogin();
        break;
      case '3':
        console.log('Até logo!');
        rl.close();
        setTimeout(() => {
          process.exit();
        }, 100); // Add this line to exit the process after closing the readline interface
        break;
      default:
        console.log('Opção inválida.');
        mostrarMenu();
    }
  });
}

mostrarMenu();
