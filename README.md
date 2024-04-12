# Product Review Analysis

This project aims to analyze customer reviews for products and services from G2, a popular software review platform. The primary goal is to extract the exact feature sets that customers are looking for, such as application performance, user experience, missing functionality, bugs, and more.

## Overview

The project utilizes the G2 API to fetch reviews for a particular product. It then employs a keyword extraction model from Hugging Face (`ml6team/keyphrase-extraction-distilbert-inspec`) to extract keywords from each review. The extracted keywords are then used as a corpus to calculate TF-IDF scores, which help determine the importance of various keywords and identify the most sought-after feature sets.

## Repository Structure

- `utilities/`
  - `KeyPhraseExtract.py`: Contains the code for keyword extraction using the Hugging Face model.
  - `g2ApiResponse.json`: Sample JSON response from the G2 API.
  - `g2ApiResponse.py`: Code for handling the API response and data processing.
  - `tf_idf.py`: Implementation of the TF-IDF algorithm for keyword importance calculation.
- `client.py`: The main entry point of the application, orchestrating the various utilities.
- `requirements.txt`: List of required Python packages and dependencies.
- `setup.sh`: A bash script for setting up the project environment and installing dependencies.

## Getting Started

1. **Clone the Repository**: Clone the repository to your local machine.

```
   $ git clone https://github.com/yourusername/your-repository.git
   $ cd your-repository
```

## Set Up the Environment

Run the `setup.sh` script to create a virtual environment, activate it, and install the required dependencies.
Before running setup.sh, replace "Your Key" with your G@ API key.

```
$ chmod +x setup.sh
$ ./setup.sh
```

## Run the Application

Once the setup is complete, execute the `client.py` script to analyze the reviews and extract the feature sets:

``` 
$ python client.py
```

The extracted feature sets and their importance scores will be printed to the console.

## Acknowledgments

- Hugging Face for the keyword extraction model (`ml6team/keyphrase-extraction-distilbert-inspec`).
- G2.com for providing the review data and API access.
