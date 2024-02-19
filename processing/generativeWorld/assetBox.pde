// brick asset
class box {
  float x, y, z, w, h;
  float theta;
  
  box(float x, float y, float z, float w, float theta) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.w = w;
    this.h = w/2;
    
    this.theta = theta;
  }
  
  void load() {
    pushMatrix();
    translate(this.x, this.y, this.z);
    rotateX(this.theta/2);
    fill(66, 50, 29);
    stroke(0);
    box(this.w, this.h, this.h);
    popMatrix();
  }
}
