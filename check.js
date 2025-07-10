document.addEventListener("DOMContentLoaded", function () {
    // State and City Data
    const statesAndCities = {
        "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Nellore", "Kurnool", "Rajahmundry", "Tirupati", "Anantapur", "Kadapa", "Srikakulam"],
        "Arunachal Pradesh": ["Itanagar", "Tawang", "Ziro", "Bomdila", "Pasighat", "Roing", "Tezu", "Naharlagun"],
        "Assam": ["Guwahati", "Silchar", "Dibrugarh", "Jorhat", "Tezpur", "Tinsukia", "Nagaon", "Karimganj"],
        "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga", "Purnia", "Begusarai", "Arrah"],
        "Chhattisgarh": ["Raipur", "Bhilai", "Bilaspur", "Korba", "Durg", "Rajnandgaon", "Jagdalpur", "Ambikapur"],
        "Goa": ["Panaji", "Margao", "Vasco da Gama", "Mapusa", "Ponda"],
        "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar", "Jamnagar", "Bhavnagar", "Anand"],
        "Haryana": ["Chandigarh", "Faridabad", "Gurgaon", "Hisar", "Panipat", "Ambala", "Rohtak", "Karnal"],
        "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala", "Solan", "Mandi", "Kullu", "Chamba", "Una"],
        "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Hazaribagh", "Deoghar", "Giridih"],
        "Karnataka": ["Bangalore", "Mysore", "Mangalore", "Hubli", "Belgaum", "Gulbarga", "Davanagere", "Tumkur"],
        "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Alappuzha", "Palakkad", "Kollam", "Kannur"],
        "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain", "Sagar", "Rewa", "Satna"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Solapur", "Kolhapur", "Thane"],
        "Manipur": ["Imphal", "Bishnupur", "Churachandpur", "Thoubal", "Ukhrul", "Senapati"],
        "Meghalaya": ["Shillong", "Tura", "Jowai", "Nongpoh", "Baghmara"],
        "Mizoram": ["Aizawl", "Lunglei", "Saiha", "Champhai", "Serchhip"],
        "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Tuensang", "Wokha"],
        "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Sambalpur", "Puri", "Berhampur", "Balasore"],
        "Punjab": ["Chandigarh", "Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda", "Hoshiarpur"],
        "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Ajmer", "Bikaner", "Alwar", "Bharatpur"],
        "Sikkim": ["Gangtok", "Namchi", "Gyalshing", "Mangan"],
        "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli", "Erode", "Vellore"],
        "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Khammam", "Karimnagar", "Mahbubnagar", "Ramagundam"],
        "Tripura": ["Agartala", "Dharmanagar", "Udaipur", "Kailashahar", "Belonia"],
        "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra", "Meerut", "Prayagraj", "Ghaziabad", "Bareilly"],
        "Uttarakhand": ["Dehradun", "Haridwar", "Rishikesh", "Haldwani", "Nainital", "Almora", "Pithoragarh"],
        "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri", "Malda", "Kharagpur", "Haldia"]
    };

    function populateStates(selectId) {
        let stateSelect = document.getElementById(selectId);
        stateSelect.innerHTML = `<option value="">Select State</option>`;
        for (let state in statesAndCities) {
            stateSelect.innerHTML += `<option value="${state}">${state}</option>`;
        }
    }

    function populateCities(stateSelectId, citySelectId) {
        let stateSelect = document.getElementById(stateSelectId);
        let citySelect = document.getElementById(citySelectId);
        citySelect.innerHTML = `<option value="">Select City</option>`;

        if (stateSelect.value) {
            statesAndCities[stateSelect.value].forEach(city => {
                citySelect.innerHTML += `<option value="${city}">${city}</option>`;
            });
        }
    }

    // Initialize State Dropdowns
    populateStates("userState");
    populateStates("seekerState");

    // Event Listeners for State Change
    document.getElementById("userState").addEventListener("change", function () {
        populateCities("userState", "userCity");
    });
    document.getElementById("seekerState").addEventListener("change", function () {
        populateCities("seekerState", "seekerCity");
    });

    // Validation Function
    function validateForm(formId) {
        let form = document.getElementById(formId);
        let email = form.querySelector('input[type="email"]').value;
        let phone = form.querySelector('input[type="tel"]').value;
        let zipCode = form.querySelector('input[id*="ZipCode"]').value;
        let dob = form.querySelector('input[type="date"]').value;
        let aadhar = form.querySelector('input[id*="AadharNo"]')?.value;
        let vehicleNumber = form.querySelector('input[id*="VehicleNo"]')?.value;
        let password = form.querySelector('input[type="password"]').value;
        let terms = form.querySelector('input[type="checkbox"]').checked;

        let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        let phonePattern = /^[6-9]\d{9}$/;
        let zipPattern = /^\d{6}$/;
        let aadharPattern = /^\d{12}$/;
        let vehiclePattern = /^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$/;
        let passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

        let today = new Date();
        let birthDate = new Date(dob);
        let age = today.getFullYear() - birthDate.getFullYear();

        if (!emailPattern.test(email)) {
            alert("Invalid email format.");
            return false;
        }
        if (!phonePattern.test(phone)) {
            alert("Invalid phone number. Must start with 6-9 and be 10 digits.");
            return false;
        }
        if (!zipPattern.test(zipCode)) {
            alert("Invalid Zip Code. Must be 6 digits.");
            return false;
        }
        if (!dob || age < 18) {
            alert("You must be at least 18 years old.");
            return false;
        }
        if (aadhar && !aadharPattern.test(aadhar)) {
            alert("Invalid Aadhar Number. Must be 12 digits.");
            return false;
        }
        if (vehicleNumber && !vehiclePattern.test(vehicleNumber)) {
            alert("Invalid Vehicle Number. Format: XX00XX0000");
            return false;
        }
        if (!passwordPattern.test(password)) {
            alert("Password must be at least 8 characters, include a number and special character.");
            return false;
        }
        if (!terms) {
            alert("You must agree to the Terms & Conditions.");
            return false;
        }

        return true;
    }

    // Form Submission Handlers
    document.getElementById("userForm").addEventListener("submit", function (event) {
        event.preventDefault();
        if (validateForm("userForm")) {
            alert("User Registration Successful!");
            this.reset();
        }
    });

    document.getElementById("seekerForm").addEventListener("submit", function (event) {
        event.preventDefault();
        if (validateForm("seekerForm")) {
            alert("Seeker Registration Successful!");
            this.reset();
        }
    });
});




document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("userForm").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission

        // Get form values
        let firstName = document.getElementById("userFirstName").value.trim();
        let lastName = document.getElementById("userLastName").value.trim();
        let email = document.getElementById("userEmail").value.trim();
        let phone = document.getElementById("userPhone").value.trim();
        let state = document.getElementById("userState").value.trim();
        let city = document.getElementById("userCity").value.trim();
        let zip = document.getElementById("userZipCode").value.trim();
        let password = document.getElementById("userPassword").value.trim();
        let termsChecked = document.getElementById("userTermsCheck").checked;

        // Basic validation
        if (!firstName || !lastName || !email || !phone || !state || !city || !zip || !password || !termsChecked) {
            alert("Please fill in all fields and agree to the terms.");
            return;
        }

        // Send data to backend (simulate submission for now)
        console.log("Submitting form with data:", {
            firstName,
            lastName,
            email,
            phone,
            state,
            city,
            zip,
            password,
        });

        // Simulate form submission success
        alert("Registration successful!");
        document.getElementById("userForm").reset(); // Reset form after submission
    });
});

