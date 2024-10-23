document.getElementById('btn-start').addEventListener('click', executeAuction);

document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        executeAuction();
    }
});

const numAuctions = document.getElementById('num_of_auctions');
const governmentOfferInput = document.getElementById('government-offer');
const actionsInput = document.getElementById('actions');
const priceInput = document.getElementById('price');

function offerStructure() {
    const offerContainer = document.getElementById('offer-container');

    numAuctions.addEventListener('input', function() {
        const numberOfOffers = parseInt(numAuctions.value, 10);
        offerContainer.innerHTML = ''; 

        for (let i = 1; i <= numberOfOffers; i++) {
            const offerInput = document.createElement('input');
            offerInput.type = 'text';
            offerInput.placeholder = `Oferta ${i}: precio, min, max`;
            offerInput.className = 'offer-input'; 

            offerContainer.appendChild(offerInput);

            if (i % 2 === 0) {
                offerContainer.appendChild(document.createElement('br'));
            }
        }
    });

    function updateGovernmentOffer() {
        const price = priceInput.value || 0; 
        const actions = actionsInput.value || 0; 
        governmentOfferInput.value = `${price}, 0, ${actions}`; 
    }

    actionsInput.addEventListener('input', updateGovernmentOffer);
    priceInput.addEventListener('input', updateGovernmentOffer);
}

function executeAuction() {
    const offers = Array.from(document.getElementsByClassName('offer-input'))
        .map(input => {
            const [price, min, max] = input.value.split(',').map(Number);
            return { price, min, max };
        }); 

    const governmentOffer = {
        price: parseFloat(governmentOfferInput.value.split(',')[0]),
        min: parseFloat(governmentOfferInput.value.split(',')[1]),
        max: parseFloat(governmentOfferInput.value.split(',')[2])
    };
    
    const data = {
        actions: parseInt(actionsInput.value, 10),
        minPrice: parseFloat(priceInput.value),
        offers: parseInt(numAuctions.value, 10), 
        detailsOffers: [...offers, governmentOffer], 
        algorithm: document.getElementById('algorithm').value
    };

    fetch('/auction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        displayResults(result);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al ejecutar la subasta.');
    });

}

function displayResults(result) {
    const resultDiv = document.getElementById('result');
    const bestAssignments = document.getElementById('best-assignment');
    const maximumValue = document.getElementById('value');

    resultDiv.style.display = 'block'; 
    bestAssignments.innerText = result.best_assignment.join(', ');
    maximumValue.innerText = result.best_price;   
}

offerStructure();





