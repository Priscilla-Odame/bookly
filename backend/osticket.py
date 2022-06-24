import requests
# This is a class to hold all methods related to osticket management


class osticket:
    url = "https://pia.northeurope.cloudapp.azure.com/api/tickets.json"

    # ticket creation method
    # fields required:
    # name -> name of ticket-creation submitter
    # subject -> subject of the ticket
    # message -> initial message for the ticket thread
    # email -> email of the ticket-creator
    # ip -> ip address of the machine issueing the request
    # api_key -> x-api-key of the machine sending the request

    def create_ticket(ticket_details: dict):

        if not ticket_details:
            return

        headers = {"content-type": "application/json",
                   "X-API-Key": ticket_details["api_key"]}

        api_key = ticket_details["api_key"]

        del ticket_details["api_key"]

        payload = {
            "alert": true,
            "autorespond": true,
            "source": ticket_details.get(source, "API"),
            "name": ticket_details["name"],
            "email": ticket_details["email"],
            "subject": ticket_details["subject"],
            "ip": ticket_details["ip"],
            "message": "data:text/plain,MESSAGE A test to create a ticket from my(Moses) pc "

        }

        # checker to identify and include any additional fields
        if len(ticket_details) > 5:
            for k, v in ticket_details:
                if payload[k] == None:
                    payload[k] = ticket_details[v]
        try:

            response = requests.post(url, payload)

            return response

        except Exception as e:
            print(f)

            # test the script with default data if run from this file alone is run
if __name__ == "__main__":
    default_payload = {
        "alert": true,
        "autorespond": true,
        "source": "API",
        "name": "Moses Wuniche",
        "email": "joseph.sarpong@scalework.com",
        "phone": "+233549124145",
        "subject": "Test ticket creation from local machine",
        "ip": "41.222.234.218",
        "message": "data:text/plain,MESSAGE A test to create a ticket from my(Moses) pc "

    }

    o = osticket()
    print(o.create_ticket(default_payload))

# Misty
