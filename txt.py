print(f"""
   <div id="bookedRides" class="section hidden">
    <h2><i class="fas fa-search"></i>  Search Rides</h2>
    <p>Search Your rides.</p>

    <div class="container-fluid">
        <div class="row booking-container">
            <div class="col-lg-10 d-flex align-items-center justify-content-center bg-light">
                <div class="booking-form-container">
                    <h3 class="text-center"><i class="fa-solid fa-car"></i> Search a Ride</h3>

                    <form id="bookingForm" method ="post" enctype="multipart/form-data">
                        <!-- From Location -->
                        <div class="mb-3">
                            <label class="form-label"><i class="fa-solid fa-location-dot"></i> From</label>
                            <input type="text" class="form-control" name="fromLocation" id="fromLocation" placeholder="Enter pickup location" required onkeyup="searchFromTo('fromLocation')">
                            <div id="fromLocationResults"></div>
                        </div>

                        <!-- To Location -->
                        <div class="mb-3">
                            <label class="form-label"><i class="fa-solid fa-map-marker-alt"></i> To</label>
                            <input type="text" class="form-control" name="toLocation" id="toLocation" placeholder="Enter drop location" required onkeyup="searchFromTo('toLocation')">
                            <div id="toLocationResults"></div>
                        </div>

                        <!-- Book Now Button -->
                        <input type="submit" name="submitb" class="btn btn-primary w-100" value="🚗 Search Here">
                    </form>
                </div>
            </div>
        </div>
    </div>

""")
# Fetch form data
search_queryf = form.getvalue("fromLocation")
search_queryt = form.getvalue("toLocation")
submit_button = form.getvalue("submitb")

# Initialize rides
rides = []

if submit_button:
    sql = "SELECT * FROM rides WHERE pickup_location = %s AND dropoff_location = %s AND status = %s"
    cur.execute(sql, (search_queryf, search_queryt, 'pending'))
    rides = cur.fetchall()

    if rides:
        print("""

        <div class="container">
            <div class="row">
        """)

        for ride in rides:
            print(f"""
                <div class="col-md-4 col-sm-6 mb-4">
                    <div class="card" style="border-radius: 15px; overflow: hidden; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2); transition: transform 0.4s ease-in-out; cursor: pointer;" 
                    onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">

                        <!-- Profile Image -->
                        <div style="width: 100%; height: 220px; background: linear-gradient(to right, #ff7e5f, #feb47b); display: flex; align-items: center; justify-content: center;">
                            <img src="./images/{ride[5]}" alt="Profile Image" style="width: 120px; height: 120px; border-radius: 50%; border: 4px solid white; object-fit: cover;">
                        </div>

                        <!-- Card Details -->
                        <div class="card-body text-white" style="background: linear-gradient(to right, #4b6cb7, #182848); text-align: center;">
                            <h5 class="card-title" style="margin: 10px 0; font-size: 22px; font-weight: bold;">{ride[2]}</h5>
                            <p class="card-text"><strong>From:</strong> {ride[6]}</p>
                            <p class="card-text"><strong>To:</strong> {ride[7]}</p>
                            <p class="card-text"><strong>Ride Date:</strong> {ride[8]}</p>
                            <p class="card-text"><strong>Vehicle:</strong> {ride[9]}</p>
                            <p class="card-text"><strong>Passengers:</strong> {ride[10]}</p>
                            <p class="card-text"><strong>Price/Seat:</strong> {ride[11]}</p>
                            <p class="card-text"><strong>Posted:</strong> {ride[12]}</p>

                            <form action="" method="POST">
                                <input type="hidden" name="ride_id" value="{ride[0]}">
                                <input type="hidden" name="from_location" value="{ride[6]}">
                                <input type="hidden" name="to_location" value="{ride[7]}">
                                <input type="hidden" name="ride_date" value="{ride[8]}">
                                <input type="hidden" name="vehicle" value="{ride[9]}">
                                <input type="hidden" name="passengers" value="{ride[10]}">
                                <input type="hidden" name="price_per_seat" value="{ride[11]}">
                                <input type="hidden" name="posted_date" value="{ride[12]}">

                                <input type="submit" class="btn book-ride-btn" name="submitss" value="Book Now" 
                                       style="margin-top: 10px; padding: 12px 24px; border-radius: 30px; background: white; 
                                              color: #182848; font-weight: bold; cursor: pointer; transition: background 0.3s, color 0.3s;"
                                       onmouseover="this.style.background='#feb47b'; this.style.color='white'"
                                       onmouseout="this.style.background='white'; this.style.color='#182848'">
                            </form>
                        </div>
                    </div>
                </div>
 """)

print("""
    </div> <!-- Closing row -->
""")

# Fetch customer details securely
cur.execute("SELECT cust_id, FirstName, Phone, address FROM userdata WHERE cust_id = %s", (cid,))
res = cur.fetchone()

if res:
    custid, Name, Phone, Address = res
else:
    print("<script>alert('Error: Customer not found!');</script>")
    exit()

# Fetch form data for booking
ride_id = form.getvalue("ride_id")
from_location = form.getvalue("from_location")
to_location = form.getvalue("to_location")
ride_date = form.getvalue("ride_date")
vehicle = form.getvalue("vehicle")
passengers = form.getvalue("passengers")
price_per_seat = form.getvalue("price_per_seat")
posted_date = form.getvalue("posted_date")
Submitbuy = form.getvalue("submitss")

# Ensure all required fields are provided before booking
if Submitbuy and all(
        [ride_id, from_location, to_location, ride_date, vehicle, passengers, price_per_seat, posted_date]):
    try:
        query = """INSERT INTO booking 
            (ride_id, froms, tos, ridedate, vehicle, passengers, priceperseat, posteddate, custid, custname, custphone, custaddress) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (
            ride_id, from_location, to_location, ride_date, vehicle, passengers, price_per_seat, posted_date,
            custid, Name, Phone, Address
        )
        cur.execute(query, values)

        # Update ride status
        update_query = "UPDATE rides SET status = %s WHERE ride_id = %s"
        cur.execute(update_query, ('booked', ride_id))

        con.commit()

        print("<script>alert('Booked successfully');</script>")

    except Exception as e:
        con.rollback()
        print(f"<script>alert('Error: {str(e)}');</script>")
