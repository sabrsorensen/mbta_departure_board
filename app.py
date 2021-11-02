from datetime import datetime
import os

from dateutil import tz
from flask import Flask
import jsonapi_requests

from auth import MbtaHeaderAuth
from departure import Departure, print_departure_header

api_key = os.getenv("MBTA_API_KEY")
station_id = "place-north"
api = jsonapi_requests.orm.OrmApi.config({
    'API_ROOT': 'https://api-v3.mbta.com',
    'APPEND_SLASH': False,
    'AUTH': MbtaHeaderAuth(api_key=os.environ.get('MBTA_API_KEY', None))
})

app = Flask(__name__)


def get_stop_predictions(stop_id):
    route_type = 2  # Commuter rail
    request_includes = ','.join(['stop', 'trip', 'schedule'])
    endpoint = api.endpoint(
        f"predictions?filter[stop]={stop_id}&filter[route_type]={route_type}&include={request_includes}")
    response = endpoint.get()
    predictions = response.data
    includes = response.payload["included"]

    return predictions, includes


def find_included_info_value(included_info: list, include_type: str, id: str, attribute_key: str):
    for include in included_info:
        if include["type"] == include_type and include["id"] == id and include["attributes"][attribute_key] is not None:
            return include["attributes"][attribute_key]
    return None


@app.route("/")
@app.route("/mbta")
def generate_departure_table():
    departures = []
    predictions, included_info = get_stop_predictions(station_id)
    for departure in predictions:
        status = departure.attributes["status"]
        destination = departure.relationships.get("route").data.id
        schedule_id = departure.relationships.get("schedule").data.id

        departure_time = find_included_info_value(
            included_info, "schedule", schedule_id, "departure_time")
        trip_id = departure.relationships.get("trip").data.id
        vehicle = find_included_info_value(
            included_info, "trip", trip_id, "name")
        stop_id = departure.relationships.get("stop").data.id
        track = find_included_info_value(
            included_info, "stop", stop_id, "platform_code")

        # Ignore arrivals with no departures (final stop?)
        if departure_time is not None:
            time_fmt = "%H:%M"
            departure_time = datetime.strptime(
                departure_time, '%Y-%m-%dT%H:%M:%S%z')
            now = datetime.now(departure_time.tzinfo)
            if departure_time > now:
                departures.append(Departure(destination, status,
                                            vehicle, track, departure_time))

    departures.sort(key=lambda x: x.departure_time)

    table_header = print_departure_header()
    table = f'<html><Table>{table_header}<tbody>'
    for departure in departures:
        departure_row = departure.print_departure()
        table += departure_row
    table += '</tbody></Table></html>'
    return table

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
