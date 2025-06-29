const eventos = Array.from(document.querySelectorAll('.evento')).map((eventoDiv, index) => {
  const dataTexto = eventoDiv.querySelector('p:nth-of-type(1)').innerText.replace('Data: ', '').trim();
  const horarioTexto = eventoDiv.querySelector('p:nth-of-type(3)').innerText.replace('Horário: ', '').trim();

  // Converte data para YYYY-MM-DD
  const [dia, mes, ano] = dataTexto.split('/');
  // Ajusta horário: de 19h vira 19:00
  const horarioLimpo = horarioTexto.replace('h', ':00');

  // Monta data no formato ISO
  const dataIso = `${ano}-${mes}-${dia}T${horarioLimpo}`;

  return {
    id: index + 1,
    data: new Date(dataIso)
  };
});

eventos.forEach(evento => {
  const contagemEl = document.getElementById(`contagem${evento.id}`);

  const interval = setInterval(() => {
    const agora = new Date().getTime();
    const distancia = evento.data.getTime() - agora;

    if (isNaN(evento.data.getTime())) {
      contagemEl.innerText = "Data inválida!";
      clearInterval(interval);
      return;
    }

    if (distancia < 0) {
      contagemEl.innerText = "Esse evento já começou!";
      clearInterval(interval);
      return;
    }

    const dias = Math.floor(distancia / (1000 * 60 * 60 * 24));
    const horas = Math.floor((distancia % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutos = Math.floor((distancia % (1000 * 60 * 60)) / (1000 * 60));
    const segundos = Math.floor((distancia % (1000 * 60)) / 1000);

    contagemEl.innerText = `${dias}d ${horas}h ${minutos}m ${segundos}s`;
  }, 1000);
});

function confirmarPresenca(id) {
  const msg = document.getElementById(`mensagem${id}`);
  if (msg) {
    msg.innerText = "✅ Presença confirmada! Te esperamos lá!";
    msg.classList.add("show");
  }
}
