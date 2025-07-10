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
    <title>Admin Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <link rel="stylesheet" href="admindash.css">
</head>

<body>

    <div class="top-navbar d-flex">
        <span class="menu-btn" onclick="toggleSidebar()"><i class="fas fa-bars"></i></span>
        <h6 class="m-0">Admin Dashboard</h6>
    </div>


    <div class="sidebar">
        <div style="margin-left: 10px; display:flex; align-items:center; ">
            <img src="./img/Ride+Share+Logo+2.jpg" style="height: 50px; width:50px; border-radius:100px;" alt="">
            <h6 class="mt-3" style="margin-left:10px;">Welcome Admin</h6>
        </div>
        <h4 class="text-center mt-3"><i class="fas fa-user-shield"></i> Admin Dashboard</h4>
        <a href="#" onclick="showSection('overview')"><i class="fas fa-tachometer-alt"></i> Overview</a>
        <div class="dropdown">
            <a class="dropdown-toggle" href="#" id="userManagementDropdown" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                <i class="fas fa-users"></i> User Management
            </a>
            <ul class="dropdown-menu" aria-labelledby="userManagementDropdown">
                <li><a class="dropdown-item" href="#" onclick="showSection('users')">Users</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('approvedUsers')">Approved Users</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('rejectedUsers')">Rejected Users</a></li>
            </ul>
        </div>       
        <div class="dropdown">
            <a class="dropdown-toggle" href="#" id="seekerManagementDropdown" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                <i class="fa-solid fa-user"></i> Seeker Management
            </a>
            <ul class="dropdown-menu" aria-labelledby="seekerManagementDropdown">
                <li><a class="dropdown-item" href="#" onclick="showSection('seekers')">Seekers</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('approvedSeekers')">Approved Seekers</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('rejectedSeekers')">Rejected Seekers</a></li>
            </ul>
        </div>
        
        <div class="dropdown">
            <a class="dropdown-toggle" href="#" id="rideManagementDropdown" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                <i class="fa-solid fa-car"></i> Ride Management
            </a>
            <ul class="dropdown-menu" aria-labelledby="rideManagementDropdown">
                <li><a class="dropdown-item" href="#" onclick="showSection('activeRides')">Active Rides</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('completedRides')">Completed Rides</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('cancelledRides')">Cancelled Rides</a></li>
            </ul>
        </div>
        

        <!-- Reports & Analytics without dropdown -->
        <a href="#" onclick="showSection('reportsAnalytics')"><i class="fa-solid fa-chart-line"></i> Reports &
            Analytics</a>

        <a href="index.html" onclick="showSection('overview')"><i class="fa-solid fa-door-open"></i> Logout</a>
    </div>


    <div class="sidebar-backdrop" onclick="toggleSidebar()"></div>

    </div>
     <div class="content">
       <div id="users" class="section hidden">
        <h2><i class="fas fa-users"></i> Users</h2>
        <div class="table-responsive">
        <table class="table table-striped table-hover">
            <thead>
                <tr>
                    <th>S.No</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>State</th>
                    <th>City</th>
                    <th>Zipcode</th>
                    
                </tr>
            </thead>
            <tbody>
""")
query = "SELECT * FROM userdata"
cur.execute(query)
res = cur.fetchall()
for i in res:
    print(f""" 
                <tr>
                    <td>{i[0]}</td>
                    <td>{i[1]}</td>
                    <td>{i[2]}</td>
                    <td>{i[3]}</td>
                    <td>{i[4]}</td>
                    <td>{i[5]}</td>
                    <td>{i[6]}</td>
                    <td>{i[7]}</td>

                </tr>
    """)
    print("""
                </tbody>
            </table>
            </div>
        </div>

        <div id="seekers" class="section hidden">
            <h2><i class="fas fa-user"></i> Seekers</h2>
            <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead>
                    <tr>
                        <th>S.No</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                         <th>Email</th>
                        <th>Phone</th>
                         <th>State</th>
                        <th>City</th>
                        <th>Zipcode</th>
                        <th>DOB</th>
                         <th>Occupation</th>
                        <th>Aadhar No</th>
                         <th>Vehicle Type</th>
                        <th>Vehicle No</th>

                    </tr>
                </thead>
                <tbody>
    """)

print("""

     <div class="sidebar-backdrop" onclick="toggleSidebar()"></div>    
    <div id="approvedUsers" class="section hidden">
        <h2><i class="fa-solid fa-user-check"></i> Approved Users</h2>
        <p>View and manage approved users.</p>
    </div>
    
    <div id="rejectedUsers" class="section hidden">
        <h2><i class="fa-solid fa-user-times"></i> Rejected Users</h2>
        <p>View and manage rejected users.</p>
    </div>
    <div id="seekers" class="section hidden">
        <h2><i class="fas fa-user"></i> Seekers</h2>
        <p>View and manage all seekers.</p>
    </div>
    
    <div id="approvedSeekers" class="section hidden">
        <h2><i class="fa-solid fa-user-check"></i> Approved Seekers</h2>
        <p>View and manage approved seekers.</p>
    </div>
    
    <div id="rejectedSeekers" class="section hidden">
        <h2><i class="fa-solid fa-user-times"></i> Rejected Seekers</h2>
        <p>View and manage rejected seekers.</p>
    </div>
    
    <div id="activeRides" class="section hidden">
        <h2><i class="fa-solid fa-car-side"></i> Active Rides</h2>
        <p>Manage all ongoing rides here.</p>
    </div>
    
    <div id="completedRides" class="section hidden">
        <h2><i class="fa-solid fa-check-circle"></i> Completed Rides</h2>
        <p>View all completed rides and details.</p>
    </div>
    
    <div id="cancelledRides" class="section hidden">
        <h2><i class="fa-solid fa-times-circle"></i> Cancelled Rides</h2>
        <p>Manage all cancelled rides.</p>
    </div>
    
    <div id="reportsAnalytics" class="section hidden">
        <h2><i class="fa-solid fa-chart-line"></i> Reports & Analytics</h2>
        <p>View statistics and analytics of the platform.</p>
    </div>
</div>
  <script>
        function showSection(sectionId) {
            document.querySelectorAll('.section').forEach(section => {
                section.classList.add('hidden');
            });
            document.getElementById(sectionId).classList.remove('hidden');
        }
    </script>
    </script> <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>
""")

form = cgi.FieldStorage()
cid = form.getvalue("cid")
user_id = form.getvalue("userid")
password = form.getvalue("password")
submit = form.getvalue("update")
reject = form.getvalue("reject")

if submit:
    q = """UPDATE seekda SET userid=%s, password=%s, status='approved' WHERE SNo=%s"""
    cur.execute(q, (user_id, password, cid))
    con.commit()

    email_query = "SELECT Email, FirstName FROM seekda WHERE SNo=%s"
    cur.execute(email_query, (cid))
    seeker_data = cur.fetchone()
    email = i[3]
    name = i[1]

    fromadd = "officialvimal01@gmail.com"
    ppassword = "gokk ckjn jvin yvuq"
    subject = "Your RideShare User ID & Password"
    body = f"Hello {name},\n\nYour User ID: {user_id}\nYour Password: {password}\n\nThank you for registering with RideShare!"

    msg = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(fromadd, ppassword)
        server.sendmail(fromadd, email, msg)
        server.quit()
        print("<script>alert('User approved & email sent successfully');</script>")
    except Exception as e:
        print(f"<script>alert('Error sending email: {str(e)}');</script>")

    query_seekers = "SELECT * FROM seekda WHERE Status = 'pending'"
    cur.execute(query_seekers)
    seekers = cur.fetchall()

    for i in seekers:
        email = i[3]

if reject:
    q = """UPDATE seekda SET status='rejected' WHERE SNo=%s"""
    cur.execute(q, (cid,))
    con.commit()

    email_query = "SELECT email, first_name FROM seekda WHERE SNo=%s"
    cur.execute(email_query, (cid,))
    seeker_data = cur.fetchone()
    email, seeker_name = seeker_data

    fromadd = "officialvimal01@gmail.com"
    ppassword = "gokk ckjn jvin yvuq"
    toadd = email
    subject = "RideShare Registration Update"
    body = f"Hello {seeker_name},\n\nUnfortunately, your registration has been rejected as you did not meet all the criteria.\n\nPlease contact support for further details."

    msg = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(fromadd, ppassword)
        server.sendmail(fromadd, email, msg)
        server.quit()
        print("<script>alert('User rejected & email sent successfully');</script>")
    except Exception as e:
        print(f"<script>alert('Error sending email: {str(e)}');</script>")
