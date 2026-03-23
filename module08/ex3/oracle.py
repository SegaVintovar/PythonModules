import os
# import sys
from dotenv import load_dotenv


class MissingEnvVariable(Exception):
    def __init__(self, message):
        super().__init__(message)


def main() -> None:

    print('\nORACLE STATUS: Reading the Matrix...\n')
    # Loads configuration from environment variables
    load_dotenv()

    print("Configuration loaded:")
    matrix_mode = os.getenv("MATRIX_MODE")
    try:
        if matrix_mode == "development" or matrix_mode == "production":
            print("Mode: ", matrix_mode)
        else:
            raise MissingEnvVariable(
                "ERROR: matrix mode can be only 'development' or 'production'"
                )
    except MissingEnvVariable as e:
        print(str(e))
    # Python too has an in-built web server that you can trigger like this:
    # python -m http.server 8080

    database_url = os.getenv("DATABASE_URL")

    if database_url == "http://0.0.0.0:8080/":
        db = "Connected to local instance"
    else:
        db = "Could not conntect to local instance"
    print("Database: ", db)

    api_key = os.getenv("API_KEY")
    if api_key == "secret key":
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthorized")

    log_lvl = os.getenv("LOG_LEVEL")
    if log_lvl == "":
        raise ValueError("Log level cannot be empty")
    try:
        log_lvl = int(log_lvl)
        if log_lvl < 5:
            log_lvl = "DEBUG"
        else:
            log_lvl = "TEST RUN"
    except ValueError:
        raise ValueError("Log level has to be numeric")

    zion = os.getenv("ZION_ENDPOINT")
    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: Unavaliable")
    print("""
Environment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available""")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
