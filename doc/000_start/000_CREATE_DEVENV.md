# Programmier-Workshop: Python / Fortgeschrittene

![Logo](doc/mp4/CreateAnimationsWithManim.gif)

![Logo](doc/logo_manim.png)

## Create Manim Development Environment

Using Docker, we will setup a development environment on Ubuntu.

Beside of the Dockerfile to create the environment, we will utilise a Makefile to easly build and run the Manim environment.

To build the envrionnment, type:
```make build```

To run the environment, type:
```make run```

### Dockerfile

- use latest Ubuntu Version

- add sudo functionality für user

- set root password

- install latex and additional fonts
  
- install manim and manimlib
