#Django FAQ Management System with Multilingual Support and WYSIWYG Editor

This project provides a Django-based FAQ management system with multilingual support, WYSIWYG editor integration, and an API for managing FAQs.

Table of Contents
Project Setup
Dependencies
Configuration
Running the Project
Features
Testing
Cache Configuration

Project Setup
To set up this project locally, follow the steps below.

Clone the repository:
          git clone https://github.com/your-username/faq-management-system.git
          cd faq-management-system

Create and activate a virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Install the dependencies:

    pip install -r requirements.txt

Dependencies
    This project requires the following dependencies:
    
    Django: The web framework used to build the application.
    django-ckeditor: To provide WYSIWYG (What You See Is What You Get) editing support for the FAQ answers.
    django-modeltranslation: To handle multilingual content for FAQs.
    djangorestframework: For creating the REST API for FAQ management.
    django-redis: For caching translations using Redis.
    googletrans: To automatically translate FAQ content using Google Translate.


Configuration
Install Redis (for caching):

If you plan to use Redis for caching (optional), make sure it’s installed and running. On macOS, you can install it using Homebrew:

      brew install redis
      redis-server

Add django-redis to the cache settings in settings.py:

If using Redis for caching, make sure to add this to your settings.py:

    CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Redis server configuration
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
    }

Add django-ckeditor and django-modeltranslation to INSTALLED_APPS:

In your settings.py, make sure to add the following:

      INSTALLED_APPS = [
    # other apps...
    'ckeditor',
    'modeltranslation',
    'rest_framework',  # For the API
]


Configure CKEditor in settings.py:

For WYSIWYG support, configure CKEditor as follows:

      CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
    }

Set up Google Translate for auto-translations (optional):

If you want to use the Google Translate API to automatically translate FAQs, you will need the googletrans library:

      





