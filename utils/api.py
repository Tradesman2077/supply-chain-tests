import time
import requests


def post_with_retry(url: str, json: dict, retries: int = 3, delay: float = 1.0) -> requests.Response:
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, json=json, timeout=10)
            if response.status_code == 200:
                return response
            last_error = f"status {response.status_code}"
        except requests.RequestException as e:
            last_error = str(e)
        if attempt < retries:
            time.sleep(delay)
    raise AssertionError(f"POST {url} failed after {retries} attempts: {last_error}")


def get_with_retry(url: str, retries: int = 3, delay: float = 1.0) -> requests.Response:
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response
            last_error = f"status {response.status_code}"
        except requests.RequestException as e:
            last_error = str(e)
        if attempt < retries:
            time.sleep(delay)
    raise AssertionError(f"GET {url} failed after {retries} attempts: {last_error}")
