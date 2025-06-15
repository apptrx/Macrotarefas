// Contagem Regressiva
const eventoData = new Date("June 30, 2025 19:00:00").getTime();

const countdownInterval = setInterval(() => {
  const agora = new Date().getTime();
  const distancia = eventoData - agora;

  if (distancia < 0) {
    document.getElementById("countdown").innerText = "🎉 O evento já começou!";
    clearInterval(countdownInterval);
    return;
  }

  const dias = Math.floor(distancia / (1000 * 60 * 60 * 24));
  const horas = Math.floor((distancia % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutos = Math.floor((distancia % (1000 * 60 * 60)) / (1000 * 60));
  const segundos = Math.floor((distancia % (1000 * 60)) / 1000);

  document.getElementById("countdown").innerText =
    `${dias}d ${horas}h ${minutos}m ${segundos}s`;
}, 1000);

// Confirmação de presença
function confirmarPresenca() {
  const msg = document.getElementById("confirmacao");
  msg.innerText = "✅ Presença confirmada! Te esperamos lá!";
  msg.classList.add("show");
}
