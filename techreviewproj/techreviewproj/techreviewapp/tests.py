from django.test import TestCase
from django.urls import reverse # goes to page and looks back
from django.contrib.auth.models import User
from .models import TechType, Product, Review #import models
import datetime
from .forms import ProductForm

#tests below:
class TechTypeCase(TestCase): #You need tests in every program.() = Inherhited. 
    def test_string(self): # classes need self
        type= TechType(techtypename="laptop")
        self.assertEqual(str(type), type.techtypename) # "","" means string is equal to typename

    def test_table(self):
        self.assertEqual(str(TechType._meta.db_table), "techtype")

class ProductTest(TestCase):
    def setUp(self):
        self.type=TechType(techtypename="tablet")
        self.prod=Product(productname="Ipad", techtype=self.type, productprice=800.00) # in python, you need self.____ 

    def test_string(self):
        self.assertEqual(str(self.prod), self.prod.productname)
    
    def test_type(self):
        self.assertEqual(str(self.prod.techtype), "tablet")

    def test_discount(self):
        self.assertEqual(self.prod.memberDiscount(), 40.0) #5% member discount

#tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetProductsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.type=TechType.objects.create(techtypename="laptop")
        self.prod=Product.objects.create(productname="product1", techtype=self.type,
        user=self.u, productprice=500.00, productentrydate="2019-04-02",
        productdescription="some kind of laptop")

        def test_product_detail_success(self):
            response=self.client.get(reverse('productdetail'), args=(self.prod.id))
            self.assertEqual(response.status_code, 200)

class ProductFormTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='user1', password='P@ssw0rd1')
        self.type=TechType.objects.create(techtypename="type1")
    def test_productForm(self):
        data={
            'productname' : 'product1',
            'techttype' : self.type,
            'user' : self.user,
            'productprice' : 200.00,
            'productentrydate' : datetime.date(2019,5,28),
        }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid)

    def test_productFormInvalid(self):
        data={
            'productname' : 'product1',
            'techttype' : 'type1',
            'user' : self.user2,
            'productentrydate' : datetime.date(2019,5,28),
        }
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid())
 



# Create your tests here.
#python manage.py test -v 2 
# ^ this command will test w/ more details/info due to -v 2