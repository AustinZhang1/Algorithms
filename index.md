---
comments: False
layout: default
title: I am under the watha
permalink: /house-price
---
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Property Search</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px; /* Added padding */
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh; /* Changed height to min-height */
      background-image: url('cherryblossom.gif'); /* Replace 'cherryblossom.gif' with the path to your GIF file */
      background-repeat: no-repeat;
      background-attachment: fixed; /* This ensures that the background image doesn't scroll with the content */
      background-size: cover; 
    }
    .container {
      max-width: 600px;
      width: 100%;
      text-align: center;
      background-color: rgba(255, 255, 255, 0.8);
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .form-group {
      margin-bottom: 20px;
      text-align: left;
    }
    label {
      display: block;
      margin-bottom: 5px;
    }
    input[type="number"],
    input[type="text"] {
      padding: 8px;
      border-radius: 5px;
      border: 1px solid #ccc;
      width: calc(100% - 18px);
    }
    button {
      padding: 8px;
      border-radius: 5px;
      border: 1px solid #ccc;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
    button.selected {
      background-color: #007bff;
      color: #fff;
    }
    button:hover {
      background-color: #0056b3;
    }
    .search {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(235, 100, 100, 1) !important;
        padding: 20px;
        border-radius: 10px;
        font-size: 30px;
        font-family: Verdana, sans-serif;
    }
    .area, .bedrooms, .bathrooms, .stories, .parking{
        position: fixed;
        text-align: left;
        left: 30%;
        transform: translate(-50%, -50%);
        background-color: rgba(55, 55, 55, 0.7);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        font-size: 20px;
        font-family: Verdana, sans-serif;
    }
    .area {
        top: 10%;
    }
    .bedrooms {
        top: 30%;
    }
    .bathrooms {
        top: 50%
    }
    .stories {
        top: 70%
    }
    .parking {
        top: 90%
    }
    .mainroad, .guestroom, .basement, .hotwater, .airconditioning, .prefarea, .furnishing {
        position: fixed;
        text-align: left;
        left: 70%;
        transform: translate(-50%, -50%);
        background-color: rgba(55, 55, 55, 0.7);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        font-size: 20px;
        font-family: Verdana, sans-serif;
    }
    .mainroad {
        top: 20%
    }
    .guestroom {
        top: 20%;
        left: 85%
    }
    .basement {
        top: 40%
    }
    .hotwater {
        top: 40%;
        left: 85%
    }
    .airconditioning {
        top: 60%
    }
    .prefarea {
        top: 60%;
        left: 85%
    }
    .furnishing {
        top: 80%;
    }
  </style>
</head>
<body>
    <div class="area">
      <label for="area">Area (Integer):</label>
      <input type="number" id="area" name="area" required>
    </div>
    <div class="bedrooms">
      <label for="bedrooms">Bedrooms (Integer):</label>
      <input type="number" id="bedrooms" name="bedrooms" required>
    </div>
    <div class="bathrooms">
      <label for="bathrooms">Bathrooms (Integer):</label>
      <input type="number" id="bathrooms" name="bathrooms" required>
    </div>
    <div class="stories">
      <label for="stories">Stories (Integer):</label>
      <input type="number" id="stories" name="stories" required>
    </div>
    <div class="parking">
      <label for="parking">Parking Spaces (Integer):</label>
      <input type="number" id="parking" name="parking" required>
    </div>
    <div class="mainroad">
      <label>Main Road:</label>
      <button id="main-road-yes" class="toggle-button" onclick="togglebutton('main')">No</button>
    </div>
    <div class="guestroom">
      <label>Guest Room:</label>
      <div id="guest-room-buttons" class="button-group">
        <button id="guest-room-yes" class="toggle-button" onclick="togglebutton('guest')">No</button>
      </div>
    </div>
    <div class="hotwater">
      <label>Hot Water:</label>
      <div id="hotwater-buttons" class="button-group">
        <button id="hotwater-yes" class="toggle-button" onclick="togglebutton('hotwater')">No</button>
      </div>
    </div>
    <div class="basement">
      <label>Basement:</label>
      <div id="basement-buttons" class="button-group">
        <button id="basement-yes" class="toggle-button" onclick="togglebutton('basement')">No</button>
      </div>
    </div>
    <div class="airconditioning">
    <label>Air Conditioning:</label>
    <div id="airconditioning-buttons" class="button-group">
        <button id="airconditioning-yes" class="toggle-button" onclick="togglebutton('airconditioning')">No</button>
    </div>
</div>
    <div class="prefarea">
        <label>Preferred Area:</label>
        <div id="prefarea-buttons" class="button-group">
            <button id="prefarea-yes" class="toggle-button" onclick="togglebutton('prefarea')">No</button>
        </div>
    </div>
    <div class="furnishing">
        <label>Furnishing Status:</label>
        <div id="furnishing-buttons" class="button-group">
            <button id="furnishing-yes" class="toggle-button" onclick="togglebutton('furnishing')">No</button>
        </div>
    </div>
    <button type="button" class="search" onclick="submitForm()">SEARCH</button>

  <script>
    var mainroad = false;guestroom = false;basement = false;hotwater = false;airconditioning = false; prefarea = false;furnishing = false;
    const toggleButtons = document.querySelectorAll('.toggle-button');

    toggleButtons.forEach(button => {
      button.addEventListener('click', function() {
        const siblingButton = this.id.includes('yes') ? this.nextElementSibling : this.previousElementSibling;
        this.classList.add('selected');
        siblingButton.classList.remove('selected');
      });
    });

    function togglebutton(buttonname) {
        if (buttonname === 'main') {
            mainroad = !mainroad;
            console.log(mainroad)
            if (mainroad == false) {
                document.getElementById("main-road-yes").innerText = "No"}
            else if (mainroad == true) {
                document.getElementById("main-road-yes").innerText = "Yes"
            }
        } else if (buttonname === 'guest') {
            guestroom = !guestroom;
            console.log(guestroom)
            if (guestroom == false) {
                document.getElementById("guest-room-yes").innerText = "No"}
            else if (guestroom == true) {
                document.getElementById("guest-room-yes").innerText = "Yes"
            }
        } else if (buttonname === 'basement') {
            basement = !basement;
            console.log(basement)
            if (basement == false) {
                document.getElementById("basement-yes").innerText = "No"}
            else if (basement == true) {
                document.getElementById("basement-yes").innerText = "Yes"
            }
        } else if (buttonname === 'hotwater') {
            hotwater = !hotwater;
            console.log(hotwater)
            if (hotwater == false) {
                document.getElementById("hotwater-yes").innerText = "No"}
            else if (hotwater == true) {
                document.getElementById("hotwater-yes").innerText = "Yes"
            }
        } else if (buttonname === 'airconditioning') {
            airconditioning = !airconditioning;
            console.log(airconditioning)
            if (airconditioning == false) {
                document.getElementById("airconditioning-yes").innerText = "No"}
            else if (airconditioning == true) {
                document.getElementById("airconditioning-yes").innerText = "Yes"
            }
        } else if (buttonname === 'prefarea') {
            prefarea = !prefarea;
            console.log(prefarea)
            if (prefarea == false) {
                document.getElementById("prefarea-yes").innerText = "No"}
            else if (prefarea == true) {
                document.getElementById("prefarea-yes").innerText = "Yes"
            }
        } else if (buttonname === 'furnishing') {
            furnishing = !furnishing;
            console.log(furnishing)
            if (furnishing == false) {
                document.getElementById("furnishing-yes").innerText = "No"}
            else if (furnishing == true) {
                document.getElementById("furnishing-yes").innerText = "Yes"
            }
        }
    }

    function submitForm() {
      const formData = {
        area: document.getElementById('area').value,
        bedrooms: document.getElementById('bedrooms').value,
        bathrooms: document.getElementById('bathrooms').value,
        stories: document.getElementById('stories').value,
        mainroad: mainroad === true ? 'yes' : 'no',
        guestroom: guestroom === true ? 'yes' : 'no',
        basement: basement === true ? 'yes' : 'no',
        hotwaterheating: hotwater === true ? 'yes' : 'no',
        airconditioning: airconditioning === true ? 'yes' : 'no',
        parking: document.getElementById('parking').value,
        prefarea: prefarea === true ? 'yes' : 'no',
        furnishingstatus: furnishing === true ? 'furnished' : 'unfurnished'
      };
      
      const jsonOutput = JSON.stringify(formData);
      console.log(jsonOutput);
      fetch("http://127.0.0.1:8086/house/", {
      method: "POST",
      body: jsonOutput,
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
      })
      .then(response => response.json())
      .then(data => {
            // Handle successful response here
            window.alert("The predicted price is: " + data);
            })
      
    
  console.log('OUR FRONTEND ACTUALLY WORKS????????????/')
      // You can do whatever you want with the JSON data here, for example, send it to a server.
    }
    
  </script>
</body>
</html>
