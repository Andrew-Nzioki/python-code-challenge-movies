# Phase 3 Code Challenge: Movies

For this assignment, we'll be working with a Movie domain.

We have three models: `Movie`, `Role`, and `Actor`.

For our purposes, a `Movie` has many `Roles`, a `Actor` has many `Roles`, and a
`Role` belongs to a `Movie` and to an `Actor`.

`Movie` - `Actor` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- SQLAlchemy Migrations
- SQLAlchemy Relationships
- Class and Instance Methods
- SQLAlchemy Querying

***

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge does not have tests. You cannot run `pytest`.
 You'll need to create your own sample instances so
that you can try out your code on your own. Make sure your relationships and
methods work in the console before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session with
your classes defined. You can test out the methods that you write here. You are
also encouraged to use the `seeds.py` file to create sample data to test your
models and relationships.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

***

## What You Already Have

The starter code has migrations and models for the initial `Actor` and `Movie`
models, and seed data for some `Actors` and `Movies`. The schema currently looks
like this:

### Actors Table

| Column | Type   |
| ------ | ------ |
| name   | String |

### Movies Table

| Column              | Type    |
| ------------------- | ------- |
| title               | String  |
| box_office_earnings | Integer |

You will need to create the migration for the `roles` table using the attributes
specified in the deliverables below.

***

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

Remember: SQLAlchemy give your classes access to a lot of methods already!
Keep in mind what methods SQLAlchemy gives you access to on each of your
classes when you're approaching the deliverables below.

### Migrations

Before working on the rest of the deliverables, you will need to create a
migration for the `roles` table.

- A `Role` belongs to a `Movie`, and a `Role` also belongs to an `Actor`. In
  your migration, create any columns your `roles` table will need to establish
  these relationships.
- The `roles` table should also have:
  - A `salary` column that stores an integer.
  - A `character_name` column that stores a string.

After creating the `roles` table using a migration, use the `seeds.py` file to
create instances of your `Role` class so you can test your code.

**Once you've set up your `roles` table**, work on building out the following
deliverables.

### Object Relationship Methods

Use SQLAlchemy query methods where
appropriate.

#### Role

- `Role actor()`
  - should return the `Actor` instance for this role
- `Role movie()`
  - should return the `Movie` instance for this role

#### Movie

- `Movie roles()`
  - returns a collection of all the roles for the movie
- `Movie actors()`
  - returns a collection of all the actors who performed in the movie

#### Actor

- `Actor roles()`
  - should return a collection of all the roles that the actor has played
- `Actor movies()`
  - should return a collection of all the movies that the actor has performed in

Use `python debug.py` and check that these methods work before proceeding. For
example, you should be able to call `session.query(Actor).first().movies` and see a list of the
movies for the first actor in the database based on your seed data; and
`session.query(Actor).first()` should return the actor for the first role in the database.

### Aggregate and Relationship Methods

#### Role

- `Role credit()`
  - should return a string formatted as follows:
    `{insert character name}: Played by {insert actor name}`

#### Movie

- `Movie cast_role(actor, character_name, salary)`
  - takes a `actor` (an instance of the `Actor` class), a `character_name`
    (string), and a `salary` (integer) as arguments, and creates a new `role` in
    the database associated with this movie and the actor
- `Movie all_credits()`
  - should return an Array of strings with all the roles for this movie
    formatted as follows:
    ["{insert character name}: Played by {insert actor name}", "{insert character name}: Played by {insert actor name}", ...]
- `Movie fire_actor(actor)`
  - takes an `actor` (an instance of the `Actor` class) and removes their role from this movie
  - you will have to delete a row from the `roles` table to get this to work!

#### Actor

- `Actor total_salary()`
  - returns the total salary for an actor based on the salary for each of their
    roles
- `Actor blockbusters()`
  - returns a collection of all the `Movie` instances the actor has performed in
    that have a `box_office_earnings` of over $50,000,000
- `Actor most_successful() class method`
  - returns _one_ actor instance for the actor who has the highest total salary
    for all their roles
