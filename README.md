# Supply Chain Tests

BDD test suite for the supply chain storefront using Behave + Playwright.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
playwright install chromium
```

## Running tests

```bash
behave
```

Run a specific feature:
```bash
behave features/storefront_orders.feature
```

## Test results

JUnit XML and Playwright traces are written to `test-results/`.

View a trace:
```bash
playwright show-trace test-results/trace_<scenario_name>.zip
```
