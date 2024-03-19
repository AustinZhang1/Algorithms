---
comments: False
layout: base
title: I am under the watha
permalink: /house-price
---
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
      background-color: #f0f0f0;
      background-image: url('https://www.transparentpng.com/thumb/clouds/cloud-clipart-kawaii-background-transparent.png');
      background-repeat: repeat;
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
    select {
      padding: 8px;
      border-radius: 5px;
      border: 1px solid #ccc;
      width: calc(100% - 18px);
    }
    input[type="text"] {
      padding: 8px;
      border-radius: 5px;
      border: 1px solid #ccc;
      width: calc(100% - 18px);
    }
    button {
      padding: 10px 20px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
<body>
  <div class="container">
    <h1>Welcome to Property Search</h1>
    <form id="property-form">
      <div class="form-group">
        <label for="area">Area (Integer):</label>
        <input type="number" id="area" name="area" required>
      </div>
      <div class="form-group">
        <label for="bedrooms">Bedrooms (Integer):</label>
        <input type="number" id="bedrooms" name="bedrooms" required>
      </div>
      <div class="form-group">
        <label for="bathrooms">Bathrooms (Integer):</label>
        <input type="number" id="bathrooms" name="bathrooms" required>
      </div>
      <div class="form-group">
        <label for="stories">Stories (Integer):</label>
        <input type="number" id="stories" name="stories" required>
      </div>
      <div class="form-group">
        <label for="main-road">Main Road (Yes/No):</label>
        <select id="main-road" name="main-road" required>
          <option value="1">Yes</option>
          <option value="0">No</option>
        </select>
      </div>
      <div class="form-group">
        <label for="guest-room">Guest Room (Yes/No):</label>
        <select id="guest-room" name="guest-room" required>
          <option value="1">Yes</option>
          <option value="0">No</option>
        </select>
      </div>
      <div class="form-group">
        <label for="basement">Basement (Yes/No):</label>
        <select id="basement" name="basement" required>
          <option value="1">Yes</option>
          <option value="0">No</option>
        </select>
      </div>
      <div class="form-group">
        <label for="hot-water-heating">Hot Water Heating (Yes/No):</label>
        <select id="hot-water-heating" name="hot-water-heating" required>
          <option value="1">Yes</option>
          <option value="0">No</option>
        </select>
      </div>
      <div class="form-group">
        <label for="airconditioning">Air Conditioning (Yes/No):</label>
        <select id="airconditioning" name="airconditioning" required>
          <option value="1">Yes</option>
          <option value="0">No</option>
        </select>
      </div>
      <div class="form-group">
        <label for="parking">Parking (Yes/No):</label>
        <select id="parking" name="parking" required>
          <option value="1">Yes</option>
          <option value="0">No</option>
        </select>
      </div>
      <div class="form-group">
        <label for="pref-area">Preferred Area (Yes/No):</label>
        <select id="pref-area" name="pref-area" required>
          <option value="1">Yes</option>
          <option value="0">No</option>
        </select>
      </div>
      <div class="form-group">
        <label for="furnishing-status">Furnishing Status (Yes/No):</label>
        <select id="furnishing-status" name="furnishing-status" required>
          <option value="1">Yes</option>
          <option value="0">No</option>
        </select>
      </div>
      <button type="button" onclick="submitForm()">Search</button>
    </form>
  </div>
    <div>
        <button class="buttontest">Test</button>
    </div>

  <script>
    function submitForm() {
      const formData = {
        area: document.getElementById('area').value,
        bedrooms: document.getElementById('bedrooms').value,
        bathrooms: document.getElementById('bathrooms').value,
        stories: document.getElementById('stories').value,
        mainroad: document.getElementById('main-road').value === '1' ? 'yes' : 'no',
        guestroom: document.getElementById('guest-room').value === '1' ? 'yes' : 'no',
        basement: document.getElementById('basement').value === '1' ? 'yes' : 'no',
        hotwaterheating: document.getElementById('hot-water-heating').value === '1' ? 'yes' : 'no',
        airconditioning: document.getElementById('airconditioning').value === '1' ? 'yes' : 'no',
        parking: document.getElementById('parking').value,
        prefarea: document.getElementById('pref-area').value === '1' ? 'yes' : 'no',
        furnishingstatus: document.getElementById('furnishing-status').value === '1' ? 'furnished' : 'unfurnished'
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
