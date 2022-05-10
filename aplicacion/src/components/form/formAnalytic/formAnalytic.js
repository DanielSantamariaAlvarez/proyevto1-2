import React, { useState } from "react";
import {Form, Button} from 'react-bootstrap';
import axios from 'axios';

// Funcion NavbarMarvel
function FormAnalytic () {
    const [datos, setDatos] = useState({
        study: ''
    })
    const [resultado, setResultado] = useState("")
    const [centinela, setCentinela] = useState(false)

    const handleInputChange = (event) => {
        setDatos({
            ...datos,
            [event.target.id] : event.target.value,
        })
    }

    const enviarDatos = (event) => {
        event.preventDefault();
        setCentinela(true)
        predecir(datos);
    }

    async function predecir(datos) {
        var url = "http://192.168.0.23:3000/rl"
        const headers = {
            'Access-Control-Allow-Origin': 'origin-list',
            'Content-Type': 'application/json',
        }
        const info = JSON.stringify({"texto": [{"study_and_condition": datos.study}]});
        axios
            .post(url, info, {headers} )
            .then((resp)=> {
                console.log("akdsjkfdjkas")
               console.log(resp)
               console.log(resp.data.prediction)
               setResultado(resp.data.prediction)
            })
            .catch((err)=> {
                console.log(err);
            })
    }

    return (
        <div className="row justify-content-center">
            <div className="col-8 ">
                <Form onSubmit={enviarDatos}>
                    <Form.Group className="my-5">
                        <Form.Label><b>Estudio y condición</b></Form.Label>
                        <Form.Control type="text" placeholder="Ingrese el estudio y la condición" id="study" onChange={handleInputChange}/>
                    </Form.Group>
                    <Form.Label><b>Algoritmo: </b>Naive Bayes (Mejores métricas)</Form.Label>
                    <div className="row">
                        <Button className="bg-primary mt-3 mb-3" variant="primary" type="submit">
                            Enviar
                        </Button>
                    </div>
                </Form>
            </div>
            <div className="col-8 ">
                <div className="d-flex justify-content-center">
                    {!centinela?
                    (
                        <div className="d-flex  justify-content-center">
                            <div className="text-justify">
                                <h3 className="text-justify">Por favor ingrese el estudio y condición.</h3>            
                            </div>
                        </div>
                    )
                    :
                    (resultado.resultadoElegibilidad === "0"
                    ? 
                    <div className="d-flex  justify-content-center">
                        <div className="text-justify">
                            <h3 className="text-justify">El paciente es adecuado para recibir pruebas clínicas de cancer.</h3>            
                        </div>
                    </div>
                    :
                    
                <div className="d-flex flex-column">
                    <h3 className="center">El paciente no es adecuado para recibir pruebas clínicas de cancer.</h3> 
                </div>)
            }
        </div>
            </div>  
        </div> 
    )
}

// Exportar funcion NavbarMarvel para ser visible en otros archivos
export default FormAnalytic;