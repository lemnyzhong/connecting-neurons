// monitor asset
class monitor {
  float x, y, z, w, h;
  float theta;
  int flicker;
  
  monitor(float x, float y, float z, float w, float theta) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.w = w;
    this.h = w/2;
    
    this.theta = theta;
  }
  
  void load() {
    flicker = int(random(0, 5));
    
    pushMatrix();
    rotateX(this.theta);
    rotateY(this.theta);
    
    beginShape();
 
    beginShape();
    stroke(0);
   
    // flicker effect on monitors
    if(flicker == 1) {
      fill(255);
    }
    else {
      fill(0);
    }
    
    // begin drawing monitor shapes
    vertex(this.x - 30, this.y + 20, this.z);
    vertex(this.x - 30, this.y - 20, this.z);
    vertex(this.x + 30, this.y - 20, this.z);
    vertex(this.x + 30, this.y + 20, this.z);
    vertex(this.x - 30, this.y + 20, this.z); 
    endShape();
    
    beginShape();
    noStroke();
    fill(100);
    vertex(this.x - 30, this.y + 20, this.z + 2);
    vertex(this.x - 30, this.y + 20, this.z - 2);
    vertex(this.x + 30, this.y + 20, this.z - 2);
    vertex(this.x + 30, this.y + 20, this.z + 2);
    endShape();
      
    beginShape();
    noStroke();
    fill(100);
    vertex(this.x - 30, this.y - 20, this.z + 2);
    vertex(this.x - 30, this.y - 20, this.z - 2);
    vertex(this.x + 30, this.y - 20, this.z - 2);
    vertex(this.x + 30, this.y - 20, this.z + 2);
    endShape();
    
    beginShape();
    noStroke();
    fill(100);
    vertex(this.x - 30, this.y + 20, this.z - 2);
    vertex(this.x - 30, this.y - 20, this.z - 2);
    vertex(this.x - 30, this.y - 20, this.z + 2);
    vertex(this.x- 30, this.y + 20, this.z + 2);
    endShape();
    
    beginShape();
    noStroke();
    fill(100);
    vertex(this.x + 30, this.y + 20, this.z - 2);
    vertex(this.x + 30, this.y - 20, this.z - 2);
    vertex(this.x + 30, this.y - 20, this.z + 2);
    vertex(this.x + 30, this.y + 20, this.z + 2);
    endShape();
 
    beginShape();
    stroke(0);
    fill(100);
    vertex(this.x - 30, this.y + 20, this.z - 2);
    vertex(this.x - 30, this.y - 20, this.z - 2);
    vertex(this.x + 30, this.y - 20, this.z - 2);
    vertex(this.x + 30, this.y + 20, this.z - 2);
    vertex(this.x - 30, this.y + 20, this.z - 2);
    endShape();
    
    endShape();
    popMatrix();
  }
  
}
