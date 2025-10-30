# Test Coverage Report

## Summary
- **Total Tests**: 14
- **Passing Tests**: 14 (100%)
- **Failed Tests**: 0 (0%)
- **Code Coverage**: 100%

## Test Structure

### Basic Endpoints Tests (`test_basic_endpoints.py`)
- ✅ Root endpoint redirects to static HTML
- ✅ GET /activities returns all activities 
- ✅ Activities have correct structure

### Signup Tests (`test_signup.py`)
- ✅ Successful signup for an activity
- ✅ Duplicate user signup fails appropriately
- ✅ Signup for nonexistent activity fails
- ✅ Signup when activity is full fails
- ✅ URL encoding handles special characters

### Unregister Tests (`test_unregister.py`)
- ✅ Successful unregistration from an activity
- ✅ Unregistering non-registered user fails appropriately
- ✅ Unregistering from nonexistent activity fails
- ✅ Unregistering existing participant works
- ✅ Complete signup and unregister workflow
- ✅ URL encoding handles special characters

## API Endpoints Tested

| Endpoint | Method | Test Coverage |
|----------|--------|---------------|
| `/` | GET | ✅ Tested |
| `/activities` | GET | ✅ Tested |
| `/activities/{name}/signup` | POST | ✅ Tested |
| `/activities/{name}/unregister` | DELETE | ✅ Tested |

## Test Features

- **Isolation**: Each test runs with a fresh copy of the activities data
- **Edge Cases**: Tests cover error conditions, invalid inputs, and boundary conditions
- **URL Encoding**: Tests handle special characters in activity names and emails
- **Workflows**: Tests cover complete user workflows (signup → unregister)
- **Error Handling**: Tests verify appropriate HTTP status codes and error messages

## Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=src --cov-report=term-missing

# Run specific test file
python -m pytest tests/test_signup.py -v
```