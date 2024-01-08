class ball {
  float x, y, z, w;
  float theta;
  int plantColour;
  
  ball(float x, float y, float z, float w, float theta, int col) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.w = w;
    
    this.theta = theta;
    
    this.plantColour = col;
  }
  
  void load() {

    pushMatrix();
    translate(this.x, this.y, this.z);
    rotateZ(this.theta);
    
    
    if(this.plantColour == 1) {
      fill(57,115,27);
    }
    if(this.plantColour == 2) {
      fill(58,164,12);
    }
    if(this.plantColour == 3) {
      fill(30,88,0);
    }
    if(this.plantColour >= 4) {
      fill(18,54,0);
    }
    noStroke();
    sphere(this.w);
    popMatrix();
  }
}
