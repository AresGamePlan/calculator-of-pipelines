let data = []
// JavaScript для обработки выбора строки
document.addEventListener('DOMContentLoaded', function() {
    // При клике на плюсик в строке таблицы
    document.querySelectorAll('.add-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const row = this.closest('tr');
            const diameter = row.cells[1].textContent;
            
            //Диаметр трубы
            data[0] = row.cells[1].textContent;

            //Диаметры 1 и 2 типа оболочки ПЭ
            data[1] = row.cells[2].textContent;
            data[2] = row.cells[3].textContent;

            //Диаметры 1 и 2 типа оболочки ОЦ
            data[3] = row.cells[4].textContent;
            data[4] = row.cells[5].textContent;

            //eel.get_data(data);

            // Устанавливаем выбранный диаметр в модальном окне
            document.getElementById('selectedDiameter').textContent = diameter;
            document.getElementById('diameter-select').value = diameter;
        });
    });
    
    // Обновляем наименование продукции при изменении диаметра
    document.getElementById('diameter-select').addEventListener('change', function() {
        document.getElementById('selectedDiameter').textContent = this.value;
    });
});


async function calculate() {
    
    data[5] = document.getElementById('quantity').value;
    data[6] = document.getElementById('type-select').value;
    data[7] = document.getElementById('thickness-select').value;

    let Dy_t = Number(data[0])
    let h_t = Number(data[7])
    let shell_diameter;
    let order_metrs = Number(data[5]);
    if (data[6] == "1") {
        shell_diameter = Number(data[1])
        
    }
    else {
        shell_diameter = Number(data[2])
    }

    await eel.calculate(Dy_t, h_t, shell_diameter, order_metrs)()
    window.location.href = "page.html";
}