function load(){
    api();
}
function api(){
    fetch('https://api.openweathermap.org/data/2.5/weather?q=Santiago,cl&appid=cd3b861fa1d5897fc03a7e3e0253279e')
        .then(response => response.json())
        .then(data =>{  
            let clima = document.getElementById("clima");
            clima.innerHTML += (data.main.temp - 273.15).toFixed(1) + "°C";
        })
        console.log(clima);
}
