# Daily Check-In Script

This repository contains a script for performing daily check-ins. The script can be run automatically at a scheduled time or manually using a command-line flag.

## Features

- **Automatic Daily Check-In**: The script is scheduled to run a check-in at 09:00 AM every day.
- **Manual Check-In**: You can trigger a manual check-in using a command-line flag.

## Requirements

- Python 3.x
- `schedule` module (specified in `requirements.txt`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/torikushiii/levelinfinite
    cd levelinfinite
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Automatic Check-In

To start the script with automatic daily check-ins, simply run:
```sh
python main.py
```

### Manual Check-In

To trigger a manual check-in, use the `--manual` flag:
```sh
python main.py --manual
```

## File Structure

- `main.py`: The main script that handles scheduling and manual check-ins.
- `check_in.py`: A module containing the check-in logic.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under MIT License.