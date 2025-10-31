import eel
import sys
import math_block

data = []

eel.init('web')

@eel.expose
def calculate(Dy_t, h_t, shell_diameter, order_metrs):
    global data
    data = math_block.calculate_for_app(Dy_t, h_t, shell_diameter, order_metrs)
    return

@eel.expose
def on_close_window():
    print("Окно закрыто пользователем")
    sys.exit()

@eel.expose
def get_data():
    global data
    return data

eel.start('index.html')