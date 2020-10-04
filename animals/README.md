# Animals TDD Tutorial

## First Test
* Create a unittest file ``test_mammals.py``
* Create a test case that creates an object of the class ``MammalsSet``. Name it ``init``.
  Run the test and watch if fail.
* Create a python file ``mammals.py`` and a class named ``MammalsSet``. Implement using a
  simple ``pass``. Import the class from the unittest, run the test again and watch it succeed.
* Rename the testcase to ``test_return_empty_list_if_no_mammals``. We have no actual need for
  the ``init`` test case, it is too simple. Instead, we extend the testcase to be as simple as
  possible, but still have a meaning. Check that the the length of the attribute ``mammals`` is 0.
  It is a very simple test, but is useful for at least two reasons.
  1. It defines the interface to the ``MammalsSet`` class by defining the name of an attribute
     or method, including its return value.
  1. It defines how the class shall behave when there are no mammals.

  This test case might seem too trivial but the purpose of it is to use it to drive the design
  and to get the implementation started. Run the test case. It will fail since the ``MammalsSet``
  class does not have a ``mammals`` attribute.
* Add a ``mammals`` attribute and set it to an empty list. We could make it a ``set()`` but we
  don't know now if that is the best way to implement it. So let's wait with that. Run the test,
  it shall now work.

The first part of the implementation is now finished. Commit?
