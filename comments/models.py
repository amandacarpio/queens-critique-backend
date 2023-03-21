from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=30, blank=False)
    
    Alabama = 'AL'
    Alaska = 'AK'
    Arizona = 'AZ'
    Arkansas = 'AR'
    California = 'CA'
    Colorado = 'CO'
    Connecticut = 'CT'
    Delaware = 'DE'
    Florida = 'FL'
    Georgia = 'GA'
    Hawaii = 'HI'
    Idaho = 'ID'
    Illinois = 'IL'
    Indiana = 'IN'
    Iowa = 'IA'
    Kansas = 'KS'
    Kentucky = 'KY'
    Lousiana = 'LA'
    Maine = 'ME'
    Maryland = 'MD'
    Massachusetts = 'MA'
    Michigan = 'MI'
    Minnesota = 'MN'
    Mississippi = 'MS'
    Missouri = 'MO'
    Montana = 'MT'
    Nebraska = 'NE'
    Nevada = 'NV'
    NH = 'NH'
    NJ = 'NJ'
    NM = 'NM'
    NY = 'NY'
    NC = 'NC'
    ND = 'ND'
    Ohio = 'OH'
    Oklahoma = 'OK'
    Oregon = 'OR'
    Pennsylvania = 'PA'
    RI = 'RI'
    SC = 'SC'
    SD = 'SD'
    Tennessee = 'TN'
    Texas = 'TX'
    Utah = 'UT'
    Vermont = 'VT'
    Virginia = 'VA'
    Washington = 'WA'
    WV = 'WV'
    Wisconsin = 'WI'
    Wyoming = 'WY'
    none = 'Prefer Not To Say'
    
    city_choices = [
        (none, 'Prefer Not To Say')
        (Alabama, 'AL'),
        (Alaska, 'AK'),
        (Arizona, 'AZ'),
        (Arkansas, 'AR'),
        (California, 'CA'),
        (Colorado, 'CO'),
        (Connecticut, 'CT'),
        (Delaware, 'DE'),
        (Florida, 'FL'),
        (Georgia, 'GA'),
        (Hawaii, 'HI'),
        (Idaho, 'ID'),
        (Illinois, 'IL'),
        (Indiana, 'IN'),
        (Iowa, 'IA'),
        (Kansas, 'KS'),
        (Kentucky, 'KY')
        (Lousiana, 'LA'),
        (Maine, 'ME'),
        (Maryland, 'MD'),
        (Massachusetts, 'MA'),
        (Michigan, 'MI'),
        (Minnesota, 'MN'),
        (Mississippi, 'MS'),
        (Missouri, 'MO'),
        (Montana, 'MT'),
        (Nebraska, 'NE'),
        (Nevada, 'NV'),
        (NH, 'NH'),
        (NJ, 'NJ'),
        (NM, 'NM'),
        (NY, 'NY'),
        (NC, 'NC'),
        (ND, 'ND'),
        (Ohio, 'OH'),
        (Oklahoma, 'OK'),
        (Oregon, 'OR'),
        (Pennsylvania, 'PA'),
        (RI, 'RI'),
        (SC, 'SC'), 
        (SD, 'SD'),
        (Tennessee, 'TN'),
        (Texas, 'TX'),
        (Utah, 'UT'),
        (Vermont, 'VT'),
        (Virginia, 'VA'),
        (Washington, 'WA'),
        (WV, 'WV'),
        (Wisconsin, 'WI'),
        (Wyoming, 'WY'),
    ]
    city = models.CharField(
        max_length=15,
        choices=city_choices,
        default=none,
    )
    
class Review(models.Model):
   
    one = 'One'
    two = 'Two'
    three = 'Three'
    four = 'Four'
    five = 'Five'
    
    rating_choices = [
        (one, '1 Star'),
        (two, '2 Star'),
        (three, 'Three'),
        (four, 'Four'),
        (five, 'Five')
   ]
   
    rating = models.CharField(
        max_length=15,
        choices=rating_choices,
        default=one
    ) 
   
    review = models.CharField(max_length=300) 
    
    
    