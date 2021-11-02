'''
Module to group departure data and format for rendering
'''


def print_departure_header():
    '''
    Helper method to generate table header
    '''
    headers = ["Destination", "Departure Time",
               "Status", "Train #", "Track #"]
    formatted_headers = []
    for header in headers:
        formatted_header = "<td>" + header + "</td>"
        formatted_headers.append(formatted_header)

    return f"<thead><tr>{''.join(formatted_headers)}</tr></thead>"


class Departure():
    '''
    Class to bundle and format the relevant info of an entry on a departure board
    '''

    def __init__(self, destination: str, status: str, train: int, track: int, departure_time: str):
        self.destination = destination
        self.status = status
        self.train = train
        self.track = track
        self.departure_time = departure_time

    def print_departure(self):
        '''
        Generate the HTML table equivalent of this departure
        '''
        return f'''<tr>
        <td>{self.destination}</td>
        <td>{self.departure_time}</td>
        <td>{self.status}</td>
        <td>{self.train}</td>
        <td>{self.track}</td>
        </tr>'''
