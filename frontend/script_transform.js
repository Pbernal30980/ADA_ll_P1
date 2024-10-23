document.getElementById('btn-start').addEventListener('click', executeTransformation);

document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        executeTransformation();
    }
});

function executeTransformation() {
    const current_string = document.getElementById('current_string').value.trim();
    const target_string = document.getElementById('target_string').value.trim();
    const costs = {
        cost_advance: document.getElementById('cost_advance').value,
        cost_insert: document.getElementById('cost_insert').value,
        cost_delete: document.getElementById('cost_delete').value,
        cost_replace: document.getElementById('cost_replace').value,
        cost_kill: document.getElementById('cost_kill').value,
    };
    const algorithm = document.getElementById('algoritmo').value;

    fetch('/transform_string', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            current_string: current_string,
            target_string: target_string,
            ...costs,
            algorithm: algorithm
        })
    })
    .then(response => response.json())
    .then(result => {
        displayResults(result);
        startConsole(result.steps, current_string);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al transformar la cadena.'); 
    });
}

function displayResults(result) {
    const resultDiv = document.getElementById('result');
    const totalCostCell = document.getElementById('total-cost');
    const stepsCell = document.getElementById('steps');

    resultDiv.style.display = 'block'; 
    totalCostCell.innerText = result.total_cost;
    stepsCell.innerText = result.steps.join('\n');
}

function startConsole(steps, current_string) {
    const consoleDiv = document.getElementById('console');
    const dynamicString = document.getElementById('dynamic-string');
    let currentIndex = 0;
    let currentStringArray = [...(current_string || ' ')];
    let operations = [...steps];
    dynamicString.innerHTML = currentStringArray.map((char) => `<span>${char}</span>`).join('');

    consoleDiv.style.display = 'block';

    const executeStep = () => {
        if (currentIndex < operations.length) {
            const operation = operations[currentIndex];

            const spans = dynamicString.getElementsByTagName('span');
            for (let i = 0; i < spans.length; i++) {
                spans[i].style.backgroundColor = ''; 
            }
            spans[currentIndex].style.backgroundColor = 'gray'; 

            let newCharacter = '';
            if (operation.startsWith("advance")) {
                currentIndex++;
            } else if (operation.startsWith("replace")) {
                newCharacter = operation.split(' ')[1];
                currentStringArray[currentIndex] = newCharacter;
                currentIndex++;
            } else if (operation.startsWith("delete")) {
                currentStringArray.splice(currentIndex, 1);
                operations.splice(currentIndex, 1);
            } else if (operation.startsWith("kill")) {
                const killIndex = currentIndex; 
                currentStringArray = currentStringArray.slice(0, currentIndex);
                operations.splice(killIndex, 1);
            } else if (operation.startsWith("insert")) {
                newCharacter = operation.split(' ')[1];
                currentStringArray.splice(currentIndex, 0, newCharacter);
                currentIndex++;
            }

            dynamicString.innerHTML = currentStringArray.map((char, idx) => `<span ${idx === currentIndex ? 'class="highlight"' : ''}>${char}</span>`).join('') + `<span class="cursor"></span>`;
            setTimeout(executeStep, 1000); 
        }
    };

    executeStep();
}


