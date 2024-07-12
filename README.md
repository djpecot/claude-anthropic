# Project Initialization Guide

## Setting Up the Virtual Environment

To initialize the project with a virtual environment using `venv`, follow these steps:

1. **Create a Virtual Environment**:

```
bash
python3 -m venv venv
```

2. **Activate the Virtual Environment**:

- On macOS and Linux:

`source venv/bin/activate`

- On Windows:

`.\venv\Scripts\activate`

3. **Install the Required Packages**:
   Make sure you have a `requirements.txt` file in your project directory. Then run:

`pip install -r requirements.txt`

## Adding API Key to Secrets

To add an API key to your secrets, follow these steps:

1. **Create a `.streamlit` Directory**:

If it doesn't already exist, create a `.streamlit` directory in your project root:

`mkdir .streamlit`

2. **Create a `secrets.toml` File**:
   Inside the `.streamlit` directory, create a file named `secrets.toml`.

3. **Add Your API Key**:
   Open the `secrets.toml` file and add your API key in the following format:

`your_api_service="your_api_key_here"`

By following these steps, you will have successfully set up your project with a virtual environment and securely added your API key to the secrets.
