function validateAdminLogin() {
    let user = document.getElementById("adminUser").value;
    let pass = document.getElementById("adminPass").value;

    if (user === "" || pass === "") {
        alert("Please fill in all fields.");
        return false;
    }

    if (user === "admin" && pass === "1234") {
        alert("Login Successful!");
        
        // Store login status in localStorage
        localStorage.setItem("isAdminLoggedIn", "true");

        // Redirect to Dashboard
        window.location.href = "Admindashboard.py";
        return false; // Prevent form submission
    } else {
        alert("Invalid User ID or Password. Try again!");
        return false;
    }
}