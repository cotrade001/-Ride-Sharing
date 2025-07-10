#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()

print("""
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
               <form id="userForm" class="row g-3 needs-validation" novalidate>
                    <div class="col-md-6">
                        <label for="userFirstName" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="userFirstName" name="userFirstName" required>
                    </div>
                    <div class="col-md-6">
                        <label for="userLastName" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="userLastName" name="userLastName" required>
                    </div> 
                    <div class="col-md-6">
                        <label for="userEmail" class="form-label">Email</label>
                        <input type="email" class="form-control" id="userEmail" name="userEmail" required>
                    </div>
                    <div class="col-md-6">
                        <label for="userPhone" class="form-label">Phone Number</label>
                        <input type="tel" class="form-control" id="userPhone" name="userPhone" required>
                    </div>
                    <div class="col-md-6">
                        <label for="userState" class="form-label">State</label>
                        <select class="form-select" id="userState" name="userState" required>
                            <option value="">Select State</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label for="userCity" class="form-label">City</label>
                        <select class="form-select" id="userCity" name="userCity" required>
                            <option value="">Select City</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label for="userZipCode" class="form-label">Zip Code</label>
                        <input type="text" class="form-control" id="userZipCode" name="userZipCode" required>
                    </div>
                    <div class="col-md-6">
                        <label for="userPassword" class="form-label">Create Password</label>
                        <input type="password" class="form-control" id="userPassword" name="userPassword" required>
                    </div>
                    <div class="col-12">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" id="userTermsCheck" name="userTermsCheck" required>
                            <label class="form-check-label">I agree to the Terms & Conditions</label>
                        </div>
                    </div>
                    <div class="col-12 text-center">
                    <input type="submit" class="btn btn-primary" value="Sign Up" name="usersubmit" >
                        <!-- <button type="submit" class="btn btn-primary">Sign Up</button> -->
                    </div>
                    <p class="text-center mt-3">Already have an account? <a href="#">Login</a></p>
                </form>
                <script src="registration.js"></script>
</html>
""")
form = cgi.FieldStorage()

# Handling seeker form data
Ssubmit = form.getvalue("seekersubmit")
if Ssubmit is not None:
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

    query = """INSERT INTO seekda (FirstName, LastName, Email, Phone, State, City, ZipCode, DateOfBirth, Occupation, AadharNo, VehicleType, VehicleNumber, Password) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (
    FName, LName, Semail, Sphone, Sstate, Scity, SzipCode, SdOB, Soccupation, SadharNo, SvehicleType, SehicleNo,
    Spassword)

    cur.execute(query, values)
    con.commit()

    print("""
    <script>
       alert("Seeker registered successfully");
    </script>
    """)

# Handling user form data
Submit = form.getvalue("usersubmit")
if Submit is not None:
    FirstName = form.getvalue("userFirstName")
    LastName = form.getvalue("userLastName")
    Email = form.getvalue("userEmail")
    Phone = form.getvalue("userPhone")
    State = form.getvalue("userState")
    City = form.getvalue("userCity")
    Zipcode = form.getvalue("userZipCode")
    Password = form.getvalue("userPassword")

    query = """INSERT INTO userdata (FirstName, Lastname, Email, Phone, State, City, ZipCode, Password) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (FirstName, LastName, Email, Phone, State, City, Zipcode, Password)

    cur.execute(query, values)
    con.commit()

    print("""
    <script>
       alert("User registered successfully");
    </script>
    """)
