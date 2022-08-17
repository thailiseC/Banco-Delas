

# Desafio de Python da WomakersCode - Banco Delas



## Enunciado do problema:

##### O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.  

Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo:  

1. Cada conta corrente pode ter um ou mais clientes como titular;
2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente;
3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos;
4. Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo;  
5. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até o valor da renda mensal negativo;  
6. Clientes homens por enquanto não têm direito a cheque especial.  

Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo". Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata".



## Resolução

A identificação dos atores do problema levou à criação das classes:

- Cliente;
- Mulher como subclasse de Cliente;
- Not_mulher como subclasse de Cliente;
- Conta_corrente;
- Banco_Delas.



### Classe Cliente

#### Atributos

1. **nome**: string que guarda o nome da cliente;
2. **telefone**: string que guarda o telefone da cliente;
3. **renda_mensal**: float que guarda a renda mensal da cliente;
4. **cheque_especial**: float que guarda o valor do cheque especial da cliente. Foi inicializado com o mesmo valor da renda mensal;
5. **mulher**: booleano *True* se a cliente for mulher,  *False* se não for. Por padrão foi inicializado como *False*.



#### Métodos

1. 

  

