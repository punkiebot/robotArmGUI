
// dom mover motores
const rangoM1 = document.getElementById("myRangeM1");
const valorM1 = document.getElementById("numeroM1");

const rangoM2 = document.getElementById("myRangeM2");
const valorM2 = document.getElementById("numeroM2");

const rangoM3 = document.getElementById("myRangeM3");
const valorM3 = document.getElementById("numeroM3");

const rangoM4 = document.getElementById("myRangeM4");
const valorM4 = document.getElementById("numeroM4");

const rangoM5 = document.getElementById("myRangeM5");
const valorM5 = document.getElementById("numeroM5");

const rangoM6 = document.getElementById("myRangeM6");
const valorM6 = document.getElementById("numeroM6");

// dom rutinas

const rutm1 = document.getElementById("rut1");
const rutm2 = document.getElementById("rut2");
const rutm3 = document.getElementById("rut3");
const rutm4 = document.getElementById("rut4");
const rutm5 = document.getElementById("rut5");
const rutm6 = document.getElementById("rut6");
const rutAll = document.getElementById("rutAll");
const rutmDef = document.getElementById("def");

// event listeners sliders
rangoM1.addEventListener("click", ()=>{
console.log(rangoM1.value);
valorM1.innerHTML = rangoM1.value+"°";
moverMotor(1, "mov1", rangoM1.value);

})
    

rangoM2.addEventListener("click", ()=>{
console.log(rangoM2.value);
valorM2.innerHTML = rangoM2.value +"°";
moverMotor(1, "mov2", rangoM2.value);


})


rangoM3.addEventListener("click", ()=>{
console.log(rangoM3.value);
valorM3.innerHTML = rangoM3.value+"°";
moverMotor(1, "mov3", rangoM3.value);

})


rangoM4.addEventListener("click", ()=>{
console.log(rangoM4.value);
valorM4.innerHTML = rangoM4.value+"°";
moverMotor(1, "mov4", rangoM4.value);

})


rangoM5.addEventListener("click", ()=>{
console.log(rangoM5.value);
valorM5.innerHTML = rangoM5.value+"°";
moverMotor(1, "mov5", rangoM5.value);

})


rangoM6.addEventListener("click", ()=>{
console.log(rangoM6.value);
valorM6.innerHTML = rangoM6.value +"°";
moverMotor(1, "mov6", rangoM6.value);

})

// event listerners de las rutinas
rutm1.addEventListener("click", ()=>{
    console.log("Ejectuar rutina 1")
    ejecutarRutina(1, "rut1");
    
    })

rutm2.addEventListener("click", ()=>{
    console.log("Ejectuar rutina 2")
    ejecutarRutina(1, "rut2");
    
    })

rutm3.addEventListener("click", ()=>{
    console.log("Ejectuar rutina 3")
    ejecutarRutina(1, "rut3");
    
    })
    

rutm4.addEventListener("click", ()=>{
    console.log("Ejectuar rutina 4")
    ejecutarRutina(1, "rut4");
    
    })

    
rutm5.addEventListener("click", ()=>{
    console.log("Ejectuar rutina 5")
    ejecutarRutina(1, "rut5");
    
    })

rutm6.addEventListener("click", ()=>{
    console.log("Ejectuar rutina 6")
    ejecutarRutina(1, "rut6");
    
    })

rutAll.addEventListener("click", ()=>{
    console.log("Ejectuar todas las rutinas")
    ejecutarRutina(1, "rutAll");
    
    })


rutmDef.addEventListener("click", ()=>{
    console.log("Volver a valores por defecto")
    valorM1.innerHTML = "90" +"°";
    rangoM1.value = 90
    valorM2.innerHTML = "60" +"°";
    rangoM2.value = 60
    valorM3.innerHTML = "120" +"°";
    rangoM3.value = 120
    valorM4.innerHTML = "150" +"°";
    rangoM4.value = 150
    valorM5.innerHTML = "110" +"°";
    rangoM5.value = 40
    valorM6.innerHTML = "40" +"°";
    rangoM6.value = 40

    ejecutarRutina(1, "rutDef");
    
    })
//************** 

    




// funciones que conectan con el backend

function ejecutarRutina(condRut,rut){

    console.log("funcion para ejercutar rutinas");

    fetch("/rut", {
        method: "POST",
        headers: {"Content-type" : "application/json"},
        body: JSON.stringify({necesitaRutina: condRut, rutina: rut})
    })
    .then (res => res.text())
    .then (data => {
        console.log(data);
    })
        


}

function moverMotor(condMov, indiceMotor, numeroAngulo){

        console.log("funcion para mover motor");

    fetch("/mov", {
        method: "POST",
        headers: {"Content-type" : "application/json"},
        body: JSON.stringify({MoverMotor: condMov, MotorAmover: indiceMotor, angulo: numeroAngulo})
    })
    .then (res => res.text())
    .then (data => {
        console.log(data);
    })

}







//console.log(base["necesitaMover"])
//console.log(base["rutinas"]["rutDef"]);
//console.log(base["mover"]["mov3"]);