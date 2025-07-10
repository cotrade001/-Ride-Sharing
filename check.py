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
    <title>Home page </title>
    <!-- css -->
    <link rel="stylesheet" href="nav.css">

  <!-- <link rel="stylesheet" href="main.css"> -->

    <!-- FontAwesome for Icons -->
    <script src="https://kit.fontawesome.com/yourkit.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <!-- navbar links -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- home links -->
    <script src="https://kit.fontawesome.com/YOUR-FONT-AWESOME-ID.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
</head>

<body>
<!-- Navbar -->
    <nav class="navbar navbar-expand-lg fixed-top" style="background:white;box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);">
        <div class="container">
            <a class="navbar-brand" href="home.html">
                <img src="./img/ridd.png" alt="Logo" style="height:75px; width: 81px;">
            </a>
            <!-- search box -->
            <div class="search-box" style="margin-left: 250px;">
                <input type="text" class="form-control" placeholder="Tell us your location" id="locationInput">

                <!-- Location Icon (Hidden on small screens) -->
                <i class="fas fa-map-marker-alt location-icon"></i>

                <!-- Search Button (Toggles input on small screens) -->
                <button class="search-btn" onclick="toggleSearch()">
                    <i class="fas fa-search"></i>
                </button>
            </div>

            <!-- Mobile Toggle Button -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>

            <!-- Navbar Links -->
            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item"><a class="nav-link" href="home.html"><i class="fa-solid fa-house"
                                style="margin-right: 10px;"></i>Home</a></li>
                                <li class="nav-item"><a class="nav-link" href="contact.html"><i class="fa-solid fa-envelope"
                                    style="margin-right: 10px;"></i>Contact</a></li>




                    <!-- Login Dropdown -->
                    <li class="nav-item dropdown">
                        <button class="btn btn-outline- dropdown-toggle me-2" type="button" data-bs-toggle="dropdown">
                            <i class="fa-solid fa-right-to-bracket" style="margin-right: 5px;"></i>
                            Login
                        </button>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                    data-bs-target="#adminLoginModal"><i class="fa-solid fa-user-tie"
                                        style="margin-right: 15px;"></i>Admin</a></li>
                            <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                    data-bs-target="#userLoginModal"><i class="fa-solid fa-users"
                                        style=" margin-right: 15px;"></i>User</a></li>
                            <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                    data-bs-target="#seekerLoginModal"><i class="fa-solid fa-user"
                                        style="margin-right: 15px;"></i></i>Seeker</a></li>
                        </ul>
                    </li>

                    <!-- Register Dropdown -->
                    <li class=" nav-item dropdown">
                        <button class="btn btn-success dropdown-toggle" type="button" data-bs-toggle="dropdown">
                            <i class="fa-solid fa-user-plus"></i> Register
                        </button>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                    data-bs-target="#userRegisterModal">User</a></li>
                            <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                    data-bs-target="#seekerRegisterModal">Seeker</a></li>
                        </ul>
                    </li>

                </ul>
            </div>
        </div>
    </nav>
   <!-- User Register Modal -->
   <div class="modal fade" id="userRegisterModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">User Registration</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
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
            </div>
        </div>
    </div>
</div>
<!-- Seeker Register Modal -->
<div class="modal fade" id="seekerRegisterModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Seeker Registration</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
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
        </div>
    </div>
</div>
   <!-- Navbar JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
   <!-- <script src="registration.js"></script> -->
</body>

</html>
""")
form = cgi.FieldStorage()

FirstName = form.getvalue("userFirstName")
LastName = form.getvalue("userLastName")
Email = form.getvalue("userEmail")
Phone = form.getvalue("userPhone")
State = form.getvalue("userState")
City = form.getvalue("userCity")
Zipcode = form.getvalue("userZipCode")
Password = form.getvalue("userPassword")
Submit = form.getvalue("usersubmit")

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

if Submit != None:
    x = """insert into userdata(FirstName,Lastname,Email,Phone,State,City,ZipCode,Password) values('%s','%s','%s','%s','%s','%s','%s','%s')""" % (FirstName,LastName,Email,Phone,State,City,Zipcode,Password)
    cur.execute(x)
    con.commit()
    print("""
    <script>
       alert("registered successfully")
    </script>
    """)


if Submit != None:
    y = """insert into seekda(FirstName,LastName,Email,Phone,State,City,ZipCode,DateOfBirth,Occupation,AadharNo,VehicleType,VehicleNumber,Password) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (FName, LName, Semail, Sphone, Sstate, Scity, SzipCode, SdOB, Soccupation, SadharNo, SvehicleType, SehicleNo,Spassword)
    cur.execute(y)
    con.commit()

    print("""
    <script>
       alert("registered successfully")
    </script>
    """)

