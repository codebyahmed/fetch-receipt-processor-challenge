# Receipt Processor API by Ahmed Iqbal

A FastAPI web service for the Fetch Backend Challenge.

## Why I chose FastAPI

- Firstly, I have extensive experience with FastAPI. As you can see from my profile, most of my projects and work experience revolve around it.  
- **Automatic Validation**: Given that the challenge involves numerous validation checks, FastAPI provides a streamlined and efficient way to handle them.  
- **Auto-Generated Documentation**: I appreciate FastAPI's built-in Swagger documentation. You can explore it at `http://localhost:8000/docs`.


## Installation

1. Clone the repository:
```bash
git clone https://github.com/codebyahmed/fetch-receipt-processor-challenge.git
```

2. Change direcotry:
```bash
cd fetch-receipt-processor-challenge
```

3. Build the Docker image:
```bash
docker build -t ahmeds-receipt-processor .
```

4. Run the container:
```bash
docker run -p 8000:8000 ahmeds-receipt-processor
```

The API will be available at http://localhost:8000

## Usage

The docs which detail the usage for the API are available at http://localhost:8000/docs

## Project Structure

- app.py - Main application with API endpoints
- models.py - Data models and validation
- services.py - Business logic 