$(function(){
    $("#Reg").validate({
    rules:{
        txtNombre:{
            required: true,
            maxlength:50,
            minlength:3}
        ,
        txtRut:{
            required: true,
            maxlength:12,
            minlength:11}
        ,
        txtGenero:{
            required: true}
        ,
        txtDirecc:{
            required: true}
        ,
        txtEmail:{
            required: true}
        ,
        txtUser:{
            required: true,
            maxlength:15,
            minlength:4}
        ,
        txtPass:{
            required: true,
            minlength:8}
        ,
        txtPassCon:{
            required: true,
            minlength:8}
        },
        messages:{
            txtNombre:{
                required:"Campo obligatorio",
                maxlength:"Excede la capacidad",
                minlength:"Nombre no es valido"}
            ,
            txtRut:{
                required:"Campo obligatorio",
                maxlength:"Rut no valido",
                minlength:"Rut no valido"}
            ,
            txtGenero:{
                required:"Campo obligatorio"}
            ,
            txtDirecc:{
                required:"Campo obligatorio"}
            ,
            txtEmail:{
                required:"Campo obligatorio"}
            ,
            txtUser:{
                required:"Campo obligatorio",
                maxlength:"Excede la capacidad",
                minlength:"Usuario no es valido"}
            ,
            txtPass:{
                required:"Campo obligatorio",
                minlength:"Contraseña no es valida"}
            ,
            txtPassCon:{
                required:"Campo obligatorio",
                minlength:"Contraseña no es valida"}
            }
    })
})
document.getElementById("ocultar").style.display="none";
function pass(){
    let input = document.getElementById("txtPassword");
    if (input.type == "password") {
        input.type = "text";
        document.getElementById("ocultar").style.display = "inline";
        document.getElementById("mostrar").style.display = "none";
    }else{
        input.type = "password";
        document.getElementById("ocultar").style.display = "none";
        document.getElementById("mostrar").style.display = "inline";
    }
}

