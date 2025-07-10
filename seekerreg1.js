document.addEventListener("DOMContentLoaded", function () {
    // Indian States and Cities
    const statesAndCities = {
        "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
        "Karnataka": ["Bangalore", "Mysore"],
        "Tamil Nadu": ["Chennai", "Coimbatore"]
    };

    // Populate State Dropdown
    let stateSelect = document.getElementById("seekerState");
    for (let state in statesAndCities) {
        stateSelect.innerHTML += `<option value="${state}">${state}</option>`;
    }

    // Populate Cities Based on Selected State
    stateSelect.addEventListener("change", function () {
        let citySelect = document.getElementById("seekerCity");
        citySelect.innerHTML = `<option value="">Select City</option>`;
        let selectedState = this.value;
        if (selectedState) {
            statesAndCities[selectedState].forEach(city => {
                citySelect.innerHTML += `<option value="${city}">${city}</option>`;
            });
        }
    });

    // Form Validation
    document.getElementById("seekerForm").addEventListener("submit", function (event) {


        // Get form values
        let firstName = document.getElementById("seekerFirstName").value.trim();
        let email = document.getElementById("seekerEmail").value.trim();
        let phone = document.getElementById("seekerPhone").value.trim();
        let state = document.getElementById("seekerState").value;
        let city = document.getElementById("seekerCity").value;
        let dob = document.getElementById("seekerDOB").value;
        let aadhar = document.getElementById("seekerAadharNo").value.trim();
        let vehicleNo = document.getElementById("seekerVehicleNo").value.trim();
        let licenseNo = document.getElementById("licenseNo").value.trim();
        let vehicleRegNo = document.getElementById("vehicleRegNo").value.trim();
        let termsChecked = document.getElementById("seekerTermsCheck").checked;

        // Validation Patterns
        let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        let phonePattern = /^[6-9]\d{9}$/;
        let aadharPattern = /^\d{12}$/;
        let vehicleNoPattern = /^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$/;
        let licensePattern = /^[A-Z]{2}\d{2}\s\d{4}\s\d{7}$/;
        let rcPattern = /^[A-Z]{2}\d{2}\s[A-Z]{2}\d{4}$/;

        // Validate Fields
        if (!firstName) {
            alert("Please enter your First Name.");
            return;
        }
        if (!emailPattern.test(email)) {
            alert("Invalid Email format.");
            return;
        }
        if (!phonePattern.test(phone)) {
            alert("Phone number must be a 10-digit Indian number starting with 6-9.");
            return;
        }
        if (!state || !city) {
            alert("Please select your State and City.");
            return;
        }
        if (!aadharPattern.test(aadhar)) {
            alert("Aadhar number must be a 12-digit numeric value.");
            return;
        }
        if (!vehicleNoPattern.test(vehicleNo)) {
            alert("Invalid Vehicle Number format (e.g., MH12AB1234).");
            return;
        }
        if (!licensePattern.test(licenseNo)) {
            alert("Invalid Driving License format (e.g., KA05 2021 0012345).");
            return;
        }
        if (!rcPattern.test(vehicleRegNo)) {
            alert("Invalid RC Number format (e.g., MH12 AB1234).");
            return;
        }

        // Validate Age (Must be 18+)
        if (dob) {
            let today = new Date();
            let birthDate = new Date(dob);
            let age = today.getFullYear() - birthDate.getFullYear();
            let monthDiff = today.getMonth() - birthDate.getMonth();
            if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
                age--;
            }
            if (age < 18) {
                alert("You must be at least 18 years old to register.");
                return;
            }
        } else {
            alert("Please enter your Date of Birth.");
            return;
        }

        if (!termsChecked) {
            alert("You must agree to the Terms & Conditions.");
            return;
        }

        // Image Validation
        let allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
        let maxSize = 2 * 1024 * 1024; // 2MB

        function validateImage(input, message) {
            if (input.files.length > 0) {
                let file = input.files[0];
                if (!allowedExtensions.test(file.name)) {
                    alert(`${message} must be in JPG, JPEG, or PNG format.`);
                    return false;
                }
                if (file.size > maxSize) {
                    alert(`${message} size should not exceed 2MB.`);
                    return false;
                }
            } else {
                alert(`Please upload ${message}.`);
                return false;
            }
            return true;
        }


            if (!validateImage("profilePic", "Profile Picture")) return false;
            if (!validateImage("seekerAadharFront", "Aadhar Front Image")) return false;
            if (!validateImage("seekerAadharBack", "Aadhar Back Image")) return false;
            if (!validateImage("vehicleImages", "Vehicle Image")) return false;
            if (!validateImage("rcPhoto", "RC Photo")) return false;
            if (!validateImage("licensePhoto", "Driving License Image")) return false;

    });
});
