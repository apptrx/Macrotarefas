// Coleta todos os elementos de contagem na página
const contagens = document.querySelectorAll('.contagem');

// Gera uma lista de eventos com suas datas convertidas
const eventos = Array.from(contagens).map((el, index) => {
  // Acha o card do evento
  const eventoDiv = el.closest('.evento');
  // Pega a data e horário dos <p>
  const dataTexto = eventoDiv.querySelector('p:nth-of-type(1)').innerText.replace('Data: ', '');
  const horarioTexto = eventoDiv.querySelector('p:nth-of-type(3)').innerText.replace('Horário: ', '');

  // Junta data e horário em um único Date
  return {
    id: index + 1,
    data: new Date(`${dataTexto} ${horarioTexto}`)
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

// Função do botão de presença
function confirmarPresenca(id) {
  const msg = document.getElementById(`mensagem${id}`);
  if (msg) {
    msg.innerText = "✅ Presença confirmada! Te esperamos lá!";
    msg.classList.add("show");
  }
}
