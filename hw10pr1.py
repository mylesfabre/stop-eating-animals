# hw10pr1.py
#
# Name: Myles Fabre
#

# Days in each month 
DIM = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date(object):
    """A user-defined data structure that
       stores and manipulates dates.
    """

    def __init__(self, month, day, year):
        """Construct a Date with the given month, day, and year."""
        self.month = month
        self.day = day
        self.year = year


    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}/{:02d}/{:04d}".format(self.month, self.day, self.year)
        return s

# method of the Date class:
    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
            """Returns a new object with the same month, day, year
            as the calling object (self).
            """
            dnew = Date(self.month, self.day, self.year)
            return dnew

    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
           whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False


    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
            in history as ==.  This way , we don't need to use the awkward
            d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False

    def isBefore(self, d2):
        '''Checks to see if d2 is before the self date'''
        if self.equals(d2):
            return False
        elif self.year == d2.year:
            if self.month == d2.month:
                if self.day > d2.day:
                    return False
                else:
                    return True
        elif self.year > d2.year:
            return False
        elif self.month > d2.month:
            return False
        else:
            return True

    def isAfter(self, d2):
        if self.equals(d2):
            return False
        if self.isBefore(d2):
            return False
        else:
            return True

    def tomorrow(self):
        if self.day == DIM[self.month]:
            if self.month == 12:
                self.year +=1
                self.month =1
                self.day =1
            else:
                self.month += 1
                self.day = 1
        else:
            self.day += 1

    def addNDays(self, N):
        if N == 365:
            self.year += 1
        else

#
# lots of dates to work with...
#

d = Date(11, 12, 2019)    # Today?
d2 = Date(12, 20, 2019)   # winter break
ny = Date(1, 1, 2019)     # new year
nd = Date(1, 1, 2020)     # new decade
nc = Date(1, 1, 2100)     # new century
graduation = Date(5, 14, 2023)   # alter to suit!
vacation = Date(5, 15, 2019)     # ditto ~ summer break!
sm1 = Date(10, 28, 1929)  # stock market crash
sn2 = Date(10, 19, 1987)  # another s.m. crash: Mondays in Oct. are risky...
