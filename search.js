function toggleSearch() {
    let searchBox = document.querySelector(".search-box");
    let inputField = document.getElementById("locationInput");

    if (window.innerWidth <= 768) {
        searchBox.classList.toggle("active");
        inputField.focus();
    } else {
        searchLocation();
    }
}

function searchLocation() {
    let location = document.getElementById("locationInput").value;
    if (location.trim() === "") {
        alert("Please enter your location!");
    } else {
        alert("Searching for: " + location);
    }
}