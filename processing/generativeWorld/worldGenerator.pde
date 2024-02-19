// all packages/library imports required for program
import processing.sound.*;
import com.krab.lazy.*;

/* GLOBAL VARIABLE DECLARATIONS */
/* Audio input and analyses variables */
AudioIn in;
Amplitude amp;
FFT fft;

// background music
SoundFile backtrack;
SoundFile clickInteraction;

// For FFT analysis and conversion of input recording
int freqBands = 512;    // can be any multiple of 2, however, any excess over 512 may be unnecessary for this program
float[] freqSpectrum = new float[freqBands]; // sets a float array for all the frequencies from FFT analysis
float fftTotal = 0;
float fftMin;
float fftMax;

// For amplitude analysis on input recording
FloatList amplitudes = new FloatList();    // using FloatList for easier list manipulation, mainly .clear() and .append()
float ampMin;
float ampMax;

// Recording booleans for input audio
boolean isRecording = false;
int recordingTimer = 11;

/* Stage Variables (background, lighting and camera movement) */
int distanceFromWorld = -100;
boolean zoom = false;

/* Assets */
ArrayList<assets> assetsList = new ArrayList<assets>();    // ArrayList to store all generated assets
float assetAmount = 0;

/* World variables */
// background variables that affect asset generation
color backgroundColour;
int backgroundRed;
int backgroundBlue;
int backgroundGreen;
int backgroundAverage;

// ArrayList to store current generated world, this should only ever be size of 1
// Does not save previous generated worlds, just incase of performance issues,
// especially due to the amount of potential assets generated, which will already affect performance
ArrayList<worlds> currentWorld = new ArrayList<worlds>();    

// Variable to detect whether world is rotating
boolean isMoving;

/* UI variables */
//backgroundButton setBackground = new backgroundButton(100, 100);
LazyGui gui;

void setup() {
  // window setup
  surface.setTitle("Welcome to generator: world");
  size(1400, 800, P3D);
  frameRate(60);
  
  // initiating input sound analysis variables 
  amp = new Amplitude(this);
  fft = new FFT(this, freqBands);
  in = new AudioIn(this, 0);
  
  // pairing input source to input sound analysis objects
  amp.input(in);
  fft.input(in);
  
  // initiating LazyGui with preset GUI options
  // this loads LazyGui with defined cellSize and
  // font size
  gui = new LazyGui(this, new LazyGuiSettings()
              .setLoadLatestSaveOnStartup(false)
              .setAutosaveOnExit(false)
              .setCellSize(36)
              .setMainFontSize(11)
              .setSideFontSize(8)
              );
  
  // background music
  backtrack = new SoundFile(this, "sounds/peaceful.wav");
  clickInteraction = new SoundFile(this, "sounds/click.wav");
  
  backtrack.play(1, 0.35);    // play backtrack on startup
  
  // generates sample world on startup, this requires no
  // sound input to be analysed and is a random generation
  // to provide the user with an initial idea of what to
  // expect
  currentWorld.add(new worlds(int(random(-1, 2))));
  generateAssets(int(random(0, 600)), int(random(1, 4)));
}


void draw() {
  /* Load GUI components and assets*/
  // folder containing toggle for tips on how to use the program
  // contains zoom, rotate and record
  // if toggle is true, it will reveal the tip
  
  // zoom tip toggle
  if(gui.toggle("how to:/zoom") == true) {
    gui.text("how to:/tip: zoom", "use up and down arrow \nkeys to move");
    gui.show("how to:/tip: zoom");
  }
  // if false, tip will be hidden from view for cleaner aesthetic
  else {
    gui.hide("how to:/tip: zoom");
  }
  
  // rotate tip toggle
  if(gui.toggle("how to:/rotate") == true) {
    gui.text("how to:/tip: rotate", "use mouse scroll wheel \nto rotate world");
    gui.show("how to:/tip: rotate");
  }
  else {
    gui.hide("how to:/tip: rotate");
  }
  
  // record tip toggle
  if(gui.toggle("how to:/record") == true) {
    gui.text("how to:/tip: record", "please select recordings \nand click record");
    gui.show("how to:/tip: record");
  }
  else {
    gui.hide("how to:/tip: record");
  }
  
  // save background colour variable to the results of the LazyGui colour picker
  // component, returns hex value and stores in variable
  backgroundColour = color(gui.colorPicker("background").hex);
  
  // sets background colour to the results of LazyGui colour picker
  background(backgroundColour);
  
  // unneccessary default LazyGui option
  gui.hide("saves");
  
  /* World Generation */
  // note: generation can only happen once an input sound has been recorded,
  // otherwise it will not generate and provide a notice "check mic"
  
  // generate button
  // once input sound has been recorded and analyzed (see further below)
  // the generate button will allow the user to utilise the values returned 
  // from the sound analysis (amp and fft) to generate a world with distinct
  // aesthetic choices depending on the analysis results
  if(gui.button("generate")) {
    // determines the average value derived from the background colour
    // this will determine the colour of the "plants"
    backgroundAverage = (backgroundRed + backgroundBlue + backgroundGreen) / 3;
    
    // error checker: no input sound recorded
    // this will check if there was an input sound received and recorded,
    // if not, this will create a notice to "check mic"
    if(amplitudes.size() == 0 || fftTotal == 0) {
      gui.text("no signal! \ncheck mic");
      gui.show("no signal! \ncheck mic");
    }
    // there is an input sound recorded
    if(amplitudes.size() != 0 && fftTotal != 0) {
      gui.hide("no signal! \ncheck mic");
      
      // clear current generated world, for new one
      currentWorld.clear();
      // initialise new world object with new aesthetic (solid or gaseous)
      currentWorld.add(new worlds(int(map(fftMax, 0, 1, 0, 2))));
      
      // clear all assets and their placements
      assetsList.clear();
      
      // set new amount of assets to be generated, mapped to maximum amplitude
      // of recorded input sound, lower amplitude, the less assets
      // and the average background colour value determines the colour of the 
      // "plants"
      generateAssets(ceil(map(ampMax, 0, 1.5, 0, 600)), int(map(backgroundAverage, 0, 255, 1, 5)));
    }
    
    // reset values once generation is complete
    // to ensure each generation has no noise from any previous inputs
    backgroundRed = 0;
    backgroundBlue = 0;
    backgroundGreen = 0;
    backgroundAverage = 0;
    fftTotal = 0;
  }
  
  /* Recording input sounds for analysis */
  // if toggle is true the program will begin recording the input
  // sounds from mic and
  if(gui.toggle("recordings/recording") == true) {
    isRecording = true;
    
    // stop backtrack music, so as to not interfere with recording
    backtrack.stop();
    
    // countdown functionality
    // 11 second count down from when user toggles record
    if(amplitudes.size() > 0 && recordingTimer == 11) {
      amplitudes.clear();
      freqSpectrum = new float[freqBands];
      ampMax = 0;
      fftTotal = 0;
    }
    
    // framerate counter to ensure recordingTimer counts down roughly
    // every second
    if(frameCount % 60 == 0) {
      recordingTimer -= 1;
    }
    
    // show "Recording signal!" message to notify user recording is happening
    gui.text("recordings/Recording signal!");
    
    // countdown timer message and input sound collecting
    // posts countdown message of how much time is left for recording
    if(recordingTimer > 0 && recordingTimer < 11) {
      pushMatrix();
      gui.hide("recordings/signal received!");
      gui.text("recordings/" + str(recordingTimer) + " seconds");
      gui.show("recordings/Recording signal!");
      gui.show("recordings/" + str(recordingTimer) + " seconds");
      popMatrix();
      
      // collected input sound amplitudes analyzed and appended to dedicated amplitude
      // list
      amplitudes.append(amp.analyze());
      // FFT analysis of FFTseries array (freqSpectrum) with size of FreqBands
      fft.analyze(freqSpectrum);
    }
    
    // Countdown timer ends, analysis of input sound finalised
    // and stored into variables required for world generation
    if(recordingTimer <= 0 && recordingTimer >= -1) {
      // show received (completion) message
      pushMatrix();
      gui.text("recordings/signal received!");
      gui.show("recordings/signal received!");
      popMatrix();
      
      pushMatrix();
      gui.hide("recordings/Recording signal!");
      for(int i = 0; i < 11; i++) {
        gui.hide("recordings/" + str(i) + " seconds");
      }
      popMatrix();
      
      // reset recording variables
      recordingTimer = 11;    // timer
      isRecording = false;    // recording boolean
      gui.toggleSet("recordings/recording", false);    // reset LazyGui recording toggle button to false
      
      // save max amplitude to variable
      ampMax = amplitudes.max();
      
      // fft min and max calculator function
      // determines the fftMin and fftMax values present in recording
      fftMin = freqSpectrum[0];
      fftMax = freqSpectrum[0];
      
      for(int i = 0; i < freqBands; i++) {
        fftTotal += freqSpectrum[i];
        
        if(freqSpectrum[i] < fftMin) {
          fftMin = freqSpectrum[i];
        }
        if(freqSpectrum[i] > fftMax) {
          fftMax = freqSpectrum[i];
        }
      }  
      
      // finds each RGB int value of currently set background colour
      // affects colour of certain assets (plants)
      backgroundRed = int(red(backgroundColour));
      backgroundBlue = int(blue(backgroundColour));
      backgroundGreen = int(green(backgroundColour));
      
      // restart backtrack once recording is done
      backtrack.play(1, 0.35);
    }
    
  }
  
  // set lights function for more 3D effects and adds depth for objects
  lights();
  
  // updates current world, so rotation and asset animation occurs
  translate(width/2, 1000, distanceFromWorld);
  currentWorld.get(0).update();
  
  // allows camera (zoom) to function using arrows up and down key
  setStage();
  
  // check if backtrack is playing, if not restart
  if(!backtrack.isPlaying() && isRecording == false) {
    backtrack.play(1, 0.35);
  }
}

// mouse click function to generate selection sound for more immersive interaction
void mousePressed() {
  if(!clickInteraction.isPlaying()) {
    clickInteraction.play(1, 0.25);
  }
  else {
    clickInteraction.stop();
    clickInteraction.play(1, 0.25);
  }
}
