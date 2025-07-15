<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Cadastro</title>
  <link rel="stylesheet" href="/static/css/pagina.css">
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>
  <div class="container">
    <h1> Criar Conta</h1>
    <form action="/cadastro" method="post">
      <input type="text" name="username" placeholder="Novo usuário" required>
      <input type="password" name="password" placeholder="Nova senha" required>
      <button type="submit">Cadastrar</button>
    </form>
    <p style="margin-top: 15px;"><a href="/portal">Já tenho conta</a></p>
  </div>
</body>
</html>
