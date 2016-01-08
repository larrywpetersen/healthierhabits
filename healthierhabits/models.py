from django.db import models

from django.utils import timezone



class Groups( models.Model):
    name = models.CharField( max_length = 200)
    address1 = models.CharField( max_length = 100)
    address2 = models.CharField( max_length = 100, blank = True)
    city = models.CharField( max_length = 100)
    state = models.CharField( max_length = 100)
    zip = models.CharField( max_length = 100)
    email = models.CharField( max_length = 100)
    phone = models.CharField( max_length = 100, blank = True)
    def __str__(self):
        return self.name
    def name_string( self):
        msg = self.name
        return msg



class Rewards( models.Model):
    group = models.ForeignKey( Groups)
    name = models.CharField( max_length = 200)
    price = models.IntegerField( default = 100)
    available = models.BooleanField( default = True)
    number_given = models.IntegerField( default = 100)
    def __str__(self):
        msg = self.name
        return msg
    def name_string( self):
        msg = self.name
        return msg
    def available_yn( self):
        msg = "No"
        if( self.available):
            msg = "Yes"
        return msg



class Customers( models.Model):
    firstname = models.CharField( max_length = 100)
    lastname = models.CharField( max_length = 100)
    address1 = models.CharField( max_length = 100)
    address2 = models.CharField( max_length = 100, blank=True)
    city = models.CharField( max_length = 100)
    state = models.CharField( max_length = 100)
    zip = models.CharField( max_length = 100)
    email1 = models.CharField( max_length = 100)
    email2 = models.CharField( max_length = 100, blank=True)
    phone1 = models.CharField( max_length = 100, blank=True)
    phone2 = models.CharField( max_length = 100, blank=True)
    group = models.ForeignKey( Groups)
    current_points = models.BigIntegerField( default = 0)
    life_points = models.BigIntegerField( default = 0)
    def __str__( self):
        msg = self.name_string() + ',  ' + self.city
        msg = msg + ', ' + self.state + '  -  ' + self.group.name
        return msg
    def name_string( self):
        return self.firstname + ' ' + self.lastname
    def address_string( self):
        return self.address1 + ', ' + self.city + ', ' + self.state


class Orders( models.Model):
#    customer = models.CharField( max_length = 200)
    customer = models.ForeignKey( Customers)
    date = models.DateTimeField( 'purchase date', default = timezone.now )
    item = models.CharField( max_length = 200)
#    item = models.ForeignKey( Rewards)
    price = models.IntegerField( default = 1)
    filled = models.BooleanField( default = False)
    def __str__(self):
        msg = self.pretty_print() + '  (' + self.nice_filled() + ')'
        return msg
    def name_string( self):
        return self.customer.name_string()
    def nice_date(self):
        msg = self.date.strftime( '%b %d, %Y')
        return msg
    def date_string(self):
        msg = self.date.strftime( '%b %d, %Y')
        return msg
    def nice_filled( self):
        if ( self.filled ):
            return 'has been filled'
        else:
            return 'has not been filled'
    def filled_yn(self):
        if ( self.filled ):
            return 'yes'
        else:
            return 'no'
    def pretty_print(self):
        msg = self.nice_date() + ' - ' + self.customer.firstname
        msg = msg + ' ' + self.customer.lastname
        msg = msg + " ordered '" + self.item + "' for "
        msg = msg + str( self.price) + ' points.'
        return msg


