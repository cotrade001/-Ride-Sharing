document.getElementById("whenSelect").addEventListener("change", function () {
    var departureTimeContainer = document.getElementById("departureTimeContainer");
    if (this.value === "schedule") {
        departureTimeContainer.classList.remove("hidden");
        document.getElementById("rideTime").required = true;
    } else {
        departureTimeContainer.classList.add("hidden");
        document.getElementById("rideTime").required = false;
    }
});

document.getElementById("whenSelect").addEventListener("change", function () {
    var departureTimeContainer = document.getElementById("departureTimeContainer");
    document.getElementById("rideTime").required = this.value === "schedule";
    departureTimeContainer.classList.toggle("hidden", this.value === "now");
});

document.getElementById("rideType").addEventListener("change", function () {
    var shareRideContainer = document.getElementById("shareRideContainer");
    var passengerContainer = document.getElementById("passengerContainer");
    var shareRideSelect = document.getElementById("shareRide");

    if (this.value === "Bike") {
        // Hide passenger container when Bike is selected
        passengerContainer.classList.add("hidden");
        // Hide share ride option for Bike
        shareRideContainer.classList.add("hidden");
        shareRideSelect.value = "no"; // Default to "No" for ride sharing if bike is selected
    } else {
        // Show passenger container and share ride option when the ride type is not Bike
        passengerContainer.classList.remove("hidden");
        shareRideContainer.classList.remove("hidden");
    }
});


document.getElementById("shareRide").addEventListener("change", function () {
    var genderContainer = document.getElementById("genderContainer");
    genderContainer.classList.toggle("hidden", this.value === "no");
});

document.getElementById("bookingForm").addEventListener("submit", function (event) {
    event.preventDefault();
    let fromLocation = document.getElementById("fromLocation").value;
    let toLocation = document.getElementById("toLocation").value;
    let rideType = document.getElementById("rideType").value;
    let shareRide = document.getElementById("shareRide").value;
    let gender = document.getElementById("gender").value;
    let passengerCount = document.getElementById("passengerCount").value;
    let whenSelect = document.getElementById("whenSelect").value;
    let rideTime = document.getElementById("rideTime").value;

    if (whenSelect === "schedule" && rideTime === "") {
        alert("Please select a date and time for your scheduled ride.");
        return;
    }

    if (shareRide === "yes" && rideType === "Bike") {
        alert("Ride sharing is not allowed for Bikes.");
        return;
    }

    let bookingDetails = `Ride booked from ${fromLocation} to ${toLocation} with ${passengerCount} passengers `;
    bookingDetails += shareRide === "yes" ? `sharing with ${gender} travelers.` : "without sharing.";

    alert(bookingDetails);
});
