from flask import Flask, render_template, request
from random import randint, seed

import csv

# Configure application
app = Flask(__name__)


@app.route("/gen_en", methods=["GET", "POST"])
def setup():
    if request.method == "POST":
        # Obtain parameters from the setup form
        rows = int(request.form.get("rows"))
        columns = int(request.form.get("columns"))
        min = int(request.form.get("min"))
        max = int(request.form.get("max"))
        currency = request.form.get("currency")

        # Initalize the random number generator
        seed()

        # Check if the min and max submitted are valid
        if min > max:
            return render_template("setup.html", alert=True, rows=rows, columns=columns, min=min, max=max, currency=currency)

        # Adjust max and min values if currency is set to on
        if currency == "on":
            min = min + 2
            max = max + 2

        # Randomly generate a unique file name
        label = randint(0000, 99999)
        filename = "files/dataset_" + str(label) + ".csv"
        path = "static/" + filename

        file = open(path, 'w', newline='')
        number_w = csv.writer(file, delimiter=',')

        # Obtain a randomized numeric range for each row
        for row in range(rows):
            row_digits = randint(min, max)
            lowest = 10 ** (row_digits - 1)
            highest = 10 ** (row_digits) - 1
            numbers = []

            # Generate numbers
            for column in range(columns):
                number = randint(lowest, highest)

                if currency == "on":
                    number = number / 100

                # Write numbers in the file
                numbers.append(number)
            number_w.writerow(numbers)

        file.close()

        # Adjust max, min and currency values for display
        if currency == "on":
            min = min - 2
            max = max - 2

        return render_template("download.html", filename=filename, rows=rows, columns=columns, min=min, max=max, currency=currency)

    else:
        return render_template("setup.html")


@app.route("/heart")
def heart():
    return render_template("heart.html")


@app.route("/help")
def help():
    return render_template("help.html")
