# Instructions

## Install the requirements

1. Create and activate a python virtual environment (optional)
2. `make install`

## Start the server

`make serve`

# To read the API specifications

- [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)
- Note: checkout the schema tab and drill down on the options

# Example HTTP request

```
POST http://localhost:8000/api/plot
content-type: application/json
```

```json
{
  "title": "Title of the plot",
  "x_label": "x label",
  "y_label": "y label",
  "type": "pie",
  "values": [
    {
        "label": "chocolate",
        "value": 123
    },
    {
        "label": "vanilla",
        "value": 321
    },
    {
        "label": "oreo",
        "value": 999
    }
  ]
}
```

# Issues

Please file an issue in this repo if you have any issues or feature requests.
