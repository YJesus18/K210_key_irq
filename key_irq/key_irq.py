import utime
from Maix import GPIO
from fpioa_manager import fm

#定义全局变量
io_led_g = 12
io_led_r = 13
io_led_b = 14

io_boot_key = 16

#注册外设资源到相应的引脚上
fm.register(io_led_g, fm.fpioa.GPIO0)
fm.register(io_led_r, fm.fpioa.GPIO1)
fm.register(io_led_b, fm.fpioa.GPIO2)
#GPIOHS为高速GPIO，只有GPIOHS支持中断
fm.register(io_boot_key, fm.fpioa.GPIOHS0)

led_g = GPIO(GPIO.GPIO0, GPIO.OUT)
led_r = GPIO(GPIO.GPIO1, GPIO.OUT)
led_b = GPIO(GPIO.GPIO2, GPIO.OUT)

key = GPIO(GPIO.GPIOHS0, GPIO.IN, GPIO.PULL_UP)

led_g .value(1)
led_r .value(1)
led_b .value(1)

led_state = True

#中断回调函数
def test_irq(key):
    global led_state
    utime.sleep_ms(20)#消除按键抖动
    if key.value() == 0:
        led_state = not led_state
        led_b.value(led_state)

#进入程序死循环
while(1):
            #回调函数名 #中断触发方式
    key.irq(test_irq, GPIO.IRQ_FALLING)

#禁用中断
#key.disirq()
