<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Login</title>
  <link rel="stylesheet" href="/static/css/pagina.css">
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>
  <div class="container">
    <h1> Acesso Restrito</h1>

    <form action="/portal" method="post">
      <input type="text" name="username" placeholder="Usuário" required>
      <input type="password" name="password" placeholder="Senha" required>
      <button type="submit">Entrar</button>
      <p style="margin-top: 15px;">
        <a href="/cadastro">Não tem conta? Cadastre-se</a>
      </p>

    </form>

  </div>
</body>
</html>
