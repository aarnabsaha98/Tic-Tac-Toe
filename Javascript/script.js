const humanPlayer = 'x'
const AIplayer = 'o'
let currentPlayer;
const WinningCombination = [
    [0, 1, 2],
    [0, 3, 6],
    [3, 4, 5],
    [1, 4, 7],
    [6, 7, 8],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
let trackPlayer = {};
const cells = document.querySelectorAll('.cell');
const Replay = document.querySelector('.game--restart');
Replay.addEventListener('click',startOver);

function startOver(){
    gameBox.classList.remove('hide');
    messageBox.classList.add('hide');
    for (var member in trackPlayer) delete trackPlayer[member];
    cells.forEach(box=>{
        box.innerText = '';
        box.removeEventListener('click',playGame);
        box.addEventListener('click', playGame,{once:true})
    });
}

cells.forEach(cell => {
    cell.addEventListener('click', playGame,{once:true})
  });

function playGame(square) {
    const targetElement = square.target;
    //switch turn
    currentPlayer = currentPlayer === humanPlayer ? AIplayer : humanPlayer;
    //place the mark
    placemark(targetElement, currentPlayer)
    //check for win
    let gameWonPlayer = checkWin(trackPlayer)
    if (gameWonPlayer == true) {
        console.log('wins')
        gameOver()
    }
    //check for drawn and if game in progress
    drawGame()
}
messageBox = document.querySelector('.game-status')
const winnerAnnounced = document.querySelector('.game--status');
const gameBox = document.querySelector('.game--container');

function gameOver(){
    gameBox.classList.add('hide');
    messageBox.classList.remove('hide');
    winnerAnnounced.innerHTML = `<h2> Wins ${currentPlayer}</h2>`;   
}

function drawGame(){
    if(checkWin(trackPlayer) == null && Object.keys(trackPlayer).length == 9) {
        console.log('draw!');
        gameBox.classList.add('hide');
        messageBox.classList.remove('hide');
        winnerAnnounced.innerHTML = `<h2> Draw!!! </h2>`; 
    }

}

function placemark(cell, currentPlayer) {
    cell.innerText = currentPlayer
    trackPlayer[cell.id] = currentPlayer
    console.log(trackPlayer)
}

function checkWin(player) {

    for (const combination of WinningCombination){
        const [a,b,c] = combination

        if(player[a] && player[a] == player[b] && player[a] == player[c]){
            console.log(combination);
            return true;
        }
    }
    return null;

}

const title = document.querySelector('.game--title');
setInterval(colorChange, 2000);
function colorChange(){
    let letters = '0123456789ABCDEF';
    let color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    title.style.color = color;
}