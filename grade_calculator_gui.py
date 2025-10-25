# Simple Flask Grade Calculator (no functions)

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        s1 = float(request.form["s1"])
        s2 = float(request.form["s2"])
        s3 = float(request.form["s3"])

        total = s1 + s2 + s3
        average = total / 3

        if average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        result = f"""
        <h3>Results:</h3>
        Total: {total:.2f}<br>
        Average: {average:.2f}<br>
        Grade: {grade}
        """

    return f"""
    <html>
    <head><title>Simple Grade Calculator</title></head>
    <body style='font-family:Arial; margin:40px;'>
        <h2>Grade Calculator (3 Subjects)</h2>
        <form method='POST'>
            Subject 1: <input type='number' name='s1' required><br><br>
            Subject 2: <input type='number' name='s2' required><br><br>
            Subject 3: <input type='number' name='s3' required><br><br>
            <input type='submit' value='Calculate'>
        </form>
        {result}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
