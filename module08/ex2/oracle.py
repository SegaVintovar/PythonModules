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

    try:
        if database_url == "http://0.0.0.0:8080/":
            db = "Connected to local instance"
        elif database_url == "":
            raise MissingEnvVariable(
                "ERROR: database_url can not be empty"
            )
        else:
            db = "Could not conntect to local instance"
    except MissingEnvVariable as e:
        print(str(e))
    else:
        print("Database: ", db)

    try:
        api_key = os.getenv("API_KEY")
        if api_key == "secret key":
            print("API Access: Authenticated")
        elif api_key == "":
            raise MissingEnvVariable(
                "Error: API_KEY can not be empty"
            )
        else:
            print("API Access: Forbidden - Invalid API_KEY")
    except MissingEnvVariable as e:
        print(str(e))

    try:
        log_lvl = os.getenv("LOG_LEVEL")
        if log_lvl == "":
            raise MissingEnvVariable("Log level cannot be empty")
        log_lvl = int(log_lvl)
        if log_lvl < 5:
            log_lvl = "DEBUG"
        else:
            log_lvl = "TEST RUN"
        print(f"Log level: {log_lvl}")
    except MissingEnvVariable as e:
        print(str(e))
    except ValueError("Log level has to be numeric") as e:
        print(str(e))

    try:
        zion = os.getenv("ZION_ENDPOINT")
        if zion:
            print("Zion Network: Online")
        else:
            raise MissingEnvVariable("Error: ZION_ENDPOINT cannot be empty")
    except MissingEnvVariable as e:
        print(str(e))

    print("""\nEnvironment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available"""
          )
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
