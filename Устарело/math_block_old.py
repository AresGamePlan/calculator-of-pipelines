import math

"""ВХОДНЫЕ ТЕСТОВЫЕ ДАННЫЕ"""

# ГЕОМЕТРИЧЕСКИЕ ПАРАМЕТРЫ ТРУБЫ И ОБОЛОЧКИ
# Параметры трубы
Dy_t = 32                    # Ду трубы, мм (C5)
h_t = 2.5                    # Толщина стенки трубы, мм (D5)

# Параметры оболочки
Dy_o = 125                   # Ду оболочки, мм (E5)
h_o = 2.5                    # Толщина оболочки, мм (H5)
shell_diameter = 125         # Диаметр оболочки (BA5)
shell_wall_thickness = 2.5   # Толщина стенки оболочки (BB5)

# Общие параметры изделия
length = 12000               # Длина изделия, мм (J5)
order_metrs = 2              # Заказ метров (мп) (G5)

# ПАРАМЕТРЫ ЗАЛИВКИ И МАТЕРИАЛОВ ППУ
p_PPU = 70                   # Заданная плотность ППУ кг/м3 (AG5)
a_machine = 2                # Производительность залив машины кг/час (AH5)

# Соотношение компонентов А/Б
a = 100                      # Компонент A (AJ5)
b = 160                      # Компонент B (AK5)

# СТОИМОСТЬ МАТЕРИАЛОВ (без НДС, тенге)
cost_of_steel_pipe_no_VAT = 330360              # Стоимость стальной трубы тенге/тн (AO5)
cost_cupper_wire_no_VAT = 110.72                # Стоимость медного провода тенге/мп (AQ5)
cost_foam_components_no_VAT = 1517               # Стоимость пенокомпонентов тенге/кг (AT5)
cost_centralizer_no_VAT = 115.86                 # Стоимость центратора тенге/шт (AX5)
cost_of_the_shell_with_transport_no_VAT = 868.505  # Стоимость оболочки с транспортом тенге/м (BC5)

# ЭНЕРГОЗАТРАТЫ
electricity = 3              # Электроэнергия, кВт (U5)
cost_one_kWt_hour = 23       # Стоимость 1 кВт/час, тенге (BF5)

# ТРУДОЗАТРАТЫ И ПРОИЗВОДСТВЕННЫЕ ПАРАМЕТРЫ
number_of_pipes_per_shift = 40  # Количество труб в 1 смены (V5)
number_of_workers = 3           # Количество рабочих (W5)

# ЗАРАБОТНАЯ ПЛАТА (нетто, тенге)
salary_gross_netto_сenterers = 500_000  # ЗП Центровщики (BK5)
salary_gross_netto_filler = 500_000     # ЗП Заливщик (BN5)
overhead_costs_from_the_workers_wage_fund = 50 #Накладные рассходы % от фонда оплаты труда рабочих

# НАЛОГИ С ФОТ ЗА СЧЕТ РАБОТОДАТЕЛЯ (%)
CO = 4        # СО (BP5)
OPVR = 2.5    # ОПВР (BQ5)
CH = 5.18     # СН (BR5)
OOCMC = 3     # ООСМС (BS5)

# ФИНАНСОВЫЕ ПАРАМЕТРЫ
VAT = 1.12           # НДС
marginality = 30     # Маржинальность % (AD5)

"""КОНЕЦ ВХОДНЫХ ДАННЫХ"""

"""РАСЧЕТНЫЕ ФУНКЦИИ"""
#Вес стальной трубы 1мп, кг (I5)
def weight_of_steel_wire(Dy_t, h_t):
    x = (math.pow(Dy_t / 1000, 2))
    y = (math.pow((Dy_t-2*h_t)/1000,2))
    return 7850 * 3.14 * (x - y) / 4

#Длина стальной трубы, м (K5)
def length_of_steel_pipe(l):
    return l / 1000

#Длина ПЭ-оболочки, мм (L5)
def length_of_PE_sheath(l):
    return l - (l*0.3/12)

#Пенокомпоненты (всего), кг вт.ч. А+Б (M5)
def foam_components(Dy_o, h_o, Dy_t, length_of_steel_pipe, p_PPU):
    stage1 = Dy_o - (h_o*2)
    stage2 = stage1 / 1000
    stage3 = stage2 * stage2
    stage4 = stage3 / 4 * 3.14
    stage6 = Dy_t / 1000
    stage7 = stage6 * stage6
    stage8 = stage7 / 4 * 3.14
    stage9 = stage4 - stage8
    return stage9 * length_of_steel_pipe / 1000 * p_PPU

# Заливка, секунды (AI5)
def filling(foam_components, a_machine):
    return foam_components, a_machine

#Компонент А (Полиол), кг (N5)
def component_A(foam_components, a, b):
    stage1 = a + b
    stage2 = stage1 / 100
    return foam_components / stage2

#Компонент В (Изоционат), кг (O5)
def component_B(component_A, b):
    return component_A * b / 100

#Количество стальной трубы, кг (P5)
def quantity_of_steel_pipe(weight_of_steel_wire, length_of_steel_pipe):
    return weight_of_steel_wire * length_of_steel_pipe

#Количество ПЭ оболочки, мп (Q5)
def quantity_of_PE(length_of_PE_sheath):
    return length_of_PE_sheath / 1000

#Провод медный ММ 1х1.5 мм2, кг (R5)
def copper_wire(length_of_steel_pipe):
    return (length_of_steel_pipe + 0.6) * 0.014 * 2

#Центраторы, сегменты (наименование) (S5)
centralizers_segments = "42/125"

#Расход центраторов, сегментов, шт (T5)
consumption_of_centralizers_segments = length_of_steel_pipe(length)

#Заработная плата Оклад Брутто тенге/месяц 
def salary_gross_brutto(salary_gross_netto):
    return (salary_gross_netto - 4830)/0.792

#Заработная плата Оклад Брутто (Цетровщики) тенге/месяц (BJ5)
salary_gross_brutto_centerers = salary_gross_brutto(salary_gross_netto_сenterers)

#Заработная плата Оклад Брутто (Заливщик) тенге/месяц (BM5)
salary_gross_brutto_filler = salary_gross_brutto(salary_gross_netto_filler)

#Стоимость работы на 1 трубу (X5)
def cost_of_work_for_one_pipe(salary_gross_brutto_filler, number_of_workers, salary_gross_brutto_centerers, number_of_pipes_per_shift):
    stage1 = salary_gross_brutto_filler * 2
    stage2 = (number_of_workers - 2) * salary_gross_brutto_centerers
    stage3 = (stage1 + stage2) / 25
    return stage3 / number_of_pipes_per_shift

#Налоги с ФОТ за счет работодателя (Y5)
def payroll_taxes_at_the_expense_of_the_employer(CO, OPVR, CH, OOCMC, cost_of_work_for_one_pipe):
    stage1 = CO + OPVR + CH + OOCMC
    stage2 = stage1 / 100 * cost_of_work_for_one_pipe
    return stage2

#Накладные рассходы (Z5)
def overheads(cost_of_work_for_one_pipe, overhead_costs_from_the_workers_wage_fund):
    return cost_of_work_for_one_pipe * overhead_costs_from_the_workers_wage_fund / 100

#Себестоимость 1 шт изделия без НДС (AA5)
def cost_price_of_one_piece_of_product_without_VAT(
        foam_components, 
        cost_foam_components_no_VAT, 
        quantity_of_steel_pipe, 
        cost_of_steel_pipe_no_VAT,
        quantity_of_PE, 
        cost_of_the_shell_with_transport_no_VAT,
        copper_wire,
        cost_cupper_wire_no_VAT,
        consumption_of_centralizers_segments,
        cost_centralizer_no_VAT,
        length,
        electricity,
        cost_one_kWt_hour,
        cost_of_work_for_one_pipe,
        payroll_taxes_at_the_expense_of_the_employer,
        overheads
        ):
    stage1 = (foam_components * cost_foam_components_no_VAT) + (quantity_of_steel_pipe * cost_of_steel_pipe_no_VAT / 1000)
    stage2 = (quantity_of_PE * cost_of_the_shell_with_transport_no_VAT) + (copper_wire * cost_cupper_wire_no_VAT) + (consumption_of_centralizers_segments * cost_centralizer_no_VAT * length / 1000)
    stage3 = (electricity * cost_one_kWt_hour) + cost_of_work_for_one_pipe +payroll_taxes_at_the_expense_of_the_employer + overheads
    return stage1 + stage2 + stage3

#Себестоимость 1 мп трубы без НДС тенге (AB5)
def cost_price_of_one_mp_of_pipe_no_VAT(_cost_price_of_one_piece_of_product_without_VAT):
    return _cost_price_of_one_piece_of_product_without_VAT / 12

#Себестоимость 1 мп трубы с НДС тенге (AC5)

def cost_price_of_one_mp_of_pipe_with_VAT(_cost_price_of_one_mp_of_pipe_no_VAT, VAT):
    return _cost_price_of_one_mp_of_pipe_no_VAT * VAT

#Стоимость заказа с НДС (AE5)
def order_cost_with_VAT(
        _cost_price_of_one_mp_of_pipe_with_VAT,
        order_metrs,
        marginality,
):
    stage1 = _cost_price_of_one_mp_of_pipe_with_VAT * order_metrs / 12
    stage2 = 1 + (marginality/100)
    return stage1 * stage2

"""КОНЕЦ РАСЧЕТНЫХ ФУНКЦИЙ"""

"""АЛГОРИТМ РАСЧЕТА"""
def calculate(
        Dy_t,
        h_t,
        Dy_o,
        h_o,
        shell_diameter,
        shell_wall_thickness,
        length,
        order_metrs,
        p_PPU,
        a,
        b,
        cost_of_steel_pipe_no_VAT,
        cost_cupper_wire_no_VAT,
        cost_foam_components_no_VAT,
        cost_centralizer_no_VAT,
        cost_of_the_shell_with_transport_no_VAT,
        electricity,
        cost_one_kWt_hour,
        number_of_pipes_per_shift,
        number_of_workers,
        salary_gross_netto_сenterers,
        salary_gross_netto_filler,
        overhead_costs_from_the_workers_wage_fund,
        CO,
        OPVR,
        CH,
        OOCMC,
        VAT,
        marginality
        ):
    _weight_of_steel_wire = weight_of_steel_wire(Dy_t, h_t)
    _length_of_steel_pipe = length_of_steel_pipe(length)
    _length_of_PE_sheath = length_of_PE_sheath(length)
    _foam_components = foam_components(Dy_o, h_o, Dy_t, _length_of_PE_sheath, p_PPU)
    _filling = filling(_foam_components, a_machine)
    _component_A = component_A(_foam_components, a, b)
    _component_B = component_B(_component_A, b)
    _quantity_of_steel_pipe = quantity_of_steel_pipe(_weight_of_steel_wire, _length_of_steel_pipe)
    _quantity_of_PE = quantity_of_PE(_length_of_PE_sheath)
    _copper_wire = copper_wire(_length_of_steel_pipe)
    _consumption_of_centralizers_segments = _length_of_steel_pipe
    _salary_gross_brutto_centerers = salary_gross_brutto(salary_gross_netto_сenterers)
    _salary_gross_brutto_filler = salary_gross_brutto(salary_gross_netto_filler)
    _cost_of_work_for_one_pipe = cost_of_work_for_one_pipe(_salary_gross_brutto_filler, number_of_workers, _salary_gross_brutto_centerers, number_of_pipes_per_shift)
    _payroll_taxes_at_the_expense_of_the_employer = payroll_taxes_at_the_expense_of_the_employer(CO, OPVR, CH, OOCMC, _cost_of_work_for_one_pipe)
    _overheads = overheads(_cost_of_work_for_one_pipe, overhead_costs_from_the_workers_wage_fund)
    _cost_price_of_one_piece_of_product_without_VAT = cost_price_of_one_piece_of_product_without_VAT(_foam_components,
                                                                                                     cost_foam_components_no_VAT,
                                                                                                     _quantity_of_steel_pipe,
                                                                                                     cost_of_steel_pipe_no_VAT,
                                                                                                     _quantity_of_PE,
                                                                                                     cost_of_the_shell_with_transport_no_VAT,
                                                                                                     _copper_wire,
                                                                                                     cost_cupper_wire_no_VAT,
                                                                                                     _consumption_of_centralizers_segments,
                                                                                                     cost_centralizer_no_VAT,length,
                                                                                                     electricity,
                                                                                                     cost_one_kWt_hour,
                                                                                                     _cost_of_work_for_one_pipe,
                                                                                                     _payroll_taxes_at_the_expense_of_the_employer,
                                                                                                     _overheads)
    _cost_price_of_one_mp_of_pipe_no_VAT = cost_price_of_one_mp_of_pipe_no_VAT(_cost_price_of_one_piece_of_product_without_VAT)
    _cost_price_of_one_mp_of_pipe_with_VAT = cost_price_of_one_mp_of_pipe_with_VAT(_cost_price_of_one_mp_of_pipe_no_VAT, VAT)
    _order_cost_with_VAT = order_cost_with_VAT(_cost_price_of_one_mp_of_pipe_with_VAT, order_metrs, marginality) #19

    return (_weight_of_steel_wire, 
            _length_of_steel_pipe, 
            _length_of_PE_sheath, 
            _foam_components,
            _filling, 
            _component_A, 
            _component_B, 
            _quantity_of_steel_pipe,
            _quantity_of_PE,
            _copper_wire,
            _consumption_of_centralizers_segments,
            _salary_gross_brutto_centerers,
            _salary_gross_brutto_filler,
            _cost_of_work_for_one_pipe,
            _payroll_taxes_at_the_expense_of_the_employer,
            _overheads,
            _cost_price_of_one_piece_of_product_without_VAT,
            _cost_price_of_one_mp_of_pipe_no_VAT,
            _cost_price_of_one_mp_of_pipe_with_VAT,
            _order_cost_with_VAT
            )


"""ТЕСТ МОДУЛЯ"""
if __name__ == "__main__":
    #print(order_cost_with_VAT(_cost_price_of_one_mp_of_pipe_with_VAT, order_metrs, marginality))
    out = calculate(
        Dy_t,
        h_t,
        Dy_o,
        h_o,
        shell_diameter,
        shell_wall_thickness,
        length,
        order_metrs,
        p_PPU,
        a,
        b,
        cost_of_steel_pipe_no_VAT,
        cost_cupper_wire_no_VAT,
        cost_foam_components_no_VAT,
        cost_centralizer_no_VAT,
        cost_of_the_shell_with_transport_no_VAT,
        electricity,
        cost_one_kWt_hour,
        number_of_pipes_per_shift,
        number_of_workers,
        salary_gross_netto_сenterers,
        salary_gross_netto_filler,
        overhead_costs_from_the_workers_wage_fund,
        CO,
        OPVR,
        CH,
        OOCMC,
        VAT,
        marginality
        )[-1]
    print(out)
