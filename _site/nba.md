<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NBA Data Table</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>NBA Data</h1>
    <table id="nbaTable">
        <thead>
            <tr>
                <th>Player Name</th>
                <th>Points</th>
            </tr>
        </thead>
        <tbody id="tableBody">
        </tbody>
    </table>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            fetch('http://127.0.0.1:8086/nba')
                .then(response => response.json())
                .then(data => generateTable(data))
                .catch(error => console.error('Error fetching data:', error));
        });

        function generateTable(data) {
            const tableBody = document.getElementById('tableBody');

            // Check if data is an array and contains subarrays
            if (!Array.isArray(data) || data.length === 0 || !Array.isArray(data[0])) {
                console.error('Invalid data format. Data should be a 2D array.');
                return;
            }

            // Generate table rows
            data.forEach(row => {
                if (Array.isArray(row) && row.length === 2) {
                    const tr = document.createElement('tr');

                    const tdPlayerName = document.createElement('td');
                    tdPlayerName.textContent = row[0];
                    tr.appendChild(tdPlayerName);

                    const tdPoints = document.createElement('td');
                    tdPoints.textContent = row[1];
                    tr.appendChild(tdPoints);

                    tableBody.appendChild(tr);
                } else {
                    console.error('Invalid row format. Each row should be an array with 2 elements.');
                }
            });
        }
    </script>
</body>
</html>
