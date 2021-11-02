# MTBA Departure Board

## How to run

### Local Python

Install Python 3 and pip, then clone this repo, change directory into your cloned working copy, and run:

```sh
python -m pip install -r requirements.txt
python -m flask run
```

### Docker (preferred)

Using your MBTA API key as an environment variable, execute:

```sh
docker run ghcr.io/sabrsorensen/mbta_departure_board -e MBTA_API_KEY=$MBTA_API_KEY -p 5000:5000
```

Then visit http://localhost:5000 to view upcoming departures from the MBTA's North Station in Boston, Massachusetts.

## References

- [MBTA V3 API documentation](https://www.mbta.com/developers/v3-api)
- [python-mbta](https://github.com/milas/python-mbta)
- [pymbta3](https://github.com/altonplace/pymbta3)
- [aliciaphes's MBTA dashboard in React](https://github.com/aliciaphes/MBTA)
