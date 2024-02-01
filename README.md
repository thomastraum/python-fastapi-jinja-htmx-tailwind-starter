# basic skeleton

`python3.10 -m venv .venv`

`source .venv/bin/activate.fish`

`pip install -r requirements.txt`

```
python -m app.main
```

```
tailwindcss -i ./app/static/src/tw.css -o ./app/static/css/main.css --watch
```

you need to add an env file

```
HOST=0.0.0.0
PORT=8001
ENV="development"
```