# Project README

## Overview
[GEN_AI Hello work project]

## Configuration
[Describe any configuration steps needed]

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b main`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
[Specify your license]

## Contact
[Add contact information or support details]
## Troubleshooting

### Common Issues
- **Port already in use**: If port 8000 is already in use, run `uvicorn main:app --reload --port 8000`
- **Module not found errors**: Ensure all dependencies from `requirements.txt` are installed with `pip install -r requirements.txt`
- **Virtual environment issues**: Create a fresh virtual environment with `python -m venv venv` and activate it before installing dependencies

## Local Development

### Quick Start
1. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the development server:
    ```bash
    uvicorn main:app --reload
    ```

4. Access the API at `http://localhost:8000`