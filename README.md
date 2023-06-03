# Simple ChatGPT App

This project is a simple ChatGPT-like application that uses the OpenAI API to generate responses to user questions. It uses React for the frontend and Flask for the backend.

## Prerequisites

To run this project, you'll need:

- Node.js and npm (for the frontend)
- Python 3.6 or higher (for the backend)
- An OpenAI API key

You can sign up for an API key from [OpenAI](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key).

## Setup Instructions

### Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/your-username/simple-chatgpt.git
```

Navigate to the project directory:

```bash
cd simple-chatgpt
```

### Set Up the Backend

Navigate to the `backend` folder:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Edit the `.env` file located in `./backend` folder and replace the value that appears right after the equals sign with your key:

```
OPENAI_API_KEY=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

```

### Set Up the Frontend

Open a new terminal window and navigate to the `frontend` folder:

```bash
cd frontend
```

Install the required Node.js dependencies:

```bash
npm install
```

## Running the Application

### Start the Backend Server

From the `backend` folder, start the Flask server:

```bash
# Python version should be >= 3.0
python app.py
```

The backend server will be running at `http://127.0.0.1:5000`.

### Start the Frontend App

From the `frontend` folder, start the React development server:

```bash
npm start
```

Now you can visit `http://127.0.0.1:3000` in your browser and start using the Simple ChatGPT app!

## License

This project is licensed under the terms of the MIT license.
