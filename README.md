# mindless

## Introduction

mindless is fun application built using an N-gram language model. In particular, we choose 3-gram because it gives the best performance. We use *Chicken Soup for the Soul* as the training corpus to generate word and context matrices. Based on Markov assumption, we continuously generate the next word using the probability calculated from the word and context matrices. We also use *add-k smoothing* to overcome the zero-count issue. 




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

