#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, smtplib, random, string, os,sys
sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()
form = cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
 <link rel="stylesheet" href="admindash.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
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
        
        .dropdown-menu {
    background-color: rgb(21 57 108);
}
.hidden {
    display: none;
}
.sidebar {
    background-color:#00008B;
}

.top-navbar {
    background-color:#00008B;
    color: white;
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
        
          <a href="#" onclick="showSection('users')"> <i class="fas fa-users"></i></i> Users</a>  
           
        <div class="dropdown">
            <a class="dropdown-toggle" href="#" id="seekerManagementDropdown" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                <i class="fa-solid fa-user"></i> Sharer Management
            </a>
            <ul class="dropdown-menu" aria-labelledby="seekerManagementDropdown">
                <li><a class="dropdown-item" href="#" onclick="showSection('approvedSeekers')"><i class="fas fa-hourglass-half"></i> Pending Sharers</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('seekers')"><i class="fas fa-users"></i>Approve Sharers</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('rejectedSeekers')"><i class="fas fa-times-circle"></i> Rejected Sharers</a></li>
            </ul>
        </div>
        
        <div class="dropdown">
            <a class="dropdown-toggle" href="#" id="rideManagementDropdown" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                <i class="fa-solid fa-car"></i> Ride Management
            </a>
            <ul class="dropdown-menu" aria-labelledby="rideManagementDropdown">
                <li><a class="dropdown-item" href="#" onclick="showSection('seekerPost')"> <i class="fas fa-share-alt"></i> Sharer-Post</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('activeRides')"> <i class="fas fa-car-side"></i> Active Rides</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('completedRides')"> <i class="fas fa-check-circle"></i> Completed Rides</a></li>
               <li><a class="dropdown-item" href="#" onclick="showSection('cancelledByUser')"> <i class="fas fa-times-circle"></i> Cancelled Rides</a></li>
            </ul>
        </div>
        

       <a href="#" onclick="showSection('queries')"> <i class="fas fa-headset"></i> Queries</a>
        <a href="home.py" onclick="showSection('overview')"><i class="fa-solid fa-door-open"></i> Logout</a>
""")
print("""
    </div>
    <div class="content">
        <div id="users" class="section hidden">
            <h2 class="text-center p-3" style="color: #ffffff; font-weight: bold; background: linear-gradient(90deg, #6a11cb, #2575fc); border-radius: 10px;">
                <i class="fas fa-users"></i> Users
            </h2>
            <div class="table-responsive" style="padding: 20px; background: #ffffff; border-radius: 10px; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);">
                <table class="table table-hover table-bordered text-center" style="border-radius: 10px; overflow: hidden;">
                    <thead class="text-white" style="background: linear-gradient(90deg, #343a40, #6a11cb);">
                        <tr>
                            <th style="width: 5%; background: #4e4e70;">S.NO</th>
                            <th style="width: 10%;">First Name</th>
                            <th style="width: 10%;">Last Name</th>
                            <th style="width: 15%;">Email</th>
                            <th style="width: 10%;">Phone</th>
                            <th style="width: 10%;">Profile</th>
                            <th style="width: 20%;">Address</th>
                            <th style="width: 10%;">State</th>
                            <th style="width: 10%;">City</th>
                            <th style="width: 10%;">Zipcode</th>
                        </tr>
                    </thead>
                    <tbody class="align-middle text-center">
""")

query = "SELECT * FROM userdata"
cur.execute(query)
res = cur.fetchall()
for i, row in enumerate(res, start=1):
    bg_color = "#f4f4f9" if i % 2 == 0 else "#dce3f2"  # Soft alternating row colors
    print(f""" 
                <tr style="background-color: {bg_color}; color: #222;">
                    <td><b>{row[0]}</b></td>
                    <td style="font-weight: bold; color: #6a11cb;">{row[1]}</td>
                    <td>{row[2]}</td>
                    <td><a href="mailto:{row[3]}" style="text-decoration: none; color: #2575fc; font-weight: bold;">{row[3]}</a></td>
                    <td><a href="tel:{row[4]}" style="text-decoration: none; color: #28a745; font-weight: bold;">{row[4]}</a></td>
                    <td>
                        <img src="./images/{row[5]}" style="width:50px; height:50px; border-radius: 50%; box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.3); transition: transform 0.3s;" 
                        onmouseover="this.style.transform='scale(1.1)'" 
                        onmouseout="this.style.transform='scale(1)'">
                    </td>
                    <td style="white-space: normal; word-wrap: break-word; font-size: 14px; color: #555;">{row[6]}</td>
                    <td style="color: #ff5722;">{row[7]}</td>
                    <td style="color: #17a2b8;">{row[8]}</td>
                    <td style="color: #795548;">{row[9]}</td>
                </tr>
    """)

print("""
            </tbody>
        </table>
        </div>
    </div> 
""")

print("""
<div id="seekers" class="section hidden">
    <h2 class="text-light bg-dark p-3 rounded"><i class="fas fa-user"></i>Approve Sharers</h2>
    <div class="table-responsive" style="background:#1e1e2f; padding:20px; border-radius:10px; box-shadow:0px 4px 10px rgba(0,0,0,0.2);">
        <table class="table table-dark table-striped table-hover">
            <thead style="background:#2a2a3c; color:#ffffff;">
                <tr>
                    <th>SNO</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>Profile</th>
                    <th>State</th>
                    <th>City</th>
                    <th>Zipcode</th>
                    <th>More Details</th>
                </tr>
            </thead>
            <tbody>
""")

query_seekers = "SELECT * FROM seekda WHERE Status = 'approved'"
cur.execute(query_seekers)
seekers = cur.fetchall()

for seeker in seekers:
    print(f"""
        <tr class="text-center">
            <td>{seeker[0]}</td>
            <td>{seeker[1]}</td>
            <td>{seeker[2]}</td>
            <td>{seeker[3]}</td>
            <td>{seeker[4]}</td>
            <td>
                <img src="./images/{seeker[10]}" style="width:50px; height:50px; border-radius:50%; box-shadow:0px 2px 8px rgba(0,0,0,0.3); transition: transform 0.3s ease;" 
                     onmouseover="this.style.transform='scale(1.2)'" onmouseout="this.style.transform='scale(1)'">
            </td>
            <td>{seeker[6]}</td>
            <td>{seeker[7]}</td>
            <td>{seeker[8]}</td>
            <td>
                <button type="button" class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#modal{seeker[0]}">
                    View More
                </button>
            </td>
        </tr>

        <div class="modal fade" id="modal{seeker[0]}" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-lg">
                <div class="modal-content" style="background:#1e1e2f; color:white; border-radius:15px; box-shadow:0px 4px 10px rgba(0,0,0,0.3);">
                    <div class="modal-header" style="border-bottom:1px solid #444;">
                        <h5 class="modal-title" style="color:#f8f9fa;">
                            <i class="fas fa-info-circle"></i> Details of {seeker[1]} {seeker[2]}
                        </h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" style="filter: invert(1);"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <div class="col-md-6">
                                <p><strong>Gender:</strong> {seeker[20]}</p>
                                <p><strong>Date of Birth:</strong> {seeker[9]}</p>
                                <p><strong>Phone:</strong> {seeker[4]}</p>
                                <p><strong>Email:</strong> {seeker[3]}</p>
                                <p><strong>Address:</strong> {seeker[5]}</p>
                                <p><strong>State:</strong> {seeker[6]}</p>
                                <p><strong>City:</strong> {seeker[7]}</p>
                                <p><strong>Zipcode:</strong> {seeker[8]}</p>
                            </div>
                            <div class="col-md-6">
                                <p><strong>Occupation:</strong> {seeker[13]}</p>
                                <p><strong>Driving License:</strong> {seeker[11]}</p>
                                <p><strong>Vehicle RC Number:</strong> {seeker[12]}</p>
                                <p><strong>Vehicle Type:</strong> {seeker[15]}</p>
                                <p><strong>Vehicle No:</strong> {seeker[16]}</p>
                                <p><strong>Aadhar No:</strong> {seeker[14]}</p>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col-md-4">
                                <p><strong>Profile Photo:</strong></p>
                                <img src="./images/{seeker[10]}" class="img-thumbnail" alt="Profile Photo">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Driving License:</strong></p>
                                <img src="./images/{seeker[24]}" class="img-thumbnail" alt="Driving License">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Vehicle RC Photo:</strong></p>
                                <img src="./images/{seeker[25]}" class="img-thumbnail" alt="Vehicle RC">
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col-md-4">
                                <p><strong>Aadhar Front:</strong></p>
                                <img src="./images/{seeker[21]}" class="img-thumbnail" alt="Aadhar Front">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Aadhar Back:</strong></p>
                                <img src="./images/{seeker[22]}" class="img-thumbnail" alt="Aadhar Back">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Vehicle Image:</strong></p>
                                <img src="./images/{seeker[23]}" class="img-thumbnail" alt="Vehicle Image">
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer" style="border-top:1px solid #444;">
                        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    """)

print("""
                </tbody>
            </table>
        </div>
    </div>
""")


print(""" 
    <div id="approvedSeekers" class="section">
        <h2 class="text-light bg-gradient p-3 rounded text-center" style="background: #3b3b5f;">
            <i class="fas fa-user"></i> Pending Sharers
        </h2>
        <div class="table-responsive" style="background:#252547; padding:20px; border-radius:10px; box-shadow:0px 4px 10px rgba(0,0,0,0.3);">
            <table class="table table-dark table-striped table-hover">
                <thead style="background:#2c2c5e; color:#ffffff;">
                    <tr class="text-center">
                        <th>SNO</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>State</th>
                        <th>City</th>
                        <th>Zipcode</th>
                        <th>Profile</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
""")

query_seekers = "SELECT * FROM seekda WHERE Status = 'pending'"
cur.execute(query_seekers)
seekers = cur.fetchall()

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

for seeker in seekers:
    seeker_id = seeker[0]
    user_id = f"RS{seeker_id}"
    password = seeker[1][:2] + seeker[6][:3] + generate_random_string(3)

    print(f"""
        <tr class="text-center">
            <td>{seeker[0]}</td>
            <td>{seeker[1]}</td>
            <td>{seeker[2]}</td>
            <td>{seeker[3]}</td>
            <td>{seeker[4]}</td>
            <td>{seeker[6]}</td>
            <td>{seeker[7]}</td>
            <td>{seeker[8]}</td>
            <td>
                <img src="./images/{seeker[10]}" style="width:50px; height:50px; border-radius:50%; box-shadow:0px 2px 8px rgba(0,0,0,0.3); transition: transform 0.3s ease;" 
                     onmouseover="this.style.transform='scale(1.2)'" onmouseout="this.style.transform='scale(1)'">
            </td>
            <td>
                <button type="button" class="btn btn-info btn-sm" data-bs-toggle="modal" data-bs-target="#mymodal{seeker_id}">
                    View More
                </button>
            </td>
        </tr>

        <div class="modal fade" id="mymodal{seeker_id}" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-lg">
                <div class="modal-content" style="background:#1e1e2f; color:white; border-radius:15px; box-shadow:0px 4px 10px rgba(0,0,0,0.3);">
                    <div class="modal-header" style="border-bottom:1px solid #444;">
                        <h5 class="modal-title" style="color:#f8f9fa;">
                            <i class="fas fa-info-circle"></i> Details of {seeker[1]} {seeker[2]}
                        </h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" style="filter: invert(1);"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <div class="col-md-6">
                                <p><strong>Gender:</strong> {seeker[20]}</p>
                                <p><strong>Date of Birth:</strong> {seeker[9]}</p>
                                <p><strong>Phone:</strong> {seeker[4]}</p>
                                <p><strong>Email:</strong> {seeker[3]}</p>
                                <p><strong>Address:</strong> {seeker[5]}</p>
                                <p><strong>State:</strong> {seeker[6]}</p>
                                <p><strong>City:</strong> {seeker[7]}</p>
                                <p><strong>Zipcode:</strong> {seeker[8]}</p>
                            </div>
                            <div class="col-md-6">
                                <p><strong>Occupation:</strong> {seeker[13]}</p>
                                <p><strong>Driving License:</strong> {seeker[11]}</p>
                                <p><strong>Vehicle RC Number:</strong> {seeker[12]}</p>
                                <p><strong>Vehicle Type:</strong> {seeker[15]}</p>
                                <p><strong>Vehicle No:</strong> {seeker[16]}</p>
                                <p><strong>Aadhar No:</strong> {seeker[14]}</p>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col-md-4">
                                <p><strong>Profile Photo:</strong></p>
                                <img src="./images/{seeker[10]}" class="img-thumbnail" alt="Profile Photo">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Driving License:</strong></p>
                                <img src="./images/{seeker[24]}" class="img-thumbnail" alt="Driving License">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Vehicle RC Photo:</strong></p>
                                <img src="./images/{seeker[25]}" class="img-thumbnail" alt="Vehicle RC">
                            </div>
                        </div>
                         <div class="row mt-3">
                            <div class="col-md-4">
                                <p><strong>Vehicle Image</strong></p>
                                <img src="./images/{seeker[23]}" class="img-thumbnail" alt="Profile Photo">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Aadhar Card Front</strong></p>
                                <img src="./images/{seeker[21]}" class="img-thumbnail" alt="Driving License">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Aadhar Card Back</strong></p>
                                <img src="./images/{seeker[22]}" class="img-thumbnail" alt="Vehicle RC">
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer" style="border-top:1px solid #444;">
                        <form method="post" action="Admindashboard.py">
                            <div class="mt-3">
                                <label><strong>User ID:</strong></label>
                                <input type="text" name="userid" class="form-control" value="{user_id}" readonly>
                                <label><strong>Password:</strong></label>
                                <input type="text" name="password" class="form-control" value="{password}" readonly>
                                <input type="hidden" name="cid" value="{seeker_id}">
                            </div>
                                <div class="modal-footer" style="border-top:1px solid #444;">
                                <input type="submit" name="update" class="btn btn-success" value="Approve">
                                <input type="submit" name="reject" class="btn btn-danger" value="Reject">
                            </div>
                        </form>
                        
                    </div>
                     <div class="modal-footer" style="border-top:1px solid #444;">
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
            </div>
                </div>
            </div>
        </div>
    """)

print("""
                </tbody>
            </table>
        </div>
    </div>
""")



print("""
    <div id="rejectedSeekers" class="section hidden">
        <h2 class="text-light bg-danger p-3 rounded text-center">
            <i class="fas fa-user-times"></i> Rejected Sharers
        </h2>
        <div class="table-responsive" style="background:#3a3a5a; padding:20px; border-radius:10px; box-shadow:0px 4px 10px rgba(0,0,0,0.3);">
            <table class="table table-dark table-hover table-bordered">
                <thead class="bg-danger text-light">
                    <tr class="text-center">
                        <th>SNO</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>State</th>
                        <th>City</th>
                        <th>Zipcode</th>
                        <th>Profile</th>
                        <th>View More</th>
                    </tr>
                </thead>
                <tbody>
""")

query_seekers = "SELECT * FROM seekda WHERE Status = 'rejected'"
cur.execute(query_seekers)
seekers = cur.fetchall()

for seeker in seekers:
    seeker_id = seeker[0]
    print(f"""
        <tr class="text-center">
            <td>{seeker[0]}</td>
            <td>{seeker[1]}</td>
            <td>{seeker[2]}</td>
            <td>{seeker[3]}</td>
            <td>{seeker[4]}</td>
            <td>{seeker[6]}</td>
            <td>{seeker[7]}</td>
            <td>{seeker[8]}</td>
            <td>
                <img src="./images/{seeker[10]}" style="width:50px;height:50px; border-radius:50%; transition: transform 0.3s ease;" 
                     onmouseover="this.style.transform='scale(1.2)'" onmouseout="this.style.transform='scale(1)'">
            </td>
            <td>
                <button type="button" class="btn btn-info btn-sm" data-bs-toggle="modal" data-bs-target="#mymodal{seeker_id}">
                    View More
                </button>
            </td>
        </tr>

        <div class="modal fade" id="mymodal{seeker_id}" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-lg">
                <div class="modal-content" style="background:#252547; color:white; border-radius:15px; box-shadow:0px 4px 10px rgba(0,0,0,0.4);">
                    <div class="modal-header" style="border-bottom:1px solid #444;">
                        <h4 class="modal-title">
                            <i class="fas fa-info-circle"></i> Details of {seeker[1]} {seeker[2]}
                        </h4>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" style="filter: invert(1);"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <div class="col-md-6">
                                <p><strong>Gender:</strong> {seeker[20]}</p>
                                 <p><strong>Address:</strong> {seeker[5]}</p>
                                <p><strong>Date of Birth:</strong> {seeker[9]}</p>
                                <p><strong>Phone:</strong> {seeker[4]}</p>
                                <p><strong>Email:</strong> {seeker[3]}</p>
                                <p><strong>State:</strong> {seeker[6]}</p>
                                <p><strong>City:</strong> {seeker[7]}</p>
                                <p><strong>Zipcode:</strong> {seeker[8]}</p>
                                <p><strong>Occupation:</strong> {seeker[13]}</p>
                            </div>
                            <div class="col-md-6">
                                <p><strong>Driving License:</strong> {seeker[11]}</p>
                                <p><strong>Vehicle RC Number:</strong> {seeker[12]}</p>
                                <p><strong>Vehicle Type:</strong> {seeker[15]}</p>
                                <p><strong>Vehicle No:</strong> {seeker[16]}</p>
                                <p><strong>Aadhar No:</strong> {seeker[14]}</p>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col-md-4">
                                <p><strong>Profile Photo:</strong></p>
                                <img src="./images/{seeker[10]}" class="img-thumbnail" alt="Profile Photo">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Driving License:</strong></p>
                                <img src="./images/{seeker[24]}" class="img-thumbnail" alt="Driving License">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Vehicle RC Photo:</strong></p>
                                <img src="./images/{seeker[25]}" class="img-thumbnail" alt="Vehicle RC">
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col-md-4">
                                <p><strong>Aadhar Front:</strong></p>
                                <img src="./images/{seeker[21]}" class="img-thumbnail" alt="Aadhar Front">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Aadhar Back:</strong></p>
                                <img src="./images/{seeker[22]}" class="img-thumbnail" alt="Aadhar Back">
                            </div>
                            <div class="col-md-4">
                                <p><strong>Vehicle Image:</strong></p>
                                <img src="./images/{seeker[23]}" class="img-thumbnail" alt="Vehicle Image">
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer" style="border-top:1px solid #444;">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    """)

print("""
                </tbody>
            </table>
        </div>
    </div>
""")
try:
    cur.execute("SELECT * FROM rides ORDER BY created_at DESC")
    data = cur.fetchall()
except pymysql.MySQLError as e:
    print(f"<h3 style='color:red;'>Error fetching data: {e}</h3>")
    data = []

print("""
    <div id="seekerPost" class="section hidden">
        <h2 style="background-color: #1a1a40; color: #ffffff; text-align: center; font-weight: bold; padding: 15px; border-radius: 10px;">
            <i class="fa-solid fa-car"></i> Sharer Post
        </h2>
        <p style="background-color: #2d2d86; text-align: center; font-size: 1.1rem; color: #ffffff; padding: 10px; border-radius: 5px;">
            Riders Posted Their Rides with Others.
        </p>
        <div class="container">
            <div class="row">
                <div style="background-color: #141432; padding: 20px; width: 100%;">
                    <div class="container mt-4">
                        <div style="background: #1f1f4d; padding: 20px; border-radius: 12px; box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3); color: #fff;">
                            <h4 class="mb-4" style="color: #ffffff; font-weight: bold;">Ride Details</h4>
                            <table class="table table-dark table-hover" style="border-radius: 12px; overflow: hidden;">
                                <thead style="background: linear-gradient(135deg, #4b0082, #1a1a40); color: #ffffff; text-align: center;">
                                    <tr>
                                        <th style="padding: 12px; text-align: center;">SNO</th>
                                        <th style="padding: 12px; text-align: center;">🆔 Ride ID</th>
                                        <th style="padding: 12px; text-align: center;">🚗 From</th>
                                        <th style="padding: 12px; text-align: center;">📍 To</th>
                                        <th style="padding: 12px; text-align: center;">👤 Rider Name</th>
                                        <th style="padding: 12px; text-align: center;">📅 Date & Time</th>
                                        <th style="padding: 12px; text-align: center;">💵 Price/Seat</th>
                                        <th style="padding: 12px; text-align: center;">👥 Available</th>
                                        <th style="padding: 12px; text-align: center;">👤 Booked</th>
                                        <th style="padding: 12px; text-align: center;">📊 Details</th>
                                    </tr>
                                </thead>
                                <tbody style="text-align: center; font-size: 1rem; font-weight: 500;">
""")

for index, i in enumerate(data, start=1):
    print(f"""
        <tr style="background-color: #2e2e4d;">
            <td style="padding: 15px; text-align: center;">{index}</td>
            <td style="padding: 15px; text-align: center;">{i[0]}</td>
            <td style="padding: 15px; text-align: center;">{i[6]}</td>
            <td style="padding: 15px; text-align: center;">{i[7]}</td>
            <td style="padding: 15px; text-align: center;">{i[2]}</td>
            <td style="padding: 15px; text-align: center;">{i[8]}</td>
            <td style="padding: 15px; text-align: center;">{i[11]}</td>
            <td style="color: #28a745; font-weight: bold; padding: 15px; text-align: center;">{int(i[10]) - int(i[14])}</td>
            <td style="color: #dc3545; font-weight: bold; padding: 15px; text-align: center;">{i[14]}</td>
            <td style="padding: 15px; text-align: center;"><button class='btn btn-outline-info btn-sm' data-toggle='modal' data-target='#rideDetails{i[0]}'>View</button></td>
        </tr>
    """)

print("""
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
""")

for i in data:
    print(f"""
        <div class="modal fade" id="rideDetails{i[0]}" tabindex="-1" role="dialog" aria-labelledby="rideModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
                <div class="modal-content" style="border-radius: 12px; background: #1B263B; color: #F1F1F1; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);">
                    <div class="modal-header" style="background: #0D1B2A; color: white; padding: 15px;">
                        <h5 class="modal-title">🚗 Ride Details</h5>
                        <button type="button" class="close" data-dismiss="modal" style="color: white; font-size: 20px; opacity: 0.8;">&times;</button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <div class="col-md-6">
                                <p><strong>📍 From:</strong> {i[6]}</p>
                                <p><strong>📍 To:</strong> {i[7]}</p>
                                <p><strong>📅 Ride Date & Time:</strong> {i[8]}</p>
                                <p><strong>⚠️ Status:</strong> <span style="background-color: #28a745; color: white; padding: 5px 10px; border-radius: 15px;"> {i[13]}</span></p>
                                <p><strong>🚘 Vehicle Type:</strong> {i[9]}</p>
                                <p><strong>👥 Available seat:</strong> {int(i[10]) - int(i[14])}</p>
                                <p><strong>💰 Price/Seat:</strong> <span style="color: #2ECC71; font-weight: bold;">{i[11]}</span></p>
                                <p><strong>📞 Driver Contact:</strong> {i[4]}</p>
                                <p><strong>🔢 Vehicle No:</strong> {i[16]}</p>
                                <p><strong>🧑‍ Driver Gender:</strong> {i[17]}</p>
                            </div>
                            <div class="col-md-6 text-center">
                                <p><strong>🧑‍ Rider Profile:</strong></p>
                                <img src="./images/{i[5]}" class="img-fluid rounded" style="max-height: 150px; border: 3px solid #E63946; border-radius: 12px;">
                                <p><strong>🚙 Vehicle Image:</strong></p>
                                <img src="./images/{i[15]}" class="img-fluid rounded" style="max-height: 150px; border: 3px solid #E63946; border-radius: 12px;">
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-outline-light" data-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    """)

print("""
            </div>
        </div>
    </div>
""")


try:
    cur.execute("SELECT id, name, email, subject, message, submitted_at FROM contacts")
    data = cur.fetchall()
except pymysql.MySQLError as e:
    print(f"<h3 style='color:red;'>Error fetching data: {e}</h3>")
    data = []

print(f"""
    <div id="queries" class="section hidden" style="background-color: #1e1e2f; color: #ffffff; padding: 20px; border-radius: 10px; text-align: center;">
        <h2 style="color: #ffcc00;">Queries</h2>
        <p style="color: #ffcc00;">This section contains query-related information.</p>
        <table style="width: 100%; border-collapse: collapse; background-color: #25253a; border-radius: 8px; overflow: hidden; margin-top: 10px;">
            <thead>
                <tr>
                    <th style="background-color: #ffcc00; color: #25253a; font-weight: bold; padding: 12px; border: 1px solid #444;">S.NO</th>
                    <th style="background-color: #ffcc00; color: #25253a; font-weight: bold; padding: 12px; border: 1px solid #444;">Name</th>
                    <th style="background-color: #ffcc00; color: #25253a; font-weight: bold; padding: 12px; border: 1px solid #444;">Email</th>
                    <th style="background-color: #ffcc00; color: #25253a; font-weight: bold; padding: 12px; border: 1px solid #444;">Subject</th>
                    <th style="background-color: #ffcc00; color: #25253a; font-weight: bold; padding: 12px; border: 1px solid #444;">Message</th>
                    <th style="background-color: #ffcc00; color: #25253a; font-weight: bold; padding: 12px; border: 1px solid #444;">Submitted At</th>
                </tr>
            </thead>
            <tbody>
""")

# Populate table rows with query data
# Populate table rows with query data
for row in data:
    print(f"""
        <tr style="border: 1px solid #444; text-align: center; background-color: {'#2e2e4a' if row[0] % 2 == 0 else '#25253a'};">
            <td style="padding: 12px; border: 1px solid #444;">{row[0]}</td>
            <td style="padding: 12px; border: 1px solid #444;">{row[1]}</td>
            <td style="padding: 12px; border: 1px solid #444;">
                <a href="mailto:{row[2]}" style="color: #4da6ff;">{row[2]}</a>
            </td>
            <td style="padding: 12px; border: 1px solid #444;">{row[3]}</td>
            <td style="padding: 12px; border: 1px solid #444;">{row[4]}</td>
            <td style="padding: 12px; border: 1px solid #444;">{row[5]}</td>
        </tr>
    """)


print("""
            </tbody>
        </table>
    </div>
""")


cur.execute("SELECT * FROM booking WHERE status IN ('booked', 'approved') ORDER BY booking_id DESC")
active_rides = cur.fetchall()

for sno, o in enumerate(active_rides, start=1):
    from collections import defaultdict

    print("""
    <div id="activeRides" class="section hidden" style="text-align: center; background: linear-gradient(to right, #0f2027, #203a43, #2c5364); color: white; padding: 20px; border-radius: 15px;">
        <h2 style="color: #f39c12;"><i class="fa-solid fa-car-side"></i> Active Rides</h2>
        <p style="font-size: 18px; font-weight: bold;">Manage all ongoing rides here.</p>
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="table-responsive">
                        <table class="table table-dark table-hover text-center" style="border-radius: 15px; overflow: hidden; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.5);">
                            <thead class="thead-dark" style="background: linear-gradient(to right, #0f2027, #203a43, #2c5364); color: white;">
                                <tr>
                                    <th style="padding: 15px; text-align: center;">SNO</th>
                                    <th style="padding: 15px; text-align: center;">🚘 Ride ID</th>
                                    <th style="padding: 15px; text-align: center;">🚗 From</th>
                                    <th style="padding: 15px; text-align: center;">📍 To</th>
                                    <th style="padding: 15px; text-align: center;">📅 Ride Date</th>
                                    <th style="padding: 15px; text-align: center;"><i class="fas fa-chair"></i> Booked Seats</th>
                                 
                                    <th style="padding: 15px; text-align: center;">🔍 Ride Details</th>
                                    <th style="padding: 15px; text-align: center;">👤 Customer Details</th>
                                </tr>
                            </thead>
                            <tbody>
    """)

    cur.execute("SELECT * FROM booking WHERE status IN ('booked', 'approved') ORDER BY booking_id DESC")
    active_rides = cur.fetchall()

    # Group by ride ID
    from collections import defaultdict

    grouped_rides = defaultdict(list)
    for row in active_rides:
        ride_id = row[1]  # ride_id assumed at index 1
        grouped_rides[ride_id].append(row)

    for sno, (ride_id, bookings) in enumerate(grouped_rides.items(), start=1):
        first = bookings[0]

        print(f"""
            <tr onmouseover="this.style.background='rgba(255, 255, 255, 0.05)';" 
                onmouseout="this.style.background='transparent';">
                <td style="padding: 15px; text-align: center;">{sno}</td>
                <td style="padding: 15px; text-align: center;">{ride_id}</td>
                <td style="padding: 15px;  text-align: center;">{first[3]}</td>
                <td style="padding: 15px; text-align: center;">{first[4]}</td>
                <td style="padding: 15px; text-align: center;">{first[7]}</td>
                <td style="padding: 15px; text-align: center;">{sum(int(b[9]) for b in bookings)}</td>
             
                <td style="padding: 15px; text-align: center;"><button class="btn btn-outline-info btn-sm" data-toggle="modal" data-target="#sharerModal{ride_id}">View</button></td>
                <td style="padding: 15px; text-align: center;"><button class="btn btn-outline-warning btn-sm" data-toggle="modal" data-target="#customerModal{ride_id}">View</button></td>
            </tr>
        """)

        print(f"""<div class="modal fade" id="customerModal{ride_id}" tabindex="-1" role="dialog">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content" style="background: linear-gradient(to right, #1e1e2f, #2c3e50); color: #ffffff; font-family: 'Segoe UI', sans-serif; border-radius: 16px; border: 1px solid #7f8c8d; box-shadow: 0 0 12px rgba(0,0,0,0.6);">
                    <div class="modal-header" style="background: linear-gradient(to right, #2c3e50, #34495e); color: #f39c12; border-bottom: 2px solid #f39c12;">
                        <h5 class="modal-title"><i class="fas fa-users"></i> Passengers on Ride ID <span style="color: #ecf0f1;">{ride_id}</span></h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close" style="color: #ffffff;">&times;</button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
        """)

        for b in bookings:
            print(f"""
                <div class="col-md-6 mb-4">
                    <div class="card text-center" style="background: #2a2a40; border-radius: 15px; padding: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); border-top: 4px solid #9b59b6;">
                        <img src="./images/{b[26]}" class="img-fluid rounded-circle mx-auto mb-3" alt="Customer Image" 
                            style="width: 100px; height: 100px; object-fit: cover; border: 3px solid #9b59b6; box-shadow: 0 2px 8px rgba(0,0,0,0.6);">
                        <h6 style="color: #ffffff;"><i class="fas fa-user"></i> {b[13]}</h6>
                        <p style="margin-bottom: 6px;color: #ffffff;"><i class="fas fa-phone"></i> {b[6]}</p>
                        <p style="margin-bottom: 6px; color: #ffffff;"><i class="fas fa-envelope"></i> {b[5]}</p>
                        <p style="margin-bottom: 6px; color: #ffffff;"><i class="fas fa-chair"></i> Seats: {b[9]}</p>
                        <p style="margin-bottom: 6px; color: #ffffff;"><i class="fas fa-rupee-sign"></i> ₹{int(b[9]) * float(b[10]):.2f}</p>
                        <p style="margin-bottom: 6px; color: #ffffff;"><i class="fas fa-credit-card"></i> {b[19]}</p>
                    </div>
                </div>
            """)

        print("""
                        </div>
                    </div>
                    <div class="modal-footer" style="background: #1e1e2f;">
                        <button class="btn btn-outline-warning" data-dismiss="modal"><i class="fas fa-times"></i> Close</button>
                    </div>
                </div>
            </div>
        </div>
        """)

        # Sharer modal (showing just the first sharer for the ride)
        print(f""" 
            <div class="modal fade" id="sharerModal{ride_id}" tabindex="-1" role="dialog">
                <div class="modal-dialog" role="document">
                    <div class="modal-content" style="background: #1e3c72; color: white; border-radius: 15px;">
                        <div class="modal-header" style="background: #16213E; color: #F8B400;">
                            <h5 class="modal-title"><i class="fas fa-user-circle"></i> Sharer Details</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close" style="color: white;">&times;</button>
                        </div>
                        <div class="modal-body d-flex align-items-start">
                            <div class="info" style="flex: 1; padding-right: 20px;">
                                <p><strong><i class="fas fa-user"></i> Name:</strong> {first[21]}</p>
                                <p><strong><i class="fas fa-venus-mars"></i> Gender:</strong> {first[20]}</p>
                                <p><strong><i class="fas fa-phone"></i> Phone:</strong> {first[6]}</p>
                                <p><strong><i class="fas fa-envelope"></i> Email:</strong> {first[5]}</p>
                                <p><strong><i class="fas fa-car"></i> Vehicle Type:</strong> {first[23]}</p>
                                <p><strong><i class="fas fa-hashtag"></i> Vehicle No:</strong> {first[22]}</p>
                            </div>
                            <div class="images text-center" style="flex: 1;">
                                <p><strong><i class="fas fa-car-side"></i> Vehicle Image:</strong></p>
                                <img src="./images/{first[24]}" class="img-fluid rounded" alt="Vehicle Image" 
                                    style="max-height: 180px; object-fit: cover; border: 3px solid #F8B400; border-radius: 12px;">
                                <p class="mt-3"><strong><i class="fas fa-user"></i> Rider Image:</strong></p>
                                <img src="./images/{first[25]}" class="img-fluid rounded" alt="Rider Image" 
                                    style="max-height: 180px; object-fit: cover; border: 3px solid #F8B400; border-radius: 12px;">
                            </div>
                        </div>
                        <div class="modal-footer" style="background: #16213E;">
                            <button class="btn btn-warning" data-dismiss="modal"><i class="fas fa-times"></i> Close</button>
                        </div>
                    </div>
                </div>
            </div>
        """)

    print("""
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """)



print("""
<div id="cancelledByUser" class="section hidden" style="text-align: center; padding: 40px; background: linear-gradient(135deg, #1f1c2c, #928dab); border-radius: 20px; color: white;">
    <h2 style="font-size: 2.2rem; font-weight: bold; color: #fecd1a; text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.4); margin-bottom: 10px;">
        <i class="fas fa-ban"></i> Canceled & Rejected Rides
    </h2>
    <p style="font-size: 1.2rem; color: #f1f1f1;">
        Filter all rides below:
    </p>

    <!-- Filter Dropdown -->
    <div style="margin: 20px 0;">
        <select id="adminRideFilter" onchange="filterAdminRides()" style="padding: 10px 20px; border-radius: 10px; border: none; font-size: 1rem; color: #333;">
            <option value="all">🚘 Show All Rides</option>
            <option value="canceled">🚫 Canceled Rides Only</option>
            <option value="rejected">❌ Rejected Rides Only</option>
        </select>
    </div>

    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-12 col-sm-12 mb-4">
                <div style="overflow-x: auto; border-radius: 20px;">
                    <table class="table" style="min-width: 1000px; border-collapse: separate; border-spacing: 0 10px;">
                        <thead>
                            <tr style="background: linear-gradient(to right, #1e3c72, #2a5298); color: white; font-size: 1.1rem; text-align: center;">
                                <th style="padding: 15px; border-top-left-radius: 12px; border-bottom-left-radius: 12px;">S.No</th>
                                <th>Ride ID</th>
                                <th>From</th>
                                <th>To</th>
                                <th>Ride Date</th>
                                <th>Passengers</th>
                                <th>Canceled By</th>
                                <th>Rejected By</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody id="adminRideTable">
""")

cur.execute("SELECT * FROM booking WHERE status IN ('rejected', 'Canceled')")
all_cancel = cur.fetchall()

if not all_cancel:
    print("<tr><td colspan='8' style='text-align:center; padding: 20px; font-weight: bold; color: #ff6b6b;'>No canceled or rejected rides available.</td></tr>")
else:
    for idx, ride in enumerate(all_cancel, start=1):
        ride_id = ride[0]
        status = ride[17].strip().lower()

        canceled_by = ride[13] if status == "canceled" else "-"
        rejected_by = ride[21] if status == "rejected" else "-"

        if status == "canceled":
            status_label = "🚫 Canceled by customer"
            row_color = "#e3f2fd"
            text_color = "#3498db"
            row_class = "canceled"
        elif status == "rejected":
            status_label = "❌ Rejected by sharer"
            row_color = "#f3e5f5"
            text_color = "#8e44ad"
            row_class = "rejected"
        else:
            status_label = "❓ Unknown"
            row_color = "#f0f0f0"
            text_color = "#7f8c8d"
            row_class = "unknown"

        print(f"""
            <tr class="adminRideRow {row_class}" style="background-color: {row_color}; font-size: 1rem; font-weight: 500; transition: 0.3s; text-align: center; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);"
                onmouseover="this.style.transform='scale(1.01)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.2)'"
                onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)'">
                <td style="padding: 15px; vertical-align: middle; color: #2c3e50;">{idx}</td>
                <td style="vertical-align: middle;">
                    <span style="color: {text_color}; background: rgba(0,0,0,0.05); padding: 6px 12px; border-radius: 8px; display: inline-block; font-weight: bold;">
                        #{ride_id}
                    </span>
                </td>
                <td style="color: #2c3e50; vertical-align: middle;">{ride[3]}</td>
                <td style="color: #2c3e50; vertical-align: middle;">{ride[4]}</td>
                <td style="color: #2c3e50; vertical-align: middle;">{ride[7]}</td>
                <td style="color: #2c3e50; vertical-align: middle;">{ride[9]}</td>
                 <td style="color: #2c3e50; vertical-align: middle;">{canceled_by}</td>
                <td style="color: #2c3e50; vertical-align: middle;">{rejected_by}</td>
                <td style="font-weight: bold; color: {text_color}; vertical-align: middle;">{status_label}</td>
            </tr>
        """)

print("""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Filter Script -->
<script>
    function filterAdminRides() {
        const filter = document.getElementById("adminRideFilter").value;
        const rows = document.querySelectorAll(".adminRideRow");

        rows.forEach(row => {
            row.style.display = "table-row";
            if (filter === "canceled" && !row.classList.contains("canceled")) {
                row.style.display = "none";
            } else if (filter === "rejected" && !row.classList.contains("rejected")) {
                row.style.display = "none";
            }
        });
    }
</script>
""")


print("""
<div id="completedRides" class="section hidden" style="background-color: #2c3e50; padding: 20px; border-radius: 10px;">
    <h2 style="text-align: center; color: #f39c12;"><i class="fa-solid fa-check-circle"></i> Completed Rides</h2>
    <p style="text-align: center; color: #ecf0f1;">View all completed rides and user details.</p>

    <div class="container mt-4">
        <div class="table-responsive">
            <table class="table table-bordered table-hover text-center" style="background-color: #ffffff; color: #2c3e50; border-radius: 10px; overflow: hidden;">
                <thead style="background-color: #1abc9c; color: white;">
                    <tr>
                        <th style="padding: 15px; text-align: center;">SNO</th>
                        <th style="padding: 15px; text-align: center;">Ride ID</th>
                        <th style="padding: 15px; text-align: center;">From</th>
                        <th style="padding: 15px; text-align: center;">To</th>
                        <th style="padding: 15px; text-align: center;">Date & Time</th>
                        <th style="padding: 15px; text-align: center;">Details</th>
                        <th style="padding: 15px; text-align: center;">Status</th>
                    </tr>
                </thead>
                <tbody>
""")

query = "SELECT * FROM booking WHERE status = 'completed'"
cur.execute(query)
completed_rides = cur.fetchall()

ride_groups = {}
for ride in completed_rides:
    ride_id = ride[1]
    if ride_id not in ride_groups:
        ride_groups[ride_id] = []
    ride_groups[ride_id].append(ride)

if not completed_rides:
    print("<tr><td colspan='7'>No completed rides available.</td></tr>")

sno = 1
for ride_id, bookings in ride_groups.items():
    first_ride = bookings[0]
    print(f"""
        <tr style="background-color: #f39c12; color: white;" 
            onmouseover="this.style.backgroundColor='#e67e22';" 
            onmouseout="this.style.backgroundColor='#f39c12';">
            <td style="padding: 15px; text-align: center;">{sno}</td>
            <td style="padding: 15px; text-align: center;">{first_ride[1]}</td>
            <td style="padding: 15px; text-align: center;">{first_ride[3]}</td>
            <td style="padding: 15px; text-align: center;">{first_ride[4]}</td>
            <td style="padding: 15px; text-align: center;">{first_ride[7]}</td>
            <td style="padding: 15px; text-align: center;"><button class="btn btn-success" data-toggle="modal" data-target="#rideModal{ride_id}">View Details</button></td>
            <td style="padding: 15px; text-align: center;"><strong style="color: #2ecc71;">Completed</strong></td>
        </tr>
    """)
    sno += 1

print("""
                </tbody>
            </table>
        </div>
    </div>
</div>
""")

# Modal Section (aligned + styled)
for ride_id, bookings in ride_groups.items():
    rider = bookings[0]
    print(f"""
    <div class="modal fade" id="rideModal{ride_id}" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-xl" role="document">
            <div class="modal-content" style="background: #1e1e2f; color: white; border-radius: 15px; border: 2px solid #f39c12;">
                <div class="modal-header" style="background: #111; border-bottom: 2px solid #f39c12;">
                    <h5 class="modal-title"><i class="fas fa-car-side"></i> Ride ID: {ride_id}</h5>
                    <button type="button" class="close" data-dismiss="modal" style="color: white;">&times;</button>
                </div>

                <div class="modal-body">
                    <div class="mb-4">
                        <h5 style="color: #f39c12;"><i class="fas fa-user-tie"></i> Sharer (Rider) Details</h5>
                        <div class="row">
                            <div class="col-md-6">
                                <p><strong>Name:</strong> {rider[21]}</p>
                                <p><strong>Gender:</strong> {rider[20]}</p>
                                <p><strong>Phone:</strong> {rider[6]}</p>
                                <p><strong>Email:</strong> {rider[5]}</p>
                                <p><strong>Vehicle:</strong> {rider[23]}</p>
                                <p><strong>Vehicle No:</strong> {rider[22]}</p>
                            </div>
                            <div class="col-md-6 text-center">
                                <img src="./images/{rider[25]}" class="img-fluid rounded mb-2" alt="Rider Image"
                                     style="height: 120px; border: 3px solid #f39c12;">
                                <p><strong>Vehicle Image:</strong></p>
                                <img src="./images/{rider[24]}" class="img-fluid rounded" alt="Vehicle Image"
                                     style="height: 120px; border: 3px solid #f39c12;">
                            </div>
                        </div>
                    </div>

                    <hr style="border-top: 1px solid #7f8c8d;">

                    <h5 style="color: #f39c12;"><i class="fas fa-users"></i> Customers Who Booked This Ride</h5>
                    <div class="row">
    """)

    for b in bookings:
        total_price = int(b[9]) * float(b[10])
        print(f"""
        <div class="col-md-4 mb-4">
            <div class="card" style="background: #2c3e50; border-radius: 15px; padding: 15px; color: white;">
                <div class="text-center mb-3">
                    <img src="./images/{b[26]}" class="rounded-circle" alt="Customer Image"
                         style="width: 80px; height: 80px; object-fit: cover; border: 3px solid #3498db;">
                    <h6 class="mt-2">{b[13]}</h6>
                </div>
                <p><i class="fas fa-phone"></i> {b[6]}</p>
                <p><i class="fas fa-envelope"></i> {b[5]}</p>
                <p><i class="fas fa-chair"></i> Seats: {b[9]}</p>
                <p><i class="fas fa-rupee-sign"></i> ₹{total_price:.2f}</p>
                <p><i class="fas fa-credit-card"></i> {b[19]} via {b[18]}</p>
            </div>
        </div>
        """)

    print("""
                    </div>
                </div>
                <div class="modal-footer" style="background: #111;">
                    <button type="button" class="btn btn-outline-warning" data-dismiss="modal"><i class="fas fa-times"></i> Close</button>
                </div>
            </div>
        </div>
    </div>
    """)





print("""
<script>
    function showSection(sectionId) {
        document.querySelectorAll('.section').forEach(section => {
            section.classList.add('hidden'); 
        });
        document.getElementById(sectionId).classList.remove('hidden'); 
    }
    
    function toggleSidebar() {
        let sidebar = document.querySelector('.sidebar');
        let backdrop = document.querySelector('.sidebar-backdrop');
         let content = document.querySelector('.content');

        if (sidebar.classList.contains('show')) {
        sidebar.classList.remove('show');
        backdrop.style.display = 'none';
        content.classList.remove('shift'); 
         } else {
        sidebar.classList.add('show');
        backdrop.style.display = 'block';
        content.classList.add('shift'); 
        }
    }   

    </script>
        <!-- jQuery and Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

cid = form.getvalue("cid")
user_id = form.getvalue("userid")
password = form.getvalue("password")
submit = form.getvalue("update")
reject = form.getvalue("reject")

if submit:
    q = "UPDATE seekda SET userid=%s, password=%s, status='approved' WHERE SNo=%s"
    cur.execute(q, (user_id, password, cid))
    con.commit()

    cur.execute("SELECT Email, FirstName FROM seekda WHERE SNo=%s", (cid,))
    seeker_data = cur.fetchone()

    if seeker_data:
        email, name = seeker_data

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
            print("<script>alert('User approved & email sent successfully'); window.location.href='Admindashboard.py';</script>")
        except Exception as e:
            print(f"<script>alert('Error sending email: {str(e)}');</script>")

if reject:
    cur.execute("SELECT Email, FirstName FROM seekda WHERE SNo=%s", (cid,))
    seeker_data = cur.fetchone()

    if seeker_data:
        email, name = seeker_data

        cur.execute("UPDATE seekda SET status='rejected' WHERE SNo=%s", (cid,))
        con.commit()

        subject = "From Ride Sharing"
        body = f"Hello {name},\n\nUnfortunately, you did not meet our criteria. Please submit original licenses."

        msg = f"Subject: {subject}\n\n{body}"

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("officialvimal01@gmail.com", "gokk ckjn jvin yvuq")
            server.sendmail("officialvimal01@gmail.com", email, msg)
            server.quit()
            print("<script>alert('Seeker rejected & email sent successfully'); window.location.href='Admindashboard.py';</script>")
        except Exception as e:
            print(f"<script>alert('Error sending email: {str(e)}');</script> """)