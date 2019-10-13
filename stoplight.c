#include <avr/io.h>
#include <util/delay.h>

#define RED      PB0
#define YELLOW   PD7
#define GREEN    PD6

#define DELAYTIME 1000

#define setBit(sfr, bit)     (_SFR_BYTE(sfr) |= (1 << bit))
#define clearBit(sfr, bit)   (_SFR_BYTE(sfr) &= ~(1 << bit))
#define toggleBit(sfr, bit)  (_SFR_BYTE(sfr) ^= (1 << bit))

void setOutput();

int main(void) {
	setOutput();
	while (1) {
		setBit(PORTB, RED);
		_delay_ms(60000);
		clearBit(PORTB, RED);
		setBit(PORTD, YELLOW);
		_delay_ms(5000);
		clearBit(PORTD, YELLOW);
		setBit(PORTD, GREEN);
		_delay_ms(55000);
		clearBit(PORTD, GREEN);

		(_SFR_BYTE(PORTB)
		 ^=
		 (
		  1 <<
		  RED));
	}
	return 0;
}

void setOutput() {
	setBit(DDRB, RED);
	setBit(DDRD, YELLOW);
	setBit(DDRD, GREEN);
}
