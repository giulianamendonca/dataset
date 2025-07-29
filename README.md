# Dataset Generator
## Video Demo:  <URL>

## Description
This tool is designed to provide a simple yet flexible generation of random datasets.

### Backstory
Having worked in no-code data analysis throughout my career, as I decided to learn the programming tools used by “regular” data analysts I found myself facing a challenge: I needed realistic datasets I could use to practice, but existing online resources either required excessive customization or lacked the flexibility I required.

My intention is that this tool can be used by other data analysis and programming students who might have similar needs.

### Key Features
Generate datasets based on three dimensions:

* Number of sets
* Length of each set
* Number of digits in each number

The latter is given by three parameters: minimum/maximum digits and a "currency" switch, which adds two decimal points to the numbers.

## Requirements
* **Back-end**
  * This project is written in Python 3.11.

  * **Python Libraries:**
    * [Flask](https://flask.palletsprojects.com/en/3.0.x/) v.3.0.0
    * [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) v.3.1.2

  * **Python Standard Libraries:**
    * random
    * csv

* **Front-end**
  * HTML5
  * CSS3

  * **Style tools**
    * [Bootstrap](https://getbootstrap.com/) v.5.3

## File Structure
* **static/**
  * **files/** - Stores the .csv files created by the generator. See [back-end section](#back-end) for details.
  * **images/** - Images used in the HTML layouts.
  * **styles.css** - CSS override code for styling.

* **templates/**
  * **layout.html** - HTML file for the standard page layout (header/footer). The remaining template files modify the body of the pages.
  * **setup.html** - HTML file for the setup form.
  * **download.html** - HTML file displaying the download link.
  * **help.html** - HTML file for user support page.
  * **heart.html** - HTML file for an "Easter-egg" page.

* **Other files**
  * **app.py** - Back-end file.
  * **readme.md** - Documentation file.

## Usage
* **URL** - Web App available at [pythonanywhere.com](https://giulianamendonca.pythonanywhere.com/)

* **Pages**
  * **Set-up**
    * By default, the page renders the `setup.html` template when accessing the home page via URL or by clicking the page title on the navbar. The set-up form allows the user to submit the parameters that will be used for dataset generation:
      * Number of sets
      * Length of each set
      * Minimum and maximum digits
      * Currency conversion switch

  * **Download**
    * The `download.html` template is rendered after the user has successfully submitted the set-up form. It displays an overview of the parameters, followed by a download link for the `.csv` file containing the dataset and a "go back" button that links back to the set-up form.

  * **Help**
    * The `help.html` template has instructions for correctly filling the set-up form. Access it through a link labelled "Help" on the right side of the navbar.
    * Link to the help page: [help](https://giulianamendonca.pythonanywhere.com/help)

## Back-end
* **File**: The back-end code is available in the `app.py` file.

* **Step 1**: Obtaining the variables
  * The first step consists in translating the parameters from the set-up form into variables that can be used by the Python program:
    * Number of sets = `rows`
    * Length of each set = `columns`
    * Minimum digits = `min`
    * Maximum digits = `max`
    * Currency conversion = `currency`

  * The program then checks if the `min` and `max` values are valid (i.e., if the maximum number of digits is at least equal to the minimum.)
    * This checkpoint triggers a set-up form reload if the submitted values aren't valid. In this case, the `render_template` function submits an `alert=True` parameter to the `setup.html` template, triggering the display of the alert message:
    ``` html
    {% if alert %}
    <div class="alert" role="alert" id="alert">
        <div style="font-weight: bold">Attention: </div>
        Please check min and max values.
    </div>
    {% endif %}
    ```

  * If `currency` is set to on, two extra digits are added to the user-submitted `min` and `max` values:
    ``` python
    if currency == "on":
      min = min + 2
      max = max + 2
    ```

* **Step 2**: Creating the `.csv` file
  * A randomized numerical suffix is added to the structure `files/dataset_(number).csv`, creating a unique file name for the current run.
    * The `download.html` template receives this file name, allowing the display of the correct download link once generation is complete.

  * The file is created in the `static/files/` folder. I opted to add `files/` to the filename to avoid problems with the download link I encountered when using Flask's `url_for` with the full path.

* **Step 3**: Number generation
  * The number generation itself is comprised of two nested for loops:
    * *For each row*, the program picks a random number between `min` and `max` values. This is then used to determine the range for the values in the row:
    ``` python
    row_digits = randint(min, max)
    lowest = 10 ** (row_digits - 1)
    highest = 10 ** (row_digits) - 1
    ```
      * *For each column*, the program selects a random integer from the range defined above. If the currency conversion is enabled, the number is then divided by 100 before proceeding.
    * Each row stores the numbers in its columns in a `numbers` list. Once the program has iterated over all the columns, the list is added as a new row to the `.csv` file:
    ``` python
      # For each column
      numbers.append(number)
    # For each row
    number_w.writerow(numbers)
    ```

* **Step 4**: Rendering `download.html` template
  * The `download.html` template receives the variables obtained from the first step, so they can be displayed for user review before download.
    * If currency conversion is set to on, `min` and `max` are reverted back to their user-submitted values before template rendering.
  ``` python
  return render_template("download.html", filename=filename, rows=rows, columns=columns, min=min, max=max, currency=currency)
  ```

## Known Issues
* As of V1, there's no "self-destruct" script in place for the `static/files/` folder. Manual deletion is possible, and a fix is a top priority.

## Next features
Possible features for next versions:
* **Automatic file deletion**

* **User login**
  * **Favourite settings**
    * This feature would allow users to save favourite parameters, allowing them to skip the set-up form for recurring scenarios.
  * **Saved sets**
    * I'm studying the feasibility (and usefulness) of developing a tool for recreating previously generated sets.

  * **Translations**
    * I might create a Portuguese (Brazil) translation for this web app. I'm also open to collaboration for other languages. 

## Credits and Acknowledgements
* This web app was created as a final project for HarvardX's CS50 course. For more information, see [their website](https://cs50.harvard.edu/x/2024/).

* Navbar icon: Spreadsheet by Zach Bogart from [The Noun Project](https://thenounproject.com/search/icons/?q=spreadsheet)

## Contact Information
I'm always open to new ideas and feedback. Feel free to contact me at:
* **Email:** giulianamendonca@outlook.com
* **GitHub:** [giulianamendonca](https://github.com/giulianamendonca)
