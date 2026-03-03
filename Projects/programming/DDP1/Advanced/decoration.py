class RateExceeds(Exception):
    def __str__(self):
        return "Number of calls exceeds bla bla, please wait in x seconds."
n_of_calls = 0

def rate_limit(func):
    def wrapper(*args, **kwargs):
        global n_of_calls
        n_of_calls += 1
        if n_of_calls <= 3:
            return func(*args, **kwargs)
        else:
            raise RateExceeds()
    return wrapper

# thanks deepseek for problem
@rate_limit
def fetch_data(api_endpoint):
    print(f"Fetching data from {api_endpoint}")
    return f"Data from {api_endpoint}"

# Test it
try:
    for i in range(5):
        print(f"Call {i+1}: {fetch_data('/users')}")
except Exception as e:
    print(f"Error: {e}")

#TODO: fawk around with *args **kwargs