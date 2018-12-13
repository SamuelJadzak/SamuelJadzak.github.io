function setup() {

  createCanvas(640, 480);
}

function draw() {
    if (mouseIsPressed) {
      fill(0);
    } else {
      if (pmouseX != mouseX) {
	 fill( random(0,256),random(0,256),random(0,256) );
      }
    } 
    rect(mouseX, mouseY, 80, 80);
}
