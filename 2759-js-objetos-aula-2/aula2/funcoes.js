const cliente = {
  nome: "Gabriel",
  idade: 17,
  email: "gabriel@gmail.com",
  telefone: ["1155555550", "1144444440"],
  saldo: 200,
  efetuaPagamento: function (valor) {
    if (valor > this.saldo) {
      console.log("Saldo insuficiente");
    } else {
      this.saldo -= valor;
      console.log(`Pagamento realizado. Novo saldo: ${this.saldo}`);
    }
  },
};

cliente.efetuaPagamento(25);
