from CBSD_Project_Flask import app, forms
from flask import request, render_template


@app.route('/', methods=["GET", "POST"])
def search():
    search_form = forms.SymbolSearchForm(request.form)
    if request.method == "POST":
        symbol_requested = search_form.symbol.data
        print("Request sent for " + symbol_requested)
        quote_params = forms.retrieve_quote_parameters(symbol_requested)

        company_symbol = quote_params["symbol"]
        company_name = quote_params["companyName"]
        latest_price = quote_params["latestPrice"]
        return render_template('company_result.html', company_symbol=company_symbol, company_name=company_name,
                               latest_price=latest_price)

    return render_template('company_search.html', form=search_form)
