<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Eventos</title>
  <link rel="stylesheet" href="/static/css/pagina.css">
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>
  <div class="container">
    <h1>EVENTOS 2025</h1>

    % for i, e in enumerate(eventos, start=1):
    <div class="evento">
      <h2>{{e.nome}}</h2>
      <p>Data: {{e.data}}</p>
      <p>Local: {{e.local}}</p>
      <p>Horário: {{e.horario}}</p>

      <div class="contagem-mae">
        <h3>⏳ Contagem Regressiva</h3>
        <div class="contagem" id="contagem{{i}}">Carregando...</div>
      </div>

      <button class="btn" onclick="confirmarPresenca({{i}})">Confirmar Presença</button>
      <p class="mensagem" id="mensagem{{i}}"></p>

      <a href="/eventos/deletar/{{e.nome.replace(' ', '_')}}" style="color: red;">Remover</a>
    </div>
    % end

    <h3>Adicionar Novo Evento</h3>
    <form id="formEvento">
      <input type="text" name="nome" placeholder="Nome do evento" required><br>
      <input type="text" name="data" placeholder="Data (ex: 30/06/2025)" required><br>
      <input type="text" name="local" placeholder="Local" required><br>
      <input type="text" name="horario" placeholder="Horário" required><br>
      <button type="submit">Adicionar</button>
    </form>

  </div>

  <script src="/static/js/pagina.js"></script>
</body>
</html>
