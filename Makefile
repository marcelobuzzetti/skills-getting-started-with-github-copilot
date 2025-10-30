.PHONY: test test-cov install-dev clean lint format

# Install dependencies
install:
	pip install -r requirements.txt

# Install development dependencies
install-dev:
	pip install -r requirements.txt
	pip install black flake8 isort

# Run tests
test:
	python -m pytest tests/ -v

# Run tests with coverage
test-cov:
	python -m pytest tests/ --cov=src --cov-report=term-missing --cov-report=html

# Run tests with coverage and open HTML report
test-cov-open: test-cov
	python -c "import webbrowser; webbrowser.open('htmlcov/index.html')"

# Lint code
lint:
	flake8 src tests
	black --check src tests
	isort --check-only src tests

# Format code
format:
	black src tests
	isort src tests

# Clean up generated files
clean:
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Run the FastAPI server
serve:
	cd src && python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload

# Run the FastAPI server in production mode
serve-prod:
	cd src && python -m uvicorn app:app --host 0.0.0.0 --port 8000

# Help
help:
	@echo "Available commands:"
	@echo "  install      - Install dependencies"
	@echo "  install-dev  - Install development dependencies"
	@echo "  test         - Run tests"
	@echo "  test-cov     - Run tests with coverage"
	@echo "  test-cov-open - Run tests with coverage and open HTML report"
	@echo "  lint         - Lint code"
	@echo "  format       - Format code"
	@echo "  clean        - Clean up generated files"
	@echo "  serve        - Run FastAPI server in development mode"
	@echo "  serve-prod   - Run FastAPI server in production mode"
	@echo "  help         - Show this help message"