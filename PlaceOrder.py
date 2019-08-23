#ImageUpload.py

import csv
import numpy as np
import codecs
import os
import glob
import webbrowser as wb
import requests as rq
import json
import datetime as dt
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1

def PlaceOrder(productid):
	secure_url = "https://grxoogle-com.3dcartstores.com"
	private_key = "57361d1dd5724f6b65af2db61da9"
	token = "03ad2b80314f27cfd"
	version = 1
	service1 = "Orders"
	service2 = "Products"
	host = "https://apirest.3dcart.com"
	#THIS IS THE HOME DIRECTORY FOR THE JSON
	cart_api_json_dir = "D:/cache docs/task/3dcart/3dcart API/" 


	ch_Order = "{}{}{}{}{}".format(host,"/3dCartWebAPI/v",version,"/",service1)
	ch_Order = ch_Order+"/"

	#For getting the product selected by the customer
	ch_Product = "{}{}{}{}{}".format(host,"/3dCartWebAPI/v",version,"/",service2)
	ch_Product = ch_Product+"/"

	order_data = json.load(open(cart_api_json_dir+"OrdeTest.json"))

	###DATA INSERTION### ALL FIELDS BELOW ARE NECESSARY FOR A SUCCESSFUL ORDER
	order_data["InvoiceNumberPrefix"] = "Order-"
	order_data["InvoiceNumber"] = str(dt.datetime.now()) #has to change
	#order_data["OrderID"] = 1993
	#order_data["CustomerID"] = 9
	order_data["OrderStatusID"] = 11
	order_data["OrderType"] = "New"
	order_data["BillingFirstName"] = ""
	order_data["BillingLastName"] = ""
	order_data["BillingCompany"] = ""
	order_data["BillingAddress"] = ""
	order_data["BillingCity"] = "Seattle"
	order_data["BillingState"] = "WA"
	order_data["BillingZipCode"] = "98105"
	order_data["BillingCountry"] = "US"
	order_data["BillingPhoneNumber"] = "54044950577"
	order_data["BillingEmail"] = ""
	order_data["BillingPaymentMethod"] = "Money Order"
	order_data["BillingOnLinePayment"] = False
	order_data["BillingPaymentMethodID"] = "42"
	order_data["ShipmentList"][0]["ShipmentID"] = 0
	order_data["ShipmentList"][0]["ShipmentBoxes"] = 1
	order_data["ShipmentList"][0]["ShipmentOrderStatus"] = 11
	order_data["ShipmentList"][0]["ShipmentAddress"] = "5008 ne 55st"
	order_data["ShipmentList"][0]["ShipmentCity"] = "Seattle"
	order_data["ShipmentList"][0]["ShipmentCost"] = 2
	order_data["ShipmentList"][0]["ShipmentCompany"] = "USPS"
	order_data["ShipmentList"][0]["ShipmentCountry"] = "US"
	order_data["ShipmentList"][0]["ShipmentFirstName"] = "S"
	order_data["ShipmentList"][0]["ShipmentLastName"] = "Pradeep"
	order_data["ShipmentList"][0]["ShipmentMethodID"] = 0
	order_data["ShipmentList"][0]["ShipmentMethodName"] = "Flat Rate"
	order_data["ShipmentList"][0]["ShipmentPhone"] = "54044950577"
	order_data["ShipmentList"][0]["ShipmentState"] = "WA"
	order_data["ShipmentList"][0]["ShipmentZipCode"] = "98105"
	order_data["ShipmentList"][0]["ShipmentWeight"] = 100
	order_data["ShipmentList"][0]["ShipmentEmail"] = ""
	#order_data["OrderItemList"][0]["CatalogID"] = 4435
	#order_data["OrderItemList"][0]["ItemIndexID"] = 0
	order_data["OrderItemList"][0]["ItemID"] = productid
	order_data["OrderItemList"][0]["ItemQuantity"] = 1
	order_data["OrderItemList"][0]["ItemDescription"] = "medicine added through code"
	order_data["OrderItemList"][0]["ItemUnitPrice"] = 56
	order_data["OrderItemList"][0]["ItemWeight"] = 100
	order_data["OrderItemList"][0]["ItemUnitCost"] = 23
	order_data["OrderItemList"][0]["ItemUnitStock"] = 1
	order_data["CardName"] = "S Pradeep"
	###END OF DATA INSERTION###


	headers = {
		"Content-Type":"application/json;charset=UTF-8",
		"Accept":"application/json",
		"SecureUrl":secure_url,
		"PrivateKey":private_key,
		"Token":token
	}

	#get the CatalogID
	CatID="/"+str(order_data["OrderItemList"][0]["CatalogID"])

	order_data = json.dumps(order_data,indent=1,sort_keys=False)
	#POST the order to 3dcart store
	r=rq.post(ch_Order,headers=headers,data=order_data)
	print(r.text)

	"""
	#GET the product ID for the ordered product
	r_getProd = rq.get(ch_Product+CatID,headers=headers)
	print("MFG ID being ordered is: ")
	print(r_getProd.json()[0]['MFGID'])
	"""

product_id = input("Enter the product ID: (type number between 1 to 150)\n")
PlaceOrder(product_id)


