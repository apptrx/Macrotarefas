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
    <h1> EVENTOS 2025 </h1>

    <div class="evento">
      <h2>FESTA 2025</h2>
      <p>Data: 30/06/2025</p>
      <p>Local: Auditório Central da UnB</p>
      <p>Horário: 19h</p>

      <div class="contagem-mae">
        <h3>⏳ Contagem Regressiva</h3>
        <div class="contagem" id="contagem1">Carregando...</div>
      </div>

      <button class="btn" onclick="confirmarPresenca(1)">Confirmar Presença</button>
      <p class="mensagem" id="mensagem1"></p>
    </div>

    <div class="evento">
      <h2>INTENSIVÃO FULLSTACK</h2>
      <p>Data: 15/07/2025</p>
      <p>Local: LTDEA</p>
      <p>Horário: 13h</p>

      <div class="contagem-mae">
        <h3>⏳ Contagem Regressiva</h3>
        <div class="contagem" id="contagem2">Carregando...</div>
      </div>

      <button class="btn" onclick="confirmarPresenca(2)">Confirmar Presença</button>
      <p class="mensagem" id="mensagem2"></p>
    </div>


  </div>
<script src="/static/js/pagina.js"></script>
</body>


