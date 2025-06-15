<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Evento do Ano</title>
  <link rel="stylesheet" href="/static/css/pagina.css">
  <script src="/static/js/pagina.js" defer></script>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>
  <div class="container">
    <h1>🔥 FESTA DEV 2025 🔥</h1>
    <p class="info"><strong>📅 Data:</strong> 30/06/2025</p>
    <p class="info"><strong>📍 Local:</strong> Auditório Central da UniTech</p>
    <p class="info"><strong>🕖 Horário:</strong> 19h</p>

    <div class="countdown-box">
      <h2>⏳ Contagem Regressiva</h2>
      <div id="countdown" class="countdown">Carregando...</div>
    </div>

    <button class="btn" onclick="confirmarPresenca()">Confirmar Presença</button>
    <p id="confirmacao" class="mensagem"></p>
  </div>
</body>
</html>
