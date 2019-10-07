"""boilerinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Import the include() function: from django.conf.urls import url, include
	3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from boilerinfo.views import home, register, change_password
from boilerinfo.forms import FormStepOne, FormStepTwo, FormStepThree, FormStepFour, FormStepFive, FormStepSix, FormStepSeven, FormStepEight, FormStepNine
from boilerinfo.views import FormWizardView, model_form_upload

from boilerinfo.views import edit_Profile_details, show_uploaded_files, quote_generated, quote_emailed, quotepad_template_help
from boilerinfo.views import ProductPriceList, ProductPriceCreate, ProductPriceUpdate, ProductPriceDelete
from boilerinfo.views import generate_quote_from_file, edit_quote_template, list_quote_archive, pdf_view

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	#url(r'^boilerform/$', FormWizardView.as_view([FormStepOne,FormStepTwo])),
	#url(r'^$', home),
	#url(r'^register/', register),
	# url(r'^login/$', auth_views.login),
	url(r'^logout/$', auth_views.logout),
	#url(r'^changepassword/$', change_password, name = 'change_password'),
	#path('', home_view, name='home'),
	path('', home, name='home'),
	path('login/', auth_views.login),
	path('passwordreset/', auth_views.password_reset),
	path('register/', register),

	#path('accounts/', include('accounts.urls')),
	path('boilerinfo/', include('django.contrib.auth.urls')),

	# Below loginredirect/ is in settings.py
	path('loginredirect/', home, name = 'home'),
	path('changepassword/', change_password, name = 'change_password'),
	path('home/', home, name = 'home'),
	path('boilerform/', FormWizardView.as_view([FormStepOne,FormStepTwo,FormStepThree, FormStepFour, FormStepFive, FormStepSix, FormStepSeven, FormStepEight, FormStepNine]), name = 'boilerform'),
	path('generatequotefromfile/<str:outputformat>/<str:quotesource>', generate_quote_from_file, name = 'generate_quote_from_file'),
	#url(r'^', include('boilerform.urls'))
	path('fileupload/', model_form_upload, name = 'file_upload'),
	path('showuploadedfiles/', show_uploaded_files, name = 'show_uploaded_files'),
	path('quotegenerated/', quote_generated, name = 'quote_generated'),
	path('quoteemailed/', quote_emailed, name = 'quote_emailed'),
	path('quotepadtemplatehelp/', quotepad_template_help, name = 'quotepad_template_help'),
	#url(r'^pdf/$', GeneratePDF.as_view()),
	# url(r'^pdf/$', GeneratePDF2, name = 'GenPDF'),
	path('edit_Profile_details/', edit_Profile_details, name = 'edit_Profile_details'),
	#path('listproductsforquote/', list_products_for_quote, name = 'list_products_for_quote'),
	# path('uploadproductpricingfile/', upload_product_pricing_file, name = 'upload_product_pricing_file'),
	path('productpricelist/', ProductPriceList.as_view(), name = 'productpricelist'),
	#path('productpricecreate/', ProductPriceCreate.as_view(), name = 'productpricecreate'),
	path('productpricecreate/', ProductPriceCreate, name = 'productpricecreate'),
	#path('productpriceupdate/<int:pk>/', ProductPriceUpdate.as_view(), name = 'productpriceupdate'),
	path('productpriceupdate/<int:product_id>/', ProductPriceUpdate, name = 'productpriceupdate'),
	path('productpricedelete/<int:pk>/', ProductPriceDelete.as_view(), name = 'productpricedelete'),
	path('editquotetemplate/', edit_quote_template, name = 'editquotetemplate'),
	path('listquotearchive/', list_quote_archive, name = 'listquotearchive'),
	path('pdfview/<str:pdf_file>', pdf_view, name = 'pdfview'),
	path('', include('payments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)