// function submitForm() {
//     // Placeholder for storing form data and sending it to a server or database
//     // For simplicity, let's just display a success message
//     document.getElementById("response-message").innerHTML = "Your request has been taken.";
// }


function submitForm() {
    // Placeholder for storing form data and sending it to a server or database
    // For simplicity, let's just display a success message and stored data
    const name = document.querySelector(".field[placeholder='Your Name']").value;
    const email = document.querySelector(".field[placeholder='Your Email']").value;
    const phone = document.querySelector(".field[placeholder='Phone']").value;
    const voterID = document.querySelector(".field[placeholder='Voter ID']").value;
    const documentUpload = document.getElementById("uploadDocument").value;
    const message = document.querySelector(".field[placeholder='Message']").value;

    // // Simulate storing data
    // const storedData = {
    //     Name: name,
    //     Email: email,
    //     Phone: phone,
    //     VoterID: voterID,
    //     // DocumentUpload: documentUpload,
    //     Message: message
    // };

    // Display success message
    document.getElementById("response-message").innerHTML = "Request has been taken, and your data has been sent.";

    // Display stored data
    displayStoredData(storedData);
}

function displayStoredData(data) {
    const storedDataDiv = document.getElementById("stored-data");
    storedDataDiv.innerHTML = "<h3>Stored Data:</h3>";
    
    for (const key in data) {
        if (data.hasOwnProperty(key)) {
            storedDataDiv.innerHTML += `<p><strong>${key}:</strong> ${data[key]}</p>`;
        }
    }
}
