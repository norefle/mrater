# MRater

This is a template project for user studies. It provides scaffolding
of pages containing a main item with all the required data and related
sorted items recommended by the system.

The user can sort the recommendations by dragging and dropping them.
Updated order is sent to the backend to update the feedback scores.

## Build

### Dependencies

For local build/run [poetry](https://poetry.eustace.io) package manager should be used.
Install it and then the following commands can be used.

Install dependencies int virtual environment:

```
poetry install
```

Run a local flask server in development mode:

```
FLASK_APP=app FLASK_ENV=development poetry run flask run -h 0.0.0.0 -p 8080 --reload --debugger --extra-files templates:static
```

Run a local gunicorn server:

```
poetry run gunicorn --bind 0.0.0.0:8080 app:app --reload
```

### Docker

Another option is to have docker only. None of the above is required.

Build image locally, assuming docker image name is `norefle/mrater`:

```
 docker build -t norefle/mrater .
```

Run the docker image locally:

```
 docker run -ti -p 8080:8080 norefle/mrater
```

Now it's available at `localhost:8080`.


## Thanks

**Dragula**

For drag and drop functionality the awesome [dragula](https://github.com/bevacqua/dragula)
library has been used.

**Images**

All test posters and text have been taken from wikipedia.
