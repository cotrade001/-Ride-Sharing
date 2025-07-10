#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, smtplib, random, string, os,sys
sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()

form = cgi.FieldStorage()
cid = form.getvalue("SNo")

print(cid)

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sharerker Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    
    <style>
        body {
            height: 100vh;
            background-color: #f8f9fa;
            font-family: Arial, sans-serif;
            overflow-x: hidden;
        }

        .sidebar {
            width: 260px;
            background-color: #586464;
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
        .hidden {
        display: none;
        }
                /* post ride */
        body,
        html {
            height: 100%;
            margin: 0;
            overflow: hidden;
        }

        .booking-container {
            height: 100vh;
            display: flex;
            align-items: stretch;
            justify-content: center;
        }

        .booking-form-container {
            background-color: white;
            padding: 40px;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            background-image: url(book\ back.png);
            overflow-y: auto;
            max-height: 100vh;
        }

        .content {
          
            height: 100vh;
            /* Full height */
            overflow-y: auto;
            /* Enables scrolling */
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
        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        }

        .btn:hover {
            filter: brightness(1.2);
        }

    </style>
</head>

<body>

    <div class="top-navbar d-flex">
        <span class="menu-btn" onclick="toggleSidebar()"><i class="fas fa-bars"></i></span>
        <h6 class="m-0">Sharer Dashboard</h6>
    </div>

    <div class="sidebar">
        <div style="margin-left: 10px; display:flex; align-items:center; ">
            <img src="./img/Free Vector _ Taxi route neon sign.jpg"
                style="height: 50px; width:50px; border-radius:100px; background-color:rgb(142, 242, 244)" alt="">
            <h6 class="mt-3" style="margin-left:10px;">Let's Go..</h6>
        </div>
        <h4 class="text-center mt-3"><i class="fas fa-user"></i> Sharer Dashboard</h4>
        <a href="#" onclick="showSection('profile')"><i class="fas fa-user-circle"></i> Profile</a>
         <a href="#" onclick="showSection('postRides')"> <i class="fas fa-plus-circle"></i> Post Ride</a>
        <div class="dropdown">
            <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown"><i class="fas fa-car"></i> My Rides</a>
            <ul class="dropdown-menu">
                 <li><a class="dropdown-item" href="#" onclick="showSection('showRides')"> <i class="fas fa-car-side"></i> View Posted Rides</a></li>
                 <li><a class="dropdown-item" href="#" onclick="showSection('approveRides')"> <i class="fas fa-handshake"></i> Requested Rides</a></li>
                <li><a class="dropdown-item" href="#" onclick="showSection('requestRides')"> <i class="fas fa-user-circle"></i> My Rides</a></li>
                <a href="#" onclick="showSection('completedRides')"> <i class="fas fa-check-square"></i> Completed Rides</a>
                <a href="#" onclick="showSection('cancelledByUser')"><i class="fas fa-ban"></i> Canceled Rides</a>
             
            </ul>
        </div>
             <a href="home.py"><i class="fa-solid fa-door-open"></i> Logout</a>
    </div>
    <div class="sidebar-backdrop" onclick="toggleSidebar()"></div>

    <div class="content">
        <div id="overview" class="section">
           
        </div>
   
""")


print("""
<div id="cancelledByUser" class="section hidden" style="text-align: center; padding: 40px; background: linear-gradient(135deg, #1f1c2c, #928dab); border-radius: 20px; color: white;">
    <h2 style="font-size: 2.2rem; font-weight: bold; color: #fecd1a; text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.4); margin-bottom: 10px;">
        <i class="fas fa-ban"></i> Canceled & Rejected Rides
    </h2>
    <p style="font-size: 1.2rem; color: #f1f1f1;">
        Filter your rides below:
    </p>

    <!-- Filter Dropdown -->
    <div style="margin: 20px 0;">
        <select id="rideFilter" onchange="filterRides()" style="padding: 10px 20px; border-radius: 10px; border: none; font-size: 1rem; color: #333;">
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
                        <tbody id="rideTable">
""")

query = "SELECT * FROM booking WHERE seekerid = %s AND LOWER(status) IN ('canceled', 'rejected')"
cur.execute(query, (cid,))
rides = cur.fetchall()

if not rides:
    print("<tr><td colspan='9' style='text-align:center; padding: 20px; font-weight: bold; color: #ff6b6b;'>No canceled or rejected rides available.</td></tr>")
else:
    for idx, a in enumerate(rides, start=1):
        ride_id = a[0]
        status = a[17].strip().lower()

        canceled_by = a[13] if status == "canceled" else "-"
        rejected_by = a[21] if status == "rejected" else "-"

        if status == "canceled":
            status_label = "🚫 Canceled by user"
            row_color = "#ffe6e6"
            text_color = "#c0392b"
            row_class = "canceled"
        elif status == "rejected":
            status_label = "❌ Rejected by me"
            row_color = "#fff4e1"
            text_color = "#e67e22"
            row_class = "rejected"
        else:
            status_label = "❓ Unknown"
            row_color = "#f0f0f0"
            text_color = "#7f8c8d"
            row_class = "unknown"

        print(f"""
            <tr class="rideRow {row_class}" style="background-color: {row_color}; font-size: 1rem; font-weight: 500; transition: 0.3s; text-align: center; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);"
                onmouseover="this.style.transform='scale(1.01)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.2)'"
                onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)'">
                <td style="padding: 15px; vertical-align: middle; color: #2c3e50;">{idx}</td>
                <td style="vertical-align: middle;">
                    <span style="color: {text_color}; background: rgba(0,0,0,0.05); padding: 6px 12px; border-radius: 8px; display: inline-block; font-weight: bold;">
                        #{ride_id}
                    </span>
                </td>
                <td style="color: #2c3e50; vertical-align: middle;">{a[3]}</td>
                <td style="color: #2c3e50; vertical-align: middle;">{a[4]}</td>
                <td style="color: #2c3e50; vertical-align: middle;">{a[7]}</td>
                <td style="color: #2c3e50; vertical-align: middle;">{a[9]}</td>
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
    function filterRides() {
        const filter = document.getElementById("rideFilter").value;
        const rows = document.querySelectorAll(".rideRow");

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


from collections import defaultdict

# Fetch bookings with 'booked' status
query = "SELECT * FROM booking WHERE seekerid = %s AND status = 'booked'"
cur.execute(query, (cid,))
app = cur.fetchall()

# Group bookings by ride_id
grouped_rides = defaultdict(list)
for a in app:
    grouped_rides[a[1]].append(a)

print("""
<div id="requestRides" class="section hidden" style="background: linear-gradient(to right, #0f2027, #203a43, #2c5364); padding: 40px 20px; border-radius: 15px; text-align: center; box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.9);">
    <h2 style="color: #ffffff; text-shadow: 2px 2px 5px rgba(0,0,0,0.5); font-size: 28px;">🚖 Approved Rides</h2>
    <p style="color: #ccc; font-size: 18px;">List of rides that have been approved.</p>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-12">
                <div class="table-responsive">
                    <table class="table text-center" style="border-radius: 15px; overflow: hidden; box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.7); background: linear-gradient(to right, #1e3c72, #2a5298);">
                        <thead style="background: linear-gradient(to right, #0f2027, #203a43, #2c5364); color: #f8f9fa;">
                            <tr>
                                <th>🚖 Ride ID</th>
                                <th>🚗 From</th>
                                <th>📍 To</th>
                                <th>📅 Date & Time</th>
                                <th>✅ Action</th>
                                <th>🔍 Customer Details</th>
                            </tr>
                        </thead>
                        <tbody>
""")

# One loop for table rows
for ride_id, bookings in grouped_rides.items():
    first = bookings[0]
    print(f"""
        <tr>
            <td>{ride_id}</td>
            <td>{first[3]}</td>
            <td>{first[4]}</td>
            <td>{first[7]}</td>
            <td>
                <form method="POST">
                    <input type="hidden" name="ride_id_all" value="{ride_id}">
                    <input type="submit" class="btn btn-success btn-sm" name="completeAllRide" value="Mark All as Completed" style="border-radius: 12px; font-weight: bold;">
                </form>
            </td>
            <td>
                <button class="btn btn-outline-info btn-sm" data-toggle="modal" data-target="#sharerModal{ride_id}" style="border-radius: 12px; font-weight: bold;">View More</button>
            </td>
        </tr>
    """)

print("""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
""")

# Modal section outside the table loop
for ride_id, bookings in grouped_rides.items():
    print(f"""
    <!-- Modal for All Customers -->
    <div class="modal fade" id="sharerModal{ride_id}" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-xl" role="document">
            <div class="modal-content" style="background: #1b1b1b; color: white; border-radius: 15px; border: 2px solid #f39c12;">
                <div class="modal-header" style="background: #111; color: #f39c12;">
                    <h5 class="modal-title"><i class="fas fa-user-circle"></i> Customers for Ride ID: {ride_id}</h5>
                    <button type="button" class="close" data-dismiss="modal" style="color: white;"><span>&times;</span></button>
                </div>
                <div class="modal-body">
                    <div class="table-responsive">
                        <table class="table table-dark table-striped table-bordered">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Phone</th>
                                    <th>Seats</th>
                                    <th>Total ₹</th>
                                    <th>Payment</th>
                                    <th>Image</th>
                                    <th>✅ Action</th>
                                </tr>
                            </thead>
                            <tbody>
    """)
    for a in bookings:
        total_price = int(a[9]) * float(a[10])
        print(f"""
            <tr>
                <td>{a[13]}</td>
                <td>{a[15]}</td>
                <td>{a[14]}</td>
                <td>{a[9]}</td>
                <td>₹{total_price:.2f}</td>
                <td>{a[19]} via {a[18]}</td>
                <td><img src="./images/{a[26]}" style="height: 60px; border-radius: 8px;"></td>
                <td>
                    <form method="POST">
                        <input type="hidden" name="booking_id" value="{a[0]}">
                        <input type="submit" class="btn btn-outline-success btn-sm" name="completeRide" value="Mark as Completed">
                    </form>
                </td>
            </tr>
        """)

    print("""
                            </tbody>
                        </table>
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
</div>
""")


# Handle "Mark One as Completed"
booking_id = form.getvalue("booking_id")
completeRide = form.getvalue("completeRide")

if completeRide and booking_id:
    cur.execute("UPDATE booking SET status = 'completed' WHERE booking_id = %s", (booking_id,))
    con.commit()
    print(f"""
        <script>
            alert("Booking marked as completed!");
            window.location.href = "seekerdashboard.py?SNo={cid}&section=requestRides";
        </script>
    """)

# Handle "Mark All as Completed"
ride_id_all = form.getvalue("ride_id_all")
completeAllRide = form.getvalue("completeAllRide")

if completeAllRide and ride_id_all:
    cur.execute("UPDATE booking SET status = 'completed' WHERE ride_id = %s AND seekerid = %s", (ride_id_all, cid))
    con.commit()
    print(f"""
        <script>
            alert("All bookings for ride ID {ride_id_all} marked as completed!");
            window.location.href = "seekerdashboard.py?SNo={cid}&section=requestRides";
        </script>
    """)
print("""
<div id="completedRides" class="section hidden">
    <h2 style="color: #ffffff; font-size: 30px; text-align: center; background: linear-gradient(to right, #0f0c29, #302b63, #24243e); padding: 20px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); letter-spacing: 1px;">
        <i class="fas fa-check-circle" style="color: #2ecc71; margin-right: 10px;"></i> Completed Rides
    </h2>
    <p style="color: #dcdcdc; font-size: 18px; text-align: center; background: #1a1a2e; padding: 15px 25px; border-radius: 12px; width: 70%; margin: 20px auto; box-shadow: 0px 6px 16px rgba(0, 0, 0, 0.6);">
        Here's a list of all the rides you've completed successfully.
    </p>
    <div class="container mt-4" style="padding: 20px;">
""")

cur.execute("SELECT * FROM booking WHERE seekerid = %s AND status = 'completed' ORDER BY booking_id DESC", (cid,))
completed_rides = cur.fetchall()

from collections import defaultdict
grouped_rides = defaultdict(list)
for ride in completed_rides:
    grouped_rides[ride[1]].append(ride)

if not grouped_rides:
    print("""
        <div class="text-center p-4">
            <p style="color: #999; font-size: 16px;">No completed rides found.</p>
        </div>
    """)
else:
    print("""
        <div style="overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; border-radius: 16px; overflow: hidden; background-color: #101026; color: #f1f1f1; font-family: 'Segoe UI', sans-serif; box-shadow: 0 12px 30px rgba(0, 0, 0, 0.75); margin-top: 20px; text-align: center;">
                <thead>
                    <tr style="background: linear-gradient(to right, #1c1c3c, #641f7a); font-size: 17px; letter-spacing: 1px; text-transform: uppercase;">
                        <th style="padding: 14px;">Ride ID</th>
                        <th style="padding: 14px;">From</th>
                        <th style="padding: 14px;">To</th>
                        <th style="padding: 14px;">Date & Time</th>
                        <th style="padding: 14px;">Total Seats</th>
                        <th style="padding: 14px;">Total Amount</th>
                        <th style="padding: 14px;">Details</th>
                    </tr>
                </thead>
                <tbody>
    """)

    modal_html = ""
    row_colors = ["#141432", "#1c1c3c"]

    for i, (ride_id, rides) in enumerate(grouped_rides.items()):
        total_seats = sum(int(r[9]) for r in rides)
        total_amount = sum(int(r[9]) * float(r[10]) for r in rides)
        first_ride = rides[0]
        bg_color = row_colors[i % 2]
        modal_id = f"rideDetailsModal_{ride_id}"

        print(f"""
            <tr style="background-color: {bg_color};">
                <td style="color: #00ffe1; font-weight: 600; padding: 12px;">{ride_id}</td>
                <td style="color: #e0e0e0; padding: 12px;">{first_ride[3]}</td>
                <td style="color: #e0e0e0; padding: 12px;">{first_ride[4]}</td>
                <td style="color: #e0e0e0; padding: 12px;">{first_ride[7]}</td>
                <td style="color: #f39c12; font-weight: bold; padding: 12px;">{total_seats}</td>
                <td style="color: #2ecc71; font-weight: bold; padding: 12px;">₹{total_amount:.2f}</td>
                <td style="padding: 12px;">
                    <button onclick="document.getElementById('{modal_id}').style.display='block'" style="padding: 8px 16px; background: #1abc9c; border: none; color: white; border-radius: 10px; cursor: pointer; font-weight: bold;">View</button>
                </td>
            </tr>
        """)

        modal_rows = ""
        for a in rides:
            profile_img = f"./images/{a[26]}" if a[26] else "./images/default.jpg"
            total_price = int(a[9]) * float(a[10])
            modal_rows += f"""
                <tr style="border-bottom: 1px solid #333;">
                    <td style="padding: 10px; color: #f1f1f1;">{a[0]}</td>
                    <td style="padding: 10px; color: #e0e0e0;">{a[13]}</td>
                    <td style="padding: 10px; color: #e0e0e0;">{a[15]}</td>
                    <td style="padding: 10px; color: #e0e0e0;">{a[14]}</td>
                    <td style="padding: 10px; color: #f39c12;">{a[9]}</td>
                    <td style="padding: 10px; color: #2ecc71;">₹{total_price:.2f}</td>
                    <td style="padding: 10px; color: #00ffe1;">{a[19]} via {a[18]}</td>
                    <td style="padding: 10px;">
                        <img src="{profile_img}" onerror="this.src='./images/default.jpg'" style="height: 60px; width: 60px; border-radius: 12px; object-fit: cover;">
                    </td>
                </tr>
            """

        modal_html += f"""
        <div id="{modal_id}" style="display: none; position: fixed; z-index: 9999; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.85);">
            <div style="background-color: #1a1a2e; color: #f1f1f1; margin: 5% auto; padding: 20px; border-radius: 16px; width: 90%; max-width: 1000px; box-shadow: 0 12px 30px rgba(0,0,0,0.6); position: relative;">
                <span onclick="document.getElementById('{modal_id}').style.display='none'" style="color: #fff; position: absolute; top: 10px; right: 20px; font-size: 28px; font-weight: bold; cursor: pointer;">&times;</span>
                <h3 style="margin-bottom: 15px; text-align: center; font-size: 26px; color: #00ffe1;">Ride Details - ID {ride_id}</h3>
                <div style="overflow-x: auto; max-height: 400px;">
                    <table style="width: 100%; border-collapse: collapse; font-size: 15px; text-align: center;">
                        <thead>
                            <tr style="background-color: #0f3460; color: #ffffff;">
                                <th style="padding: 12px;">Booking ID</th>
                                <th style="padding: 12px;">Name</th>
                                <th style="padding: 12px;">Email</th>
                                <th style="padding: 12px;">Phone</th>
                                <th style="padding: 12px;">Seats</th>
                                <th style="padding: 12px;">Amount</th>
                                <th style="padding: 12px;">Payment</th>
                                <th style="padding: 12px;">Profile</th>
                            </tr>
                        </thead>
                        <tbody>
                            {modal_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        """

    print("""
                </tbody>
            </table>
        </div>
    """)
    print(modal_html)

print("""
    </div>
</div>
""")


querys = """select * from seekda where SNo='%s' """%(cid)
cur.execute(querys)
res = cur.fetchall()
for t in res:
    print(f"""  
     <div id="postRides" class="section">
           <h2 style="font-size: 2.2rem; font-weight: bold; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); align-items: center; justify-content: center; text-align: center;">
        🚗 Post a Ride
    </h2>
    <p style="font-size: 1.2rem; margin-top: 10px; font-weight: 500; color: #ffcc00; align-items: center; justify-content: center; text-align: center;">
        Share your ride details and find passengers easily.
    </p>
            <div class="container-fluid">
                <div class="row booking-container">
                    <div class="col-lg-5 d-flex align-items-center justify-content-center bg-light">
                        <div class="booking-form-container">
                            <h3 class="text-center"><i class="fa-solid fa-car"></i> Post a Ride</h3>
                      <form id="bookingForm" method="POST"  enctype="multipart/form-data">
                      <input type="hidden" name="Sno" value="%s"> 
                      <input type="hidden" name="names" value="{t[1]} {t[2]}"> 
                      <input type="hidden" name="emails" value="{t[3]}">  
                      <input type="hidden" name="profile" value="{t[10]}">
                      <input type="hidden" name="phones" value="{t[4]}">  
                      <input type="hidden" name="genders" value="{t[20]}"> 
                      <input type="hidden" name="vehimgs" value="{t[23]}">  
                      <input type="hidden" name="vehnum" value="{t[16]}">
                      <input type="hidden" name="vehicleType" value="Car">
                                <div class="mb-3">
                                    <label class="form-label"><i class="fa-solid fa-location-dot"></i> From</label>
                                    <input type="text" class="form-control" name="fromLocation" id="fromLocation"
                                        placeholder="Enter pickup location" required>
                                </div>
                                <div class="mb-3">
                                    <label class="form-label"><i class="fa-solid fa-map-marker-alt"></i> To</label>
                                    <input type="text" class="form-control" name="toLocation" id="toLocation"
                                        placeholder="Enter drop location" required>
                                </div>
                                <div class="mb-3">
                                    <label class="form-label"><i class="fa-regular fa-calendar"></i> Select Date & Time</label>
                                    <input type="datetime-local" class="form-control" name="rideTime" id="rideTime" required>

                                </div>
                                <div class="mb-3" id="passengerContainer">
                                    <label class="form-label"><i class="fa-solid fa-users"></i> Number of Passengers</label>
                                    <select class="form-select" name="passengerCount" id="passengerCount">
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                    </select>
                                </div>
                                <div class="mb-3">
                                    <label class="form-label"><i class="fa-solid fa-tag"></i> Price per Seat (&#8377;)</label>
                                    <input type="number" class="form-control" name="pricePerSeat" id="pricePerSeat" placeholder="Enter price" min="0" required>
                                </div> 
                               <input type="submit" name="submitsr" class="btn btn-primary w-100" value="🚗 Post Ride">
                      </form>
                        </div>
                    </div>
                    <div class="col-lg-7">
                        <div class="row image-container">
                            <div class="col-6 image-box" style="background-image: url('./img/3644592.jpg');"></div>
                        </div>  
                    </div>
                </div>
            </div>
     </div>
    """ % (cid))

sno = form.getvalue("Sno")
names = form.getvalue("names")
emails = form.getvalue("emails")
profile = form.getvalue("profile")
phones = form.getvalue("phones")
from_location = form.getvalue("fromLocation")
to_location = form.getvalue("toLocation")
ride_datetime = form.getvalue("rideTime")
vehicle_type = "Car"
passenger_count = form.getvalue("passengerCount")
price_per_seat = form.getvalue("pricePerSeat")
Genders = form.getvalue("genders")
Vehimgs = form.getvalue("vehimgs")
Vehnums = form.getvalue("vehnum")
submits = form.getvalue("submitsr")


if submits is not None:
    insert_query = """INSERT INTO rides (SNo, names, emails, phones, profile, pickup_location, dropoff_location, ride_datetime, vehicle_type, passenger_count, price_per_seat,Vehicleimg,VehicleNo,gender) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','Car','%s','%s','%s','%s','%s') """%(sno, names, emails, phones,profile, from_location, to_location, ride_datetime, passenger_count, price_per_seat,Vehimgs,Vehnums,Genders)
    cur.execute(insert_query)
    con.commit()
    print(f"""
          <script>
            alert("Ride Posted Successfully");
            window.location.href = "seekerdashboard.py?SNo={cid}&section=postRides";
          </script>
    """)


print("""
<div id="showRides" class="section hidden">
    <h2 style="color: #fff; background: linear-gradient(to right, #141e30, #243b55); padding: 15px; border-radius: 10px; text-align: center; font-weight: bold;">
        <i class="fa-solid fa-car-side" style="color: #ffffff;"></i> Your Posted Rides Status
    </h2>
    <div class="container">
        <div class="row justify-content-center">
            <div style="background: linear-gradient(to right, #1e3c72, #2a5298); padding: 30px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3); margin-top: 20px;">
                <div class="container mt-4">
                    <div style="background: #1c1c1c; padding: 25px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4); text-align: center;">
                        <h4 class="mb-4" style="font-weight: bold; color: #ffffff;">All Rides</h4>
                        <table class="table table-bordered" style="background: #2c2c2c; border-radius: 10px; overflow: hidden; color: #ffffff; text-align: center;">
                            <thead style="background: linear-gradient(to right, #8e2de2, #4a00e0); color: white;">
                                <tr style="text-align: center;">
                                    <th>SNO</th>
                                    <th>🚗 From</th>
                                    <th>📍 To</th>
                                    <th>📅 Ride Date & Time</th>
                                    <th>🧑‍👩 Passengers</th>
                                    <th>💵 Price/Seat</th>
                                    <th>📆 Posted On</th>
                                    <th>🎟️ Booked seat</th>
                                    <th>⚠️ Status</th>
                                    <th>🗑️ Ride</th>
                                </tr>
                            </thead>
                            <tbody style="text-align: center; font-size: 15px;">
""")

query = "SELECT * FROM rides WHERE SNo = %s AND is_deleted = 0"
cur.execute(query, (cid,))
res = cur.fetchall()

for idx, i in enumerate(res, start=1):
    ride_id = i[0]
    booked_seat = i[14]

    print(f"""<tr style="vertical-align: middle;">
        <td>{idx}</td>
        <td>{i[6]}</td>
        <td>{i[7]}</td>
        <td>{i[8]}</td>
        <td>{i[10]}</td>
        <td>{i[11]}</td>
        <td>{i[12]}</td>
        <td>{i[14]}</td>
        <td><span style="background-color: #28a745; color: white; padding: 5px 12px; border-radius: 20px;">{i[13]}</span></td>
        <td>""")

    if int(booked_seat) == 0:
        print(f"""
            <form method="post">
                <input type="hidden" name="delete_ride_id" value="{ride_id}">
                <input type="submit" name="deleteRide" value="Delete" 
                    class="btn btn-danger btn-sm" 
                    style="border-radius: 20px; font-weight: bold; padding: 5px 12px; transition: 0.3s;"
                    onmouseover="this.style.backgroundColor='#c82333';" 
                    onmouseout="this.style.backgroundColor='#dc3545';"
                    onclick="return confirm('Are you sure you want to delete this ride?');">
            </form>
        """)
    else:
        print("<span style='color: #bbbbbb; font-weight: bold;'>Can't Delete</span>")

    print("</td></tr>")

print("""
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""")


delete_ride_id = form.getvalue("delete_ride_id")
submit_delete = form.getvalue("deleteRide")

if submit_delete and delete_ride_id:
    # Debugging: Check values
    print(f"DEBUG: Received delete_ride_id={delete_ride_id}")

    # Fetch the booked seat count again before deleting
    cur.execute("SELECT bookedseat FROM rides WHERE ride_id = %s", (delete_ride_id,))
    data = cur.fetchone()

    if data:
        booked_seat_count = int(data[0])  # Convert to integer

        if booked_seat_count == 0:
            cur.execute("DELETE FROM rides WHERE ride_id = %s", (delete_ride_id,))
            con.commit()
            print(f"""
                <script>
                    alert("Ride deleted successfully!");
                    window.location.href = "seekerdashboard.py?SNo={cid}&section=showRides";
                </script>
            """)
        else:
            print(f"""
                <script>
                    alert("Cannot delete ride: seats are already booked!");
                </script>
            """)
    else:
        print(f"""
            <script>
                alert("Error: Ride not found!");
            </script>
        """)


print("""
  <div id="approveRides" class="section hidden" style="background: linear-gradient(to right, #f8f9fa, #e9ecef); padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
        <h2 style="color: #007bff; font-size: 24px; margin-bottom: 10px;"><i class="fas fa-clock"></i> Ride Requests</h2>
        <p style="font-size: 16px; color: #6c757d;">Manage ride bookings based on their current status.</p>
        <div class="container">
            <div class="row">
""")

query = """
    SELECT * FROM booking 
    WHERE seekerid = %s 
    AND status IN ('booked', 'pending', 'approved') 
    ORDER BY booking_id DESC
"""
cur.execute(query, (cid,))
bookings = cur.fetchall()

from collections import defaultdict
ride_groups = defaultdict(list)
for booking in bookings:
    ride_groups[booking[1]].append(booking)

for ride_id, ride_bookings in ride_groups.items():
    first_booking = ride_bookings[0]
    status = first_booking[17]
    booking_id = first_booking[0]

    if status == "pending":
        header = "Pending Ride Request"
        message = ""
    elif status == "approved":
        header = "Ride Approved - Waiting for Payment"
        message = "<div class='alert alert-info'>Ride approved and waiting for payment</div>"
    elif status == "booked":
        header = "Ride Booked"
        message = "<div class='alert alert-success'>Ride successfully booked. Payment received.</div>"

    modal_content = ""
    total_seats = 0
    total_price = 0
    for b in ride_bookings:
        total_seats += int(float(b[9]))
        total_price += int(float(b[9])) * int(float(b[10]))

        booked_seats = int(float(b[9]))
        price_per_seat = int(float(b[10]))
        payment_method = b[18]
        payment_status = b[19]
        booking_id_inner = b[0]
        is_approved = b[17] == "approved"

        customer_div_id = f"customerDiv_{booking_id_inner}"

        if payment_status.lower() in ["completed", "paid"]:
            action_buttons_html = "<button class='btn btn-secondary w-100 mt-2' disabled>Paid - Cannot Reject</button>"
        elif is_approved:
            action_buttons_html = f"""
                <div class='alert alert-success mt-2'>Ride Approved - Awaiting Payment</div>
                <form action="" method="POST" class="mt-2">
                    <input type="hidden" name="booking_id" value="{booking_id_inner}">
                    <input type="submit" class="btn btn-danger w-100" name="rejectRide" value="Reject Ride" onclick=\"document.getElementById('{customer_div_id}').style.display='none';\">
                </form>
            """
        else:
            action_buttons_html = f"""
                <form action="" method="POST" class="mt-2">
                    <input type="hidden" name="booking_id" value="{booking_id_inner}">
                    <input type="submit" class="btn btn-success w-100 mb-2" name="approveRide" value="Approve Ride">
                    <input type="submit" class="btn btn-danger w-100" name="rejectRide" value="Reject Ride" onclick=\"document.getElementById('{customer_div_id}').style.display='none';\">
                </form>
            """

        modal_content += f"""
        <div class='border p-2 rounded mb-3 text-center' id="{customer_div_id}">
            <img src='./images/{b[26]}' class='img-fluid rounded mb-2' alt='Customer Image' style='max-height: 150px; border: 2px solid #007bff; border-radius: 12px;'>
            <p><strong>Name:</strong> {b[13]}</p>
            <p><strong>Phone:</strong> {b[14]}</p>
            <p><strong>Email:</strong> {b[15]}</p>
            <p><strong>Address:</strong> {b[16]}</p>
            <p><strong>Booked Seats:</strong> {booked_seats}</p>
            <p><strong>Price per Seat:</strong> ₹{price_per_seat}</p>
            <p><strong>Total Price:</strong> ₹{booked_seats * price_per_seat}</p>
            <p><strong>Payment Status:</strong> {payment_status}</p>
            <p><strong>Payment Method:</strong> {payment_method}</p>
            {action_buttons_html}
        </div>
        """

    cancel_all_button = f"""
    <form method=\"POST\" class=\"mt-2\">
        <input type=\"hidden\" name=\"ride_id\" value=\"{ride_id}\">
        <input type=\"submit\" name=\"cancelAll\" value=\"Cancel All Pending Rides\" class=\"btn btn-warning w-100\">
    </form>
    """

    print(f"""
        <div class=\"col-md-4 col-sm-6 mb-4\">
            <div class=\"card\" style=\"border-radius: 15px; overflow: hidden; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2); transition: transform 0.4s ease-in-out; cursor: pointer;\" 
            onmouseover=\"this.style.transform='scale(1.05)'\" onmouseout=\"this.style.transform='scale(1)'\">
                <div class=\"card-header\" style=\"background: linear-gradient(to right, #f7b733, #fc4a1a); color: white; text-align: center; font-weight: bold;\">
                    {header}
                </div>
                <div class=\"card-body text-dark text-center\">
                    <h5 class=\"card-title\">Ride ID: {ride_id}</h5>
                    <p><strong>From:</strong> {first_booking[3]}</p>
                    <p><strong>To:</strong> {first_booking[4]}</p>
                    <p><strong>Ride Date:</strong> {first_booking[7]}</p>
                    <p><strong>Total Booked Seat:</strong> {total_seats}</p>
                    <p><strong>Total Price:</strong> ₹{total_price}</p>
                    <p><strong>Payment Status:</strong> {first_booking[19]}</p>
                    <p><strong>Payment Method:</strong> {first_booking[18]}</p>
                    {message}
                    <button type=\"button\" class=\"btn btn-primary w-90 mt-1 mb-2\" data-bs-toggle=\"modal\" data-bs-target=\"#customerDetailsModal{ride_id}\">
                        View Customer Details
                    </button>
                    {cancel_all_button}
                </div>
            </div>
        </div>

        <!-- Customer Details Modal -->
        <div class=\"modal fade\" id=\"customerDetailsModal{ride_id}\" tabindex=\"-1\" aria-labelledby=\"customerDetailsModalLabel\" aria-hidden=\"true\">
            <div class=\"modal-dialog\">
                <div class=\"modal-content\">
                    <div class=\"modal-header\">
                        <h5 class=\"modal-title\">Customer Details</h5>
                        <button type=\"button\" class=\"btn-close\" data-bs-dismiss=\"modal\" aria-label=\"Close\" style=\"filter: invert(1) brightness(1.5); opacity: 1;\"></button>
                    </div>
                    <div class=\"modal-body text-center\">
                        {modal_content}
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

# ---------- BACKEND LOGIC ----------
booking_id = form.getvalue("booking_id")
approveRide = form.getvalue("approveRide")
rejectRide = form.getvalue("rejectRide")
cancelAll = form.getvalue("cancelAll")
ride_id_input = form.getvalue("ride_id")

if approveRide:
    cur.execute("SELECT ride_id FROM booking WHERE booking_id = %s", (booking_id,))
    ride_id_result = cur.fetchone()
    if ride_id_result:
        ride_id = ride_id_result[0]
        cur.execute("UPDATE booking SET status = 'approved' WHERE booking_id = %s", (booking_id,))
        con.commit()

        cur.execute("SELECT email, custname, froms, tos, Emailseek, Phoneseek FROM booking WHERE booking_id = %s", (booking_id,))
        user = cur.fetchone()
        if user:
            email, custname, froms, tos, Emailseek, Phoneseek = user
            subject = "Your ride has been approved"
            body = f"""Hello {custname},\n\nYour ride from {froms} to {tos} has been approved.\nPlease proceed with the payment to confirm your booking.\n\nSharer Contact:\nEmail: {Emailseek}\nPhone: {Phoneseek}\n"""
            msg = f"Subject: {subject}\n\n{body}"

            try:
                fromadd = "officialvimal01@gmail.com"
                ppassword = "gokk ckjn jvin yvuq"
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(fromadd, ppassword)
                server.sendmail(fromadd, email, msg)
                server.quit()
            except Exception as e:
                print(f"<script>alert('Email error: {str(e)}');</script>")

        print(f"<script>window.location.href = 'seekerdashboard.py?SNo={cid}&section=approveRides';</script>")

elif rejectRide:
    cur.execute("SELECT passengers, ride_id, custname, email, froms, tos FROM booking WHERE booking_id = %s", (booking_id,))
    result = cur.fetchone()

    if result:
        seats_to_restore, ride_id, custname, custemail, froms, tos = result
        cur.execute("UPDATE booking SET status = 'rejected' WHERE booking_id = %s", (booking_id,))
        con.commit()
        cur.execute("UPDATE rides SET bookedseat = bookedseat - %s WHERE ride_id = %s", (seats_to_restore, ride_id))
        con.commit()

        subject = "Ride Rejected"
        body = f"Hello {custname},\n\nYour ride from {froms} to {tos} has been rejected by the sharer."
        msg = f"Subject: {subject}\n\n{body}"

        try:
            fromadd = "officialvimal01@gmail.com"
            ppassword = "gokk ckjn jvin yvuq"
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(fromadd, ppassword)
            server.sendmail(fromadd, custemail, msg)
            server.quit()
        except Exception as e:
            print(f"<script>alert('Email error: {str(e)}');</script>")

        print(f"<script>window.location.href = 'seekerdashboard.py?SNo={cid}&section=approveRides';</script>")

elif cancelAll:
    cur.execute("SELECT booking_id, passengers, email, custname, froms, tos FROM booking WHERE ride_id = %s AND status = 'pending'", (ride_id_input,))
    pending_bookings = cur.fetchall()

    for booking in pending_bookings:
        booking_id, passengers, email, custname, froms, tos = booking
        cur.execute("UPDATE booking SET status = 'rejected' WHERE booking_id = %s", (booking_id,))
        con.commit()
        cur.execute("UPDATE rides SET bookedseat = bookedseat - %s WHERE ride_id = %s", (passengers, ride_id_input))
        con.commit()

        subject = "Ride Rejected"
        body = f"Hello {custname},\n\nYour ride from {froms} to {tos} has been rejected by the sharer."
        msg = f"Subject: {subject}\n\n{body}"

        try:
            fromadd = "officialvimal01@gmail.com"
            ppassword = "gokk ckjn jvin yvuq"
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(fromadd, ppassword)
            server.sendmail(fromadd, email, msg)
            server.quit()
        except Exception as e:
            print(f"<script>alert('Email error: {str(e)}');</script>")

    print(f"<script>alert('All pending rides cancelled'); window.location.href = 'seekerdashboard.py?SNo={cid}&section=approveRides';</script>")


query = """select * from seekda where SNo='%s' """%(cid)
cur.execute(query)
res = cur.fetchall()
for j in res:
 print(f"""
<div id="profile" class="section hidden" style="background: linear-gradient(135deg, #ff9a9e, #fad0c4); padding: 20px; border-radius: 10px; color: #4a4e69;">
    <div class="profile-card" style="background: #ffdde1; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0,0,0,0.2);">
        <div class="profile-header" style="font-size: 24px; font-weight: bold; text-align: center; color: #2a2d43;"> 
            Profile Information
        </div>
        <p style="text-align: center; font-size: 16px; margin-top: 10px; color: #5d536b;">Keep your profile updated to enjoy seamless access to our services.</p>
        <div class="profile-img-container" style="text-align: center; margin-top: 15px;">
            <label for="profilePicUpload">
                <img id="profilePicPreview" src="./images/{j[10]}" class="profile-img" alt="Profile" style="border-radius: 50%; width: 100px; height: 100px; border: 3px solid #ff4081;">
                <button data-bs-toggle="modal" data-bs-target="#addressModallph{cid}" class="btn btn-sm edit-btn ms-2" style="background: #ff6f61; color: #2a2d43; border: none; padding: 5px 10px; border-radius: 5px;">Change</button>
            </label>
        </div>
        <table class="table table-bordered mt-3" style="background: #ffc3a0; color: #4a4e69; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0,0,0,0.1);">
            <tbody>
                <tr style="background: #ffb74d; color: #2a2d43; font-weight: bold;">
                    <th>Name</th>
                    <td>
                        <input type="text" class="form-control text-center fw-bold" id="userName" value="{j[1]} {j[2]}" readonly style="background: transparent; color: #2a2d43; border: none;">
                    </td>
                </tr>
                <tr>
                    <th>Email</th>
                    <td class="d-flex align-items-center">
                        <input type="email" class="form-control" id="addressModalll" value="{j[3]}" style="background: transparent; color: #2a2d43; border: none;">
                    </td>
                </tr>
                <tr style="background: #ff8a80;">
                    <th>Contact</th>
                    <td class="d-flex align-items-center">
                        <input type="text" class="form-control" id="userPhone" value="+91{j[4]}" readonly style="background: transparent; color: #2a2d43; border: none;">
                    </td>
                </tr>
                <tr>
                    <th>Password</th>
                    <td class="d-flex align-items-center">
                        <input type="text" class="form-control" id="userPhone" value="********" readonly style="background: transparent; color: #2a2d43; border: none;">
                        <button data-bs-toggle="modal" data-bs-target="#addressModallp{cid}" class="btn btn-sm edit-btn ms-2" style="background: #ff6f61; color: #2a2d43; border: none; padding: 5px 10px; border-radius: 5px;">Change</button>
                    </td>
                </tr>
                <tr style="background: #ffd54f;">
                    <th>Address</th>
                    <td class="d-flex align-items-center">
                        <input type="text" class="form-control" id="userAddress" value="{j[5]}" readonly style="background: transparent; color: #2a2d43; border: none;">
                        <button data-bs-toggle="modal" data-bs-target="#addressModal{cid}" class="btn btn-sm edit-btn ms-2" style="background: #ff6f61; color: #2a2d43; border: none; padding: 5px 10px; border-radius: 5px;">Change</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="text-center mt-3">
            <button data-bs-toggle="modal" data-bs-target="#vehicleInfoModal{cid}" class="btn btn-primary">Your Vehicle Information</button>
        </div>
    </div>
</div>
<div class="modal fade" id="vehicleInfoModal{cid}" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content" style="background:#1e1e2f; color:white; border-radius:15px; box-shadow:0px 4px 10px rgba(0,0,0,0.3);">
            <div class="modal-header" style="border-bottom:1px solid #444;">
                <h5 class="modal-title" style="color:#f8f9fa;">
                    <i class="fas fa-car"></i> Your Vehicle Information
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" style="filter: invert(1);"></button>
            </div>
            <div class="modal-body">
                <p><strong>Date of Birth:</strong> {j[9]}</p>
                <p><strong>State:</strong> {j[6]}</p>
                <p><strong>City:</strong> {j[7]}</p>
                <p><strong>Zipcode:</strong> {j[8]}</p>
                <p><strong>Occupation:</strong> {j[13]}</p>
                <p><strong>Driving License:</strong> {j[11]}</p>
                <p><strong>Vehicle RC Number:</strong> {j[12]}</p>
                <p><strong>Vehicle Type:</strong> {j[15]}</p>
                <p><strong>Aadhar No:</strong> {j[14]}</p>
                <p><strong>Vehicle No:</strong> {j[16]}</p>
                <div class="row mt-3">
                    <div class="col-md-4"><p><strong>Driving License:</strong></p><img src="./images/{j[24]}" class="img-thumbnail" alt="DL"></div>
                    <div class="col-md-4"><p><strong>Vehicle RC:</strong></p><img src="./images/{j[25]}" class="img-thumbnail" alt="RC"></div>
                    <div class="col-md-4"><p><strong>Aadhar Front:</strong></p><img src="./images/{j[21]}" class="img-thumbnail" alt="Aadhar Front"></div>
                </div>
                <div class="row mt-3">
                    <div class="col-md-4"><p><strong>Aadhar Back:</strong></p><img src="./images/{j[22]}" class="img-thumbnail" alt="Aadhar Back"></div>
                    <div class="col-md-4"><p><strong>Vehicle Image:</strong></p><img src="./images/{j[23]}" class="img-thumbnail" alt="Vehicle"></div>
                </div>
            </div>
            <div class="modal-footer" style="border-top:1px solid #444;">
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>

""")
print(f"""<!-- Change Modal -->
        <div class="modal fade" id="addressModal{cid}" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                    <form method="post">
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
                        <form method="post">
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
        </div>

   """)
print(f"""

        <div class="modal fade" id="addressModallp{cid}" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                        <form method="post">
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
        </div>

   """)
cid = form.getvalue("cid")
Address = form.getvalue("addressn")
Submit = form.getvalue("submitn")

if Submit != None:
    q = """UPDATE seekda SET City ='%s' WHERE SNo='%s'""" % (Address, cid)
    cur.execute(q)
    con.commit()
    print("""
       <script>
          alert("Address updated successfully")
          location.href="seekerdashboard.py?SNo=%s&section=profile";
       </script>
    """ % (cid))

cid = form.getvalue("cidd")
Phonen = form.getvalue("phonen")
Submitp = form.getvalue("submitp")

if Submitp != None:
    q = """UPDATE seekda SET Phone ='%s' WHERE  SNo='%s'""" % (Phonen, cid)
    cur.execute(q)
    con.commit()
    print("""
       <script>
          alert("Phone no updated successfully")
          location.href="seekerdashboard.py?SNo=%s&section=profile";
       </script>
    """ % (cid))

cid = form.getvalue("ciddd")
Emailn = form.getvalue("emailn")
Submite = form.getvalue("submite")

if Submite != None:
    q = """UPDATE seekda SET Email ='%s' WHERE  SNo='%s'""" % (Emailn, cid)
    cur.execute(q)
    con.commit()
    print("""
       <script>
          alert("Email updated successfully")
          location.href="seekerdashboard.py?SNo=%s&section=profile";
       </script>
    """ % (cid))

cid = form.getvalue("cidp")
Passn = form.getvalue("passnn")
Submitpa = form.getvalue("submitpass")

if Submitpa != None:
    q = """UPDATE seekda SET Password ='%s' WHERE  SNo='%s'""" % (Passn, cid)
    cur.execute(q)
    con.commit()
    print("""
       <script>
          alert("Password updated successfully")
          location.href="seekerdashboard.py?SNo=%s&section=profile";
       </script>
    """ % (cid))

cid = form.getvalue("cidph")
Submitpr = form.getvalue("submitpro")

if Submitpr != None:
    Imageu = form['photon']
    sn = os.path.basename(Imageu.filename)
    open("images/" + sn, "wb").write(Imageu.file.read())

    q = """UPDATE seekda SET profile ='%s' WHERE  SNo='%s'""" % (sn, cid)
    cur.execute(q)
    con.commit()
    print("""
       <script>
          alert("Profile updated successfully")
          location.href="seekerdashboard.py?SNo=%s&section=profile";
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
    function toggleSidebar() {
        document.querySelector('.sidebar').classList.toggle('show');
        document.querySelector('.sidebar-backdrop').classList.toggle('show');
    }

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
 <!-- post js -->
<script>
    document.getElementById("vehicleType").addEventListener("change", function () {
        var passengerContainer = document.getElementById("passengerContainer");
        if (this.value === "Bike") {
            passengerContainer.classList.add("hidden");
        } else {
            passengerContainer.classList.remove("hidden");
        }
    });
</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script

        
        <!-- Bootstrap JS, Popper.js, and jQuery -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
""")