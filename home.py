#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os, sys
sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()

form = cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home page </title>
    <!-- css -->
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="search.css">
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

 <!-- Hero Section -->
<section class="hero-section">
    <div class="container">
        <div class="row align-items-center mt-5">
            
            <!-- Search Form - Now at the Top -->
            <div class="col-8 mx-auto">
                <div class="p-4 bg-light shadow-sm rounded border">
                 <h3 class="text-center mb-3 fw-bold text-primary">🔍 Search Available Rides</h3>
                    <form class="row g-2 align-items-center mx-auto" action="search.py" id="bookingForm" method="GET">
                        <!-- From Location -->
                        <div class="col-md-4 col-12">
                            <div class="input-group">
                                <span class="input-group-text bg-white"><i class="fa-solid fa-location-dot"></i></span>
                                <input type="text" class="form-control" name="fromLocation" id="fromLocation" 
                                       placeholder="Enter Pickup Location" required onkeyup="searchFromTo('fromLocation')">
                                <div id="fromLocationResults"></div>
                            </div>
                        </div>

                        <!-- To Location -->
                        <div class="col-md-4 col-12">
                            <div class="input-group">
                                <span class="input-group-text bg-white"><i class="fa-solid fa-map-marker-alt"></i></span>
                                <input type="text" class="form-control" name="toLocation" id="toLocation" 
                                       placeholder="Enter Drop Location" required onkeyup="searchFromTo('toLocation')">
                                <div id="toLocationResults"></div>
                            </div>
                        </div>

                        <!-- Date -->
                        <div class="col-md-2 col-12">
                            <input type="date" class="form-control" name="rideDate" id="rideDate">
                        </div>
                        <!-- Search Button -->
                        <div class="col-md-2 col-12">
                            <input type="submit" name="submitb" class="btn btn-primary w-100" value="Search">
                        </div>
                    </form>
                </div>
            </div>

            <!-- Left Text Section -->
            <div class="col-lg-6 text-center text-lg-start mt-4">
                <div class="hero-text">
                    <!-- Small Badge -->
                    <span class="badge bg-light text-success fw-bold px-3 py-2 mb-3">
                        <i class="fa-solid fa-check-circle me-2"></i> The Perfect Ride Awaits
                    </span>

                    <!-- Main Heading -->
                    <h1 class="fw-bold display-4" style="color: #f7cc7f;">
                        Get Where You Need to Go, Safely and Affordably
                    </h1>

                    <!-- Subtext -->
                    <p class="fs-5" style="color: rgba(59, 57, 57, 0.883);">
                        <strong><i class="fa-solid fa-car me-2"></i> Tere – The Smart Way to Share Rides!</strong>
                        <i class="fa-solid fa-leaf text-success"></i> Save money,
                        <i class="fa-solid fa-hand-holding-dollar text-warning"></i> reduce your carbon footprint,
                        and <i class="fa-solid fa-users text-primary"></i> make new friends along the way.
                        Join us in creating a <i class="fa-solid fa-globe text-info"></i> greener, more affordable,
                        and connected way to travel!
                    </p>

                    <!-- Buttons -->
                    <div class="mt-4">
                        <button class="btn btn-success btn-lg me-3" data-bs-toggle="modal" data-bs-target="#userLoginModal">
                            Book Your Ride
                        </button>
                        <button class="btn btn-outline-info btn-lg" data-bs-toggle="modal" data-bs-target="#seekerLoginModal">
                            Post Your Ride
                        </button>
                    </div>
                </div>
            </div>

            <!-- Right Image Section -->
            <div class="col-lg-6 text-center mt-4">
                <div class="hero-image">
                    <img src="./img/Group vm.png" alt="Ride Share Illustration">
                </div>
            </div>

        </div>
    </div>
</section>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg fixed-top" style="background:white;box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);">
        <div class="container">
            <a class="navbar-brand" href="home.py">
                <img src="./img/ridd.png" alt="Logo" style="height:75px; width: 81px;">
            </a>
            

            <!-- Mobile Toggle Button -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
                    
              

            <!-- Navbar Links -->
            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item"><a class="nav-link" href="home.py"><i class="fa-solid fa-house"
                                style="margin-right: 10px;"></i>Home</a></li>
                                <li class="nav-item"><a class="nav-link" href="contactt.py"><i class="fa-solid fa-envelope"
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
                                        style="margin-right: 15px;"></i></i>Sharer</a></li>
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
                                    data-bs-target="#seekerRegisterModal">Sharer</a></li>
                        </ul>
                    </li>

                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Section -->
    <!-- Admin Login Modal -->
    <div class="modal fade" id="adminLoginModal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title"><i class="fa-solid fa-user-gear"></i> Admin Login</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <form name="adminLoginForm" onsubmit="return validateAdminLogin()">
                        <div class="mb-3">
                            <label class="form-label"><i class="fa-solid fa-user"></i> User ID</label>
                            <input type="text" class="form-control" id="adminUser" placeholder="Enter Admin User ID"
                                required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label"><i class="fa-solid fa-lock"></i> Password</label>
                            <input type="password" class="form-control" id="adminPass" placeholder="Enter Password"
                                required>
                        </div>
                        
                         <button type="submit" class="btn btn-primary w-100"><i class="fa-solid fa-right-to-bracket"></i>
                        Login</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- User Login Full-Screen Modal -->
    <div class="modal fade" id="userLoginModal" tabindex="-1">
        <div class="modal-dialog modal-fullscreen">
            <div class="modal-content">
                <div class="modal-body" style="background-color: #ded9da;">
                    <div class="container py-2 h-100">
                        <div class="row d-flex justify-content-center align-items-center h-100">
                            <div class="col col-xl-10">
                                <div class="card" style="border-radius: 1rem;">
                                    <div class="row g-0">
                                        <div class="col-md-6 col-lg-5 d-none d-md-block mt-5">
                                            <img src="./img/mobile.png" alt="login form" class="img-fluid"
                                                style="border-radius: 1rem 0 0 1rem; height:600px; width: auto;" />
                                        </div>
                                        <div class="col-md-6 col-lg-7 d-flex align-items-center">
                                            <div class="card-body p-4 p-lg-5 text-black">
                                                <form action="" method="post" enctype="multipart/form-data">
                                                    <div class="d-flex align-items-center mb-3">
                                                        <img src="./img/Ride+Share+Logo+2.jpg" alt=""
                                                            style="height:75px; width: 80px;">
                                                    </div>
                                                    <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign
                                                        into your account</h5>
                                                    
                                                    <div class="mb-4">
                                                        <label for="emailus" class="form-label fw-bold">Email Address</label>
                                                        <input type="email" id="emailus" name="emailus" class="form-control form-control-lg" required />
                                                    </div>
                                                    <div class="mb-4">
                                                        <label for="passus" class="form-label fw-bold">Password</label>
                                                         <input type="password" id="passus" name="passus" class="form-control form-control-lg" required />
                                                    </div>
                                                    <div class="pt-1 mb-4">
                                                         <input type="submit" name="submitus" class="btn btn-dark btn-lg btn-block" value="Login">
                                                    </div>

                                                    <p class="mb-5 pb-lg-2">Don't have an account? <a href="#"
                                                            class="text-decoration-none">Register here</a></p>
                                                    <a href="#" class="small text-muted">Terms of use.</a>
                                                    <a href="#" class="small text-muted">Privacy policy</a>
                                                </form>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <button type="button" class="btn btn-danger position-absolute top-0 end-0 m-3"
                                    data-bs-dismiss="modal">X</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- sker login -->
    <div class="modal fade" id="seekerLoginModal" tabindex="-1">
        <div class="modal-dialog modal-fullscreen">
            <div class="modal-content">
                <div class="modal-body" style="background-color: #ded9da;">
                    <div class="container py-2 h-100">
                        <div class="row d-flex justify-content-center align-items-center h-100">
                            <div class="col col-xl-10">
                                <div class="card" style="border-radius: 1rem;">
                                    <div class="row g-0">
                                        <div class="col-md-6 col-lg-5 d-none d-md-block mt-5">
                                            <img src="./img/map.jpg" alt="login form" class="img-fluid"
                                                style="border-radius: 1rem 0 0 1rem; height:600px; width: auto;" />
                                        </div>
                                        <div class="col-md-6 col-lg-7 d-flex align-items-center">
                                            <div class="card-body p-4 p-lg-5 text-black">
                                                <form method="post" action="" enctype="multipart/form-data">
                                                     <div class="d-flex align-items-center mb-3">
                                                        <img src="./img/Ride+Share+Logo+2.jpg" alt="" style="height:75px; width: 80px;">
                                                    </div>
                                                        <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign into your account</h5>

                                                    <div class="mb-4">
                                                        <label for="userid" class="form-label fw-bold">User ID</label>
                                                         <input type="text" id="userid" name="userid"
                                                        class="form-control form-control-lg" required />
                                                    </div>
                                                
                                                   <div class="mb-4">
                                                        <label for="pass" class="form-label fw-bold">Password</label>
                                                        <input type="password" id="pass" name="pass"
                                                        class="form-control form-control-lg" required />
                                                   </div>
                                                
                                                    <div class="pt-1 mb-4">
                                                        <input type="submit" name="submitl" class="btn btn-dark btn-lg btn-block" value="Login">
                                                    </div>
                                                
                                                
                                                    <p class="mb-5 pb-lg-2">Don't have an account? <a href="#" class="text-decoration-none">Register here</a></p>
                                                    <a href="#" class="small text-muted">Terms of use.</a>
                                                    <a href="#" class="small text-muted">Privacy policy</a>
                                                </form>

                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <button type="button" class="btn btn-danger position-absolute top-0 end-0 m-3"
                                    data-bs-dismiss="modal">X</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
   <!-- User Register Modal -->
   <div class="modal fade" id="userRegisterModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">User Registration</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <form id="userForm" method = "post" class="row g-3 needs-validation" novalidate enctype="multipart/form-data">
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
                      <!-- Profile Picture Upload -->
                    <div class="col-md-12">
                        <label for="profilePic" class="form-label">Upload Profile Picture</label>
                        <input type="file" class="form-control" id="profiPic" name="profiPic" accept=".jpg, .jpeg, .png">
                    </div>
                    <div class="col-md-12">
                        <label for="useraddre" class="form-label">Address</label>
                        <input type="text" class="form-control" id="useraddre" name="useraddre" placeholder = "Local address (123 ....main street )">
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













<div class="modal fade" id="seekerRegisterModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Sharer Registration</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <form method="post" id="seekerForm" class="row g-3 needs-validation" novalidate enctype="multipart/form-data">
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
                    <div class="col-md-12">
                        <label for="seekerAddress" class="form-label">Address</label>
                        <input type="text" class="form-control" id="seekerAddress" name="seekerAddress" required>
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
                        <label for="seekerGender" class="form-label">Gender</label>
                        <select class="form-select" id="seekerGender" name="seekerGender" required>
                            <option value="">Select Gender</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label for="profilePic" class="form-label">Upload Profile Picture</label>
                        <input type="file" class="form-control" id="profilePic" name="seekerProfile" required>
                    </div>
                    <div class="col-md-6">
                        <label for="seekerAadharNo" class="form-label">Aadhar Number</label>
                        <input type="text" class="form-control" id="seekerAadharNo" name="seekerAadharNo" required>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">Upload Aadhar Card (Front & Back)</label>
                        <input type="file" class="form-control" name="seekerAadharFront" required>
                        <input type="file" class="form-control mt-2" name="seekerAadharBack" required>
                    </div>
                    <div class="col-md-6">
                        <label for="vehicleImages" class="form-label">Upload Vehicle Images</label>
                        <input type="file" class="form-control" id="vehicleImages" name="seekerVehicleImages">
                    </div>
                    <div class="col-md-6">
                        <label for="licenseNo" class="form-label">Driving License No</label>
                        <input type="text" class="form-control" id="licenseNo" name="seekerDRlicense" required>
                    </div>
                    <div class="col-md-6">
                        <label for="vehicleRegNo" class="form-label">Vehicle Registration Certificate (RC) Number</label>
                        <input type="text" class="form-control" id="vehicleRegNo" name="seekerRCnumber" name="seekerRCnumber" required>
                    </div>
                    <div class="col-md-6">
                        <label for="seekerOccupation" class="form-label">Occupation</label>
                        <input type="text" class="form-control" id="seekerOccupation" name="seekerOccupation" required>
                    </div>
                    <div class="col-md-6">
                        <label for="seekerVehicleType" class="form-label">Vehicle Type</label>
                        <select class="form-select" id="seekerVehicleType" name="seekerVehicleType" required>
                            <option value="">Select Vehicle Type</option>
                            <option value="Car">car</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label for="licensePhoto" class="form-label">Upload Driving License Photo</label>
                        <input type="file" class="form-control" id="licensePhoto" name="seekerLicimg" required>
                    </div>
                    <div class="col-md-6">
                        <label for="seekerVehicleNo" class="form-label">Vehicle Number</label>
                        <input type="text" class="form-control" id="seekerVehicleNo" name="seekerVehicleNo" required>
                    </div>
                    <div class="col-md-6">
                        <label for="rcPhoto" class="form-label">Upload Vehicle RC Photo</label>
                        <input type="file" class="form-control" id="rcPhoto" name="seekerRCPhoto" required>
                    </div>
                    <div class="col-12">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" id="seekerTermsCheck" required>
                            <label class="form-check-label">I agree to the Terms & Conditions</label>
                        </div>
                    </div>
                    <div class="col-12 text-center">
                        <input type="submit" class="btn btn-primary" value="Sign Up" name="seekersubmit">
                    </div>
                              <div class="col-12 text-center"><p>Already have an account
                    <a class="dropdown-item" href="#" data-bs-toggle="modal"
                                    data-bs-target="#seekerLoginModal"><i class="fa-solid fa-user"
                                        style="margin-right: 15px;"></i></i>Login</a></p>
                                        </div>
                    </form>
            </div>
        </div>
    </div>
</div>


    <!-- 2nd section -->
    <section class="travel-section">
        <div class="container">
            <div class="row align-items-center">
                <!-- Left Content -->
                <div class="col-lg-6">
                    <div class="travel-content">
                        <h2>Make your travel experience as easy and stress-free as possible</h2>
                        <p>Seamless Rides, Transparent Pricing, and Professional Service – Your Journey, Your Way...</p>

                        <ul class="feature-list">
                            <li><i class="fas fa-check-circle"></i>Find the perfect vehicle for your trip</li>
                            <li><i class="fas fa-check-circle"></i> Clear and transparent prices</li>
                            <li><i class="fas fa-check-circle"></i> Professional Drivers</li>
                            <li><i class="fas fa-check-circle"></i> Diverse vehicles for your needs</li>
                        </ul>
                    </div>
                </div>

                <!-- Right Image -->
                <div class="col-lg-6 text-center position-relative">
                    <div class="travel-image">
                        <img src="./img/travel.jpg" alt="Taxi Service">
                    </div>                                                                                                              
                    <!-- Dashed Route Image -->
                    <img src="./img/map-ornamen-1.png" alt="" class="map-overlay">
                </div>
            </div>
        </div>
    </section>
    <!-- booking section -->
    <section class="booking-section">
        <div class="container">
            <div class="booking-content">
                <h2>Simple Steps to Book Your Ride</h2>
                <p>Follow these easy steps to get your ride ready in no time.</p>
            </div>
            <div class="row align-items-center">
                <div class="col-lg-6 step-list">
                    <h5>1. Type Your Destination</h5>
                    <p>Enter your destination and find the best routes available.</p>
                    <hr>

                    <h5>2. Confirm Pick-up Location</h5>
                    <p>Select your current location to ensure a smooth pickup.</p>
                    <hr>

                    <h5>3. Choose Payment Method</h5>
                    <p>Pick from multiple payment options for convenience.</p>
                    <hr>

                    <h5>4. Driver On The Way To Pick-up</h5>
                    <p>Track your driver and be ready when they arrive.</p>
                </div>
                <div class="col-lg-6 phone-image text-center">
                    <img src="./img/Step-1.png" alt="Booking App" style="height:500px;">
                </div>
            </div>
        </div>
    </section>
    <!-- Services Section -->
    <section class="service-section">
        <div class="container">
            <h2>The Ultimate Taxi Service Experience Awaits</h2>
            <p>Choose from a range of reliable and convenient transportation options.</p>

            <div class="row g-4">
                <!-- Card 1 -->
                <!-- Card 2: Scheduled Rides -->
                <div class="col-lg-4 col-md-6">
                    <div class="service-card">
                        <div class="icon-circle">
                            <i class="fas fa-calendar-alt"></i>
                        </div>
                        <h5 class="service-title">Scheduled Rides</h5>
                        <p class="service-text">Pre-book your rides to ensure timely and stress-free travel.</p>
                    </div>
                </div>
                <!-- Card 2 -->
                <div class="col-lg-4 col-md-6 mx-auto">
                    <div class="service-card">
                        <div class="icon-circle">
                            <i class="fas fa-users"></i>
                        </div>
                        <h5 class="service-title">Ride-Sharing</h5>
                        <p class="service-text">Share your ride with others to save costs while being eco-friendly.
                        </p>
                    </div>
                </div>

                <!-- Card 3 -->
                <!-- Card 1: Package Delivery -->
                <div class="col-lg-4 col-md-6">
                    <div class="service-card">
                        <div class="icon-circle">
                            <i class="fas fa-box"></i>
                        </div>
                        <h5 class="service-title">Package Delivery</h5>
                        <p class="service-text">Fast and reliable package delivery right at your doorstep.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="row text-center text-md-start">

                <!-- Left Section: Logo & About -->
                <div class="col-md-3 mb-3">
                    <img src="./img/ridd.png" alt="Logo" class="footer-logo">
                    <p>We are committed to providing seamless ride-sharing experiences with safety and efficiency.</p>
                </div>
                <!-- About Section -->
                <div class="col-md-3 mb-3">
                    <h4 style="color: black; font-weight: 600;font-size: 25px;">About</h4>
                    <ul class="list-unstyled">
                        <li><a href="#" class="text-light text-decoration-none">Home</a></li>
                        <li><a href="#" class="text-light text-decoration-none">Offers</a></li>
                        <li><a href="#" class="text-light text-decoration-none">Safety</a></li>
                        <li><a href="#" class="text-light text-decoration-none">Blog</a></li>
                    </ul>
                </div>

                <!-- Middle Section: Contact Details -->
                <div class="col-md-3 mb-3">
                    <h4 style="color: black; font-weight: 600;font-size: 25px;">Contact</h4>
                    <p><i class="fa-solid fa-location-dot"></i> 123 Main Street Saibaba Colony,Coimbatore,India</p>
                    <p><i class="fa-solid fa-phone"></i>+919973788650</p>
                    <p><i class="fa-solid fa-envelope"></i>officialvimal01@gmail.com</p>
                </div>

                <div class="col-md-3 mb-3">
                    <h4 style="color: black; font-weight: 600;font-size: 25px; margin-top: 100px;">Follow Us</h4>
                    <div class="social-icons">
                        <a href="#"><i class="fa-brands fa-facebook"></i></a>
                        <a href="#"><i class="fa-brands fa-twitter"></i></a>
                        <a href="#"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#"><i class="fa-brands fa-telegram"></i></a>
                    </div>

                </div>
            </div>

            <div class="footer-bottom">
                <p>© 2025 RideShare Inc. All rights reserved.</p>
            </div>
    </footer>
    <!-- Navbar JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
   <script src="registration.js"></script>
    <script src="admin.js"></script> 
    <script src="nav.js"></script>
    <script src="search.js"></script>
    <script src="ulget.js"></script>
    <script src="slget.js"></script>
    <script src="seekerreg1.js"></script>
</body>

</html>
""")





FirstName = form.getvalue("userFirstName")
LastName = form.getvalue("userLastName")
Email = form.getvalue("userEmail")
Phone = form.getvalue("userPhone")
addresu = form.getvalue("useraddre")
State = form.getvalue("userState")
City = form.getvalue("userCity")
Zipcode = form.getvalue("userZipCode")
Password = form.getvalue("userPassword")
Submit = form.getvalue("usersubmit")

if Submit is not None:
    image = form['profiPic']
    dl = os.path.basename(image.filename)
    open("images/" + dl, "wb").write(image.file.read())

    query = """INSERT INTO userdata (FirstName,Lastname,Email,Phone,profile,address,State,City,ZipCode,Password) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""%(FirstName, LastName, Email, Phone, dl, addresu, State, City, Zipcode, Password)
    cur.execute(query)
    con.commit()
    print("""
    <script>
       alert("User registered successfully");
    </script>
    """)






FName = form.getvalue("seekerFirstName")
LName = form.getvalue("seekerLastName")
Semail = form.getvalue("seekerEmail")
Sphone = form.getvalue("seekerPhone")
Saddress = form.getvalue("seekerAddress")
Sstate = form.getvalue("seekerState")
Scity = form.getvalue("seekerCity")
SzipCode = form.getvalue("seekerZipCode")
SdOB = form.getvalue("seekerDOB")
Sgender = form.getvalue("seekerGender")
SadharNo = form.getvalue("seekerAadharNo")
SDrlicense = form.getvalue("seekerDRlicense")
SRcnumber = form.getvalue("seekerRCnumber")
Soccupation = form.getvalue("seekerOccupation")
SvehicleType = form.getvalue("seekerVehicleType")
SehicleNo = form.getvalue("seekerVehicleNo")
Ssubmits = form.getvalue("seekersubmit")

if Ssubmits is not None:

    # Check if the user already exists (based on email or phone)
    check_query = "SELECT * FROM seekda WHERE Email = %s OR Phone = %s"
    cur.execute(check_query, (Semail, Sphone))
    existing_user = cur.fetchone()

    if existing_user:
        print("""
        <script>
           alert("User already registered with this Email or Phone!");
           window.location.replace("home.py");
        </script>
        """)
    else:
        # Default values for images in case they are not uploaded
        el = fl = gl = hl = il = jl = None

        if 'seekerProfile' in form:
            image1 = form['seekerProfile']
            el = os.path.basename(image1.filename)
            open("images/" + el, "wb").write(image1.file.read())

        if 'seekerAadharFront' in form:
            image2 = form['seekerAadharFront']
            fl = os.path.basename(image2.filename)
            open("images/" + fl, "wb").write(image2.file.read())

        if 'seekerAadharBack' in form:
            image3 = form['seekerAadharBack']
            gl = os.path.basename(image3.filename)
            open("images/" + gl, "wb").write(image3.file.read())

        if 'seekerVehicleImages' in form:
            image4 = form['seekerVehicleImages']
            hl = os.path.basename(image4.filename)
            open("images/" + hl, "wb").write(image4.file.read())

        if 'seekerLicimg' in form:
            image5 = form['seekerLicimg']
            il = os.path.basename(image5.filename)
            open("images/" + il, "wb").write(image5.file.read())

        if 'seekerRCPhoto' in form:
            image6 = form['seekerRCPhoto']
            jl = os.path.basename(image6.filename)
            open("images/" + jl, "wb").write(image6.file.read())

        # Insert the user data into database
        query = """INSERT INTO seekda 
            (FirstName, LastName, Email, Phone, addres, State, City, ZipCode, DateOfBirth, Profile, DrLicense, RcNumber, 
             Occupation, AadharNO, VehicleType, VehicleNumber, Gender, AadharFront, AadharBack, DrLicensePhoto, RCPhoto, VehicleImages) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (FName, LName, Semail, Sphone, Saddress, Sstate, Scity, SzipCode, SdOB, el, SDrlicense, SRcnumber,
                  Soccupation, SadharNo, SvehicleType, SehicleNo, Sgender, fl, gl, il, jl, hl)

        cur.execute(query, values)
        con.commit()

        print("""
        <script>
           alert("Registered successfully as a Seeker");
        </script>
        """)



    # Seeker Login
Emailsl = form.getvalue("userid")
Passsl = form.getvalue("pass")
Submitsl = form.getvalue("submitl")

if Submitsl != None:
    query = "SELECT SNo FROM seekda WHERE Userid = %s AND Password = %s"
    cur.execute(query, (Emailsl, Passsl))
    rec = cur.fetchone()

    if rec != None:
        print(f"""
              <script>
              alert("Login successful as Seeker!");
              location.href = "seekerdashboard.py?SNo={rec[0]}";
              </script>
              """)
    else:
        print("""
              <script>
              alert("Seeker not found or incorrect credentials!");
              </script>
            """)
    # user Login

Emailul = form.getvalue("emailus")
Passul = form.getvalue("passus")
Submitul = form.getvalue("submitus")

if Submitul != None:
    query = """SELECT cust_id FROM userdata WHERE Email = '%s' AND Password = '%s' """%(Emailul,Passul)
    cur.execute(query)
    res = cur.fetchone()

    if res != None:
        print("""
          <script>
          alert("Login successful as User!");
          location.href = "userdashboard.py?cust_id=%s";
          </script>
          """%(res[0]))
    else:
        print("""
              <script>
              alert("User not found or incorrect credentials!");
              </script>
            """)

