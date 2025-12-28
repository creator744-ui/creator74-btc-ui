# Copilot Instructions for creator74-btc-ui

## Project Overview

This repository contains a FastAPI-based web application for Mergington High School's extracurricular activities management system. The application allows students to view and sign up for various activities through a simple web interface.

### Technology Stack

- **Backend**: Python with FastAPI framework
- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **Components**: React/TypeScript components (note: WalletCard.tsx appears to be example/legacy code for cryptocurrency balances, not currently integrated with the main application)
- **Server**: Uvicorn ASGI server

## Project Structure

```
.
├── src/
│   ├── app.py              # Main FastAPI application
│   ├── static/             # Static web assets
│   │   ├── index.html      # Main HTML page
│   │   ├── app.js          # Frontend JavaScript
│   │   └── styles.css      # Styling
│   ├── components/         # React/TypeScript components
│   │   └── WalletCard.tsx  # Wallet balance display component
│   └── README.md           # Project documentation
├── requirements.txt        # Python dependencies
└── .github/               # GitHub configuration and workflows
```

## Getting Started

### Installing Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install fastapi uvicorn
```

### Running the Application

```bash
cd src
uvicorn app:app --reload
```

The application will be available at:
- Main page: http://localhost:8000
- API documentation: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Redirects to main HTML page |
| GET | `/activities` | Get all activities with details and participants |
| POST | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity (Note: Currently does not validate duplicates or capacity limits) |

## Coding Guidelines

### Python Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable names
- Include docstrings for functions and classes
- The codebase uses simple, straightforward Python without excessive abstraction
- In-memory data storage is used (data resets on server restart)

### Data Models

- **Activities**: Use activity name as the primary identifier
  - Contains: description, schedule, max_participants, participants list
- **Students**: Use email as the identifier
  - Email format: `name@mergington.edu`

### Frontend Code

- Use vanilla JavaScript for static files
- Keep JavaScript simple and readable
- Use semantic HTML5 elements
- CSS should be organized and maintainable

### React Components

- Use TypeScript for React components
- Include JSDoc comments for component documentation
- Use functional components with React.FC type

## Important Conventions

1. **Data Persistence**: All data is stored in-memory in the `activities` dictionary. Changes are lost on server restart.

2. **Email Validation**: Student emails should follow the pattern `*@mergington.edu`

3. **Static Files**: Static assets are mounted at `/static` and served from `src/static/` directory

4. **Error Handling**: Use FastAPI's HTTPException for API errors with appropriate status codes

5. **Current Limitations**: 
   - The signup endpoint does not check if a student is already signed up for an activity (allows duplicates)
   - The signup endpoint does not enforce the `max_participants` limit
   - These are potential areas for improvement

## Testing

Currently, there is no formal test infrastructure in this repository. When adding tests:
- Consider using `pytest` for Python tests
- Test both API endpoints and business logic
- Mock external dependencies if needed

## Common Tasks

### Adding a New Activity

1. Add the activity to the `activities` dictionary in `src/app.py`
2. Follow the existing structure with description, schedule, max_participants, and participants list

### Adding a New Endpoint

1. Define the endpoint in `src/app.py` using FastAPI decorators
2. Update the README.md API endpoints table
3. Consider error handling for invalid inputs

### Modifying Frontend

1. Update HTML in `src/static/index.html`
2. Add JavaScript logic to `src/static/app.js`
3. Style changes go in `src/static/styles.css`
4. Ensure changes are compatible with the FastAPI static file serving

## Best Practices for Working on This Repository

### For Bug Fixes
- Identify the specific endpoint or function with the issue
- Make minimal changes to fix the problem
- Verify the fix doesn't break existing functionality

### For New Features
- Follow the existing code patterns and structure
- Keep the API simple and RESTful
- Update documentation (README.md) when adding new endpoints
- Consider backward compatibility

### For Refactoring
- Make incremental changes
- Preserve existing API contracts
- Test thoroughly after changes
- Update comments and docstrings as needed

## Security Considerations

- Always validate user input
- Use FastAPI's built-in request validation
- Sanitize email inputs to prevent injection attacks
- Be cautious with data that gets stored in the activities dictionary

## File Naming Conventions

- Python files: Use snake_case (e.g., `app.py`)
- React/TypeScript: Use PascalCase for component files (e.g., `WalletCard.tsx`)
- Static assets: Use lowercase with hyphens (e.g., `styles.css`)

## Dependencies Management

- All Python dependencies are listed in `requirements.txt`
- Keep the dependency list minimal and only add what's necessary
- Pin versions for production stability if needed

## Notes

- This is a learning/demonstration project focused on simplicity
- The application doesn't use a database; all data is ephemeral
- The codebase is intentionally simple to make it accessible for learning
