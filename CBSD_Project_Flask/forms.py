from CBSD_Project_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms import StringField

class SymbolSearchForm(FlaskForm):
    symbol = StringField(u"Enter stock symbol")

    '''
    Complete this class with the appropriate parameters inside SelectField for the dropdown menu
    '''
def retrieve_quote_parameters(symbol):
    #Concatenate stuff to send out the request.
    base_url = "https://cloud.iexapis.com/stable/stock/" + symbol + "/quote"
    iex_key = main_functions.read_from_file("CBSD_Project_Flask/JSON_Files/iex_key.json")["iex_key"]
    request_url = base_url + "?token=" + iex_key
    #JSON Stuff
    response_json = requests.get(request_url).json() #Get the json based on the URL
    main_functions.save_to_file(response_json, "CBSD_Project_Flask/JSON_Files/retrieve_quote.json") #Save the json to file
    response_json_file = main_functions.read_from_file("CBSD_Project_Flask/JSON_Files/retrieve_quote.json") #Read back from the file

    #Parse to dictionary
    params = {"companyName":  response_json_file["companyName"],
              "latestPrice" : response_json_file["latestPrice"],
              "avgTotalVolume": response_json_file["avgTotalVolume"],
              "marketCap": response_json_file["marketCap"],
              "week52High": response_json_file["week52High"],
              "week52Low": response_json_file["ytdChange"]}

    return params

def retreive_company_parameters(symbol):
    base_url = "https://cloud.iexapis.com/stable/stock/" + symbol + "/company"
    iex_key = main_functions.read_from_file("CBSD_Project_Flask/JSON_Files/iex_key.json")["iex_key"]
    request_url = base_url + "?token=" + iex_key
    #JSON Stuff
    response_json = requests.get(request_url).json() #Get the json based on the URL
    main_functions.save_to_file(response_json, "CBSD_Project_Flask/JSON_Files/retrieve_company.json") #Save the json to file
    response_json_file = main_functions.read_from_file("CBSD_Project_Flask/JSON_Files/retrieve_company.json") #Read back from the file

    params = {"industry": response_json_file["industry"],
              "website": response_json_file["website"],
              "description":response_json_file["description"]}
    return params
