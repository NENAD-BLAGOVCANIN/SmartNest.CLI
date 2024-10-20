import requests

def send(method, url, body=None, headers=None, params=None):
    """
    Sends an HTTP request with the specified method, URL, and optional body and headers.

    :param method: HTTP method as a string (e.g., 'GET', 'POST', 'PUT', 'DELETE')
    :param url: The URL to send the request to
    :param body: The request payload (for POST, PUT, etc.), optional
    :param headers: Optional headers to include in the request
    :param params: Optional query parameters for the request
    :return: The response from the request
    """
    try:
        method = method.upper()

        if method == 'GET':
            response = requests.get(url, headers=headers, params=params)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=body)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, json=body)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
