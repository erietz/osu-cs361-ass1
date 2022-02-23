# To start the server

`make`

# To read the API specifications

[http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)

# Example

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
