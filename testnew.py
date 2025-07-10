#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body>
<div class="modal-body">
               <form id="seekerForm" class="row g-3 needs-validation" novalidate>
                   <div class="col-md-6">
                       <label for="seekerFirstName" class="form-label">First Name</label>
                       <input type="text" class="form-control" id="seekerFirstName" name="seekerFirstName" required>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerLastName" class="form-label">Last Name</label>
                       <input type="text" class="form-control" id="seekerLastName" name="seekerLastName" required>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerEmail" class="form-label">Email</label>
                       <input type="email" class="form-control" id="seekerEmail" name="seekerEmail" required>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerPhone" class="form-label">Phone Number</label>
                       <input type="tel" class="form-control" id="seekerPhone" name="seekerPhone" required>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerState" class="form-label">State</label>
                       <select class="form-select" id="seekerState" name="seekerState" required>
                           <option value="">Select State</option>
                       </select>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerCity" class="form-label">City</label>
                       <select class="form-select" id="seekerCity" name="seekerCity" required>
                           <option value="">Select City</option>
                       </select>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerZipCode" class="form-label">Zip Code</label>
                       <input type="text" class="form-control" id="seekerZipCode" name="seekerZipCode" required>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerDOB" class="form-label">Date of Birth</label>
                       <input type="date" class="form-control" id="seekerDOB" name="seekerDOB" required>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerOccupation" class="form-label">Occupation</label>
                       <input type="text" class="form-control" id="seekerOccupation" name="seekerOccupation" required>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerAadharNo" class="form-label">Aadhar Number</label>
                       <input type="text" class="form-control" id="seekerAadharNo" name="seekerAadharNo" required>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerVehicleType" class="form-label">Vehicle Type</label>
                       <select class="form-select" id="seekerVehicleType" name="seekerVehicleType" required>
                           <option value="">Select Vehicle Type</option>
                           <option value="Bike">Bike</option>
                           <option value="Auto">Auto Rickshaw</option>
                           <option value="Car">Car</option>
                       </select>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerVehicleNo" class="form-label">Vehicle Number</label>
                       <input type="text" class="form-control" id="seekerVehicleNo" name="seekerVehicleNo" required>
                   </div>
                   <div class="col-md-6">
                       <label for="seekerPassword" class="form-label">Create Password</label>
                       <input type="password" class="form-control" id="seekerPassword" name="seekerPassword" required>
                   </div>
                   <div class="col-12">
                       <div class="form-check">
                           <input class="form-check-input" type="checkbox" id="seekerTermsCheck" required>
                           <label class="form-check-label">I agree to the Terms & Conditions</label>
                       </div>
                   </div>
                   <div class="col-12 text-center">
                       <input type="submit" class="btn btn-primary" value="Sign Up" name="seekersubmit" >
                   </div>
                   <p class="text-center mt-3">Already have an account? <a href="#">Login</a></p>
               </form>
           </div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
          <script>
document.addEventListener("DOMContentLoaded", function () {
    // Indian States and Cities
    const statesAndCities = {
        "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur"],
        "Bihar": ["Patna", "Gaya", "Bhagalpur"],
        "Delhi": ["New Delhi"],
        "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
        "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur"],
        "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
        "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi"],
        "West Bengal": ["Kolkata", "Howrah", "Durgapur"]
    };

    // Populate States Dropdown
    let stateSelect = document.getElementById("seekerState");
    for (let state in statesAndCities) { 
        stateSelect.innerHTML += `<option value="${state}">${state}</option>`;
    }

    // Populate Cities Based on Selected State
    document.getElementById("seekerState").addEventListener("change", function () {
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
        let firstName = document.getElementById("seekerFirstName").value.trim();
        let lastName = document.getElementById("seekerLastName").value.trim();
        let email = document.getElementById("seekerEmail").value.trim();
        let phone = document.getElementById("seekerPhone").value.trim();
        let state = document.getElementById("seekerState").value;
        let city = document.getElementById("seekerCity").value;
        let zip = document.getElementById("seekerZipCode").value.trim();
        let dob = document.getElementById("seekerDOB").value;
        let occupation = document.getElementById("seekerOccupation").value.trim();
        let aadhar = document.getElementById("seekerAadharNo").value.trim();
        let vehicleType = document.getElementById("seekerVehicleType").value;
        let vehicleNo = document.getElementById("seekerVehicleNo").value.trim();
        let password = document.getElementById("seekerPassword").value.trim();
        let termsChecked = document.getElementById("seekerTermsCheck").checked;

        // Validation Patterns
        let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        let phonePattern = /^[6-9]\d{9}$/;
        let zipPattern = /^\d{6}$/;
        let aadharPattern = /^\d{12}$/;
        let vehicleNoPattern = /^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$/;  // Format: MH12AB1234
        let passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

        // Check Age (Must be 18+)
        let today = new Date();
        let birthDate = new Date(dob);
        let age = today.getFullYear() - birthDate.getFullYear();
        let monthDiff = today.getMonth() - birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }

        if (!firstName || !lastName) {
            alert("Please enter your full name.");
            event.preventDefault();
            return;
        }
        if (!emailPattern.test(email)) {
            alert("Invalid email format.");
            event.preventDefault();
            return;
        }
        if (!phonePattern.test(phone)) {
            alert("Phone number must be a 10-digit Indian number starting with 6-9.");
            event.preventDefault();
            return;
        }
        if (!state || !city) {
            alert("Please select your state and city.");
            event.preventDefault();
            return;
        }
        if (!zipPattern.test(zip)) {
            alert("Zip code must be 6 digits.");
            event.preventDefault();
            return;
        }
        if (!dob) {
            alert("Please enter your date of birth.");
            event.preventDefault();
            return;
        }
        if (age < 18) {
            alert("You must be at least 18 years old to register.");
            event.preventDefault();
            return;
        }
        if (!occupation) {
            alert("Please enter your occupation.");
            event.preventDefault();
            return;
        }
        if (!aadharPattern.test(aadhar)) {
            alert("Aadhar number must be a 12-digit numeric value.");
            event.preventDefault();
            return;
        }
        if (!vehicleType) {
            alert("Please select your vehicle type.");
            event.preventDefault();
            return;
        }
        if (!vehicleNoPattern.test(vehicleNo)) {
            alert("Invalid vehicle number format (e.g., MH12AB1234).");
            event.preventDefault();
            return;
        }
        if (!passwordPattern.test(password)) {
            alert("Password must be at least 8 characters long and include a letter, number, and special character.");
            event.preventDefault();
            return;
        }
        if (!termsChecked) {
            alert("You must agree to the Terms & Conditions.");
            event.preventDefault();
            return;
        }

        alert("Seeker Registration Successful!");
    });
});
</script>

</body>
</html>
""")
form = cgi.FieldStorage()
FName = form.getvalue("seekerFirstName")
LName = form.getvalue("seekerLastName")
Semail = form.getvalue("seekerEmail")
Sphone = form.getvalue("seekerPhone")
Sstate = form.getvalue("seekerState")
Scity = form.getvalue("seekerCity")
SzipCode = form.getvalue("seekerZipCode")
SdOB = form.getvalue("seekerDOB")
Soccupation = form.getvalue("seekerOccupation")
SadharNo = form.getvalue("seekerAadharNo")
SvehicleType = form.getvalue("seekerVehicleType")
SehicleNo = form.getvalue("seekerVehicleNo")
Spassword = form.getvalue("seekerPassword")
Ssubmit = form.getvalue("seekersubmit")

if Ssubmit != None:
    y = """insert into seekda(FirstName,LastName,Email,Phone,State,City,ZipCode,DateOfBirth,Occupation,AadharNo,VehicleType,VehicleNumber,Password) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (FName, LName, Semail, Sphone, Sstate, Scity, SzipCode, SdOB, Soccupation, SadharNo, SvehicleType, SehicleNo,Spassword)
    cur.execute(y)
    con.commit()

    print("""
    <script>
       alert("registered successfully")
    </script>
    """)