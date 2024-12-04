const enterButton = document.getElementById('enterButton');
const introPage = document.getElementById('introPage');
const mainSite = document.getElementById('mainSite');

// end, show the enter button
introVideo.addEventListener('ended', function() {
    enterButton.style.display = 'block';
});

function enterSite() {
    window.location.href = "index.html";

    introPage.style.display = 'none';
    mainSite.style.display = 'block';
}


document.getElementById("loginButton").addEventListener("click", function () {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;


    if (username && password) {
        alert(`Welcome, ${username}! to your Account`);
    } else {
        alert("Please reenter Username and Password.");
    }
});

document.getElementById("subscribeButton").addEventListener("click", function() {
    const email = document.getElementById("emailInput").value;

    if (email) {
        alert(`Thankyou for subscribing`)

    } else {
        alert("Please enter a valid email");
    }
});

//Registration page

function handleRegister() {
//?info for registration?
const username = document.getElementById('new-username').value;
const password = document.getElementById('new-password').value;
const confirmPassword = document.getElementById('confirm-password').value
const age = document.getElementById('age').value

if (password !== confirmPassword) {
alert("passwords do not match");
return;
}
console.log("Registration function call",{username, password, age});
//add info to save to databases
}