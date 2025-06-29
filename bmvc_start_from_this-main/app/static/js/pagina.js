// Coleta todos os elementos de evento na página
const eventos = Array.from(document.querySelectorAll('.evento')).map((eventoDiv, index) => {
  const dataTexto = eventoDiv.querySelector('p:nth-of-type(1)').innerText.replace('Data: ', '').trim();
  const horarioTexto = eventoDiv.querySelector('p:nth-of-type(3)').innerText.replace('Horário: ', '').trim();

  // Ajusta horário (ex: "19h" => "19:00")
  const horarioAjustado = horarioTexto.replace('h', ':00');

  // Ajusta data (br -> iso)
  const [dia, mes, ano] = dataTexto.split('/');
  const dataFormatada = `${ano}-${mes}-${dia} ${horarioAjustado}`;

  return {
    id: index + 1,
    data: new Date(dataFormatada)
  };
});

// Para cada evento, cria o setInterval da contagem
eventos.forEach(evento => {
  const contagemEl = document.getElementById(`contagem${evento.id}`);

  const interval = setInterval(() => {
    const agora = new Date().getTime();
    const distancia = evento.data.getTime() - agora;

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
