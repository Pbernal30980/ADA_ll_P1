document.getElementById('btn-transformar').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('transformar-form').style.display = 'block';
});

document.getElementById('btn-iniciar').addEventListener('click', ejecutarTransformacion);

document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        ejecutarTransformacion();
    }
});

function ejecutarTransformacion() {
    const cadena_actual = document.getElementById('cadena_actual').value.trim();
    const cadena_objetivo = document.getElementById('cadena_objetivo').value.trim();
    const costos = {
        costo_avance: document.getElementById('costo_avance').value,
        costo_insert: document.getElementById('costo_insert').value,
        costo_delete: document.getElementById('costo_delete').value,
        costo_replace: document.getElementById('costo_replace').value,
        costo_kill: document.getElementById('costo_kill').value,
    };
    const algoritmo = document.getElementById('algoritmo').value;

    fetch('/transform_string', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            cadena_actual: cadena_actual,
            cadena_objetivo: cadena_objetivo,
            ...costos,
            algoritmo: algoritmo
        })
    })
    .then(response => response.json())
    .then(result => {
        mostrarResultados(result);
        iniciarConsola(result.pasos, cadena_actual);
    })
    .catch(error => console.error('Error:', error));
}


function mostrarResultados(result) {
    const resultadoDiv = document.getElementById('resultado');
    const costoTotalCell = document.getElementById('costo-total');
    const pasosCell = document.getElementById('pasos');

    resultadoDiv.style.display = 'block';
    costoTotalCell.innerText = result.costo_total;
    pasosCell.innerText = result.pasos.join('\n');
}

function iniciarConsola(pasos, cadena_actual) {
    const consoleDiv = document.getElementById('console');
    const cadenaDinamica = document.getElementById('cadena-dinamica');
    let indexActual = 0;
    let cadenaActualArray = [...(cadena_actual || ' ')]; 
    let operaciones = [...pasos];
    cadenaDinamica.innerHTML = cadenaActualArray.map((char) => `<span>${char}</span>`).join('');

    consoleDiv.style.display = 'block';

    const ejecutarPaso = () => {
        if (indexActual < operaciones.length) {
            const operacion = operaciones[indexActual];

            const spans = cadenaDinamica.getElementsByTagName('span');
            for (let i = 0; i < spans.length; i++) {
                spans[i].style.backgroundColor = ''; 
            }
            spans[indexActual].style.backgroundColor = 'gray'; 

            let nuevoCaracter = '';
            if (operacion.startsWith("advance")) {
                indexActual++;
            } else if (operacion.startsWith("replace")) {
                nuevoCaracter = operacion.split(' ')[1];
                cadenaActualArray[indexActual] = nuevoCaracter;
                indexActual++;
            } else if (operacion.startsWith("delete")) {
                cadenaActualArray.splice(indexActual, 1);
                operaciones.splice(indexActual, 1); 
            } else if (operacion.startsWith("kill")) {
                const killIndex = indexActual; 
                cadenaActualArray = cadenaActualArray.slice(0, indexActual);
                operaciones.splice(killIndex, 1);
            } else if (operacion.startsWith("insert")) {
                nuevoCaracter = operacion.split(' ')[1];
                cadenaActualArray.splice(indexActual, 0, nuevoCaracter);
                indexActual++;
            }

            cadenaDinamica.innerHTML = cadenaActualArray.map((char, idx) => `<span ${idx === indexActual ? 'class="highlight"' : ''}>${char}</span>`).join('') + `<span class="cursor"></span>`;
            setTimeout(ejecutarPaso, 1000); 
        } 
    };

    ejecutarPaso();
}
