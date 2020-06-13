# Federated Learning: an empirical analysis of convergence rates in different learning regimes

Author: Lorenzo Mancuso

Supervisors: Prof. Roberto Esposito, Prof. Marco Aldinucci

University of Turin, Computer Science Department

July 2020

# Horizontal Federated Learning

Federated learning distributes the machine learning process over to the edge. It enables mobile phones to collaboratively learn a shared model using the training data on the device and keeping the data on device. It decouples the need for doing machine learning with the need to store the data in the cloud. Functionally, a mobile device that is a part of a FL computing architecture, downloads a model that is meant for running on mobile devices. It then runs the model locally on the phone and improves it by learning from data stored there. Subsequently, it summarizes the changes as a small update, typically containing the model parameters and corresponding weights. The update to the model is then sent to the cloud or central server using encrypted communication, for example, homomorphic encryption (HE). This update is then averaged with other user updates to improve the shared model. Most importantly, all the training data remains on user’s device, and no individual updates are identifiably stored in the cloud.

Horizontal Federated Learning, also known as sample-based federated learning, is introduced in the scenarios that data sets share the same feature space but different in samples. 

For example, two regional banks may have very different user groups from their respective regions, and the intersection set of their users is very small. However, their business is very similar, so the feature spaces are the same.



# Architecture

## Network Architecture
The next Figure shows how the two actor, the device (client) and the FL Server, communicate to each other:

![network](/assets/network_architecture.png)

This project uses an MQTT protocol for communications between server and devices. 

## Server Architecture
The FL server is designed around the Actor Programming Model (Hewitt et al., 1973). Actors are universal primitives of concurrent computation which use message passing as the sole communication mechanism. Each actor handles a stream of messages/events strictly sequentially, leading to a simple programming model. Running multiple instances of actors of the same type allows a natural scaling to large number of processors/machines. In response  to a message, an actor can make local decisions, send messages to other actors, or create more actors dynamically.

![server](/assets/server_architecture.png)

The main actors in the system are:
* Coordinators: are the top-level actors which enable global synchronization and advancing rounds in lockstep. 
* Selectors: are responsible for accepting and forwarding device connections.
* Aggregators: manage the rounds of each FL task.

This implementation has only one actor for each type described before.

### Server actors sequence diagram

![server_actors](/assets/server_actors_states.png)

### Server workflow

![server_workflow](/assets/server_workflow.png)

## Client Architecture
The device’s first responsibility in on-device learning is to maintain a repository of locally collected data for model training and evaluation. The FL runtime, when provided a task by the FL server, accesses an appropriate example store to compute model updates, or evaluate model quality on held out data.

![client](/assets/client_architecture.png)

### Client workflow

![client_workflow](/assets/client_workflow.png)

# Project

## Run

```
python Server/main.py
```

```
python Client/app.py
```



## Requirements
* paho.mqtt.client
* thespian.actors
* tensorflow
* tensorflow_federated
* numpy
* six
* collections
* warnings
* datetime
* json


# References
* Keith Bonawitz, Hubert Eichner, Wolfgang Grieskamp, Dzmitry Huba, Alex Ingerman, Vladimir Ivanov, Chloe Kiddon, Jakub Konecn, Stefano Mazzocchi, H. Brendan McMahan, Timon Van Overveldt, David Petrou, Daniel Ramage, Jason Roselander - Google Inc., Mountain View, CA, USA. [TOWARDS FEDERATED LEARNING AT SCALE: SYSTEM DESIGN](https://arxiv.org/pdf/1902.01046.pdf). 

