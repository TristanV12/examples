var frame_DFS = -1;
function init() {
  setInterval(draw, 1000);
}

function draw() {
  frame_DFS += 1;
  var ctx = document.getElementById('DFS_animation').getContext('2d');

  ctx.clearRect(0, 0, 300, 150); // clear canvas

  if(frame_DFS % 7 == 0){ ctx.strokeStyle="red"; }
  else{ ctx.strokeStyle="black"; }
  ctx.beginPath();
  ctx.moveTo(150,20);
  ctx.lineTo(100,75);
  ctx.stroke();
  ctx.closePath();

  if(frame_DFS % 7 == 3 || frame_DFS % 7 == 5 || frame_DFS % 7 == 6){ ctx.strokeStyle="red"; }
  else{ ctx.strokeStyle="black"; }
  ctx.beginPath();
  ctx.moveTo(150,20);
  ctx.lineTo(200,75);
  ctx.stroke();
  ctx.closePath();

  if(frame_DFS % 7 == 1){ ctx.strokeStyle="red"; }
  else{ ctx.strokeStyle="black"; }
  ctx.beginPath();
  ctx.moveTo(100,75);
  ctx.lineTo(60,140);
  ctx.stroke();
  ctx.closePath();

  if(frame_DFS % 7 == 2){ ctx.strokeStyle="red"; }
  else{ ctx.strokeStyle="black"; }
  ctx.beginPath();
  ctx.moveTo(100,75);
  ctx.lineTo(120,140);
  ctx.stroke();
  ctx.closePath();

  if(frame_DFS % 7 == 4 || frame_DFS % 7 == 5 || frame_DFS % 7 == 6){ ctx.strokeStyle="red"; }
  else{ ctx.strokeStyle="black"; }
  ctx.beginPath();
  ctx.moveTo(200,75);
  ctx.lineTo(180,140);
  ctx.stroke();
  ctx.closePath();

  ctx.strokeStyle="black";
  ctx.beginPath();
  ctx.moveTo(200,75);
  ctx.lineTo(240,140);
  ctx.stroke();
  ctx.closePath();

  ctx.fillStyle = 'blue';
  ctx.beginPath();
  ctx.arc(150, 20, 10, 0, 2 * Math.PI, false);
  ctx.closePath();
  ctx.fill();

  ctx.fillStyle = 'grey';
  ctx.beginPath();
  ctx.arc(100, 75, 10, 0, 2 * Math.PI, false);
  ctx.closePath();
  ctx.fill();
  ctx.beginPath();
  ctx.arc(200, 75, 10, 0, 2 * Math.PI, false);
  ctx.closePath();
  ctx.fill();

  ctx.beginPath();
  ctx.arc(60, 140, 10, 0, 2 * Math.PI, false);
  ctx.closePath();
  ctx.fill();
  ctx.beginPath();
  ctx.arc(120, 140, 10, 0, 2 * Math.PI, false);
  ctx.closePath();
  ctx.fill();
  ctx.beginPath();
  ctx.arc(240, 140, 10, 0, 2 * Math.PI, false);
  ctx.closePath();
  ctx.fill();
  ctx.fillStyle = 'red';
  ctx.beginPath();
  ctx.arc(180, 140, 10, 0, 2 * Math.PI, false);
  ctx.closePath();
  ctx.fill();
}

init();
