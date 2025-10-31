async function calculate() {
      let a = parseFloat(document.getElementById('a').value);
      let b = parseFloat(document.getElementById('b').value);
      let result = await eel.multiply(a, b)();
      document.getElementById('result').innerText = 'Результат: ' + result;
    }
    window.onbeforeunload = function () {
        eel.on_close_window();  // вызывается перед закрытием
    }