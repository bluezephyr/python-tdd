# Animals TDD Tutorial

## First Test
* Create a unittest file `test_mammals.py`
* Create a test case that creates an object of the class `MammalsSet`. Name it `init`.
  Run the test and watch if fail.
* Create a python file `mammals.py` and a class named `MammalsSet`. Implement using a
  simple `pass`. Import the class from the unittest, run the test again and watch it succeed.
* Rename the testcase to `test_return_empty_list_if_no_mammals`. We have no actual need for
  the `init` test case, it is too simple. Instead, we extend the testcase to be as simple as
  possible, but still have a meaning. Check that the the length of the attribute `mammals` is 0.
  It is a very simple test, but is useful for at least two reasons.
  1. It defines the interface to the `MammalsSet` class by defining the name of an attribute
     or method, including its return value.
  1. It defines how the class shall behave when there are no mammals.

  This test case might seem too trivial but the purpose of it is to use it to drive the design
  and to get the implementation started. Run the test case. It will fail since the `MammalsSet`
  class does not have a `mammals` attribute.
* Add a `mammals` attribute and set it to an empty list. We could make it a `set()` but we
  don't know now if that is the best way to implement it. So let's wait with that. Run the test,
  it shall now work.

The first part of the implementation is now finished. Commit.

## Second Test
With the first test case done, what would be a good next step? A natural thing would be to add
some mammals to the list. But how do we do that? If we consult our draft overview design, we see
that we have planned for a `refresh` message that the client can send to the `MammalsSet`
object. Let's write a test for that. If we send a `refresh` message, what should happen? In the
first test case we had a query to the object and we got a list in return. In this case, we want
something to happen; a command. A command typically has side effects and we need to define those
side effects and also write a test to check that it happens.

In the draft design, we have envisioned a database that contains all animals that we know of. A
natural effect of that `refresh` command message is sente to the `MammalsSet` object could be
that a new message is sent from the `MammalSet` object to the database. Since we have no
database implementation database yet, we are free to define the interface. In order to write the
test, we need to do this but we also need to understand the relationship between the `MammalSet`
object and the database and the life cycle. We assume that the database will exist before the
`MammalSet` object. The simplest thing to do right now is to give the database as an input
argument when the `MammalSet` object is created and send messages to that instance. Let's
assume that we have an `Animals` class with an `animals`method. The simplest test case that
we can the write is to check that an `animals` message is sent to the `Animals` instance if
the `refresh` message is sent to a `MammalsSet` object.

* Create a new test case `test_refresh_generates_call_to_database`. In that test case, do the
 following:
  1. Create a mock database
  1. Create an instance of a `MammalsSet` and provide the mock database as input

There is builtin support for mocks in the Python unittest module. Simply import unittest.mock and
create an instance of the Mock class.

* Run the test case and watch it fail.
* Make the minimal change to make it pass. In this example, we add a parameter to the init
  function of the `MammalsSet` class. Store a reference to the database in an instance variable.
* Add the following to the test case:
  1. Send the `refresh` message to the `MammalsSet` instance (i.e., call the `refresh` method)
* Run the test case and watch it fail.
* Add the `refresh` method to the `MammalsSet` class. Implement it with `pass`
* Finalize the test case with an assert that the `animals` message is sent to the mock database.
* Run the test case and watch it fail.
* Implement the `refresh` function with a call to the database's `animals` method. The test now
  passes.

The second test case is now complete and we have a working implementation that fulfils all
(!) the tests in our suite. Maybe not very impressive at the moment but we have made a few important
design decisions on the way and we have documented them in working code. Let's head for the next
test.
