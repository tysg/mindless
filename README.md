# mindless

## Introduction

mindless is fun application built using an N-gram language model. 


## Up and Running

You'll need Python 3 and Node.js to build and run the project.

Install the Python dependencies using

```
pip3 install -r requirements.txt
```

To compile the frontend assets, 

```
cd web
yarn install
yarn build
```

To start the server,

```
python3 app.py
```

This spins up a Python Flask server that servers the frontend asset,
and also provides the API to the backend language model via `/api/talk`

