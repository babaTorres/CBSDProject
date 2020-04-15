from CBSD_Project_Flask import app, forms
from flask import request, render_template

import locale
locale.setlocale(locale.LC_ALL, "en_US")

@app.route('/', methods=["GET", "POST"])
def search():
    search_form = forms.SymbolSearchForm(request.form)
    if request.method == "POST":
        symbol_requested = search_form.symbol.data
        print("Request sent for " + symbol_requested)
        quote_params = forms.retrieve_quote_parameters(symbol_requested)
        company_params = forms.retrieve_company_parameters(symbol_requested)

        #Quote Params
        company_symbol = quote_params["symbol"]
        company_name = quote_params["companyName"]
        latest_price = quote_params["latestPrice"]
        avg_total_volume = locale.format_string('%.2f', quote_params["avgTotalVolume"], True)[0:]
        market_cap = locale.format_string('%.2f', quote_params["marketCap"], True)
        wk_52_high = locale.format_string('%.2f', quote_params["week52High"], True)
        wk_52_low = locale.format_string('%.2f', quote_params["week52Low"], True)

        #Company Params
        industry = company_params["industry"]
        website = company_params["website"]
        description = company_params["description"]


        return render_template('company_result.html', company_symbol=company_symbol, company_name=company_name,
                               latest_price=latest_price, avg_total_volume = avg_total_volume, market_cap = market_cap,
                               wk_52_high = wk_52_high, wk_52_low = wk_52_low, industry = industry, website = website, description = description)

    return render_template('company_search.html', form=search_form)
