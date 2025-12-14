# Social Media API – User Authentication System

A Django REST Framework-based social media backend with custom user profiles and token-based authentication.

## Features
- Custom user model with bio, profile picture, and follower relationships
- Token authentication (returns token on registration and login)
- Endpoints: register, login, view/update profile
- Profile picture upload support

## Requirements
- Python 3.9+
- Django 5.x
- djangorestframework
- pillow (for image uploads)

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install django djangorestframework pillow