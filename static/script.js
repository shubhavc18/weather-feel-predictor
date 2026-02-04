function predictFeeling() {
    const tempInput = document.getElementById('temperature').value;
    const output = document.getElementById('output');

    if (tempInput === "") {
        output.innerText = "Please enter a temperature!";
        output.style.color = "orange";
        return;
    }

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `temperature=${tempInput}`
    })
    .then(response => response.json())
    .then(data => {
        const temp = parseFloat(tempInput);
        output.innerText = `At ${temp}°C, today feels ${data.feeling}`;

        if (temp <= 15) output.style.color = "blue";
        else if (temp <= 25) output.style.color = "green";
        else output.style.color = "red";
    })
    .catch(err => console.log(err));
}
