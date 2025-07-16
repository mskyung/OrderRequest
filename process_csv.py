from bs4 import BeautifulSoup

# Load the original HTML file
with open("index 4.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Create form fields for Product_Name, Number, Unit_Price, and Sum
form_html = """
<h2>Product Entry Form</h2>
<form id="productForm">
  <label>Product Name: <input type="text" id="Product_Name" /></label><br />
  <label>Number: <input type="number" id="Number" /></label><br />
  <label>Unit Price: <input type="number" id="Unit_Price" /></label><br />
  <label>Sum: <input type="number" id="Sum" /></label><br />
</form>
<br />
<label>Upload CSV: <input type="file" id="csvFileInput" accept=".csv" /></label>
<p id="totalSumDisplay"><strong>Total Sum:</strong> <span id="totalSum">0</span></p>
"""

# JavaScript to handle CSV upload and populate form
script_html = """
<script>
document.getElementById('csvFileInput').addEventListener('change', function (e) {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (event) {
        const text = event.target.result;
        const rows = text.trim().split('\\n').map(row => row.split(','));

        if (rows.length < 2) return;

        // Fill the form with the first data row
        const headers = rows[0];
        const firstRow = rows[1];

        const headerMap = {};
        headers.forEach((h, i) => headerMap[h.trim()] = i);

        document.getElementById('Product_Name').value = firstRow[headerMap['Product_Name']];
        document.getElementById('Number').value = firstRow[headerMap['Number']];
        document.getElementById('Unit_Price').value = firstRow[headerMap['Unit_Price']];
        document.getElementById('Sum').value = firstRow[headerMap['Sum']];

        // Calculate total sum
        let total = 0;
        for (let i = 1; i < rows.length; i++) {
            const row = rows[i];
            const sumValue = parseFloat(row[headerMap['Sum']]);
            if (!isNaN(sumValue)) {
                total += sumValue;
            }
        }
        document.getElementById('totalSum').textContent = total.toLocaleString();
    };
    reader.readAsText(file);
});
</script>
"""

# Insert the form and script into the HTML
body = soup.body
if body:
    body.append(BeautifulSoup(form_html, "html.parser"))
    body.append(BeautifulSoup(script_html, "html.parser"))

# Save the modified HTML
with open("index_4_modified.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Modified HTML with CSV auto-fill and total sum calculation saved as 'index_4_modified.html'.")

