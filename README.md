# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey marcelobuzzetti!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/marcelobuzzetti/skills-getting-started-with-github-copilot/issues/1)

## Mergington High School Activity Management System

This is a FastAPI-based web application for managing extracurricular activities at Mergington High School. Students can view available activities and sign up for them.

### Features

- View all available activities with details
- Sign up for activities 
- Unregister from activities (with delete button UI)
- Real-time participant count and availability
- Responsive web interface

### API Endpoints

- `GET /` - Redirects to the main application
- `GET /activities` - Get all activities
- `POST /activities/{activity_name}/signup` - Sign up for an activity
- `DELETE /activities/{activity_name}/unregister` - Unregister from an activity

### Testing

This project includes comprehensive test coverage using pytest:

- **14 tests** covering all endpoints and functionality
- **100% code coverage** 
- Tests for success cases, error cases, and edge cases
- Automated data reset between tests for isolation

#### Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
python -m pytest tests/ -v

# Run tests with coverage
python -m pytest tests/ --cov=src --cov-report=term-missing

# Using make (if available)
make test
make test-cov
```

#### Test Structure

- `tests/test_basic_endpoints.py` - Basic API endpoint tests
- `tests/test_signup.py` - Activity signup functionality tests  
- `tests/test_unregister.py` - Activity unregistration functionality tests
- `tests/conftest.py` - Test configuration and fixtures

### Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server
cd src && python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload

# Or using make
make serve
```

The application will be available at http://localhost:8000

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

