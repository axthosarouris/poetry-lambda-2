from datetime import date


def handle_request(event, context):
    current_date = date.today()
    name = event.get("name")
    return {"name": name, "timestamp": str(current_date)}
