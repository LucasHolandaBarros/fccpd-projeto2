# fccpd-projeto2

Esse projeto está destinado à implementação de desafios da disciplina de Fundamentos de Computação Concorrente e Paralela - FCCPD
Abaixo estão as **explicações de cada desafio**, separados em seções, propostos pelo professor

<details>
  <summary>desafio 1:</summary>

  <h2>Contexto do Desafio</h2>
  Nesse primeiro desafio foi proposto pelo professor uma conexão entre dois containers utilizando uma network personalizada

  <br>
  <br>
  <ul>
    <li><strong>Network:</strong> desafio1_net</li>
    <li><strong>Primeiro container:</strong> client</li>
    <li><strong>Segundo container:</strong> server</li>
  </ul>

  A network é criada no docker-compose, o server abre a porta 8080 e o client se conecta a ela para estabelecer a conexão. Cada diretório (client e server) possuem uma Dockerfile de configuração para buildar os containers


  1. Para rodar basta entrar na pasta:
  ```bash
  cd desafio1
  ```
  2. E dar compose no docker-compose:
  ```bash
  docker-compose up
  ```
  
</details>
<details>
  <summary>desafio 2:</summary>

  <h2>Contexto do Desafio</h2>
  Nesse desafio foi proposto pelo professor utilzar o docker para demonstrar persistência utilizando volumes

  <br>
  <br>
  <ul>
    <li><strong>docker-compose:</strong> onde estão subindo um banco e o leitor desse banco</li>
    <li><strong>init_sql:</strong> inicia a table de clientes para visualizar os dados</li>
    <li><strong>desafio2_db:</strong> inicia o banco de dados postgres</li>
    <li><strong>desafio2_reader:</strong> inicia o leitor do banco de dados</li>
    <li><strong>volumes:</strong> inicia os volumes</li>
  </ul>

  1. Para rodar basta entrar na pasta:
  ```bash
  cd desafio1
  ```
  2. E dar compose no docker-compose:
  ```bash
  docker-compose up
  ```
  3. Testar se os dados se mantêm:
  ```bash
  docker exec -it desafio2_db psql -U user -d desafio2 -c "SELECT * FROM clientes;"
  ```
  Para testar se os dados se mantiveram:
  ##
  1. Para rodar basta entrar na pasta:
  ```bash
  cd desafio1
  ```
  2. E dar compose down no docker-compose:
  ```bash
  docker-compose down
  ```
  3. Subir novamente:
  ```bash
  docker-compose up -d
  ```
  4. Testar se os dados realmente persistiram:
  ```bash
  docker exec -it desafio2_db psql -U user -d desafio2 -c "SELECT * FROM clientes;"
  ```
</details>

<details>
  <summary>desafio 3:</summary>

  <h2>Contexto do Desafio</h2>
</details>
<details>
  <summary>desafio 4:</summary>

  <h2>Contexto do Desafio</h2>
</details>
<details>
  <summary>desafio 5:</summary>

  <h2>Contexto do Desafio</h2>
</details>
