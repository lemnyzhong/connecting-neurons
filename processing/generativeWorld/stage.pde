void setStage() {
  camZoom();
}

// camera zoom functionality
// allows user to zoom in and out using the up and down arrow keys
void camZoom() {
  if(zoom == true) {
    if(keyCode == UP) {
      distanceFromWorld += 3;
    }
    
    if(keyCode == DOWN) {
      distanceFromWorld -= 3;
    }
  }
}

// ensure zoom starts and is able to stop
void keyPressed() {
  zoom = true;
}
void keyReleased() {
  zoom = false;
}
