

# Desafio de Python da WomakersCode - Banco Delas



## Enunciado do problema:

#### O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.  

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

Um objetivo pessoal alcançado foi desenvolver o sistema de forma que todas as operações, desde o cadastro, abertura de conta e alteração de dados dos clientes até a desativação de uma conta, fossem realizadas através de um menu. Assim, não é necessário que o programador insira valores diretamente no código. Ao executar o arquivo o sistema é aberto e pode-se abrir contas, cadastrar clientes e fazer operações. 

A seguir segue a descrição de cada classe e seus respectivos atributos e métodos.


### Classe Cliente

Prótotipo das clientes do banco e também proprietárias de contas-correntes. 

#### Atributos

1. **nome**: string que guarda o nome da cliente;
2. **telefone**: string que guarda o telefone da cliente;
3. **renda_mensal**: float que guarda a renda mensal da cliente;
4. **cheque_especial**: float que guarda o valor do cheque especial da cliente. Foi inicializado com o mesmo valor da renda mensal;
5. **mulher**: booleano *True* se a cliente for mulher,  *False* se não for. Por padrão foi inicializado como *False*.

#### Métodos especiais

1. Getter **nome**: retorna o nome do cliente com a primeira letra de cada palavra com a letra maiúscula;
2. Getter **cheque_especial**: faz a verificação do valor do atributo **mulher**. Se for *True* retorna o valor da **renda_mensal**, senão retorna o valor *0.0*.


### Classe Mulher

Uma subclasse da classe Cliente. É instanciada quando se quer cadastrar uma cliente que se autodeclara mulher.

#### Atributos

1. **nome**: herdado da classe ***Cliente***;
2. **telefone**: herdado da classe ***Cliente***;
3. **renda_mensal**: herdado da classe ***Cliente***;
4. **cheque_especial**: herdado da classe ***Cliente***;
5. **mulher**: reescreve o atributo herdado da classe ***Cliente*** como *True*.


### Classe Not_mulher

Uma subclasse da classe Cliente. É instanciada quando se quer cadastrar uma cliente que __NÃO__ se autodeclara mulher.

#### Atributos

1. **nome**: herdado da classe ***Cliente***;
2. **telefone**: herdado da classe ***Cliente***;
3. **renda_mensal**: herdado da classe ***Cliente***;
4. **cheque_especial**: herdado da classe ***Cliente***;
5. **mulher**: reescreve o atributo herdado da classe ***Cliente*** como *False*.

  
### Classe Conta_corrente

Prótotipo das contas a serem cadastradas no banco. 

#### Atributos

1. **titular**: lista que guarda instâncias do tipo ***Cliente***. É inicializada como vazia;
2. **numero_da_conta**: string única que identifica a conta;
3. **saldo**: float que guarda o valor em reais que está na conta;
4. **status**: booleano *True* se a conta estiver ativa,  *False* se não estiver. Por padrão foi inicializado como *False*.
5. **cheque_especial_total**: float que guarda o valor do cheque especial total disponível. Foi inicializado com o valor *0.0*;
6. **cheque_especial_inicial**: float que guarda o valor do cheque especial máximo que a conta pode ter. Foi inicializado com o valor *0.0*;

#### Métodos especiais

1. Getter **titular()**: retorna a lista de titulares **titular**;
2. Setter **titular(cliente)**: recebe um valor que deve ser uma instância do tipo ***Cliente*** e o adiciona na lista de titulares **titular**. Em seguida chama o método **atualiza_cheque_especial()**, que será descrito a seguir.

#### Métodos

1. **atualiza_cheque_especial()**: calcula o cheque especial máximo de acordo com cada tipo de cliente titular e atualiza o cheque especial disponível de acordo com o saldo. Executa os seguintes passos:
    - zera o valor de **cheque_especial_total**; 
    - inicia uma iteração com um contador *i* igual a zero até o tamanho da lista **titular** em que, para cada *i*, o valor do **cheque_especial_total** é igualado a ele mesmo somado com o valor do **cheque_especial** do cliente na posição *i* da lista;
    - dá ao **cheque_especial_inicial** o mesmo valor do **cheque_especial_total**;
    - verifica se o saldo é menor que zero. Se sim, dá ao **cheque_especial_total**, o valor de cheque especial disponível, como ele mesmo somado com o valor do **saldo**.
2. 
