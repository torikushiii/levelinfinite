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

To trigger a manual check-in, use the `-m` or `--manual` flag:
```sh
python main.py --manual
```

## Obtaining Cookie and User-Agent

To perform the check-in, you may need to provide your Cookie and User-Agent. Here’s how you can obtain them:

1. **Open your browser and navigate to the Level Infinite website** (make sure you're logged in).

2. **Open Developer Tools:**

   - **For Chrome:** Press Ctrl+Shift+I or F12.
   - **For Firefox:** Press Ctrl+Shift+I or F12.

3. **Go to the Network tab in the Developer Tools.**

4. **Find a request in the Network tab whose URL contains `GetUserTotalPoints`.** The full URL might be `https://api-pass.levelinfinite.com/api/rewards/proxy/lipass/Points/GetUserTotalPoints` or something similar. You might need to refresh the page or navigate around the Level Infinite website until you see a request with this URL prefix.

5. **Click on the request to view its details.**

6. **Copy the Cookie:**

   - Go to the Headers section.
   - Find the `Cookie` header.
   - Copy the value of the Cookie header.

7. **Copy the User-Agent:**

   - In the same Headers section.
   - Find the `User-Agent` header.
   - Copy the value of the User-Agent header.

8. **Configure the Script:**

   - Rename the `example.config.py` file to `config.py`.
   - Open `config.py` and paste your Cookie and User-Agent values into the appropriate variables:

     ```python
     COOKIE = 'your_cookie_here'
     USER_AGENT = 'your_user_agent_here'
     ```

     **Replace `'your_cookie_here'` and `'your_user_agent_here'` with the actual values you copied.**

Now you can run the script, and it will use your provided Cookie and User-Agent for the check-in process.

## File Structure

- `main.py`: The main script that handles scheduling and manual check-ins.
- `check_in.py`: A module containing the check-in logic.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under MIT License.