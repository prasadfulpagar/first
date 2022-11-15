from warnings import filterwarnings
filterwarnings("ignore")

def print_msg(message: str) -> str:
    return f"hello, {message}"


if __name__ == "__main__":
    msg = "This is Prasad Fulpagar, from Nasik."
    print(print_msg(msg))
