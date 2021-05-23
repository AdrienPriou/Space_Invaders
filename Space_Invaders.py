from pyb import SPI, UART, Pin, delay, LED
import machine

precision = 300
led1 = LED(1)
led2 = LED(2)
led3 = LED(3)
led4 = LED(4)

Uart = UART(2, 115200)
Size_width = 300
Size_height = 50
coo_x = 50

class Starship_S:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin

Starship = Starship_S(x=Size_width//2, y=50, skin="\_/|\_/")

class Invaders_Mob:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin

Invader1 = Invaders_Mob(x=coo_x, y=10, skin="[-=-]")
Invader2 = Invaders_Mob(x=65, y=15, skin="|\"/|")
Invader3 = [Invaders_Mob(x=coo_x, y=20, skin="[-=-]")]

class Bullet_B:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin
        
Bullet = Bullet_B(x=Starship.x, y=Starship.y, skin = "|")
Group_bullet = []

CS = Pin("PE3", Pin.OUT_PP)

SPI_1 = SPI(
    1, 
    SPI.MASTER,
    baudrate=50000,
    polarity=0,
    phase=0,
)

def read_reg(addr):
    CS.low()
    SPI_1.send(addr | 0x80) 
    tab_values = SPI_1.recv(1) 
    CS.high()
    return tab_values[0]

def write_reg(addr, value):
    CS.low()
    SPI_1.send(addr | 0x00)
    SPI_1.send(value)
    CS.high()

def convert_value(high, low):
    value = (high << 8) | low
    if value & (1 << 15):
       value = value - (1 << 16)
    return value * 2000 / 32768

def read_acceleration(base_addr):
    low = read_reg(base_addr)
    high = read_reg(base_addr + 1)
    return convert_value(high, low)

def clear_screen():
    Uart.write("\x1b[2J\x1b[?25l")

def move(x, y):
    Uart.write("\x1b[{};{}H".format(y, x))

def x_pos():
    x_accel = read_acceleration(0x28)
    return x_accel >= precision
   
def x_neg():
    x_accel = read_acceleration(0x28)
    return x_accel <= -precision

def push_button():
    push_button = pyb.Pin("PA0", pyb.Pin.IN, pyb.Pin.PULL_DOWN)
    return push_button


if __name__ == "__main__":

    addr_who_am_i = 0x0F
    print(read_reg(addr_who_am_i))
    addr_ctrl_reg4 = 0x20
    write_reg(addr_ctrl_reg4, 0x77)

clear_screen()

while Invader1.x < 280:
    move(Invader1.x, Invader1.y)
    Uart.Write(" "+Invader1.skin+" ")
    Invader1.x += 10

while Invader2.x < 275:
    move(Invader2.x, Invader2.y)
    Uart.Write(" "+Invader2.skin+" ")
    Invader2.x += 10

while Invader3.x < 280:
    move(Invader3.x, Invader3.y)
    Uart.Write(" "+Invader3.skin+" ")
    Invader3.x += 10

while(True):

    if x_pos() == True and Starship.x < 300:
        led2.off()
        led3.off()
        led1.on()
        Starship.x+=1
        move(Starship.x, Starship.y)
        
        Uart.write(" "+Starship.skin+" ")   
        delay(50)

    elif x_neg() == True and Starship.x > 10:
        led2.on()
        led1.off()
        led3.off()
        Starship.x-=1
        move(Starship.x, Starship.y)
        
        Uart.write(" "+Starship.skin+" ")
        delay(50)