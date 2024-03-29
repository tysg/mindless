# mindless

## Introduction

*Mindless* is a fun web application built using an N-gram language model. In particular, we choose 3-gram because it gives the best performance. We use *Chicken Soup for the Soul* as the training corpus to generate word and context matrices. Based on Markov assumption, we continuously generate the next word using the probability calculated from the word and context matrices. We also use *add-k smoothing* to overcome the zero-count issue. 

*Mindless* can help people de-stress. It's a fast-paced society, and we sometimes get anxious and overwhelmed by all those to-dos and deadlines. Through looking at a cute character talking gibberish, we derive fun, happiness, and inspirations to those unanswered questions in our heart. 

Mind LESS and laugh MORE with *Mindless* 😉


## Give It A Try

You can try out *Mindless* at https://mind-less.herokuapp.com.


## Building The Project

You can use Python 3 and Node.js to build and run the project.

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

## Deploying to fly.io

There's some rough edges that hasn't yet to be evened out. For now, 
comment out the front-end `build` folder from the `.dockerignore` file
so that it'll be included in the built image. 


## Examples

Here are some of the examples: 

<img src="demo_pics/IMG_3990.PNG" width="23%"></img> <img src="demo_pics/IMG_3992.PNG" width="23%"></img> <img src="demo_pics/IMG_3996.PNG" width="23%"></img> <img src="demo_pics/IMG_4002.PNG" width="23%"></img> 
