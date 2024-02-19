// determines and generates what assets will be shown and where
class assets {
  // declaring asset variables
  float theta, phi;
  float x, y, z, w;
  float radius = currentWorld.get(0).radius;
  float type;
  int plantColour;
  
  // initialising function
  assets(int col) {
    this.theta = random(-PI, PI);
    this.phi = random(-PI, PI);
    this.w = random(10, 40);
    
    // mathematical equation so that the assets are generated on or very near
    // surface of the generated world, for more realistic effect
    // *Thank you MIT Maths on youtube*
    this.x = (radius + this.w/2) * sin(phi) * cos(theta);
    this.y = (radius + this.w/2) * sin(phi) * sin(theta);
    this.z = (radius + this.w/2) * cos(phi);
    
    // determines what type of asset will be added to list
    this.type = int(random(1, 8));
    
    // determines potential colour of plants
    this.plantColour = col;
  }
  
  void load() {
    // asset decider
    // based on the type int, will have a chance to generate one of 4 assets
    // box/brick, ball/bush, tree and monitor
    // some have a higher chance of being added
    if(this.type == 1 || this.type == 4 || this.type == 5) {
      box box = new box(this.x, this.y, this.z, this.w/3, this.theta);
      box.load();
    }
    if(this.type == 2 || this.type == 7) {
      ball ball = new ball(this.x, this.y, this.z, this.w/2, this.theta, this.plantColour);
      ball.load();
    }
    if(this.type == 3) {
      monitor monitor = new monitor(this.x, this.y, this.z, this.w, this.theta);
      monitor.load();
    }
    if(this.type == 6) {
      tree tree = new tree(this.x, this.y, this.z, this.w, this.w*2, this.plantColour);
      tree.load();
    }
  }
}

// function to add generated assets to asset arraylist
void generateAssets(int amount, int col) {
  for(int i = 0; i < amount; i++) {
    assetsList.add(new assets(col));
  }
}
