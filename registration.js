document.addEventListener("DOMContentLoaded", function () {
    // Indian States and Cities
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

    // Populate States Dropdown
     let stateSelect = document.getElementById("userState");
     for (let state in statesAndCities) {
        stateSelect.innerHTML += `<option value="${state}">${state}</option>`;
    }

    // Populate Cities Based on Selected State
    document.getElementById("userState").addEventListener("change", function () {
        let citySelect = document.getElementById("userCity");
        citySelect.innerHTML = `<option value="">Select City</option>`;
        let selectedState = this.value;
        if (selectedState) {
            statesAndCities[selectedState].forEach(city => {
                citySelect.innerHTML += `<option value="${city}">${city}</option>`;
            });
        }
    });

    // Form Validation
    document.getElementById("userForm").addEventListener("submit", function (event) {
        let firstName = document.getElementById("userFirstName").value.trim();
        let lastName = document.getElementById("userLastName").value.trim();
        let email = document.getElementById("userEmail").value.trim();
        let phone = document.getElementById("userPhone").value.trim();
        let profilePic = document.getElementById("profiPic");
        let address = document.getElementById("useraddre").value.trim();
        let state = document.getElementById("userState").value;
        let city = document.getElementById("userCity").value;
        let zip = document.getElementById("userZipCode").value.trim();
        let password = document.getElementById("userPassword").value.trim();
        let termsChecked = document.getElementById("userTermsCheck").checked;



        // Validation Patterns
        let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        let phonePattern = /^[6-9]\d{9}$/;
        let zipPattern = /^\d{6}$/;
        let passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

         // Validate Fields
        if (!firstName) {
            alert("Please enter your First Name.");
            event.preventDefault();
            return;
        }
        if (!lastName) {
            alert("Please enter your Last Name.");
            event.preventDefault();
            return;
        }
        if (!emailPattern.test(email)) {
            alert("Invalid Email. Please enter a valid email address.");
            event.preventDefault();
            return;
        }
        if (!phonePattern.test(phone)) {
            alert("Invalid Phone Number. It must start with 6-9 and be 10 digits.");
            event.preventDefault();
            return;
        }
         if (!address) {
            alert("Address field cannot be empty.");
            event.preventDefault();
            return;
        }
         // Profile Picture Validation
        if (profilePic.files.length > 0) {
             let file = profilePic.files[0];
              let allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
        if (!allowedExtensions.test(file.name)) {
            alert("Profile picture must be in JPG or PNG format.");
            event.preventDefault();
         return;
        }
        if (file.size > 2 * 1024 * 1024) {  // 2MB limit
          alert("Profile picture size should not exceed 2MB.");
          event.preventDefault();
          return;
        }
        } else {
            alert("Please upload your profile picture.");
            event.preventDefault();
             return;
        }


        if (!state) {
            alert("Please select a State.");
            event.preventDefault();
            return;
        }
        if (!city) {
            alert("Please select a City.");
            event.preventDefault();
            return;
        }
        if (!zipPattern.test(zip)) {
            alert("Invalid ZIP Code. It must be a 6-digit number.");
            event.preventDefault();
            return;
        }
        if (!passwordPattern.test(password)) {
            alert("Password must be at least 8 characters, contain a letter, a number, and a special character.");
            event.preventDefault();
            return;
        }
        if (!termsChecked) {
            alert("You must agree to the Terms & Conditions.");
            event.preventDefault();
            return;
        }
    });
});

