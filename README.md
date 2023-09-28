# To-Calm, A To-Do App With Focus on Emotional Health

## Goals

* Demonstrate Full-Stack web application development skills
  * Python backend
    * Django
    * django-ninja
    * SQLite
    * TODO: Postgres
  * TypeScript front end
    * React
    * TODO: Tree Map chart
    * React Query
    * Vite
  * TODO: [Authentication](https://python-social-auth.readthedocs.io/en/latest/configuration/django.html)?

## Design

  * Allow easy entry, with emotional weight value
  * From the list of to-dos, allow for increase/decrease of the weight
  * Reorder the list with the heaviest items on top
  * TODO: Encourage mitigating the heavier items
    * Break up into smaller items
    * Ask for help from contacts
    * Reevaluate importance

## Tasks

* [x] Data model
  * User (foreign key)
  * Task name (string)
  * Weight (int)
  * Done (bool)
  * TODO: Importance, due date, etc.
* [ ] CRUD API
  * Except, the *D* is a soft delete
* [ ] UI
  * List of items
  * Click to edit task name
  * Click to edit task weight
  * Save on enter or on click save?