Front-end test framework based on Selenium and Pytest

It provides:
- Mobile emulation
- Utils for actions, validations, conditional waiting, etc
- Light POM architecture
- Basic step logs (stdout)
- HTML test report with embedded failure screenshots

Project structure:
```
├── pages/
│   ├── base.py
│   ├── home.py
│   ├── search.py
│   ├── search_results.py
│   └── streamer.py
│
├── test_report/  #auto generated upon test run 
│   ├── assets
│   └── report.html
│
├── tests/
│   └── test_twitch_mobile_nav.py
│
├── utils/
│   └── driver_factory.py
│
├── conftest.py
├── pytest.ini
└── requirements.txt
```

Running tests:
1) install dependencies:
>pip install -r requirements.txt
2) to run all tests:
>pytest