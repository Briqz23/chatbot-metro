let timer 
let contagem 

function resetTimer() {
    clearTimeout(timer) // Limpa contagens anteriores
    clearInterval(contagem)

    let timeLeft = 60 // segundos

    // Contador DEBUG
    contagem = setInterval(() => {
        console.log(`${timeLeft}`)
        timeLeft--
    }, 1000)

    // Timer 1 minuto
    timer = setTimeout(() => {
        clearInterval(contagem)
        socket.send(JSON.stringify({ 'action': 'close' }))
        socket.close() 
        window.location.href = '/'
        console.log("Usuário desconectado por inatividade!")
    }, 60000)
}

window.onload = resetTimer
document.onmousemove = resetTimer
document.onkeypress = resetTimer
document.onclick = resetTimer