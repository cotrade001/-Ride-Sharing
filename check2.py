#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, sys

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Rides - RideShare</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
</head>
<body>

<div class="container">
    <h2 class="text-center mt-4">Search Rides</h2>
    <p class="text-center">Find available rides matching your route.</p>
    <div class="row justify-content-center">
        <div class="col-lg-8">
            <div class="card p-4 shadow">
                <h3 class="text-center">Search a Ride</h3>
                <form class="row g-2 align-items-center mx-auto" id="bookingForm" action="search.py" method="GET" enctype="multipart/form-data">
                    <div class="col-md-4 col-12">
                        <div class="input-group">
                            <span class="input-group-text"><i class="fa-solid fa-location-dot"></i></span>
                            <input type="text" class="form-control" name="fromLocation" id="fromLocation" placeholder="Enter Pickup Location"
                                required onkeyup="searchFromTo('fromLocation')">
                            <div id="fromLocationResults"></div>
                        </div>
                    </div>
                    <div class="col-md-4 col-12">
                        <div class="input-group">
                            <span class="input-group-text"><i class="fa-solid fa-map-marker-alt"></i></span>
                            <input type="text" class="form-control" name="toLocation" id="toLocation" placeholder="Enter Drop Location"
                                required onkeyup="searchFromTo('toLocation')">
                            <div id="toLocationResults"></div>
                        </div>
                    </div>
                    <div class="col-md-2 col-12">
                        <input type="submit" name="submitb" class="btn btn-primary w-100" value="Search">
                    </div>
                </form>
            </div>
        </div>
    </div>


    <!-- Display Search Results -->


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")
