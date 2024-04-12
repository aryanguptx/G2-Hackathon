#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

#Add environment variable
export G2_API_TOKEN="Your Key"

# Install dependencies using pip
pip install -r requirements.txt
