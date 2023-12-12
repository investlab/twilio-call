# FastAPI Twilio Caller

This project is a FastAPI application that initiates a Twilio call based on specified credentials and parameters.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- **Docker:** [Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose:** [Installation Guide](https://docs.docker.com/compose/install/)

### Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-twilio-caller.git
cd fastapi-twilio-caller
```
### Set Up Twilio Credentials

Edit the `credentials.json` file with your Twilio credentials.
The `credentials.json` file should have the following format:
```
{
    "thaopt": {
        "account_sid": "AC01cf68731c8e4639xxxxxxxxxxf0f39",
        "auth_token": "441bb98caa9e5e17e73xxxxxxxxxxb4ce6",
        "from_phone_number": "+1xxxxxxxxxxx",
        "to_phone_number": "+84xxxxxxxxxxxx"
    },
    "your-name-1": {
        "account_sid": "your_account_sid_2",
        "auth_token": "your_auth_token_2",
        "from_phone_number": "your_from_phone_number_2",
        "to_phone_number": "your_to_phone_number_2"
    },
    "your-name-2": {
        "account_sid": "your_account_sid_3",
        "auth_token": "your_auth_token_3",
        "from_phone_number": "your_from_phone_number_3",
        "to_phone_number": "your_from_phone_number_3"
    }
}
```
### Build and Run the Docker Container

To build and run the Docker container, execute the following command in the project directory:

```
docker-compose up --build
```

### Make a call
To initiate a Twilio call, you can send a GET request to the `/make_call/{credential_name}` endpoint, where credential_name represents the name of the credential you want to use for the call. Replace `{credential_name}` with the actual credential name you intend to use.
Example:
```
curl http://localhost:8000/make_call/thaopt
```
Replace `thaopt` with the specific credential name associated with your Twilio account. Adjust the endpoint accordingly for other credentials.
This request triggers the FastAPI application to make a Twilio call using the specified credential. Check the console or logs for any relevant information about the call process.
