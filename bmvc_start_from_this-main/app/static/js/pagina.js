const eventos = [
  { id: 1, data: new Date("June 30, 2025 19:00:00") },
  { id: 2, data: new Date("July 15, 2025 13:00:00") }
];

eventos.forEach(evento => {
  const contagemEl = document.getElementById("contagem" + evento.id);

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
  const msg = document.getElementById("mensagem" + id);
  if (!msg) {
    console.log("Mensagem não encontrada:", "mensagem" + id);
    return;
  }

  msg.innerText = "✅ Presença confirmada! Te esperamos lá!";
  msg.classList.add("show");
}
