document.getElementById('signup-form').addEventListener('submit', function(event) {
    // Prevent the form's default submission behavior
    event.preventDefault();

    // Extract form data
    let email = document.getElementById('email').value;
    let firstName = document.getElementById('firstName').value;
    let password1 = document.getElementById('password1').value;
    let password2 = document.getElementById('password2').value;

    // Basic validation to check if passwords match
    if (password1 !== password2) {
        document.getElementById('signup-message').innerText = 'Passwords do not match!';
        return;
    }

    // Send data to /register endpoint
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            first_name: firstName,
            password: password1
        })
    })
    .then(response => response.json())
    .then(data => {
        // Display success or error message based on server response
        document.getElementById('signup-message').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('signup-message').innerText = 'An error occurred. Please try again.';
    });
});

document.getElementById('login-form').addEventListener('submit', function(event) {
    // Prevent the form's default submission behavior
    event.preventDefault();

    // Extract form data
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    // Send data to /login endpoint
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/';  // Redirect to home page on successful login
        } else {
            // Display error message based on server response
            document.getElementById('login-message').innerText = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('login-message').innerText = 'An error occurred. Please try again.';
    });
});
