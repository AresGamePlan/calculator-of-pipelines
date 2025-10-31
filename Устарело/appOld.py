import tkinter as tk
from tkinter import ttk
import math

# Данные пресетов
PRESETS = {
    1: {'name': 'Ду32×2.5/125×2.5', 'Dy_t': 32.0, 'h_t': 2.5, 'Dy_o': 125.0, 'h_o': 2.5, 'shell_diameter': 125.0, 'shell_wall_thickness': 2.5, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 115.85999999999999, 'cost_of_the_shell_with_transport_no_VAT': 868.505, 'electricity': 3.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 40, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    2: {'name': 'Ду38×2.5/125×2.5', 'Dy_t': 38.0, 'h_t': 2.5, 'Dy_o': 125.0, 'h_o': 2.5, 'shell_diameter': 125.0, 'shell_wall_thickness': 2.5, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 115.85999999999999, 'cost_of_the_shell_with_transport_no_VAT': 868.505, 'electricity': 3.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 40, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    3: {'name': 'Ду48×2.8/125×2.5', 'Dy_t': 48.0, 'h_t': 2.8, 'Dy_o': 125.0, 'h_o': 2.5, 'shell_diameter': 125.0, 'shell_wall_thickness': 2.5, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 115.85999999999999, 'cost_of_the_shell_with_transport_no_VAT': 868.505, 'electricity': 3.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 45, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    4: {'name': 'Ду57×3/125×2.5', 'Dy_t': 57.0, 'h_t': 3.0, 'Dy_o': 125.0, 'h_o': 2.5, 'shell_diameter': 125.0, 'shell_wall_thickness': 2.5, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 115.85999999999999, 'cost_of_the_shell_with_transport_no_VAT': 868.505, 'electricity': 3.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 45, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    5: {'name': 'Ду57×3/140×3.5', 'Dy_t': 57.0, 'h_t': 3.0, 'Dy_o': 140.0, 'h_o': 3.5, 'shell_diameter': 140.0, 'shell_wall_thickness': 3.5, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 115.85999999999999, 'cost_of_the_shell_with_transport_no_VAT': 1143.7250000000001, 'electricity': 3.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 45, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    6: {'name': 'Ду76×3.5/140×3', 'Dy_t': 76.0, 'h_t': 3.5, 'Dy_o': 140.0, 'h_o': 3.0, 'shell_diameter': 140.0, 'shell_wall_thickness': 3.0, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 119.88, 'cost_of_the_shell_with_transport_no_VAT': 1143.7250000000001, 'electricity': 4.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 45, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    7: {'name': 'Ду76×3.5/160×3', 'Dy_t': 76.0, 'h_t': 3.5, 'Dy_o': 160.0, 'h_o': 3.0, 'shell_diameter': 160.0, 'shell_wall_thickness': 3.0, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 119.88, 'cost_of_the_shell_with_transport_no_VAT': 1315.71, 'electricity': 4.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 45, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    8: {'name': 'Ду89×4/160×3', 'Dy_t': 89.0, 'h_t': 4.0, 'Dy_o': 160.0, 'h_o': 3.0, 'shell_diameter': 160.0, 'shell_wall_thickness': 3.0, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 135.84, 'cost_of_the_shell_with_transport_no_VAT': 1315.71, 'electricity': 4.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 45, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    9: {'name': 'Ду89×4/180×3', 'Dy_t': 89.0, 'h_t': 4.0, 'Dy_o': 180.0, 'h_o': 3.0, 'shell_diameter': 180.0, 'shell_wall_thickness': 3.0, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 135.84, 'cost_of_the_shell_with_transport_no_VAT': 1479.0600000000002, 'electricity': 4.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 45, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    10: {'name': 'Ду108×4/180×3', 'Dy_t': 108.0, 'h_t': 4.0, 'Dy_o': 180.0, 'h_o': 3.0, 'shell_diameter': 180.0, 'shell_wall_thickness': 3.0, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 151.85999999999999, 'cost_of_the_shell_with_transport_no_VAT': 1479.0600000000002, 'electricity': 5.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 40, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    11: {'name': 'Ду108×4/200×3.2', 'Dy_t': 108.0, 'h_t': 4.0, 'Dy_o': 200.0, 'h_o': 3.2, 'shell_diameter': 200.0, 'shell_wall_thickness': 3.2, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 151.85999999999999, 'cost_of_the_shell_with_transport_no_VAT': 1922.2500000000002, 'electricity': 5.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 40, 'number_of_workers': 3, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    12: {'name': 'Ду133×4/225×3.5', 'Dy_t': 133.0, 'h_t': 4.0, 'Dy_o': 225.0, 'h_o': 3.5, 'shell_diameter': 225.0, 'shell_wall_thickness': 3.5, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 187.74, 'cost_of_the_shell_with_transport_no_VAT': 2233.0, 'electricity': 6.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 40, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    13: {'name': 'Ду133×4/250×3.9', 'Dy_t': 133.0, 'h_t': 4.0, 'Dy_o': 250.0, 'h_o': 3.9, 'shell_diameter': 250.0, 'shell_wall_thickness': 3.9, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 187.74, 'cost_of_the_shell_with_transport_no_VAT': 2691.59, 'electricity': 6.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 40, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    14: {'name': 'Ду159×4.5/250×3.9', 'Dy_t': 159.0, 'h_t': 4.5, 'Dy_o': 250.0, 'h_o': 3.9, 'shell_diameter': 250.0, 'shell_wall_thickness': 3.9, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 211.68, 'cost_of_the_shell_with_transport_no_VAT': 2691.59, 'electricity': 6.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 40, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    15: {'name': 'Ду159×4.5/280×4.4', 'Dy_t': 159.0, 'h_t': 4.5, 'Dy_o': 280.0, 'h_o': 4.4, 'shell_diameter': 280.0, 'shell_wall_thickness': 4.4, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 211.68, 'cost_of_the_shell_with_transport_no_VAT': 3470.5000000000005, 'electricity': 6.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 40, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    16: {'name': 'Ду219×6/315×4.9', 'Dy_t': 219.0, 'h_t': 6.0, 'Dy_o': 315.0, 'h_o': 4.9, 'shell_diameter': 315.0, 'shell_wall_thickness': 4.9, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 150.0, 'cost_of_the_shell_with_transport_no_VAT': 4196.445, 'electricity': 7.5, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 30, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    17: {'name': 'Ду219×6/355×5.6', 'Dy_t': 219.0, 'h_t': 6.0, 'Dy_o': 355.0, 'h_o': 5.6, 'shell_diameter': 355.0, 'shell_wall_thickness': 5.6, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 330360.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 200.0, 'cost_of_the_shell_with_transport_no_VAT': 5560.5, 'electricity': 7.5, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 30, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    18: {'name': 'Ду273×7/400×5.6', 'Dy_t': 273.0, 'h_t': 7.0, 'Dy_o': 400.0, 'h_o': 5.6, 'shell_diameter': 400.0, 'shell_wall_thickness': 5.6, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 200.0, 'cost_of_the_shell_with_transport_no_VAT': 6148.450000000001, 'electricity': 9.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 25, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    19: {'name': 'Ду273×7/450×5.6', 'Dy_t': 273.0, 'h_t': 7.0, 'Dy_o': 450.0, 'h_o': 5.6, 'shell_diameter': 450.0, 'shell_wall_thickness': 5.6, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 225.0, 'cost_of_the_shell_with_transport_no_VAT': 7042.805000000001, 'electricity': 9.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 25, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    20: {'name': 'Ду325×7/450×5.6', 'Dy_t': 325.0, 'h_t': 7.0, 'Dy_o': 450.0, 'h_o': 5.6, 'shell_diameter': 450.0, 'shell_wall_thickness': 5.6, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 200.0, 'cost_of_the_shell_with_transport_no_VAT': 7042.805000000001, 'electricity': 10.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 20, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    21: {'name': 'Ду325×7/500×6.2', 'Dy_t': 325.0, 'h_t': 7.0, 'Dy_o': 500.0, 'h_o': 6.2, 'shell_diameter': 500.0, 'shell_wall_thickness': 6.2, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 225.0, 'cost_of_the_shell_with_transport_no_VAT': 8332.800000000001, 'electricity': 10.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 20, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    22: {'name': 'Ду377×7/500×6.2', 'Dy_t': 377.0, 'h_t': 7.0, 'Dy_o': 500.0, 'h_o': 6.2, 'shell_diameter': 500.0, 'shell_wall_thickness': 6.2, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 200.0, 'cost_of_the_shell_with_transport_no_VAT': 8332.800000000001, 'electricity': 10.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 15, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    23: {'name': 'Ду377×7/560×7', 'Dy_t': 377.0, 'h_t': 7.0, 'Dy_o': 560.0, 'h_o': 7.0, 'shell_diameter': 560.0, 'shell_wall_thickness': 7.0, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 225.0, 'cost_of_the_shell_with_transport_no_VAT': 12607.123200000002, 'electricity': 10.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 15, 'number_of_workers': 4, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    24: {'name': 'Ду426×8/560×7', 'Dy_t': 426.0, 'h_t': 8.0, 'Dy_o': 560.0, 'h_o': 7.0, 'shell_diameter': 560.0, 'shell_wall_thickness': 7.0, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 200.0, 'cost_of_the_shell_with_transport_no_VAT': 12607.123200000002, 'electricity': 10.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 10, 'number_of_workers': 5, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    25: {'name': 'Ду426×8/630×7.9', 'Dy_t': 426.0, 'h_t': 8.0, 'Dy_o': 630.0, 'h_o': 7.9, 'shell_diameter': 630.0, 'shell_wall_thickness': 7.9, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 250.0, 'cost_of_the_shell_with_transport_no_VAT': 21546.537600000003, 'electricity': 10.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 10, 'number_of_workers': 5, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    26: {'name': 'Ду530×8/710×8.9', 'Dy_t': 530.0, 'h_t': 8.0, 'Dy_o': 710.0, 'h_o': 8.9, 'shell_diameter': 710.0, 'shell_wall_thickness': 8.9, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 225.0, 'cost_of_the_shell_with_transport_no_VAT': 24375.0, 'electricity': 10.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 9, 'number_of_workers': 5, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    27: {'name': 'Ду630×8/800×10', 'Dy_t': 630.0, 'h_t': 8.0, 'Dy_o': 800.0, 'h_o': 10.0, 'shell_diameter': 800.0, 'shell_wall_thickness': 10.0, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 225.0, 'cost_of_the_shell_with_transport_no_VAT': 27222.2496, 'electricity': 14.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 9, 'number_of_workers': 5, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    28: {'name': 'Ду720×8/900×11.2', 'Dy_t': 720.0, 'h_t': 8.0, 'Dy_o': 900.0, 'h_o': 11.2, 'shell_diameter': 900.0, 'shell_wall_thickness': 11.2, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 225.0, 'cost_of_the_shell_with_transport_no_VAT': 34366.0, 'electricity': 14.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 9, 'number_of_workers': 5, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    29: {'name': 'Ду820×10/1000×12.4', 'Dy_t': 820.0, 'h_t': 10.0, 'Dy_o': 1000.0, 'h_o': 12.4, 'shell_diameter': 1000.0, 'shell_wall_thickness': 12.4, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 225.0, 'cost_of_the_shell_with_transport_no_VAT': 52320.0, 'electricity': 14.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 9, 'number_of_workers': 5, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    30: {'name': 'Ду920×10/1100×13.8', 'Dy_t': 920.0, 'h_t': 10.0, 'Dy_o': 1100.0, 'h_o': 13.8, 'shell_diameter': 1100.0, 'shell_wall_thickness': 13.8, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 225.0, 'cost_of_the_shell_with_transport_no_VAT': 58785.71, 'electricity': 14.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 9, 'number_of_workers': 5, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
    31: {'name': 'Ду1020×10/1200×14.9', 'Dy_t': 1020.0, 'h_t': 10.0, 'Dy_o': 1200.0, 'h_o': 14.9, 'shell_diameter': 1200.0, 'shell_wall_thickness': 14.9, 'length': 12000, 'order_metrs': 1, 'p_PPU': 70.0, 'a_machine': 2.0, 'a': 100.0, 'b': 160.0, 'cost_of_steel_pipe_no_VAT': 419642.0, 'cost_cupper_wire_no_VAT': 110.72, 'cost_foam_components_no_VAT': 1517.0, 'cost_centralizer_no_VAT': 225.0, 'cost_of_the_shell_with_transport_no_VAT': 62785.71, 'electricity': 14.0, 'cost_one_kWt_hour': 23.0, 'number_of_pipes_per_shift': 9, 'number_of_workers': 5, 'salary_gross_netto_сenterers': 500000, 'salary_gross_netto_filler': 500000, 'overhead_costs_from_the_workers_wage_fund': 50.0, 'CO': 4.0, 'OPVR': 2.5, 'CH': 5.18, 'OOCMC': 3.0, 'VAT': 1.12, 'marginality': 30.0},
}

# Расчетные функции
def weight_of_steel_wire(Dy_t, h_t):
    x = (math.pow(Dy_t / 1000, 2))
    y = (math.pow((Dy_t-2*h_t)/1000,2))
    return 7850 * 3.14 * (x - y) / 4

def length_of_steel_pipe(l):
    return l / 1000

def length_of_PE_sheath(l):
    return l - (l*0.3/12)

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

def component_A(foam_components, a, b):
    stage1 = a + b
    stage2 = stage1 / 100
    return foam_components / stage2

def component_B(component_A, b):
    return component_A * b / 100

def quantity_of_steel_pipe(weight_of_steel_wire, length_of_steel_pipe):
    return weight_of_steel_wire * length_of_steel_pipe

def quantity_of_PE(length_of_PE_sheath):
    return length_of_PE_sheath / 1000

def copper_wire(length_of_steel_pipe):
    return (length_of_steel_pipe + 0.6) * 0.014 * 2

def salary_gross_brutto(salary_gross_netto):
    return (salary_gross_netto - 4830)/0.792

def cost_of_work_for_one_pipe(salary_gross_brutto_filler, number_of_workers, salary_gross_brutto_centerers, number_of_pipes_per_shift):
    stage1 = salary_gross_brutto_filler * 2
    stage2 = (number_of_workers - 2) * salary_gross_brutto_centerers
    stage3 = (stage1 + stage2) / 25
    return stage3 / number_of_pipes_per_shift

def payroll_taxes_at_the_expense_of_the_employer(CO, OPVR, CH, OOCMC, cost_of_work_for_one_pipe):
    stage1 = CO + OPVR + CH + OOCMC
    stage2 = stage1 / 100 * cost_of_work_for_one_pipe
    return stage2

def overheads(cost_of_work_for_one_pipe, overhead_costs_from_the_workers_wage_fund):
    return cost_of_work_for_one_pipe * overhead_costs_from_the_workers_wage_fund / 100

def cost_price_of_one_piece_of_product_without_VAT(foam_components, cost_foam_components_no_VAT, quantity_of_steel_pipe, cost_of_steel_pipe_no_VAT, quantity_of_PE, cost_of_the_shell_with_transport_no_VAT, copper_wire, cost_cupper_wire_no_VAT, consumption_of_centralizers_segments, cost_centralizer_no_VAT, length, electricity, cost_one_kWt_hour, cost_of_work_for_one_pipe, payroll_taxes_at_the_expense_of_the_employer, overheads):
    stage1 = (foam_components * cost_foam_components_no_VAT) + (quantity_of_steel_pipe * cost_of_steel_pipe_no_VAT / 1000)
    stage2 = (quantity_of_PE * cost_of_the_shell_with_transport_no_VAT) + (copper_wire * cost_cupper_wire_no_VAT) + (consumption_of_centralizers_segments * cost_centralizer_no_VAT * length / 1000)
    stage3 = (electricity * cost_one_kWt_hour) + cost_of_work_for_one_pipe + payroll_taxes_at_the_expense_of_the_employer + overheads
    return stage1 + stage2 + stage3

def cost_price_of_one_mp_of_pipe_no_VAT(cost_price_of_one_piece_of_product_without_VAT):
    return cost_price_of_one_piece_of_product_without_VAT / 12

def cost_price_of_one_mp_of_pipe_with_VAT(cost_price_of_one_mp_of_pipe_no_VAT, VAT):
    return cost_price_of_one_mp_of_pipe_no_VAT * VAT

def order_cost_with_VAT(cost_price_of_one_mp_of_pipe_with_VAT, order_metrs, marginality):
    stage1 = cost_price_of_one_mp_of_pipe_with_VAT * order_metrs / 12
    stage2 = 1 + (marginality/100)
    return stage1 * stage2

def calculate_all(params):
    """Полный расчет всех параметров"""
    _weight_of_steel_wire = weight_of_steel_wire(params["Dy_t"], params["h_t"])
    _length_of_steel_pipe = length_of_steel_pipe(params["length"])
    _length_of_PE_sheath = length_of_PE_sheath(params["length"])
    _foam_components = foam_components(params["Dy_o"], params["h_o"], params["Dy_t"], _length_of_PE_sheath, params["p_PPU"])
    _filling = (_foam_components / params["a_machine"]) * 3600
    _component_A = component_A(_foam_components, params["a"], params["b"])
    _component_B = component_B(_component_A, params["b"])
    _quantity_of_steel_pipe = quantity_of_steel_pipe(_weight_of_steel_wire, _length_of_steel_pipe)
    _quantity_of_PE = quantity_of_PE(_length_of_PE_sheath)
    _copper_wire = copper_wire(_length_of_steel_pipe)
    _consumption_of_centralizers_segments = _length_of_steel_pipe
    _salary_gross_brutto_centerers = salary_gross_brutto(params["salary_gross_netto_сenterers"])
    _salary_gross_brutto_filler = salary_gross_brutto(params["salary_gross_netto_filler"])
    _cost_of_work_for_one_pipe = cost_of_work_for_one_pipe(_salary_gross_brutto_filler, params["number_of_workers"], _salary_gross_brutto_centerers, params["number_of_pipes_per_shift"])
    _payroll_taxes_at_the_expense_of_the_employer = payroll_taxes_at_the_expense_of_the_employer(params["CO"], params["OPVR"], params["CH"], params["OOCMC"], _cost_of_work_for_one_pipe)
    _overheads = overheads(_cost_of_work_for_one_pipe, params["overhead_costs_from_the_workers_wage_fund"])
    _cost_price_of_one_piece_of_product_without_VAT = cost_price_of_one_piece_of_product_without_VAT(_foam_components, params["cost_foam_components_no_VAT"], _quantity_of_steel_pipe, params["cost_of_steel_pipe_no_VAT"], _quantity_of_PE, params["cost_of_the_shell_with_transport_no_VAT"], _copper_wire, params["cost_cupper_wire_no_VAT"], _consumption_of_centralizers_segments, params["cost_centralizer_no_VAT"], params["length"], params["electricity"], params["cost_one_kWt_hour"], _cost_of_work_for_one_pipe, _payroll_taxes_at_the_expense_of_the_employer, _overheads)
    _cost_price_of_one_mp_of_pipe_no_VAT = cost_price_of_one_mp_of_pipe_no_VAT(_cost_price_of_one_piece_of_product_without_VAT)
    _cost_price_of_one_mp_of_pipe_with_VAT = cost_price_of_one_mp_of_pipe_with_VAT(_cost_price_of_one_mp_of_pipe_no_VAT, params["VAT"])
    _order_cost_with_VAT = order_cost_with_VAT(_cost_price_of_one_mp_of_pipe_with_VAT, params["order_metrs"], params["marginality"])
    
    return {
        "_weight_of_steel_wire": _weight_of_steel_wire,
        "_length_of_steel_pipe": _length_of_steel_pipe,
        "_length_of_PE_sheath": _length_of_PE_sheath,
        "_foam_components": _foam_components,
        "_filling": _filling,
        "_component_A": _component_A,
        "_component_B": _component_B,
        "_quantity_of_steel_pipe": _quantity_of_steel_pipe,
        "_quantity_of_PE": _quantity_of_PE,
        "_copper_wire": _copper_wire,
        "_consumption_of_centralizers_segments": _consumption_of_centralizers_segments,
        "_salary_gross_brutto_centerers": _salary_gross_brutto_centerers,
        "_salary_gross_brutto_filler": _salary_gross_brutto_filler,
        "_cost_of_work_for_one_pipe": _cost_of_work_for_one_pipe,
        "_payroll_taxes_at_the_expense_of_the_employer": _payroll_taxes_at_the_expense_of_the_employer,
        "_overheads": _overheads,
        "_cost_price_of_one_piece_of_product_without_VAT": _cost_price_of_one_piece_of_product_without_VAT,
        "_cost_price_of_one_mp_of_pipe_no_VAT": _cost_price_of_one_mp_of_pipe_no_VAT,
        "_cost_price_of_one_mp_of_pipe_with_VAT": _cost_price_of_one_mp_of_pipe_with_VAT,
        "_order_cost_with_VAT": _order_cost_with_VAT
    }

GOST_STANDARDS = [
    "ГОСТ 30732-2020",
    "ГОСТ Р 58398-2019",
    "ТУ 1390-001-00000000-2018",
    "СТО 002-2020",
    "EN 253:2019",
    "ISO 14692:2017"
]

class PPUCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ППУ Калькулятор")
        self.root.geometry("1400x900")
        
        # Цветовая схема
        self.colors = {
            'bg': '#f8fafc',
            'card_bg': '#ffffff',
            'primary': '#3b82f6',
            'text_primary': '#1e293b',
            'text_secondary': '#64748b',
            'border': '#e2e8f0',
            'highlight': '#fef3c7',
            'gost_bg': '#dbeafe'
        }
        
        self.root.configure(bg=self.colors['bg'])
        self.create_widgets()
        
    def create_widgets(self):
        """Создание интерфейса"""
        # Главный контейнер
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Заголовок
        title_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(title_frame, 
                text="ППУ Калькулятор", 
                font=("Arial", 24, "bold"),
                bg=self.colors['bg'],
                fg=self.colors['text_primary']).pack(side=tk.LEFT)
        
        # Поле ввода количества метров
        input_frame = tk.Frame(title_frame, bg=self.colors['bg'])
        input_frame.pack(side=tk.RIGHT, padx=20)
        
        tk.Label(input_frame, 
                text="Количество трубы (мп):",
                font=("Arial", 11),
                bg=self.colors['bg'],
                fg=self.colors['text_primary']).pack(side=tk.LEFT, padx=(0, 10))
        
        self.order_metrs_var = tk.DoubleVar(value=1.0)  # Значение по умолчанию
        self.order_metrs_entry = tk.Entry(input_frame, 
                                         textvariable=self.order_metrs_var,
                                         width=10,
                                         font=("Arial", 11),
                                         justify='right')
        self.order_metrs_entry.pack(side=tk.LEFT)
        
        # Выбор ГОСТа (информационный)
        gost_frame = tk.Frame(title_frame, bg=self.colors['bg'])
        gost_frame.pack(side=tk.RIGHT, padx=20)
        
        tk.Label(gost_frame, 
                text="Выбор ГОСТа:",
                font=("Arial", 11),
                bg=self.colors['bg'],
                fg=self.colors['text_primary']).pack(side=tk.LEFT, padx=(0, 10))
        
        self.gost_var = tk.StringVar(value=GOST_STANDARDS[0])
        self.gost_combo = ttk.Combobox(gost_frame, 
                                      textvariable=self.gost_var,
                                      values=GOST_STANDARDS,
                                      state="readonly", 
                                      width=20,
                                      background=self.colors['gost_bg'])
        self.gost_combo.pack(side=tk.LEFT)

        # Панель управления
        control_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], relief="solid", bd=1)
        control_frame.pack(fill=tk.X, pady=(0, 20))
        
        inner_control = tk.Frame(control_frame, bg=self.colors['card_bg'])
        inner_control.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Label(inner_control, 
                text="Выбор конфигурации:",
                font=("Arial", 14, "bold"),
                bg=self.colors['card_bg'],
                fg=self.colors['text_primary']).pack(side=tk.LEFT)
        
        # Комбобокс
        self.preset_var = tk.StringVar()
        preset_options = [f"{k}: {v['name']}" for k, v in PRESETS.items()]
        self.preset_combo = ttk.Combobox(inner_control, 
                                        textvariable=self.preset_var,
                                        values=preset_options,
                                        state="readonly", 
                                        width=30)
        self.preset_combo.pack(side=tk.LEFT, padx=(20, 20))
        self.preset_combo.set(preset_options[0])
        self.preset_combo.bind("<<ComboboxSelected>>", self.update_order_metrs)
        
        # Кнопка
        self.calc_button = tk.Button(inner_control, 
                                    text="Рассчитать",
                                    font=("Arial", 12, "bold"),
                                    bg=self.colors['primary'],
                                    fg="white",
                                    relief="flat",
                                    padx=30,
                                    pady=8,
                                    command=self.calculate)
        self.calc_button.pack(side=tk.LEFT)
        
        # Контейнер для результатов
        results_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Левая колонка
        left_frame = tk.Frame(results_frame, bg=self.colors['card_bg'], relief="solid", bd=1)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        tk.Label(left_frame, 
                text="📊 Материалы и параметры",
                font=("Arial", 14, "bold"),
                bg=self.colors['card_bg'],
                fg=self.colors['text_primary']).pack(pady=15)
        
        # Создаем scrollable область для левой колонки
        self.left_canvas = tk.Canvas(left_frame, bg=self.colors['card_bg'])
        left_scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=self.left_canvas.yview)
        self.left_scrollable_frame = tk.Frame(self.left_canvas, bg=self.colors['card_bg'])
        
        self.left_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.left_canvas.configure(scrollregion=self.left_canvas.bbox("all")))
        
        self.left_canvas.create_window((0, 0), window=self.left_scrollable_frame, anchor="nw")
        self.left_canvas.configure(yscrollcommand=left_scrollbar.set)
        
        self.left_canvas.pack(side="left", fill="both", expand=True, padx=20, pady=(0, 20))
        left_scrollbar.pack(side="right", fill="y")
        
        # Правая колонка
        right_frame = tk.Frame(results_frame, bg=self.colors['card_bg'], relief="solid", bd=1)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        tk.Label(right_frame, 
                text="💰 Экономические показатели",
                font=("Arial", 14, "bold"),
                bg=self.colors['card_bg'],
                fg=self.colors['text_primary']).pack(pady=15)
        
        # Создаем scrollable область для правой колонки
        self.right_canvas = tk.Canvas(right_frame, bg=self.colors['card_bg'])
        right_scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=self.right_canvas.yview)
        self.right_scrollable_frame = tk.Frame(self.right_canvas, bg=self.colors['card_bg'])
        
        self.right_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.right_canvas.configure(scrollregion=self.right_canvas.bbox("all")))
        
        self.right_canvas.create_window((0, 0), window=self.right_scrollable_frame, anchor="nw")
        self.right_canvas.configure(yscrollcommand=right_scrollbar.set)
        
        self.right_canvas.pack(side="left", fill="both", expand=True, padx=20, pady=(0, 20))
        right_scrollbar.pack(side="right", fill="y")
        
        # Автоматический расчет
        self.root.after(100, self.calculate)

    def update_order_metrs(self, event=None):
        """Обновить значение метража при выборе пресета"""
        preset_text = self.preset_var.get()
        if not preset_text:
            return
            
        preset_num = int(preset_text.split(':')[0])
        params = PRESETS[preset_num]
        
        # Устанавливаем значение из пресета
        self.order_metrs_var.set(params["order_metrs"])
    
    def create_result_item(self, parent, label_text, value, is_highlight=False, icon=""):
        """Создание простого элемента результата"""
        item_frame = tk.Frame(parent, bg=self.colors['highlight'] if is_highlight else self.colors['card_bg'])
        item_frame.pack(fill=tk.X, pady=2, padx=10)
        
        # Используем grid для четкого выравнивания
        item_frame.columnconfigure(1, weight=1)
        
        # Иконка
        if icon:
            tk.Label(item_frame, 
                    text=icon,
                    font=("Arial", 12),
                    bg=item_frame['bg']).grid(row=0, column=0, sticky="w", padx=(5, 5))
        
        # Название
        tk.Label(item_frame,
                text=label_text,
                font=("Arial", 10),
                bg=item_frame['bg'],
                fg=self.colors['text_secondary'],
                anchor="w").grid(row=0, column=1, sticky="ew", padx=(0, 10))
        
        # Значение
        tk.Label(item_frame,
                text=str(value),
                font=("Courier", 10, "bold" if is_highlight else "normal"),
                bg=item_frame['bg'],
                fg="#d97706" if is_highlight else self.colors['text_primary'],
                anchor="e").grid(row=0, column=2, sticky="e", padx=(10, 5))
        
        return item_frame
    
    def calculate(self):
        """Расчет и отображение результатов"""
        # Получение пресета
        preset_text = self.preset_var.get()
        if not preset_text:
            return
            
        preset_num = int(preset_text.split(':')[0])
        params = PRESETS[preset_num].copy()

        try:
            params["order_metrs"] = float(self.order_metrs_var.get())
        except ValueError:
            # Если введено не число, используем значение по умолчанию
            params["order_metrs"] = 1.0
            self.order_metrs_var.set("1.0")
        
        # Расчеты
        results = calculate_all(params)
        
        # Очистка
        for widget in self.left_scrollable_frame.winfo_children():
            widget.destroy()
        for widget in self.right_scrollable_frame.winfo_children():
            widget.destroy()

        # Материалы (левая колонка)
        material_data = [
            ("_weight_of_steel_wire", "Вес стальной трубы (1мп)", "⚖️", "кг"),
            ("_length_of_steel_pipe", "Длина стальной трубы", "📏", "м"), 
            ("_length_of_PE_sheath", "Длина ПЭ-оболочки", "📐", "мм"),
            ("_foam_components", "Пенокомпоненты (всего)", "🧪", "кг"),
            ("_filling", "Время заливки", "⏱️", "сек"),
            ("_component_A", "Компонент А (Полиол)", "🔵", "кг"),
            ("_component_B", "Компонент В (Изоционат)", "🔴", "кг"),
            ("_quantity_of_steel_pipe", "Количество стальной трубы", "🏗️", "кг"),
            ("_quantity_of_PE", "Количество ПЭ оболочки", "📦", "мп"),
            ("_copper_wire", "Провод медный", "⚡", "кг"),
            ("_consumption_of_centralizers_segments", "Расход центраторов", "🔧", "шт")
        ]
        
        for key, name, icon, unit in material_data:
            if key in results:
                value = results[key]
                if key == "_filling":
                    formatted_value = f"{value:.1f} {unit}"
                elif key in ["_length_of_steel_pipe", "_consumption_of_centralizers_segments"]:
                    formatted_value = f"{value:.1f} {unit}"
                elif key == "_length_of_PE_sheath":
                    formatted_value = f"{value:.0f} {unit}"
                else:
                    formatted_value = f"{value:.3f} {unit}"
                
                self.create_result_item(self.left_scrollable_frame, name, formatted_value, icon=icon)
        
        # Экономика (правая колонка)
        economic_data = [
            ("_salary_gross_brutto_centerers", "ЗП Центровщики (брутто)", "👷", "₸"),
            ("_salary_gross_brutto_filler", "ЗП Заливщик (брутто)", "👨‍🔧", "₸"),
            ("_cost_of_work_for_one_pipe", "Стоимость работы на 1 трубу", "⚒️", "₸"),
            ("_payroll_taxes_at_the_expense_of_the_employer", "Налоги с ФОТ", "📋", "₸"),
            ("_overheads", "Накладные расходы", "📊", "₸"),
            ("_cost_price_of_one_piece_of_product_without_VAT", "Себестоимость 1 шт без НДС", "💼", "₸"),
            ("_cost_price_of_one_mp_of_pipe_no_VAT", "Себестоимость 1 мп без НДС", "📈", "₸"),
            ("_cost_price_of_one_mp_of_pipe_with_VAT", "Себестоимость 1 мп с НДС", "💰", "₸"),
            ("_order_cost_with_VAT", "Стоимость заказа с НДС", "🎯", "₸")
        ]
        
        for key, name, icon, currency in economic_data:
            if key in results:
                value = results[key]
                is_highlight = (key == "_order_cost_with_VAT")
                
                # Форматирование чисел
                if key in ["_salary_gross_brutto_centerers", "_salary_gross_brutto_filler"]:
                    formatted_value = f"{value:,.0f} {currency}".replace(",", " ")
                else:
                    formatted_value = f"{value:,.2f} {currency}".replace(",", " ")
                
                self.create_result_item(self.right_scrollable_frame, name, formatted_value, 
                                      is_highlight=is_highlight, icon=icon)
        
        # Обновление scroll regions
        self.root.after(100, self.update_scroll_regions)
    
    def update_scroll_regions(self):
        """Обновление областей прокрутки"""
        self.left_canvas.configure(scrollregion=self.left_canvas.bbox("all"))
        self.right_canvas.configure(scrollregion=self.right_canvas.bbox("all"))

def main():
    """Запуск приложения"""
    root = tk.Tk()
    root.minsize(1200, 800)
    
    # Центрирование окна
    x = (root.winfo_screenwidth() // 2) - (700)
    y = (root.winfo_screenheight() // 2) - (450)
    root.geometry(f"1400x900+{x}+{y}")
    
    app = PPUCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()