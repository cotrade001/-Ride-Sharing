#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, smtplib, random, string

cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
 <link rel="stylesheet" href="admindash.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

    <style>
        /* Table Styling */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #fff;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #343a40;
            color: white;
            font-weight: bold;
            text-transform: uppercase;
        }
        tbody tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        tbody tr:hover {
            background-color: #e9ecef;
            transition: 0.3s;
        }
        .table-responsive {
            overflow-x: auto;
            padding: 15px;
        }
    </style>
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

          <a href="#" onclick="showSection('users')"> <i class="fas fa-users"></i></i> Users</a>  

        <div class="dropdown">
            <a class="dropdown-toggle" href="#" id="seekerManagementDropdown" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                <i class="fa-solid fa-user"></i> Seeker Management
            </a>
            <ul class="dropdown-menu" aria-labelledby="seekerManagementDropdown">
                <li><a class="dropdown-item" href="#" onclick="showSection('seekers')">Seekers</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('approvedSeekers')">Approve Seekers</a></li>
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


        <!-- Reports & Analytics -->
        <a href="#" onclick="showSection('reportsAnalytics')"><i class="fa-solid fa-chart-line"></i> Reports &
            Analytics</a>
        <a href="index.html" onclick="showSection('overview')"><i class="fa-solid fa-door-open"></i> Logout</a>
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

query_seekers = "SELECT * FROM seekda WHERE Status = 'approved'"
cur.execute(query_seekers)
seekers = cur.fetchall()
for seeker in seekers:
    print(f"""
                <tr>
                    <td>{seeker[0]}</td>
                    <td>{seeker[1]}</td>
                    <td>{seeker[2]}</td>
                    <td>{seeker[3]}</td>
                    <td>{seeker[4]}</td>
                    <td>{seeker[5]}</td>
                    <td>{seeker[6]}</td>
                    <td>{seeker[7]}</td>
                    <td>{seeker[8]}</td>
                    <td>{seeker[9]}</td>
                    <td>{seeker[10]}</td>
                    <td>{seeker[11]}</td>
                    <td>{seeker[12]}</td>

                </tr>
    """)

print("""
            </tbody>
        </table>
        </div>
        </div> """)

print("""

        
        <div class="content">
        <div id="approvedSeekers" class="section">
            <h2><i class="fas fa-user"></i> Pending Seekers</h2>
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
                    <th>Status</th>
                    <th>Action</th>

                </tr>
            </thead>
            <tbody>
""")

query_seekers = "SELECT * FROM seekda where Status = 'pending'"
cur.execute(query_seekers)
seekers = cur.fetchall()

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

for seeker in seekers:
    seeker_id = seeker[0]

    user_id = f"RS{seeker_id}"
    password = seeker[1][:2] + seeker[6][:3] + generate_random_string(3)

for seeker in seekers:

     print(f"""
                <tr>
                    <td>{seeker[0]}</td>
                    <td>{seeker[1]}</td>
                    <td>{seeker[2]}</td>
                    <td>{seeker[3]}</td>
                    <td>{seeker[4]}</td>
                    <td>{seeker[5]}</td>
                    <td>{seeker[6]}</td>
                    <td>{seeker[7]}</td>
                    <td>{seeker[8]}</td>
                    <td>{seeker[9]}</td>
                    <td>{seeker[10]}</td>
                    <td>{seeker[11]}</td>
                    <td>{seeker[12]}</td>
                    <td>{seeker[15]}</td>
                     <td>
                <button type="button" class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#mymodal{seeker_id}">Generate</button>
            </td>
        </tr>

        <!-- Modal for Each Seeker -->
        <div class="modal fade" id="mymodal{seeker_id}" tabindex="-1" aria-labelledby="modalLabel{seeker_id}" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title">User Details</h4>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <form method="post">
                        <div class="modal-body">
                            <label>User ID:</label>
                            <input type="text" name="userid" class="form-control" value="{user_id}" readonly>

                            <label>Password:</label>
                            <input type="text" name="password" class="form-control" value="{password}" readonly>

                            <input type="hidden" name="cid" value="{seeker_id}">
                        </div>
                        <div class="modal-footer">
                            <input type="submit" name="update" class="btn btn-success" value="Approve">
                            <input type="submit" name="reject" class="btn btn-danger" value="Reject">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    """)

print("""
                </tbody>
            </table>
            </div>
        </div>
    </div> """)

print("""
<script>
    function showSection(sectionId) {
        document.querySelectorAll('.section').forEach(section => {
            section.classList.add('hidden'); // Hide all sections
        });
        document.getElementById(sectionId).classList.remove('hidden'); // Show selected section
    }
    </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
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
    email = seeker[3]
    name = seeker[1]

    fromadd = "officialvimal01@gmail.com"
    ppassword = "gokk ckjn jvin yvuq"
    subject = "Your RideShare User ID & Password"
    body = f"Hello {name},\n\nYour User ID: {user_id}\nYour Password: {password}\n\nThank you for registering with RideShare!"

    msg = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
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
        Name = i[1]

if reject:
    # Fetch seeker data before rejection
    email_query = "SELECT Email, FirstName FROM seekda WHERE SNo=%s"
    cur.execute(email_query, (cid,))
    seeker_data = cur.fetchone()

    if seeker_data:
        email = seeker_data[0]
        Name = seeker_data[1]

        # Update seeker status to rejected
        q = """UPDATE seekda SET status='rejected' WHERE SNo=%s"""
        cur.execute(q, (cid,))
        con.commit()

        print("""
        <script>
            alert("Seeker rejected successfully");
            location.href="Admindashboard.py";
        </script>
        """)

        # Send rejection email
        fromadd = "officialvimal01@gmail.com"
        ppassword = "gokk ckjn jvin yvuq"
        toadd = email
        subject = "From Ride Sharing"
        body = f"Hello {Name},\n\nThank you for registering with us!\n\nUnfortunately, you did not meet our criteria. Please submit original licenses."

        msg = f"Subject: {subject}\n\n{body}"

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(fromadd, ppassword)
            server.sendmail(fromadd, toadd, msg)
            server.quit()
            print("<script>alert('Seeker rejected & email sent successfully');</script>")
        except Exception as e:
            print(f"<script>alert('Error sending email: {str(e)}');</script>")
    else:
        print("<script>alert('Seeker not found in the database');</script>")

