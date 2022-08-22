

# Desafio de Python da WomakersCode - Banco Delas



## Enunciado do problema:

#### O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.  

Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo:  

- Cada conta corrente pode ter um ou mais clientes como titular;
- O banco controla apenas o nome, o telefone e a renda mensal de cada cliente;
- A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos;
- Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo;  
- Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até o valor da renda mensal negativo;  
- Clientes homens por enquanto não têm direito a cheque especial.  

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

- **nome**: string que guarda o nome da cliente;
- **telefone**: string que guarda o telefone da cliente;
- **renda_mensal**: float que guarda a renda mensal da cliente;
- **cheque_especial**: float que guarda o valor do cheque especial da cliente. Foi inicializado com o mesmo valor da renda mensal;
- **mulher**: booleano *True* se a cliente for mulher,  *False* se não for. Por padrão foi inicializado como *False*.

#### Métodos especiais

1. Getter **nome**: retorna o nome do cliente com a primeira letra de cada palavra com a letra maiúscula;
2. Getter **cheque_especial**: faz a verificação do valor do atributo **mulher**. Se for *True* retorna o valor da **renda_mensal**, senão retorna o valor *0.0*.


### Classe Mulher

Uma subclasse da classe Cliente. É instanciada quando se quer cadastrar uma cliente que se autodeclara mulher.

#### Atributos

- **nome**: herdado da classe ***Cliente***;
- **telefone**: herdado da classe ***Cliente***;
- **renda_mensal**: herdado da classe ***Cliente***;
- **cheque_especial**: herdado da classe ***Cliente***;
- **mulher**: reescreve o atributo herdado da classe ***Cliente*** como *True*.


### Classe Not_mulher

Uma subclasse da classe Cliente. É instanciada quando se quer cadastrar uma cliente que __NÃO__ se autodeclara mulher.

#### Atributos

- **nome**: herdado da classe ***Cliente***;
- **telefone**: herdado da classe ***Cliente***;
- **renda_mensal**: herdado da classe ***Cliente***;
- **cheque_especial**: herdado da classe ***Cliente***;
- **mulher**: reescreve o atributo herdado da classe ***Cliente*** como *False*.

  
### Classe Conta_corrente

Prótotipo das contas a serem cadastradas no banco. 

#### Atributos

- **titular**: lista que guarda instâncias do tipo ***Cliente***. É inicializada como vazia;
- **numero_da_conta**: string única que identifica a conta;
- **saldo**: float que guarda o valor em reais que está na conta;
- **status**: booleano *True* se a conta estiver ativa,  *False* se não estiver. Por padrão foi inicializado como *False*.
- **cheque_especial_total**: float que guarda o valor do cheque especial total disponível. Foi inicializado com o valor *0.0*;
- **cheque_especial_inicial**: float que guarda o valor do cheque especial máximo que a conta pode ter. Foi inicializado com o valor *0.0*;

#### Métodos especiais

- Getter **titular()**: retorna a lista de titulares **titular**;
- Setter **titular(cliente)**: recebe um valor que deve ser uma instância do tipo ***Cliente*** e o adiciona na lista de titulares **titular**. Em seguida chama o método **atualiza_cheque_especial()**, que será descrito a seguir.

#### Métodos

- **atualiza_cheque_especial()**: calcula o cheque especial máximo de acordo com cada tipo de cliente titular e atualiza o cheque especial disponível de acordo com o saldo. Executa os seguintes passos:
    1. zera o valor de **cheque_especial_total**; 
    2. inicia uma iteração com um contador *i* igual a zero até o tamanho da lista **titular** em que, para cada *i*, o valor do **cheque_especial_total** é igualado a ele mesmo somado com o valor do **cheque_especial** do cliente na posição *i* da lista;
    3. dá ao **cheque_especial_inicial** o mesmo valor do **cheque_especial_total**;
    4. verifica se o saldo é menor que zero. Se sim, dá ao **cheque_especial_total**, o valor de cheque especial disponível, como ele mesmo somado com o valor do **saldo**.
- **depositar(valor)**: recebe um valor e o adiciona ao saldo da conta se algumas condições forem satisfeitas. Executa os seguintes passos:
    1. verifica se o **status** da conta é *True*. Caso sim, executa o passo ii. Caso não, executa o passo vii; 
    2. verifica se o **saldo** é menor que zero. Caso sim, executa o passo iii. Caso não, executa o passo vi;
    3. verifica se o resultado da soma entre o valor do **saldo** e o valor depositado é menor ou igual a zero. Caso sim, execulta o passo iv. Caso não, executa o passo v;
    4. atualiza o valor do **cheque_especial_total** para o valor dele mesmo somado ao valor depositado. E executa o passo vi;
    5. atualiza o valor do **cheque_especial_total** para seu valor máximo, isto é, para o valor de **cheque_especial_inicial**. E executa o passo vi;  
    6. atualiza o valor do **saldo** para o valor dele mesmo somado ao valor depositado, e finaliza;
    7. escreve na tela a mensagem "Operação não realizada. Conta inativa." e finaliza.
- **sacar(valor)**: recebe um valor e o subtrai do saldo da conta se algumas condições forem satisfeitas. Executa os seguintes passos:
    1. verifica se o **status** da conta é *True*. Caso sim, executa o passo ii. Caso não, executa o passo ix; 
    2. verifica se o resultado da subtração entre o valor do **saldo** e o valor sacado é maior ou igual a zero. Caso sim, executa o passo vii. Caso não, executa o passo iii;
    3. verifica se o módulo absoluto do resultado da subtração entre o valor do **saldo** e o valor sacado é menor ou igual ao valor do **cheque_especial_total**. Caso sim, executa o passo iv. Caso não, executa o passo viii;
    4. verifica se o **saldo** é menor ou igual a zero. Caso sim, executa o passo v. Caso não, executa o passo vi;
    5. executa o passo vi, porém antes de finalizar atualiza o valor do **cheque_especial_total** para o valor dele mesmo *menos* o valor do novo sacado;
    6. executar o passo vi, porém antes de finalizar atualiza o valor do **cheque_especial_total** para o valor dele mesmo somado ao valor do novo **saldo** calculado;
    7. atualiza o valor do **saldo** para o valor dele *menos* o valor sacado, e finaliza;
    8. escreve na tela a mensagem "Operação não realizada. Saldo insuficiente." e finaliza
    9. escreve na tela a mensagem "Operação não realizada. Conta inativa." e finaliza.

