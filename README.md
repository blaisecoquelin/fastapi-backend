# FastAPI Backend for AI Prompt Application

This is the backend for an AI Prompt Application, built with FastAPI. It handles API requests, manages user authentication, and communicates with the OpenAI API.

## Features
- FastAPI framework for high-performance backend
- OpenAI API integration
- User authentication and authorization
- CRUD operations for managing prompts
- CORS support for frontend integration
- Deployed on Render (or other cloud platforms)

## Tech Stack
- **Backend**: FastAPI
- **Deployment**: Render / Other cloud platforms

## Installation
### Prerequisites
- Python 3.9+
- Virtual environment (optional but recommended)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/blaisecoquelin/fastapi-backend.git
   cd fastapi-backend
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file and add:
     ```sh
     OPENAI_API_KEY=your_openai_api_key
   
     ```

## Running the Server
Start the FastAPI server with:
```sh
uvicorn main:app --reload
```
- The API will be available at: `http://127.0.0.1:8000`
- Interactive docs: `http://127.0.0.1:8000/docs`

## API Endpoints
| Method | Endpoint        | Description              |
|--------|----------------|---------------------------|
| GET    | /              | Health check              |
| POST   | /api/chat      | Enter your prompt         |


## Deployment
### Deploy on Render
1. Create a new service on Render.
2. Set the  `OPENAI_API_KEY`` in environment variables.
3. Deploy and monitor logs via Render dashboard.

## Contributing
1. Fork the repo and clone locally.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push the branch: `git push origin feature-name`
5. Open a Pull Request on GitHub.

## License
This project is licensed under the MIT License.

