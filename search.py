#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, sys

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()

# Get form data
form = cgi.FieldStorage()
search_queryf = form.getvalue("fromLocation")
search_queryt = form.getvalue("toLocation")
ride_date = form.getvalue("rideDate")  # Optional
vehicle_type = form.getvalue("vehicleType")  # Optional
submit_button = form.getvalue("submitb")

rides = []

# Ensure fromLocation and toLocation are provided
if submit_button and search_queryf and search_queryt:
    sql = "SELECT * FROM rides WHERE pickup_location = %s AND dropoff_location = %s AND status = 'pending'"
    params = [search_queryf, search_queryt]

    # Add optional filters
    if ride_date:
        sql += " AND DATE(ride_datetime) = %s"  # Use DATE() function to compare only the date
        params.append(ride_date)

    if vehicle_type:
        sql += " AND vehicle_type = %s"
        params.append(vehicle_type)

    cur.execute(sql, params)
    rides = cur.fetchall()

    # Print HTML Output
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Available Rides - RideShare</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
        <style>
            body {{ background-color: #f8f9fa; }}
            .ride-card {{ border-radius: 15px; overflow: hidden; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2); transition: transform 0.3s ease-in-out; cursor: pointer; background: white; }}
            .ride-card:hover {{ transform: scale(1.05); }}
            .card-header {{ background: linear-gradient(to right, #ff7e5f, #feb47b); color: white; font-size: 1.2rem; font-weight: bold; padding: 15px; text-align: center; }}
            .card-body {{ padding: 20px; text-align: left; }}
            .btn-book {{ background: linear-gradient(to right, #ff416c, #ff4b2b); border: none; font-weight: bold; }}
            .btn-book:hover {{ background: linear-gradient(to right, #ff4b2b, #ff416c); }}
        </style>
    </head>
    <body>

    <div class="container mt-5">
        <h2 class="text-center">Available Rides</h2>
        <p class="text-center">Showing rides from <b>{search_queryf}</b> to <b>{search_queryt}</b></p>
    """)

    if ride_date:
        print(f"<p class='text-center'>📅 Date: <b>{ride_date}</b></p>")
    if vehicle_type:
        print(f"<p class='text-center'>🚘 Vehicle Type: <b>{vehicle_type}</b></p>")

    print("<div class='row'>")

    # Display rides
    if rides:
        for ride in rides:
            print(f"""
            <div class="col-md-4 col-sm-6 mb-4">
                <div class="card ride-card">
                    <div class="card-header">
                        🚖 Available Ride
                    </div>
                    <div class="card-body">
                        <h5 class="mb-3"><i class="fas fa-map-marker-alt"></i> Ride Information</h5>
                        <p><strong>🚗 From:</strong> {ride[6]}</p>
                        <p><strong>📍 To:</strong> {ride[7]}</p>
                        <p><strong>📅 Ride Date:</strong> {ride[8]}</p>
                        <p><strong>🚘 Vehicle Type:</strong> {ride[9]}</p>
                        <p><strong>🧑‍🤝‍🧑 Seats Available:</strong> {ride[10]}</p>
                        <p><strong>💰 Price/Seat:</strong> {ride[11]}</p>

                        <a href="#" class="btn btn-book w-100 mt-2" data-bs-toggle="modal" data-bs-target="#userLoginModal" onclick="setRideId('{ride[0]}')">
                               Login & Book Now
                        </a>
                    </div>
                </div>
            </div>
            """)

    else:
        print("<p class='text-center mt-4 alert alert-warning'>No rides found for this route.</p>")

    print("</div></div></body></html>")

    print("""
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

<script>
    function setRideId(rideId) {
        document.getElementById('modalRideId').value = rideId;
    }
</script>
     <script src="registration.js"></script>
    <script src="admin.js"></script> 
    <script src="nav.js"></script>
    <script src="search.js"></script>
    <script src="ulget.js"></script>
    <script src="slget.js"></script>
     <script src="seekerreg1.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
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