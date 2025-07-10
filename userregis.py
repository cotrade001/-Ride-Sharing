#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()

print("""
<form id="userForm" class="row g-3 needs-validation" novalidate enctype="multipart/form-data" method="POST" name="" onsubmit="()">
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
""")
form = cgi.FieldStorage()

Fname = form.getvalue("userFirstName")
Lname = form.getvalue("userLastName")
Email = form.getvalue("userEmail")
Phone = form.getvalue("userPhone")
State = form.getvalue("userState")
City = form.getvalue("userCity")
Zipcode = form.getvalue("userZipCode")
Password = form.getvalue("userPassword")
Submit = form.getvalue("usersubmit")

if Submit != None:
    x = """insert into userdata(FirstName,Lastname,Email,Phone,State,City,ZipCode,Password) values('%s','%s','%s','%s','%s','%s','%s','%s')""" % (Fname,Lname,Email,Phone,State,City,Zipcode,Password)
    cur.execute(x)
    con.commit()
    print("""
    <script>
       alert("registered successfully")
    </script>
    """)