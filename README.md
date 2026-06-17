# Clinic Appointment API

This project is a simple Clinic Appointment API built using FastAPI and Docker.

## Laboratory Context

This project was developed in an offline Windows 11 laboratory environment.

Python was not installed directly on the computer. The application was executed using Docker and a prebuild Docker image named clinic-fastapi-base:1.0.

## Features

- Create clinic appointments
- View all appointments
- View one appointment
- Update appointment details
- Cancel appointments

## Technologies Used

- Python
- FastAPI
- Docker
- Git

## How to Run

docker compose up --build

Open http://localhost:8000/docs.

## Logout behavior

This project uses basic, static bearer tokens for instructional purposes, so there is no formal "logout" endpoint on the server side. To logout, the client application just needs to delete the token from its own side. If the client forgets the token, they are effectively logged out.

In a production-ready application (using JWTs or opaque tokens), logging out is typically handled in one of three ways:

- Client-Side Deletion: The frontend application deletes the token from its storage (localStorage, cookies, or app state).

- Token Expiration & Refresh Tokens: Access tokens are given a very short lifespan (e.g., 15 minutes). 

- Token Blacklisting: The server maintains a list of revoked token IDs (a blacklist) and checks it during incoming API requests to block access.