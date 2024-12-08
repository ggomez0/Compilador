#include <nombreDeLibreria.Extension>
#include <servo.h>
int MD1;
int MD2 = 3;
void setup(){
    pinMode(MD1, INPUT);
    pinMode(MD2, OUTPUT);

}
void loop(){
avanzar();
esperar(10);
giro_izquierda();
parar();

}
