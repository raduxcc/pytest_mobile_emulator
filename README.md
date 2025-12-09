# Light front-end test framework based on Selenium and Pytest

Tech stack:
- Selenium
- Pytest
- webdriver-manager: to auto-download and manage the correct ChromeDriver version
- Pytest-HTML: to auto-generate HTML test reports after each test run

It provides:
- Mobile emulation
- Utils for actions, validations, conditional waiting, etc
- Light POM architecture
- Basic step logs (stdout)
- HTML test report with embedded failure screenshots


## Project structure:

```
├── pages/
│   ├── base.py                   # BasePage with common methods, assertions, waits, and logging
│   ├── home.py                   # Home page object (search bar, browse button, etc.)
│   ├── search.py                 # Search page page object
│   ├── search_results.py         # Search results page object
│   └── streamer.py               # Streamer-specific page object
│
├── test_report/                  # Auto-generated after each test run
│   ├── assets/                   # Screenshots and other media captured during tests
│   └── report.html               # Pytest HTML report containing test run data and screenshots for failed scenarios
│
├── tests/
│   └── test_twitch_mobile_nav.py  # Test scenario for twitch.tv mobile navigation
│
├── utils/
│   └── driver_factory.py          # Driver setup
│
├── conftest.py                    # Pytest hooks and fixtures
└── pytest.ini                     # Pytest configuration
```

Running tests:
1) install dependencies:
>pip install -r requirements.txt
2) to run all tests:
>pytest


Test run:

[![fe-twitch-nav.gif](https://i.postimg.cc/xTWFLrzC/fe-twitch-nav.gif)](https://postimg.cc/rKNJLPgX)


Test report:

[![fe-test-report.gif](https://i.postimg.cc/k5hjMkqM/fe-test-report.gif)](https://postimg.cc/xkMGtpXB)