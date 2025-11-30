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
  3. Para ver os logs dos arquivos:
  ```bash
  docker logs <nome_do_container>
  ```
  exemplo:
  ```bash
  docker logs desafio1_client
  docker logs desafio1_server
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
  cd desafio2
  ```
  2. E dar compose no docker-compose:
  ```bash
  docker-compose up
  ```
  3. Testar se os dados se mantêm:
  ```bash
  docker exec -it desafio2_db psql -U user -d desafio2 -c "SELECT * FROM clientes;"
  ```
  <strong>Para testar se os dados se mantiveram:</strong>
  ##
  1. Para rodar basta entrar na pasta:
  ```bash
  cd desafio2
  ```
  2. Verificar a presença do volume, procure por <strong>desafio2_db_data</strong>:
  ```bash
  docker volume ls
  ```
  3. E dar compose down no docker-compose:
  ```bash
  docker-compose down
  ```
  4. Verificar a presença do volume novamente:
  ```bash
  docker volume ls
  ```
  5. Subir novamente:
  ```bash
  docker-compose up -d
  ```
  6. Testar se os dados realmente persistiram:
  ```bash
  docker exec -it desafio2_db psql -U user -d desafio2 -c "SELECT * FROM clientes;"
  ```
</details>

<details>
  <summary>desafio 3:</summary>

  <h2>Contexto do Desafio</h2>
  Nesse desafio proposto pelo professor foi necessário criar um docker compose que orquestrasse 3 serviços distintos, foram utilizados: rede interna e o uso do depends_on no server web para estabelecer essa conexão (dependendo da cache e do db)

  <br>
  <br>
  <ul>
    <li><strong>docker-compose:</strong> arquivo responsável por subir os 3 serviços (cache, web, db)</li>
    <li><strong>servço web:</strong> aplicação Flask que acessa o banco e o Redis</li>
    <li><strong>db - banco de dados:</strong> banco de dados com produtos que inicializa com o init_sql</li>
    <li><strong>cache:</strong> serviço de cache para acelerar o processo - redis 7</li>
    <li><strong>internal_net:</strong> rede que permite conexão isolada entre os containers</li>
  </ul>

  1. Para rodar basta entrar na pasta:
  ```bash
  cd desafio3
  ```
  2. E dar compose no docker-compose:
  ```bash
  docker-compose up
  ```
  3. Para ver os logs dos arquivos:
  ```bash
  docker logs <nome_do_container>
  ```
  exemplo:
  ```bash
  docker logs desafio3_web
  docker logs desafio3_db
  docker logs desafio3_cache
  ```
  
</details>
<details>
  <summary>desafio 4:</summary>

  <h2>Contexto do Desafio</h2>
  Nesse desafio foi proposto pelo professor que fossem criados dois microsserviços que se conectassem via HTTP, o microsserviço A disponibiliza uma lista de usuários no formato json e o microsserviço B consome esses dados e retorna uma mensagem completa informando (ex: "Usuário X ativo desde...")

  <br>
  <br>
  <ul>
    <li><strong>docker-compose:</strong> sobe os dois microsserviços (A e B), cada um em portas diferentes</li>
    <li><strong>microsserviço A (porta 5000):</strong> disponibiliza os dados a serem consumidos pelo microsserviço B via HTTP</li>
    <li><strong>microsserviço B (porta 5001):</strong> consome os dados e transforma os dados recebidos do microsserviço A em frases completas</li>
  </ul>

  1. Para rodar basta entrar na pasta:
  ```bash
  cd desafio4
  ```
  2. E dar compose no docker-compose:
  ```bash
  docker-compose up
  ```
  3. Para ver os logs dos arquivos:
  ```bash
  docker logs <nome_do_container>
  ```
  exemplo:
  ```bash
  docker logs microsservico_a
  docker logs microsservico_b
  ```

  Os containers se comunicam entre si através dos nomes atribuídos no docker-compose
</details>
<details>
  <summary>desafio 5:</summary>

  <h2>Contexto do Desafio</h2>
  Nesse desafio foi proposto pelo professor criar uma API Gateway para mediar dois microsserviços, um microsserviço fornecerá os usuários e outro microsserviço fornecerá os pedidos. O gateway centraliza as requisições externas e distribui internamente para cada serviço

  <br>
  <br>
  <ul>
    <li><strong>docker-compose:</strong> sobe os dois microsserviços (pedidos e usuários) e o gateway, cada um em portas diferentes</li>
    <li><strong>microsserviço Pedidos (porta 5002):</strong> fornece os pedidos</li>
    <li><strong>microsserviço Usuários (porta 5001):</strong> fornece os usuários</li>
  </ul>

  1. Para rodar basta entrar na pasta:
  ```bash
  cd desafio5
  ```
  2. E dar compose no docker-compose:
  ```bash
  docker-compose up
  ```
  3. Para ver os logs dos arquivos:
  ```bash
  docker logs <nome_do_container>
  ```
  exemplo:
  ```bash
  docker logs usuarios
  docker logs pedidos
  docker logs gateway
  ```
</details>
