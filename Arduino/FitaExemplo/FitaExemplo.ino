#include <FastLED.h>

FASTLED_USING_NAMESPACE
 
#if defined(FASTLED_VERSION) && (FASTLED_VERSION < 3001000)
#warning "Requires FastLED 3.1 or later; check github for latest code."
#endif

/* Code for testing the LED strip
 * Código para testar a fita LED */

#define DATA_PIN    3        //Data pin - Pino de dados ligado na fita
#define LED_TYPE    WS2812B  //LED strip type - Modelo da fita LED
#define COLOR_ORDER GRB      //Color Order - Ordem das cores
#define NUM_LEDS    30       //Number of LEDs - Número de LEDs na fita
CRGB leds[NUM_LEDS];

void setup() {
  // Configura a Fita LED
  FastLED.addLeds<LED_TYPE,DATA_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
}

void loop()
{
  // RGB color for each LED - Cor RGB de cada LED
  leds[0].r = 0;
  leds[0].g = 137;
  leds[0].b = 255;

  leds[1].r = 255;
  leds[1].g = 0;
  leds[1].b = 0;
  
  leds[2].r = 125;
  leds[2].g = 0;
  leds[2].b = 125;

  leds[3].r = 255;
  leds[3].g = 255;
  leds[3].b = 255;
  
  FastLED.show();  
  delay(500);
}
