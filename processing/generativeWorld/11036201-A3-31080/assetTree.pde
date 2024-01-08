// tree asset
class tree {
  float x, y, z, w, h;
  float theta = 0;
  int plantColour;
  
  tree(float x, float y, float z, float w, float h, int col) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.w = w;
    this.h = h;
    this.plantColour = col;
    
  }
  
  void load() {
    beginShape();
    
    // specific rotation of tree object to generate right side up
    // unfortunately does not work properly
    if(this.y < 0) {
      this.theta = PI;
      rotateY(this.theta);
    }
    if(this.x < 0) {
      this.theta = PI;
      rotateZ(this.theta);
    }
    if(this.z < 0) {
      this.theta = PI/4;
      rotateX(this.theta);
    }
    
    if(this.y > 0) {
      this.theta = -PI;
      rotateY(this.theta);
    }
    if(this.x > 0) {
      this.theta = -PI;
      rotateZ(this.theta);
    }
    if(this.z > 0) {
      this.theta = -PI/4;
      rotateX(this.theta);
    }

    pushMatrix();
    translate(this.x, this.y + 20, this.z);
    stroke(0.1);
    fill(77, 51, 18);
    box(this.w/3, this.h + 10, this.w/2);
    popMatrix();
    
    pushMatrix();
    translate(this.x, this.y - 20, this.z);
    stroke(61, 92, 34);
    strokeWeight(0.05);
    if(this.plantColour == 1) {
      fill(48, 84, 18);
    }
    if(this.plantColour == 2) {
      fill(78, 122, 40);
    }
    if(this.plantColour == 3) {
      fill(120, 69, 25);
    }
    if(this.plantColour >= 4) {
      fill(168, 86, 50);
    }
    sphere(this.w);
    popMatrix();
    endShape();
  }
}
