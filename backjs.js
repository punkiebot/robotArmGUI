const express = require("express")
const fs = require("fs")

const app = express()

//middlewares

app.use(express.json())
app.use(express.urlencoded({extended: true}))
app.use(express.static("./"))


// routes

// ruta por defecto, carga la pagina
app.get("/", (req,res) =>{
    res.setHeader("Content-type", "text/html")
    res.sendFile("./index.html")

})

app.post("/mov", (req,res) =>{
    res.setHeader("Content-type", "text/plain")

    const MoverMotor = req.body.MoverMotor;
    const MotorAmover = req.body.MotorAmover;
    const angulo = req.body.angulo;

    console.log(`condicional para mover es ${MoverMotor} y el motor a mover es ${MotorAmover} y se movera en un angulo de ${angulo} `);

    // abrir el documento.json

    let file = fs.readFileSync("./documento.json", "UTF-8")
    const json = JSON.parse(file)
    console.log(json);

    json["necesitaMover"] = MoverMotor;
    json["mover"][MotorAmover] = angulo;
    json["queMotor"] = MotorAmover;

    file =fs.writeFileSync("./documento.json", JSON.stringify(json))
   
   // enviar texto al frontend 
    res.send("data de mover servos recibida en el backend")

})


app.post("/rut", (req,res) =>{
    res.setHeader("Content-type", "text/plain")

    const condRut = req.body.necesitaRutina;
    const rutina = req.body.rutina;

    console.log(`condicional de la rutina ${condRut} y se ejecutara la rutina ${rutina}`);

    
    // abrir el documento.json
    let file = fs.readFileSync("./documento.json", "UTF-8")
    const json = JSON.parse(file)
    console.log(json);


    json["necesitaRutina"] = condRut
    json["rutinas"] = rutina

    file =fs.writeFileSync("./documento.json", JSON.stringify(json))


    res.send("data de rutinas recibida exitosamente")



})

// inicio del servidor
app.listen(3000, ()=>{
    console.log("Server running on port 3000");
    
})
