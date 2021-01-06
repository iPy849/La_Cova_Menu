window.addEventListener("DOMContentLoaded", () => {
    const currency_settings = document.querySelector("#currency-data");

    //Trigger de todos los cambios
    function TriggerChange(currency){
        currency_settings.dataset.currency = currency;

        //cambia los precios
        document.querySelectorAll(".price > p").forEach(price => {
            let calc = parseFloat(price.innerHTML);
            calc = currency_settings.dataset.currency === 'cup' ? calc *= 25 : calc /= 25;
            price.innerHTML = calc.toFixed(2);
        });

        //cambia las etiquetas de la moneda
        document.querySelectorAll(".currency_info").forEach(currency => {
            currency.innerHTML = currency_settings.dataset.currency === 'cup' ? 'CUP' : 'CUC';
        });
    }

    //Empezando en cuc
    TriggerChange('cup');

    document.querySelector('#cuc_option').onclick = () => TriggerChange('cuc');
    document.querySelector('#cup_option').onclick = () => TriggerChange('cup');

  });