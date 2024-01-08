// determines aesthetics for generated world
class worlds {
  // declaring class variables
  float radius;
  float rotation;
  float distance;
  int isGaseous;
  color worldCol = color(int(random(0, 255)), int(random(0, 255)), int(random(0, 255)));
  
  worlds(int s) {
    this.radius = 500;
    this.rotation = 0;
    this.distance = 0;
    
    // isGaseous will mean that the world is generated with no stroke and is relatively 
    // see-through
    this.isGaseous = s;
  }
  
  void update() {
    // orbital rotation 
    rotateX(-1 * this.rotation);
    rotateY(0.5 * this.rotation);
    
    pushMatrix();
    // loads generated world
    loadWorld();  
    
    pushMatrix();
    
    // adds assets to the world
    for(assets asset : assetsList) {
      asset.load();
    }
    popMatrix();
    
    popMatrix();
    
    // allows for constant rotation
    if(isMoving == true) {
      this.rotation += 0.01;
    }
  }
  
  void loadWorld() {
    pushMatrix();
    strokeWeight(0.5);
    
    // isGaseous stroke determiner
    if(this.isGaseous == 0) {
      stroke(1);
    }
    else {
      noStroke();
    }
    
    // create sphere for world
    fill(worldCol);
    sphere(radius);
    popMatrix();
  }
}

// user scroll function to begin rotation
void mouseWheel() {
  if(isMoving == false) {
    isMoving = true;
  }
  else {
    isMoving = false;
  }
}
