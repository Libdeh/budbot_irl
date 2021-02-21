#include <LiquidCrystal.h>
 
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
 
void setup() {​​​​​​
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.print("budbot.irl");
}​​​​​​
 
void loop() {​​​​​​
  if (Serial.available()) {​​​​​​
    delay(100); //wait some time for the data to fully be read
    lcd.clear();

    // set the cursor to (16,1):
    lcd.setCursor(16,1);

    while (Serial.available() > 0) {​​​​​​
      lcd.autoscroll();  // set the display to automatically scroll:
      char c = Serial.read();
      lcd.write(c); 
      delay(500);      
    }​​​​​​
  }​​​​​​
}​​​​​​
