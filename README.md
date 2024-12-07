# Complaint Classification - Amazon

This project automates the classification of complaints into predicted categories, and generating appropriate reply to give back to the user and uses X(formerly twitter) as a platform to interact with the user.

The main script, `main.py`, performs the following tasks:
1. **Login to X.com**: It logs in using provided credentials.
2. **Extract Complaints**: It fetches recent complaints from the user's mentions.
3. **Classify Complaints**: It classifies the complaint into predefined categories using a machine learning model.
4. **Generate Reply**: Based on the classification and labels, it generates an appropriate response.
5. **Post Reply**: The generated reply is posted as a response to the complaint.

## Dependencies

This project requires the following Python libraries:

- `selenium`: WebDriver to automate the browser for interaction with X.com.
- `webdriver-manager`: Helps manage the WebDriver (in this case, ChromeDriver) automatically.
- `pandas`: Used in the classification functions.
- `scikit-learn`: For machine learning model operations (specifically for loading the classifier `GBC_classifier.pkl`).
- `time`: For adding delays to mimic human interaction.
- `classify.py`: Contains the logic to classify complaints into categories (uses `GBC_classifier.pkl`).
- `check_labels.py`: Checks and updates complaint labels based on predefined categories.
- `reply.py`: Generates automated replies based on complaint classification.

You can install the required dependencies by running:

```bash
pip install selenium pandas scikit-learn webdriver-manager
```

Ensure that your Chrome browser version is compatible with the version of chromedriver being used by the `webdriver-manager`.

## Setup

Before running the script, ensure you have the following:

1. Create the necessary Python files:

  - `main.py`: The main script for automating the interaction.
  - `classify.py`: Contains the logic for classifying complaints into categories (uses GBC_classifier.pkl).
  - `reply.py`: Contains logic for generating a suitable reply to the complaint.

2. Set up your machine learning model:

   - Ensure that you have a valid classifier file named `GBC_classfier.pkl`. This file is loaded in `classify.py` to classify incoming complaints.

3. Set up the classifier:

   - Ensure that the classifer pickle (`.pkl`) file is in the same directory as `classify.py`.

## Usage

1. Clone or download the project files to your local machine.
2. Modify the credentials in `main.py` for login.
3. Ensure that `main.py`, 'classify.py', 'reply.py` are in the same directory.
4. Run the `main.py` script.

   ```bash
   python main.py
   ```
This will
- Log into **X.com**.
- Extract the recent complaint from mentions.
- Classify the complaint into categories.
- Generate a reply based on complaint's labels.
- Post the reply back to the user on **X.com**.

## Code Explanation

`main.py`

This script orchestrates the entire process, using Selenium to log in to X.com, interact with the web page, and handle complaints.

1. **Login Process:** Uses Selenium to input username, password, and handle multi-step login (email verification).

2. **Complaint Extraction:** Extracts the most recent complaint from the notifications page.

3. **Classification:** Calls `classify_into_categories()` from `classify.py` to classify the complaint using the pre-trained model.

4. **Generating Reply:** Uses `generate_reply()` from `reply.py` to generate a custom reply based on the complaint's classification and labels. 

5. **Reply Posting:** Posts the generated reply back to X.com using Selenium.

`classify.py`

The `classify.py` script is responsible for classifying new complaints into predefined categories using the `classify_into_categories()` function. The classification process involves utilizing a pre-trained machine learning model and multiple text processing techniques.

### Process Overview

1. **Pre-defined categories:**

    - A set of predefined categories is created based on clustering methods such as **LDA (Latent Dirichlet Allocation)**, **Topic Modeling**, and **K-Means clustering**, among other techniques like **NMF (Non-        negative Matrix Factorization)**.
  
    - These categories are derived after a comprehensive text analysis, including tokenization, dictionary creation, corpus construction, and transformations using **TF-IDF (Term Frequency-Inverse Document             Frequency)** to represent textual data numerically.
    
2. **New Complaint:**

   - When a new complaint is extracted (as seen in `main.py`), the complaint text is passed as input to the `classify_into_categories()` function for classification.

   - The complaint text typically consists of natural language data (e.g., complaints, feedback), which needs to be processed before classification.

3. **Text Preprocesing:**

    Before classification, the complaint undergoes a series of preprocessing steps:

    1. **Tokenization**: Breaking the complaint text into individual words (tokens).
    2. **Stopword Removal**: Eliminating common words (e.g., "the", "is") that do not contribute much to the meaning.
    3. **Vectorization**: Converting text into a numerical format (e.g., using **TF-IDF** or **Bag of Words**).
    4. **Lemmatization**: Reducing words to their base forms (e.g., "running" to "run").

   
4. **Model Loading:**

   - The pre-trained machine learning model `GBC_classifier.pkl` (which uses **Gradient Boosting Classifier**) is loaded using **joblib**.
   - This model has been trained on a labeled dataset of complaints, and it will predict which predefined category best fits the new complaint.

5. **Predicted Labels:**

   - The model predicts the labels for the new complaint and the predicted labels are returned back to `main.py`.

`reply.py`

The `reply.py` is responsible for generating a response for a complaint based on it's predicted categories.

1. **Sample response dictionary:**

   - A dictionary based on few samples for each label is defined in `generate_reply()` function.

2. **API Calling:**

   - The sample response dictionary and the labels along with the complaint and a prompt are sent to Gemini through an API call to get a contextual answer.

   - The response from the API is parsed and relevant response is sent back to `main.py`.

`GBC_classifier.pkl`

  - Classifier trained using **GBC(Gradient Bossting Classification)** from **sklearn**.

  - The model is trained on 4700 rows comprising of user complaints, complaint title and complaint date.

  - The dataset is made from extracting user complaints from various sources on the internet such as **X.com** (formerly twitter), **Amazon**, **flipkart**, **National Complaints Website** etc. and merged             together.

  - The model is saved using `joblib`.

## Notes

- **Error Handling:** 
  - Since automation is implemented using **Selenium** and relies on hardcoded elements such as classes and button clicks, continuous monitoring and maintenance are essential to ensure the code remains functional.
  - Any changes in X.com's (formerly Twitter) frontend code, such as class names, element IDs, or layout changes, may cause the automation to break. Regular checks and updates to the code are necessary to adapt to these changes.
  - Consider implementing additional **exception handling** mechanisms to catch common errors such as missing elements, timeouts, or unexpected page structures. This will improve the robustness and reliability of the automation process.
  
- **Maintainability:**
  - Given the reliance on web scraping techniques, it's important to ensure that the automation logic is modular and easily adjustable when changes in the X.com UI occur.
  - Using more generic or robust methods to locate elements (e.g., `XPath` with more general attributes) can reduce the impact of minor frontend changes.

- **Long-term Sustainability:**
  - Since web scraping and automation scripts are vulnerable to platform changes, it’s recommended to periodically review and update the automation to ensure that it remains aligned with the latest version of X.com’s interface.
  - Engage in **version control** and testing to quickly detect if something breaks due to changes in the target website.

## Contributing

Feel free to submit issues or pull requests if you find any bugs or would like to contribute enhancements.

## License

This project is open-source and available under the MIT License.
