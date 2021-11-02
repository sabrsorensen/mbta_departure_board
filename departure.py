
def print_departure_header():
    headers = ["Destination", "Departure Time",
               "Status", "Train #", "Track #"]
    formatted_headers = []
    for header in headers:
        formatted_header = "<td>" + header + "</td>"
        formatted_headers.append(formatted_header)

    return f"<thead><tr>{''.join(formatted_headers)}</tr></thead>"


class Departure():
    def __init__(self, destination: str, status: str, train: int, track: int, departure_time: str):
        self.destination = destination
        self.status = status
        self.train = train
        self.track = track
        self.departure_time = departure_time

    def __str__(self):
        return f'''<tr>
        <td>{self.destination}</td>
        <td>{self.departure_time}</td>
        <td>{self.status}</td>
        <td>{self.train}</td>
        <td>{self.track}</td>
        </tr>'''

    def print_departure(self):
        return self.__str__()
