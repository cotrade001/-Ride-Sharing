#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, smtplib, random, string, os, sys, json, razorpay

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()

form = cgi.FieldStorage()
cid = form.getvalue("cust_id")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">


    <style>
        body {
            height: 100vh;
            background-color: #f8f9fa;
            font-family: Arial, sans-serif;
            overflow-x: hidden;
        }

        .sidebar {
            width: 260px;
            background-color: #ffbfbf;
            color: white;
            height: 100vh;
            position: fixed;
            top: 0;
            left: 0;
            padding-top: 20px;
            transition: all 0.3s ease;
        }

        .sidebar a {
            display: flex;
            align-items: center;
            padding: 15px;
            color: white;
            text-decoration: none;
            font-size: 16px;
        }

        .sidebar a i {
            margin-right: 10px;
        }

        .sidebar a:hover {
            background-color: #ffffff;
            color: rgb(232, 11, 11);
        }

        .dropdown-menu {
            background-color: black;
        }

        .content {
            margin-left: 260px;
            padding: 20px;
            width: calc(100% - 260px);
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(219, 47, 47, 0.1);
            transition: margin-left 0.3s ease;
        }

        .hidden {
            display: none;
        }

        .top-navbar {
            display: none;
            background-color: #95eccbb8;
            color: white;
            padding: 10px 15px;
            align-items: center;
            justify-content: space-between;
        }

        .top-navbar .menu-btn {
            font-size: 22px;
            cursor: pointer;
        }

        @media (max-width: 768px) {
            .sidebar {
                left: -260px;
                position: fixed;
                z-index: 1000;
            }

            .sidebar.show {
                left: 0;
            }

            .content {
                margin-left: 0;
                width: 100%;
            }

            .top-navbar {
                display: flex;
            }

            .sidebar-backdrop {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.5);
                z-index: 999;
            }

            .sidebar.show+.sidebar-backdrop {
                display: block;
            }
        }

        .profile-card {
            max-width: 600px;
            margin: 50px auto;
            background: linear-gradient(135deg, #1e1e1e, #292929);
            border-radius: 15px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
            padding: 20px;
            text-align: center;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }

        .profile-card:hover {
            transform: scale(1.02);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
        }

        .profile-header {
            background: linear-gradient(135deg, #ff416c, #ff4b2b);
            padding: 15px;
            border-radius: 10px 10px 0 0;
            font-size: 20px;
            font-weight: bold;
            color: #fff;
        }

        .profile-img {
            margin-top: 40px;
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 4px solid #ff416c;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }

        .profile-img:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 12px rgba(255, 65, 108, 0.6);
            cursor: pointer;
        }

        .file-input {
            display: none;
        }

        .edit-btn {
            background-color: #ff416c;
            color: white;
            border-radius: 5px;
            padding: 5px 10px;
            transition: all 0.3s ease;
            border: none;
        }

        .edit-btn:hover {
            background-color: #ff4b2b;
            transform: scale(1.1);
        }

        .upload-btn {
            background-color: #ff416c;
            border: none;
            padding: 10px 15px;
            font-size: 14px;
            border-radius: 5px;
            transition: all 0.3s ease;
            margin-top: 10px;
        }

        .upload-btn:hover {
            background-color: #ff4b2b;
            transform: scale(1.1);
        }

        .modal-custom {
            background: linear-gradient(135deg, #1a1a1a, #292929);
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(255, 65, 108, 0.6);
        }

        .modal-header-custom {
            background: linear-gradient(135deg, #ff416c, #ff4b2b);
            color: white;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        }

        .btn-close-white {
            filter: invert(1);
        }

        .modal-body {
            padding: 20px;
            background: #252525;
            color: white;
        }

        .input-custom {
            background-color: #333;
            border: 2px solid #ff416c;
            padding: 10px;
            border-radius: 8px;
            width: 100%;
            color: white;
            transition: all 0.3s ease;
        }

        .input-custom:focus {
            border: 2px solid #ff4b2b;
            outline: none;
            box-shadow: 0 0 10px rgba(255, 65, 108, 0.5);
        }

        .modal-footer-custom {
            background: #1c1c1c;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
            padding: 15px;
            display: flex;
            justify-content: space-between;
        }

        .cancel-btn {
            background-color: #444;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .cancel-btn:hover {
            background-color: #666;
            transform: scale(1.05);
        }

        .save-btn {
            background: linear-gradient(135deg, #ff416c, #ff4b2b);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            transition: all 0.3s ease;
            box-shadow: 0 0 10px rgba(255, 65, 108, 0.5);
        }

        .save-btn:hover {
            background: linear-gradient(135deg, #ff4b2b, #ff416c);
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(255, 65, 108, 0.8);
        }
        .modal-content {
            background-color: #1a1a40;
            color: white;
            border-radius: 10px;
        }
        .modal-header {
            border-bottom: 1px solid #444;
        }
        .modal-footer {
            border-top: 1px solid #444;
        }
        .btn-update {
            background-color: #4c00ff;
            border: none;
        }
        .btn-update:hover {
            background-color: #3500d3;
        }
          /* Booking table  */
        body,
        html {
            height: 100%;
            margin: 0;
        }

        .booking-container {
            height: calc(100vh - 80px);
            height: 50vh;
            display: flex;
            align-items: stretch;
            justify-content: center;
            margin-top: -40px;
        }

        .booking-form-container {
            background-color: white;
            padding: 40px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            background-image: url(book\ back.png);
            max-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            height: 100%;

        }

        .image-container {
            height: 100vh;
            display: flex;
        }

        .image-box {
            background-size: cover;
            background-position: center;
            width: 100%;
            height: 100%;
        }
         /* Booking table  */
        body,
        html {
            height: 100%;
            margin: 0;
        }

        .booking-container {
            height: calc(100vh - 80px);
            height: 50vh;
            display: flex;
            align-items: stretch;
            justify-content: center;
            margin-top: 50px;
        }

        .booking-form-container {
            background-color: white;
            padding: 40px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            background-image: url(book\ back.png);
            max-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            height: 100%;

        }

        .image-container {
            height: 100vh;
            display: flex;
        }

        .image-box {
            background-size: cover;
            background-position: center;
            width: 100%;
            height: 100%;
        }
        .booking-form-container .form-control, 
        .booking-form-container .form-select {
            height: 50px;
            font-size: 16px;
        }

        .booking-form-container .btn-primary {
            height: 50px;
            font-size: 18px;
        }


    </style>
</head>

<body>

    <div class="top-navbar d-flex">
        <span class="menu-btn" onclick="toggleSidebar()"><i class="fas fa-bars"></i></span>
        <h6 class="m-0">User Dashboard</h6>
    </div>


    <div class="sidebar">
        <div style="margin-left: 10px; display:flex; align-items:center; ">
            <img src="./img/ride-sharing- logope.webp" 
                style="height: 50px; width:50px; border-radius:100px; background-color:rgb(142, 242, 244)" alt="">
            <h6 class="mt-3" style="margin-left:10px;">YOUR RIDE</h6>
        </div>
        <h4 class="text-center mt-3"><i class="fas fa-user-shield" style="margin-right:10px;"></i>User Dashboard</h4>

        <a href="#" onclick="showSection('profile')">
            <i class="fas fa-user-circle"></i> Profile
        </a>
      
         """)
cur.execute("SELECT COUNT(*) FROM rides WHERE  status = 'pending'")
carts_count = cur.fetchone()[0]
print(f"""
        <a href="#" onclick="showSection('availableRides')"><i class="fas fa-car"></i> Available Rides 
         <span style="background: red; color: white; font-size: 12px; padding: 2px 8px; border-radius: 12px; margin-left: 5px;">
                {carts_count}
            </span>
        </a>
        """)
print("""
             <div class="dropdown">
                <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown"><i class="fas fa-calendar-alt"></i>  My Rides</a>
                <ul class="dropdown-menu">
                 <a href="#" onclick="showSection('requestedRides')"><i class="fas fa-car-side"></i> Requested Rides</a>
               <a href="#" onclick="showSection('scheduleRides')"><i class="fas fa-calendar-alt"></i> My rides</a>

                       <a href="#" onclick="showSection('userCompletedRides')"><i class="fas fa-check-circle"></i> Completed Rides</a>
                       <a href="#" onclick="showSection('cancelledRides')"><i class="fas fa-times-circle"></i> Cancelled Rides</a>
                  </ul>
              </div>
            
             """)

print("""
 
        <a href="home.py"><i class="fa-solid fa-door-open"></i> Logout</a>

    </div>
    </div>
    <div class="sidebar-backdrop" onclick="toggleSidebar()"></div>

         <div class="content">
        <div id="overview" class="section hidden">
            <h2><i class="fa-solid fa-chart-pie"></i> Overview</h2>

        </div>



        """)

print("""
<div id="cancelledRides" class="section hidden" style="text-align: center; padding: 40px; background: linear-gradient(135deg, #1f1c2c, #928dab); border-radius: 20px; color: white;">
    <h2 style="font-size: 2.2rem; font-weight: bold; color: #fecd1a; text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.4); margin-bottom: 10px;">
        <i class="fas fa-ban"></i> Canceled & Rejected Rides
    </h2>
    <p style="font-size: 1.2rem; color: #f1f1f1;">
        Filter your rides below:
    </p>

    <!-- Filter Dropdown -->
    <div style="margin: 20px 0;">
        <select id="userRideFilter" onchange="filterUserRides()" style="padding: 10px 20px; border-radius: 10px; border: none; font-size: 1rem; color: #333;">
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
                                <th style="padding-right: 15px; border-top-right-radius: 12px; border-bottom-right-radius: 12px;">Status</th>
                            </tr>
                        </thead>
                        <tbody id="userRideTable">
""")

cur.execute("SELECT * FROM booking WHERE custid = %s AND LOWER(status) IN ('canceled', 'rejected')", (cid,))
rides = cur.fetchall()

if not rides:
    print("<tr><td colspan='8' style='text-align:center; padding: 20px; font-weight: bold; color: #ff6b6b;'>No canceled or rejected rides available.</td></tr>")
else:
    for idx, a in enumerate(rides, start=1):
        ride_id = a[0]
        status = a[17].strip().lower()
        canceled_by = a[13] if status == "canceled" else "-"
        rejected_by = a[21] if status == "rejected" else "-"

        if status == "canceled":
            status_label = "🚫 Canceled by Me"
            row_color = "#ffe6e6"
            text_color = "#c0392b"
            row_class = "canceled"
        elif status == "rejected":
            status_label = "❌ Rejected by Sharer"
            row_color = "#fff4e1"
            text_color = "#e67e22"
            row_class = "rejected"
        else:
            status_label = "❓ Unknown"
            row_color = "#f0f0f0"
            text_color = "#7f8c8d"
            row_class = "unknown"

        print(f"""
            <tr class="userRideRow {row_class}" style="background-color: {row_color}; font-size: 1rem; font-weight: 500; transition: 0.3s; text-align: center; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);"
                onmouseover="this.style.transform='scale(1.01)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.2)'"
                onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)'">
                <td style="padding: 15px; vertical-align: middle; color: #2c3e50;">{idx}</td>
                <td>
                    <span style="color: {text_color}; background: rgba(0,0,0,0.05); padding: 6px 12px; border-radius: 8px; display: inline-block; font-weight: bold;">
                        #{ride_id}
                    </span>
                </td>
                <td style="color: #2c3e50;">{a[3]}</td>
                <td style="color: #2c3e50;">{a[4]}</td>
                <td style="color: #2c3e50;">{a[7]}</td>
                <td style="color: #2c3e50;">{a[9]}</td>
                 <td style="color: #2c3e50; vertical-align: middle;">{canceled_by}</td>
                <td style="color: #2c3e50; vertical-align: middle;">{rejected_by}</td>
                <td style="font-weight: bold; color: {text_color};">{status_label}</td>
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
    function filterUserRides() {
        const filter = document.getElementById("userRideFilter").value;
        const rows = document.querySelectorAll(".userRideRow");

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

<div id="scheduleRides" class="section hidden" style="background: #f4f4f4;">
   <div style="text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <h2 style="font-size: 30px; margin-bottom: 15px; background: rgba(0, 0, 0, 0.3); padding: 20px; border-radius: 20px; box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3); color: #ffdd57; display: inline-block;">
            <i class="fas fa-calendar-alt" style="margin-right: 10px; color: #ffdd57;"></i> My Rides
        </h2>
        <p style="font-size: 20px; color: white; background: rgba(0, 0, 0, 0.3); padding: 15px; border-radius: 15px; display: inline-block; box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);">
            See your approved rides here. For further confirmation, you will receive an email from the rider.
        </p>
   </div>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="table-responsive">
                
                    <table class="table table-dark table-hover text-center" style="border-radius: 15px; overflow: hidden; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);">
                        <thead class="thead-dark" style="background: linear-gradient(to right, #1e3c72, #2a5298); color: white;">
                            <tr>
                                <th>🚖 Booking ID</th>
                                <th>🆔 Ride ID</th>
                                <th>🚗 From</th>
                                <th>📍 To</th>
                                <th>📅 Ride Date</th>
                                <th>✅ Action</th>
                                <th>🔍 Ride Details</th>
                                <th>👥 Co-Travelers</th>
                            </tr>
                        </thead>
                        <tbody>
""")

cur.execute("SELECT * FROM booking WHERE custid = %s AND status IN ('approved', 'booked')", (cid,))
approve_ride = cur.fetchall()

for o in approve_ride:
    print(f""" 
        <tr style="transition: background 0.3s; cursor: pointer;" onmouseover="this.style.background='rgba(255, 255, 255, 0.1)';" onmouseout="this.style.background='transparent';">
            <td>{o[0]}</td>
            <td>{o[1]}</td>
            <td>{o[3]}</td>
            <td>{o[4]}</td>
            <td>{o[7]}</td>
            <td>
                <form action="" method="POST">
                    <input type="hidden" name="rideids" value="{o[1]}">
                    <input type="hidden" name="booking_id" value="{o[0]}">
                    <input type="submit" class="btn btn-success btn-sm" name="completeRide" value="Mark as Completed" style="border-radius: 10px;">
                </form>
            </td>
            <td>
                <button class="btn btn-info btn-sm" data-toggle="modal" data-target="#sharerModal{o[0]}" style="border-radius: 10px;">View More</button>
            </td>
            <td>
                <button class="btn btn-warning btn-sm" data-toggle="modal" data-target="#coTravelersModal{o[1]}" style="border-radius: 10px;">View</button>
            </td>
        </tr>
    """)

    # Ride Details Modal
    print(f""" 
    <div class="modal fade" id="sharerModal{o[0]}" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
            <div class="modal-content" style="background: #1e3c72; color: white; border-radius: 15px;">
                <div class="modal-header" style="background: #16213E; color: #F8B400;">
                    <h5 class="modal-title"><i class="fas fa-user-circle"></i> Ride Details</h5>
                    <button type="button" class="close" data-dismiss="modal" style="color: white;"><span>&times;</span></button>
                </div>
                <div class="modal-body d-flex align-items-start">
                    <div class="info" style="flex: 1; padding-right: 20px;">
                        <p><strong><i class="fas fa-user"></i> Name:</strong> {o[21]}</p>
                        <p><strong><i class="fas fa-venus-mars"></i> Gender:</strong> {o[20]}</p>
                        <p><strong><i class="fas fa-phone"></i> Phone:</strong> {o[6]}</p>
                        <p><strong><i class="fas fa-envelope"></i> Email:</strong> {o[5]}</p>
                        <p><strong><i class="fas fa-chair"></i> Booked Seat:</strong> {o[9]}</p>
                        <p><strong><i class="fas fa-indian-rupee-sign"></i> Total Price:</strong> ₹{int(o[9]) * float(o[10]):.2f}</p>
                        <p><strong><i class="fas fa-credit-card"></i> Payment Status:</strong> {o[19]}</p>
                        <p><strong><i class="fas fa-money-bill-wave"></i> Payment Method:</strong> {o[18]}</p>
                        <p><strong><i class="fas fa-hashtag"></i> Vehicle No:</strong> {o[22]}</p>
                    </div>
                    <div class="images text-center" style="flex: 1;">
                        <p><strong><i class="fas fa-car-side"></i> Vehicle Image:</strong></p>
                        <img src="./images/{o[24]}" class="img-fluid rounded" style="max-height: 180px; border: 3px solid #F8B400;">
                        <p class="mt-3"><strong><i class="fas fa-user"></i> Rider Image:</strong></p>
                        <img src="./images/{o[25]}" class="img-fluid rounded" style="max-height: 180px; border: 3px solid #F8B400;">
                    </div>
                </div>
                <div class="modal-footer" style="background: #16213E;">
                    <button type="button" class="btn btn-warning" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
    """)

    # Co-Travelers Modal
    cur.execute(
        "SELECT custname, custphone, email, custprofile FROM booking WHERE ride_id = %s AND custid != %s AND status IN ('approved', 'booked')",
        (o[1], cid))
    co_travelers = cur.fetchall()

    print(f"""
    <div class="modal fade" id="coTravelersModal{o[1]}" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-lg modal-dialog-scrollable" role="document">
            <div class="modal-content" style="background: linear-gradient(135deg, #1f4068, #1b1b2f); color: #f1f1f1; border-radius: 20px;">
                <div class="modal-header" style="background: linear-gradient(to right, #0f2027, #203a43, #2c5364); border-top-left-radius: 20px; border-top-right-radius: 20px;">
                    <h5 class="modal-title" style="color: #ffdd57;">
                        <i class="fas fa-users" style="margin-right: 10px;"></i> Co-Travelers for Ride ID: {o[1]}
                    </h5>
                    <button type="button" class="close" data-dismiss="modal" style="color: #ffffff;"><span>&times;</span></button>
                </div>
                <div class="modal-body" style="padding: 20px;">
    """)

    if co_travelers:
        print('<div class="row">')
        for traveler in co_travelers:
            name, phone, email, profile = traveler
            print(f"""
                <div class="col-md-6 mb-4">
                    <div class="card h-100" style="background-color: rgba(255, 255, 255, 0.05); border: none; border-radius: 15px; box-shadow: 0 0 10px rgba(255, 221, 87, 0.2); transition: transform 0.3s;">
                        <div class="card-body d-flex align-items-center">
                            <img src="./images/{profile}" class="rounded-circle mr-3" style="width: 70px; height: 70px; object-fit: cover; border: 3px solid #ffdd57; box-shadow: 0 0 10px rgba(255, 221, 87, 0.5);">
                            <div>
                                <h6 style="margin: 0; color: #ffdd57;">{name}</h6>
                                <p style="margin: 2px 0; font-size: 14px; color: #f1f1f1;"><i class="fas fa-envelope"></i> {email}</p>
                                <p style="margin: 2px 0; font-size: 14px; color: #f1f1f1;"><i class="fas fa-phone-alt"></i> {phone}</p>
                            </div>
                        </div>
                    </div>
                </div>
            """)
        print('</div>')
    else:
        print("""
            <div class="text-center">
                <p style="font-size: 16px; color: #cccccc;">No co-travelers have joined this ride yet.</p>
            </div>
        """)

    print("""
                </div>
                <div class="modal-footer" style="background: #16213E; border-bottom-left-radius: 20px; border-bottom-right-radius: 20px;">
                    <button type="button" class="btn btn-warning" data-dismiss="modal" style="border-radius: 10px;">Close</button>
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

# Handle ride completion form
booking_id = form.getvalue("booking_id")
completeRide = form.getvalue("completeRide")

if completeRide and booking_id:
    cur.execute("UPDATE booking SET status = 'completed' WHERE booking_id = %s AND custid = %s", (booking_id, cid))
    con.commit()

    cur.execute("SELECT status FROM booking WHERE booking_id = %s", (booking_id,))
    updated_status = cur.fetchone()

    if updated_status and updated_status[0] == 'completed':
        print(f"""
        <script>
            alert("Ride marked as completed successfully!");
            window.location.href = "userdashboard.py?cust_id={cid}&section=completedRides";
        </script>
        """)
    else:
        print(f"""
        <script>
            alert("Error: Ride status update failed. Please try again.");
            window.location.href = "userdashboard.py?cust_id={cid}&section=scheduleRides";
        </script>
        """)

print(f"""
 <div id="availableRides" class="section">

 <div class="container-fluid" style="background: url('your-background-image.jpg') no-repeat center center/cover;margin-left:-120px; margin-top:-100px;width:120%; ">
     <div class="row booking-container justify-content-center py-5">
         <div class="col-lg-8 d-flex align-items-center justify-content-center bg-light p-4 rounded shadow-lg">
             <div class="booking-form-container ">
                 <h3 class="text-center text-dark mb-4"><i class="fa-solid fa-car"></i> Search a Ride</h3>
                 <form action="userdashboard.py" id="bookingForm" method="post" enctype="multipart/form-data">
                    <input type="hidden" name="cust_id" value="{cid}">    
                     <div class="row g-3">
                         <div class="col-md-3 col-12">
                             <div class="input-group">
                                 <span class="input-group-text bg-white"><i class="fa-solid fa-location-dot"></i></span>
                                 <input type="text" class="form-control" name="fromLocation" id="fromLocation" 
                                        placeholder="Enter Pickup Location" required>
                             </div>      
                         </div>
                         """)
print("""

                         <div class="col-md-3 col-12">
                             <div class="input-group">
                                 <span class="input-group-text bg-white"><i class="fa-solid fa-map-marker-alt"></i></span>
                                 <input type="text" class="form-control" name="toLocation" id="toLocation" 
                                        placeholder="Enter Drop Location" required>
                             </div>
                         </div>

                         <div class="col-md-2 col-12">
                             <input type="date" class="form-control" name="rideDate" id="rideDate" min="{datetime.datetime.now().strftime('%Y-%m-%d')}">
                         </div>

                         <div class="col-md-3 col-12">
                             <input type="submit" name="submitb" class="btn btn-primary w-100" value="🚗 Search Here">
                         </div>
                     </div>
                 </form>
             </div>
         </div>
     </div>
 </div>

     <h2 style="text-align:center; color:#2c3e50; font-weight:bold; font-family: 'Poppins', sans-serif; letter-spacing: 1px; text-transform: uppercase;">
         <i class="fas fa-car"></i> Available Rides
     </h2>
     <p style="text-align:center; color:#7f8c8d; font-family: 'Roboto', sans-serif; font-size: 16px;">
         Find and book the perfect ride for your journey.
     </p>
     <div class="container">
         <div class="row">
 """)

search_queryf = form.getvalue("fromLocation")
search_queryt = form.getvalue("toLocation")
ride_date = form.getvalue("rideDate")
vehicle_type = form.getvalue("vehicleType")
submit_button = form.getvalue("submitb")

cleanup_query = "DELETE FROM rides WHERE ride_datetime < NOW()"
cur.execute(cleanup_query)
con.commit()

# Query rides based on search criteria
params = ['pending']
sql = """
    SELECT *, passenger_count - bookedseat AS available_seats 
    FROM rides 
    WHERE status = %s AND ride_datetime >= NOW()
"""

if submit_button and search_queryf and search_queryt:
    sql += " AND pickup_location = %s AND dropoff_location = %s"
    params.extend([search_queryf, search_queryt])

if ride_date:
    sql += " AND DATE(ride_datetime) = %s"
    params.append(ride_date)

if vehicle_type:
    sql += " AND vehicle_type = %s"
    params.append(vehicle_type)

cur.execute(sql, params)
rides = cur.fetchall()

# Display rides
if rides:
    for i in rides:
        print(f""" 
          <div class=\"col-md-4 col-sm-6 mb-4\">
                    <div class=\"card\" style=\"border-radius: 20px; overflow: hidden; box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.2); transition: 0.4s; cursor: pointer; background: #f5f5f5;\" 
                    onmouseover=\"this.style.transform='scale(1.05)'\" onmouseout=\"this.style.transform='scale(1)'\">

                        <!-- Profile Image -->
                        <div style=\"width: 100%; height: 180px; background: linear-gradient(135deg, #e74c3c, #c0392b); display: flex; align-items: center; justify-content: center;\">
                            <img src=\"./images/{i[5]}\" alt=\"Profile Image\" style=\"width: 90px; height: 90px; border-radius: 50%; border: 5px solid white; object-fit: cover;\">
                        </div>

                        <!-- Card Details -->
                        <div class=\"card-body text-dark\" style=\"background: #ecf0f1; text-align: center; font-family: 'Roboto', sans-serif;\">
                            <h5 class=\"card-title\" style=\"margin: 10px 0; font-size: 18px; font-weight: bold; color:#2c3e50; letter-spacing: 0.5px;\">{i[2]}</h5>
                            <p class=\"card-text\" style=\"font-size: 14px; color: #34495e; font-style: italic;\"><strong>From:</strong> {i[6]}</p>
                            <p class=\"card-text\" style=\"font-size: 14px; color: #34495e; font-style: italic;\"><strong>To:</strong> {i[7]}</p>

                            <!-- View Details Button -->
                            <button class=\"btn btn-danger\" data-toggle=\"modal\" data-target=\"#rideModal{i[0]}\" 
                                    style=\"margin-top: 10px; padding: 10px 18px; border-radius: 30px; background: #e74c3c; color: white; font-weight: bold; border: none; transition: 0.3s;\"
                                    onmouseover=\"this.style.opacity='0.8'\" onmouseout=\"this.style.opacity='1'\">
                                View Ride Information
                            </button>
                        </div>
                    </div>
                </div>

               <!-- Premium Ride Information Modal -->
<div class="modal fade" id="rideModal{i[0]}" tabindex="-1" role="dialog" aria-labelledby="rideModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
        <div class="modal-content" style="border-radius: 12px; background: #1B263B; color: #F1F1F1; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);">

            <!-- Modal Header -->
            <div class="modal-header" style="background: #0D1B2A; color: white; padding: 15px; border-top-left-radius: 12px; border-top-right-radius: 12px;">
                <h5 class="modal-title" id="rideModalLabel" style="flex-grow: 1; font-weight: bold;">🚗 Ride Details</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close" style="color: white; font-size: 20px; opacity: 0.8;">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>

            <!-- Modal Body -->
            <div class="modal-body" style="padding: 20px;">
                <div class="row">
                    <!-- Left Section: Ride Info -->
                    <div class="col-md-6">
                        <div style="padding: 15px; border-left: 4px solid #E63946; background: #1F3B5F; border-radius: 8px;">
                            <p><strong>📍 From:</strong> {i[6]}</p>
                            <p><strong>📍 To:</strong> {i[7]}</p>
                            <p><strong>🕒 Posted:</strong> {i[12]}</p>
                            <p><strong>🚘 Vehicle:</strong> {i[9]}</p>
                            <p><strong>👥 Available seat:</strong> {int(i[10]) - int(i[14])}</p>
                            <p><strong>💰 Price/Seat:</strong> <span style="color: #2ECC71; font-weight: bold;">{i[11]}</span></p>
                            
                            <p><strong>📅 Ride Date:</strong> {i[8]}</p>
                            <p><strong>📞 Driver Contact:</strong> {i[4]}</p>
                            <p><strong>🔢 Vehicle No:</strong> {i[16]}</p>
                            <p><strong>🧑‍ Driver Gender:</strong> {i[17]}</p>
                        </div>
                    </div>

                    <!-- Right Section: Vehicle Image -->
                    <div class="col-md-6 text-center d-flex align-items-center justify-content-center">
                        <div>
                            <p><strong>🚙 Vehicle Image:</strong></p>
                            <img src="./images/{i[15]}" class="img-fluid rounded" alt="Vehicle Image" style="max-height: 200px; object-fit: cover; border: 3px solid #E63946; border-radius: 12px; box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);">
                        </div>
                    </div>
                </div>
            </div>

            <!-- Modal Footer -->
            <div class="modal-footer" style="background: #0D1B2A; padding: 15px; border-bottom-left-radius: 12px; border-bottom-right-radius: 12px; display: flex; justify-content: space-between;">
                <button type="button" class="btn btn-outline-light" data-dismiss="modal" style="border-radius: 20px; padding: 10px 20px;">Close</button>
                <form action="userdashboard.py" method="post"enctype="multipart/form-data"> 
                    <input type="hidden" name="ride_id" value="{i[0]}">        
                    <input type="hidden" name="seekerids" value="{i[1]}">
                    <input type="hidden" name="from_location" value="{i[6]}">
                    <input type="hidden" name="to_location" value="{i[7]}">
                    <input type="hidden" name="email" value="{i[3]}">
                    <input type="hidden" name="phone" value="{i[4]}">
                    <input type="hidden" name="ride_date" value="{i[8]}">
                    <input type="hidden" name="vehicle" value="{i[9]}">
                    <input type="hidden" name="passengers" value="{i[10]}">
                    <input type="hidden" name="price_per_seat" value="{i[11]}">
                    <input type="hidden" name="posted_date" value="{i[12]}">
                    <input type="hidden" name="ridergend" value="{i[17]}">
                    <input type="hidden" name="ridername" value="{i[2]}">
                    <input type="hidden" name="vehnum" value="{i[16]}">
                    <input type="hidden" name="vehtyp" value="{i[9]}">
                    <input type="hidden" name="vehimg" value="{i[15]}">
                    <input type="hidden" name="ridimg" value="{i[5]}">
                     <input type="hidden" name="cust_id" value="{cid}">

                    <!-- Seat Selection Dropdown -->
                    <label for="seats_book" class="text-white mr-2"><strong>🪑 Select Seats:</strong></label>
                    <select name="seats_book" required class="form-control" style="width: 100px; display: inline-block;">
                        {''.join([f"<option value='{x}'>{x}</option>" for x in range(1, (int(i[10]) - int(i[14])) + 1)])}
                    </select>

                    <input type="submit" class="btn btn-danger mt-2" name="book_now" value="Book Now"
                           style="padding: 12px 24px; border-radius: 30px; background: #E63946; color: white; font-weight: bold; border: none; transition: 0.3s; box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);"
                           onmouseover="this.style.opacity='0.9'" onmouseout="this.style.opacity='1'">
                </form>
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

cid = form.getvalue("cust_id")
# Fetch ride booking details
ridegend = form.getvalue("ridergend")
ridename = form.getvalue("ridername")
vehnum = form.getvalue("vehnum")
vehtyp = form.getvalue("vehtyp")
vehimg = form.getvalue("vehimg")
ridimg = form.getvalue("ridimg")
ride_id = form.getvalue("ride_id")
seek_id = form.getvalue("seekerids")
from_location = form.getvalue("from_location")
to_location = form.getvalue("to_location")
Emails = form.getvalue("email")
Phones = form.getvalue("phone")
ride_date = form.getvalue("ride_date")
vehicle = form.getvalue("vehicle")
passengers = form.getvalue("passengers")
price_per_seat = form.getvalue("price_per_seat")
posted_date = form.getvalue("posted_date")
Submitbuy = form.getvalue("book_now")

# Convert passengers to integer
passengers = int(passengers) if passengers else 0

cur.execute("SELECT cust_id, FirstName, Email, Phone, address, profile FROM userdata WHERE cust_id = %s", (cid,))
ress = cur.fetchone()

if ress:
    custid = ress[0]
    Name = ress[1]
    Email = ress[2]
    Phone = ress[3]
    Address = ress[4]
    Profile = ress[5]

selected_seats = form.getvalue("seats_book")
selected_seats = int(selected_seats) if selected_seats else 1

if Submitbuy is not None:
    # Fetch current ride details
    cur.execute("SELECT passenger_count, bookedseat FROM rides WHERE ride_id = %s", (ride_id,))
    ride_data = cur.fetchone()

    if ride_data:
        total_seats, booked_seats = ride_data
        available_seats = total_seats - int(booked_seats)  # Convert booked_seats to int for safety

        if selected_seats > available_seats:
            print("<script>alert('Error: Not enough seats available.');</script>")
            exit()
        new_booked_seats = int(booked_seats) + selected_seats

        if available_seats <= 0:
            print("<script>alert('Error: No seats available.');</script>")
            exit()

        query = """
            INSERT INTO booking 
            (ride_id, seekerid, froms, tos, Emailseek, Phoneseek, ridedate, vehicle, passengers, priceperseat, posteddate, 
             custid, custname, custphone, email, custaddress,ridgender, ridname, vehnum, vehtyp, vehimg, ridimg, custprofile) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            ride_id, seek_id, from_location, to_location, Emails, Phones, ride_date, vehicle, selected_seats,
            # Always book 1 seat
            price_per_seat, posted_date, cid, Name, Phone, Email, Address, ridegend, ridename, vehnum, vehtyp,
            vehimg, ridimg, Profile
        )
        cur.execute(query, values)

        # Update booked seats count
        update_query = "UPDATE rides SET bookedseat = %s WHERE ride_id = %s"
        cur.execute(update_query, (new_booked_seats, ride_id))

        # Check if ride is fully booked now
        if new_booked_seats >= total_seats:
            cur.execute("UPDATE rides SET status = 'booked' WHERE ride_id = %s", (ride_id,))

        # Commit changes
        con.commit()


        print(f"""
          <script>
            alert("Booked Successfully");
            setTimeout(function() {{
                window.location = "userdashboard.py?cust_id={cid}&section=requestedRides";
            }}, 500);
          </script>
        """)


print("""
<div id="userCompletedRides" class="section hidden" style="background-color: #2c3e50; color: #ecf0f1; padding: 20px; border-radius: 15px; box-shadow: 0 8px 20px rgba(0,0,0,0.3);">
    <h2 style="text-align: center; color: #f1c40f; margin-bottom: 20px;">
        <i class="fas fa-check-circle"></i> Your Completed Rides
    </h2>
    <p style="text-align: center; color: #bdc3c7; font-size: 18px;">View all the rides you have completed.</p>
    <div class="container">
        <div class="table-responsive">
""")

# Fetch completed rides
cur.execute("SELECT * FROM booking WHERE custid = %s AND status = 'completed'", (cid,))
user_completed_rides = cur.fetchall()

if not user_completed_rides:
    print("""
        <p class="text-muted text-center" style="color: #95a5a6; font-size: 16px; margin-top: 20px;">No completed rides found.</p>
    """)
else:
    print("""
        <table class="table table-bordered table-hover text-center" style="background-color: #1abc9c; color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);">
            <thead style="background-color: #16a085;">
                <tr style="color: #ffffff;">
                    <th>🚖 Booking ID</th>
                    <th>🆔 Ride ID</th>
                    <th>📍 From</th>
                    <th>📍 To</th>
                    <th>📅 Ride Date</th>
                    <th>👤 Rider Name</th>
                    <th>💺 Booked Seat</th>
                    <th>💰 Paid Amount</th>
                    <th>✅ Status</th>
                </tr>
            </thead>
            <tbody>
    """)

    for ride in user_completed_rides:
        total_paid = int(float(ride[9])) * int(float(ride[10]))
        print(f"""
            <tr style="transition: all 0.3s ease; background-color: #2ecc71;"
                onmouseover="this.style.backgroundColor='#27ae60';"
                onmouseout="this.style.backgroundColor='#2ecc71';">
                <td><strong>{ride[0]}</strong></td>
                <td><span style="color: #ffeaa7;">{ride[1]}</span></td>
                <td>{ride[3]}</td>
                <td>{ride[4]}</td>
                <td>{ride[7]}</td>
                <td>{ride[21]}</td>
                <td>{ride[9]}</td>
                <td><strong>₹{total_paid}</strong></td>
                <td style="font-weight: bold; color: #f1c40f;">✅ Completed</td>
            </tr>
        """)

    print("""
            </tbody>
        </table>
    """)

print("""
        </div>
    </div>
</div>
""")


cur.execute("SELECT * FROM booking WHERE custid = %s AND status IN ('pending', 'approved')", (cid,))
pending_rides = cur.fetchall()

# Display Requested Rides Section
print("""
<div id="requestedRides" class="section hidden" style="text-align: center; background-color: #f0f0f0;">
    <h2 style="font-size: 32px; margin-bottom: 15px; background: linear-gradient(135deg, #1e88e5, #42a5f5); padding: 20px; border-radius: 20px; box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3); color: white; display: inline-block;">
        <i class="fas fa-credit-card" style="margin-right: 10px; color: #ffdd57;"></i> Payment Required
    </h2>
    <p style="font-size: 20px; color: #444;">
        <span style="color: #e53935; font-weight: bold;">Your ride has been requested!</span> " Once the sharer approves it, you'll receive the Email and payment option. Complete the payment to confirm your ride <br>
        <span style="color: #1e88e5; font-weight: bold;">Secure your seat now</span> and enjoy a smooth ride.
    </p>

    <div style="font-family: 'Poppins', sans-serif; background-color: #1b263b; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0;">
        <div style="width: 90%; max-width: 1100px; background: #274c77; padding: 20px; border-radius: 12px; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);">
            <table style="width: 100%; border-collapse: collapse;">
                <thead>
                    <tr style="background: #6096ba; color: rgb(6, 6, 6);">
                        <th style="padding: 15px; text-align: center;">From</th>
                        <th style="padding: 15px; text-align: center;">To</th>
                        <th style="padding: 15px; text-align: center;">Date</th>
                        <th style="padding: 15px; text-align: center;">Booked seat</th>
                        <th style="padding: 15px; text-align: center;">Total Price</th>
                        <th style="padding: 15px; text-align: center;">Status</th>
                        <th style="padding: 15px; text-align: center;">Action</th>
                    </tr>
                </thead>
                <tbody>
""")

if pending_rides:
    for ride in pending_rides:
        booking_status = ride[17]         # status
        payment_status = ride[19]         # paymentstatus

        print(f"""
            <tr style="background: #8badd0; color: white; text-align: center;">
                <td style="padding: 15px;">{ride[3]}</td>
                <td style="padding: 15px;">{ride[4]}</td>
                <td style="padding: 15px;">{ride[7]}</td>
                <td style="padding: 15px;">{ride[9]}</td>
                <td style="padding: 15px;">₹{int(float(ride[9])) * int(float(ride[10]))}</td>
                <td style="padding: 15px; color: yellow; font-weight: bold;">Requested ride</td>
                <td style="padding: 15px;">
                    <form method="post" enctype="multipart/form-data">
                        <input type="hidden" name="rideid" value="{ride[1]}">
                        <input type="hidden" name="custid" value="{ride[12]}">
                        <input type="hidden" name="bookingid" value="{ride[0]}">
        """)

        # Conditionally show "Pay Now"
        if booking_status == 'approved' and payment_status == 'Payment In Process':
            print("""
                <input type="submit" name="submitpay" style="background: #2d6a4f; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; font-size: 14px; margin-right: 5px;" value="Pay Now">
            """)

        # Show "Cancel" for both pending and approved
        if booking_status in ['pending', 'approved']:
            print("""
                <input type="submit" name="submitcan" style="background: #c1121f; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; font-size: 14px;" value="Cancel">
            """)

        # Ride Details button to trigger modal
        print(f"""
                        <button type="button" class="btn btn-info" data-toggle="modal" data-target="#rideModal{ride[0]}" style="background: #2196F3; color: white; padding: 8px 12px; border: none; border-radius: 5px; margin-top: 5px;">
                            <i class="fas fa-info-circle"></i> Ride Details
                        </button>
                    </form>
                </td>
            </tr>

            <!-- Ride Details Modal -->
            <div class="modal fade" id="rideModal{ride[0]}" tabindex="-1" role="dialog">
                <div class="modal-dialog" role="document">
                    <div class="modal-content" style="background: #1e3c72; color: white; border-radius: 15px; overflow: hidden;">
                        <div class="modal-header" style="background: #16213E; color: #F8B400;">
                            <h5 class="modal-title"><i class="fas fa-car-side"></i> Ride Details</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close" style="color: white;">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body d-flex align-items-start">
                            <div class="info" style="flex: 1; padding-right: 20px;">
                                <p><strong><i class="fas fa-user"></i> Name:</strong> {o[21]}</p>
                                <p><strong><i class="fas fa-venus-mars"></i> Gender:</strong> {o[20]}</p>
                                <p><strong><i class="fas fa-phone"></i> Phone:</strong> {o[6]}</p>
                                <p><strong><i class="fas fa-envelope"></i> Email:</strong> {o[5]}</p>
                                <p><strong><i class="fas fa-map-marker-alt"></i> From:</strong> {ride[3]}</p>
                                <p><strong><i class="fas fa-map-marker-alt"></i> To:</strong> {ride[4]}</p>
                                <p><strong><i class="fas fa-calendar-alt"></i> Date:</strong> {ride[7]}</p>
                                <p><strong><i class="fas fa-hashtag"></i> Vehicle No:</strong> {ride[22]}</p>
                            </div>
                            <div class="images text-center" style="flex: 1;">
                                <p><strong><i class="fas fa-car-side"></i> Vehicle Image:</strong></p>
                                <img src="./images/{ride[24]}" class="img-fluid rounded" alt="Vehicle Image" 
                                    style="max-height: 180px; object-fit: cover; border: 3px solid #F8B400; border-radius: 12px; 
                                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3);">
                                <p class="mt-3"><strong><i class="fas fa-user"></i> Rider Image:</strong></p>
                                <img src="./images/{ride[25]}" class="img-fluid rounded" alt="Rider Image" 
                                    style="max-height: 180px; object-fit: cover; border: 3px solid #F8B400; border-radius: 12px; 
                                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3);">
                            </div>
                        </div>
                        <div class="modal-footer" style="background: #16213E; border-top: none;">
                            <button type="button" class="btn btn-warning" data-dismiss="modal"><i class="fas fa-times"></i> Close</button>
                        </div>
                    </div>
                </div>
            </div>
        """)

# Close the table and container divs
print("""
                </tbody>
            </table>
        </div>
    </div>
</div>
""")

# Handle form actions
ridesid = form.getvalue("rideid")
custid = form.getvalue("custid")
bookingid = form.getvalue("bookingid")
Submitp = form.getvalue("submitpay")
Submitz = form.getvalue("submitcan")

if Submitz is not None:
    cur.execute("SELECT passengers FROM booking WHERE booking_id = %s", (bookingid,))
    result = cur.fetchone()

    if result:
        booked_seats = int(result[0])

        # Cancel booking
        cur.execute("UPDATE booking SET status = %s WHERE custid = %s AND booking_id = %s", ('Canceled', custid, bookingid))
        con.commit()

        # Update ride seat count
        cur.execute("UPDATE rides SET bookedseat = bookedseat - %s , status = 'pending' WHERE ride_id = %s", (booked_seats, ridesid))
        con.commit()

        print(f"""
            <script>
                alert("Ride Canceled successfully");
                location.href="userdashboard.py?cust_id={custid}&section=requestedRides";
            </script>
        """)

if Submitp is not None:
    print(f"""
        <script>
            alert("Successfully redirected to payment...");
            location.href="payment.py?cust_id={custid}&book_id={bookingid}";
        </script>
    """)



query = """select * from userdata where cust_id = '%s'""" % (cid)
cur.execute(query)
res = cur.fetchall()
for j in res:
    print(f"""
            <div id="profile" class="section hidden" 
                    style="background: linear-gradient(135deg, #0F2027, #203A43, #2C5364); color: white; padding: 30px; border-radius: 15px; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);">
                   <h2 class="text-center text-white p-3" 
                    style="background: #034f84; border-radius: 12px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); font-weight: bold;">
                    <i class="fas fa-user-circle"></i> My Profile
                  </h2>
                <div class="profile-card" >
                    <div class="profile-header">
                        Profile Information
                    </div>
                <div class="profile-img-container">
                    <label for="profilePicUpload">
                        <img id="profilePicPreview" src="./images/{j[5]}" class="profile-img" alt="Profile">
                         <button data-bs-toggle="modal" data-bs-target="#addressModallph{cid}" class="btn btn-sm edit-btn ms-2"> Change</button>
                    </label>
                    </div>
                <table class="table table-dark table-bordered mt-3">
                    <tbody>
                        <tr>
                            <th>Name</th>
                             <td class="d-flex align-items-center">
                             <input type="text" class="form-control text-center fw-bold" id="userName" value="{j[1]} {j[2]}"
                                    readonly>
                            </td>
                        </tr>
                        <tr>
                            <th>Email</th>
                            <td class="d-flex align-items-center">
                                <input type="email" class="form-control" id="addressModalll" value="{j[3]} ">
                             </td>
                        </tr>
                        <tr>
                            <th>Contact</th>
                            <td class="d-flex align-items-center">
                                <input type="text" class="form-control" id="userPhone" value="+91{j[4]}" readonly>
                            </td>
                        </tr>
                         <tr>
                            <th>Password</th>
                            <td class="d-flex align-items-center">
                                <input type="text" class="form-control" id="userPhone" value="********" readonly>
                                 <button data-bs-toggle = "modal" data-bs-target = "#addressModallp{cid}" class="btn btn-sm edit-btn ms-2" > Change </button>
                            </td>
                        </tr>
                        <tr>
                        <tr>
                            <th>Address</th>
                            <td class="d-flex align-items-center">
                                <input type="text" class="form-control" id="userAddress" value="{j[6]}" readonly>
                                <button data-bs-toggle = "modal" data-bs-target = "#addressModal{cid}" class="btn btn-sm edit-btn ms-2" > Change </button>
                            </td>
                        </tr>

                    </tbody>
                </table>

            </div>
        </div>
               """)

print(f"""<!-- Change Modal -->
        <div class="modal fade" id="addressModal{cid}" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                    <form method="post" enctype="multipart/form-data">
                        <div class="modal-header">
                            <h5 class="modal-title" id="modalLabel">Change Your Address</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <textarea class="form-control" name="addressn" rows="3" placeholder="Enter your address here..."></textarea required>
                            <input type="hidden" name="cid" value="{cid}">
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <input type="submit" name="submitn" class="btn btn-update" value="Update Address">
                        </div>
                    </form>
                </div>
            </div>
        </div>
        """)

print(f"""

        <div class="modal fade" id="addressModall{cid}" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                        <form method="post" enctype="multipart/form-data">
                            <div class="modal-header">
                                <h5 class="modal-title" id="modalLabel">Change Phone Number</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <input class="form-control" name="phonen" rows="3" placeholder="Enter your Phone No. here..."  minlength="10" maxlength="10">
                                <input type="hidden" name="cidd" value="{cid}">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <input type="submit" name="submitp" class="btn btn-update" value="Update Phone">
                            </div>
                        </form>
                </div>
            </div>
        </div>

   """)
print(f"""

        <div class="modal fade" id="addressModallp{cid}" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                        <form method="post" enctype="multipart/form-data">
                            <div class="modal-header">
                                <h5 class="modal-title" id="modalLabel">Change Your Password</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <input type="text" class="form-control" name="passnn" rows="3" placeholder="Enter your Password here..." minlength="8" maxlength="8" required>
                                <input type="hidden" name="cidp" value="{cid}">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <input type="submit" name="submitpass" class="btn btn-update" value="Update Password">
                            </div>
                        </form>
                </div>
            </div>
        </div>

    """)
print(f"""

        <div class="modal fade" id="addressModallem{cid}" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                        <form method="post" enctype="multipart/form-data">
                            <div class="modal-header">
                                <h5 class="modal-title" id="modalLabel">Change Email id.</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <input type="email" class="form-control" name="emailn" rows="3" placeholder="Enter your Email here..."  required>
                                <input type="hidden" name="ciddd" value="{cid}">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <input type="submit" name="submite" class="btn btn-update" value="Update Email">
                            </div>
                        </form>
                </div>
            </div>
        </div>

    """)
print(f"""

        <div class="modal fade" id="addressModallph{cid}" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                        <form method="post" enctype="multipart/form-data">
                            <div class="modal-header">
                                <h5 class="modal-title" id="modalLabel">Change Your Profile Picture</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <input type="file" class="form-control" name="photon" rows="3" placeholder="Enter your Profile picture here."required>
                                <input type="hidden" name="cidph" value="{cid}">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <input type="submit" name="submitpro" class="btn btn-update" value="Update Profile Pic">
                            </div>
                        </form>
                </div>
            </div>
        </div>

   """)
cid = form.getvalue("cid")
Address = form.getvalue("addressn")
Submita = form.getvalue("submitn")

if Submita != None:
    q = """UPDATE userdata SET address ='%s' WHERE cust_id='%s'""" % (Address, cid)
    cur.execute(q)
    con.commit()
    print("""
       <script>
          alert("Address updated successfully")
          location.href="userdashboard.py?cust_id=%s&section=profile";
       </script>
    """ % (cid))

cid = form.getvalue("cidd")
Phonen = form.getvalue("phonen")
Submitp = form.getvalue("submitp")

if Submitp != None:
    q = """UPDATE userdata SET Phone ='%s' WHERE cust_id='%s'""" % (Phonen, cid)
    cur.execute(q)
    con.commit()
    print("""
       <script>
          alert("Phone no updated successfully")
          location.href="userdashboard.py?cust_id=%s&section=profile";
       </script>
    """ % (cid))

cid = form.getvalue("ciddd")
Emailn = form.getvalue("emailn")
Submite = form.getvalue("submite")

if Submite != None:
    q = """UPDATE userdata SET Email ='%s' WHERE cust_id='%s'""" % (Emailn, cid)
    cur.execute(q)
    con.commit()
    print("""
       <script>
          alert("Email updated successfully")
          location.href="userdashboard.py?cust_id=%s&section=profile";
       </script>
    """ % (cid))

cid = form.getvalue("cidp")
Passn = form.getvalue("passnn")
Submitpa = form.getvalue("submitpass")

if Submitpa != None:
    q = """UPDATE userdata SET Password ='%s' WHERE cust_id='%s'""" % (Passn, cid)
    cur.execute(q)
    con.commit()
    print("""
       <script>
          alert("Password updated successfully")
          location.href="userdashboard.py?cust_id=%s&section=profile";
       </script>
    """ % (cid))

cid = form.getvalue("cidph")
Submitpr = form.getvalue("submitpro")

if Submitpr != None:
    Imageu = form['photon']
    sn = os.path.basename(Imageu.filename)
    open("images/" + sn, "wb").write(Imageu.file.read())

    q = """UPDATE userdata SET profile ='%s' WHERE cust_id='%s'""" % (sn, cid)
    cur.execute(q)
    con.commit()
    print("""
       <script>
          alert("Profile updated successfully")
          location.href="userdashboard.py?cust_id=%s&section=profile";
       </script>
    """ % (cid))

print("""
     <script>
            document.addEventListener("DOMContentLoaded", function () {
                const params = new URLSearchParams(window.location.search);
                const section = params.get("section");
                if (section) {
                    document.querySelectorAll(".section").forEach(s => s.classList.add("hidden"));
                    document.getElementById(section).classList.remove("hidden");
                }
            });
       </script>

    <script>
        function showSection(sectionId) {
            // Hide all sections
            document.querySelectorAll('.section').forEach(section => {
                section.classList.add('hidden');
            });

            // Show the selected section
            document.getElementById(sectionId).classList.remove('hidden');
        }
    </script>
    <script>
        function openEditModal(fieldTitle, fieldId) {
            document.getElementById('fieldTitle').innerText = fieldTitle;
            document.getElementById('newFieldValue').value = document.getElementById(fieldId).value;
            document.getElementById('fieldId').value = fieldId;
            let modal = new bootstrap.Modal(document.getElementById('changeModal'));
            modal.show();
        }

        function saveChanges() {
            let fieldId = document.getElementById('fieldId').value;
            let newValue = document.getElementById('newFieldValue').value;
            if (newValue) {
                document.getElementById(fieldId).value = newValue;
            }
            let modalElement = document.getElementById('changeModal');
            let modal = bootstrap.Modal.getInstance(modalElement);
            modal.hide();
        }

        function previewProfileImage(event) {
            let reader = new FileReader();
            reader.onload = function () {
                document.getElementById('profilePicPreview').src = reader.result;
            };
            reader.readAsDataURL(event.target.files[0]);
        }
    </script>
    <script>
        function toggleSidebar() {
            let sidebar = document.querySelector('.sidebar');
            let backdrop = document.querySelector('.sidebar-backdrop');

            // Toggle the 'show' class on the sidebar
            sidebar.classList.toggle('show');

            // Show or hide the backdrop when sidebar is toggled
            if (sidebar.classList.contains('show')) {
                backdrop.style.display = 'block';
            } else {
                backdrop.style.display = 'none';
            }
        }
    </script>
    <script>
        // Booking js 
document.getElementById("whenSelect").addEventListener("change", function () {
    var departureTimeContainer = document.getElementById("departureTimeContainer");
    if (this.value === "schedule") {
        departureTimeContainer.classList.remove("hidden");
        document.getElementById("rideTime").required = true;
    } else {
        departureTimeContainer.classList.add("hidden");
        document.getElementById("rideTime").required = false;
    }
});

document.getElementById("whenSelect").addEventListener("change", function () {
    var departureTimeContainer = document.getElementById("departureTimeContainer");
    document.getElementById("rideTime").required = this.value === "schedule";
    departureTimeContainer.classList.toggle("hidden", this.value === "now");
});

document.getElementById("rideType").addEventListener("change", function () {
    var shareRideContainer = document.getElementById("shareRideContainer");
    var passengerContainer = document.getElementById("passengerContainer");
    var shareRideSelect = document.getElementById("shareRide");

    if (this.value === "Bike") {
        // Hide passenger container when Bike is selected
        passengerContainer.classList.add("hidden");
        // Hide share ride option for Bike
        shareRideContainer.classList.add("hidden");
        shareRideSelect.value = "no"; // Default to "No" for ride sharing if bike is selected
    } else {
        // Show passenger container and share ride option when the ride type is not Bike
        passengerContainer.classList.remove("hidden");
        shareRideContainer.classList.remove("hidden");
    }
});


document.getElementById("shareRide").addEventListener("change", function () {
    var genderContainer = document.getElementById("genderContainer");
    genderContainer.classList.toggle("hidden", this.value === "no");
});

document.getElementById("bookingForm").addEventListener("submit", function (event) {
    event.preventDefault();
    let fromLocation = document.getElementById("fromLocation").value;
    let toLocation = document.getElementById("toLocation").value;
    let rideType = document.getElementById("rideType").value;
    let shareRide = document.getElementById("shareRide").value;
    let gender = document.getElementById("gender").value;
    let passengerCount = document.getElementById("passengerCount").value;
    let whenSelect = document.getElementById("whenSelect").value;
    let rideTime = document.getElementById("rideTime").value;

    if (whenSelect === "schedule" && rideTime === "") {
        alert("Please select a date and time for your scheduled ride.");
        return;
    }

    if (shareRide === "yes" && rideType === "Bike") {
        alert("Ride sharing is not allowed for Bikes.");
        return;
    }

    let bookingDetails = `Ride booked from ${fromLocation} to ${toLocation} with ${passengerCount} passengers `;
    bookingDetails += shareRide === "yes" ? `sharing with ${gender} travelers.` : "without sharing.";

    alert(bookingDetails);
});
    </script>
    <script>
     <!-- search js -->
   function searchFromTo(field) {
    let query = document.getElementById(field).value.trim();

    if (query.length < 2) return; // Prevent unnecessary queries

    fetch(`/cgi-bin/userdashboard.py?query=${query}`)
        .then(response => response.json())
        .then(data => {
            let resultsDiv = document.getElementById(field + "Results");

            if (!resultsDiv) {
                resultsDiv = document.createElement("div");
                resultsDiv.className = "search-results";
                resultsDiv.id = field + "Results";
                document.getElementById(field).parentNode.appendChild(resultsDiv);
            }

            resultsDiv.innerHTML = ""; // Clear previous results

            if (data.length > 0) {
                data.forEach(location => {
                    let resultItem = document.createElement("p");
                    resultItem.innerText = location;
                    resultItem.onclick = function () {
                        document.getElementById(field).value = location;
                        resultsDiv.innerHTML = ""; // Clear results after selection
                    };
                    resultsDiv.appendChild(resultItem);
                });
            } else {
                resultsDiv.innerHTML = "<p>No results found</p>";
            }
        })
        .catch(error => console.error("Error fetching search results:", error));
}

    </script>
    <script>
    document.querySelectorAll('.book-ride-btn').forEach(button => {
        button.addEventListener('click', function () {
            let rideId = this.getAttribute('data-ride-id');
            fetch('userdashboard.py', {
                method: 'POST',
                body: new URLSearchParams({ 'ride_id': rideId })
            })
            .then(response => response.text())
            .then(data => alert(data))
            .catch(error => console.error('Error:', error));
        });
    });
</script>
<script>
    function showSection(sectionId) {
        // Hide all sections
        document.querySelectorAll('.section').forEach(section => {
            section.classList.add('hidden');
        });

        // Show the selected section
        document.getElementById(sectionId).classList.remove('hidden');

        // Update the URL hash without reloading
        history.pushState(null, null, '#' + sectionId);
    }

</script>

<script>
    function showSection(sectionId) {
        // Hide all sections
        document.querySelectorAll('.section').forEach(section => {
            section.classList.add('hidden');
        });

        // Show the selected section
        let targetSection = document.getElementById(sectionId);
        if (targetSection) {
            targetSection.classList.remove('hidden');
        } else {
            console.error("Section not found: " + sectionId);
        }

        // Update the URL hash without reloading
        history.pushState(null, null, '#' + sectionId);
    }

    document.addEventListener("DOMContentLoaded", function () {
        const params = new URLSearchParams(window.location.search);
        const section = params.get("section");
        if (section) {
            showSection(section);
        }
    });
</script>

            
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.6.0/js/bootstrap.bundle.min.js"></script>

        <!-- Bootstrap JS, Popper.js, and jQuery -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>
      """)