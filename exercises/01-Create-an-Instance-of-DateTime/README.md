# `01` Create an instance of a datetime

Python has some pre-defined modules that you can use whenever you want. One of these modules is the datetime.
The datetime module supplies classes for manipulating dates and times.

For example, to print the current date, we can use the datetime module like this:

```Python
import datetime

# getting current date and time
d = datetime.datetime.today()
print('Current date and time: ', d)
```

## 📝 Instructions:

1. Create a new datetime object with format month-day-year and print it on the console like this:
```Python
Today is: 9-13-2019
```

## 💡Hint:
**datetime** is a method to format a date in Python. You can convert a date into any possible desired format by using this method.
**strftime** method is used to create a string representing the date under the control of explicit format string.

Check the docs:
- https://docs.python.org/3/library/datetime.html#datetime.date.strftime

