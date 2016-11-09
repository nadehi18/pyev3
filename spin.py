import ev3dev.ev3 as ev3
from time import sleep

motor_b = ev3.LargeMotor(address='outB')
motor_c = ev3.LargeMotor(address='outC')

motor_b.command = 'run-direct'
motor_c.command = 'run-direct'

while True:

    motor_b.duty_cycle_sp = 50
    motor_c.duty_cycle_sp = -50

    sleep(.1)

    motor_b.duty_cycle_sp = 0
    motor_c.duty_cycle_sp = 0

