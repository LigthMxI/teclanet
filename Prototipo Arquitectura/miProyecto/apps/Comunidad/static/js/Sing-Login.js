console.log("Funciona diablo");
        let front = document.getElementById("front");
        let back = document.getElementById("back");
        back.style.display= "none";
let login= true;

function cambio() {
    if (login){
        back.style.display= "inline";
        front.style.display= "none";
    login= false;

    }
    else{
        front.style.display= "inline";
        back.style.display= "none";
        login=true;
    } 
    console.log("variable login",login)   
}