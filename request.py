import requests
import json

url = 'http://0.0.0.0:5000/api/'

data = {
 'bank_eq_user_country': 1,
 'authorised_times_cnt': 0,
 'received_date_cnt': 0,
 'billing_addr_date_cnt': 0,
 'delivery_addr_date_cnt': 0,
 'ip_dates_cnt': 0,
 'is_bank_country_89': 0,
 'is_bank_country_105': 0,
 'is_bank_country_6': 1,
 'is_bank_country_68': 0,
 'is_bank_country_45': 0,
 'is_user_country_unknown': 0,
 'is_user_country_6': 0,
 'is_user_country_45': 0,
 'amount_eur': 17,
 'refused_by_adyen_risk': 0,
 'refused_by_bank': 0,
 'is_merchant_Shop1': 1,
 'is_merchant_Shop2': 0,
 'is_merchant_Shop3': 0,
 'is_merchant_Shop4': 0,
 'is_merchant_Shop5': 0,
 'is_merchant_Shop6': 0,
 'is_merchant_Shop7': 0,
 'is_merchant_Shop8': 0,
 'is_merchant_nan': 0,
 'is_card_network_SchemeB': 0,
 'is_card_network_SchemeD': 1,
 'is_card_network_SchemeDA': 0,
 'is_card_network_SchemeDB': 0,
 'is_card_network_SchemeF': 0,
 'is_card_network_SchemeFA': 0,
 'is_card_network_SchemeFB': 0,
 'is_card_network_SchemeG': 0,
 'is_card_network_SchemeH': 0,
 'is_card_network_SchemeI': 0,
 'is_card_network_SchemeIA': 0,
 'is_card_network_nan': 0,
 'is_card_type_CREDIT': 1,
 'is_card_type_DEBIT': 0,
 'is_card_type_DEFFERED_DEBIT': 0,
 'is_card_type_PREPAID': 0,
 'is_card_type_nan': 0,
 'is_device_family_Desktop': 1,
 'is_device_family_GamingConsole': 0,
 'is_device_family_Mobile': 0,
 'is_device_family_Other': 0,
 'is_device_family_Tablet': 0,
 'is_device_family_Unknown': 0,
 'is_device_family_nan': 0,
 'is_device_type_Android Mobile': 0,
 'is_device_type_Android Tablet': 0,
 'is_device_type_MacOS': 1,
 'is_device_type_Nintendo Switch': 0,
 'is_device_type_Other': 0,
 'is_device_type_Unknown': 0,
 'is_device_type_Windows': 0,
 'is_device_type_Windows Mobile': 0,
 'is_device_type_iPad': 0,
 'is_device_type_iPhone': 0,
 'is_device_type_iPod': 0,
 'is_device_type_nan': 0,
 'is_dow_0.0': 1,
 'is_dow_1.0': 0,
 'is_dow_2.0': 0,
 'is_dow_3.0': 0,
 'is_dow_4.0': 0,
 'is_dow_5.0': 0,
 'is_dow_6.0': 0,
 'is_dow_nan': 0,
 'is_hour_0.0': 0,
 'is_hour_1.0': 0,
 'is_hour_2.0': 1,
 'is_hour_3.0': 0,
 'is_hour_4.0': 0,
 'is_hour_5.0': 0,
 'is_hour_6.0': 0,
 'is_hour_7.0': 0,
 'is_hour_8.0': 0,
 'is_hour_9.0': 0,
 'is_hour_10.0': 0,
 'is_hour_11.0': 0,
 'is_hour_12.0': 0,
 'is_hour_13.0': 0,
 'is_hour_14.0': 0,
 'is_hour_15.0': 0,
 'is_hour_16.0': 0,
 'is_hour_17.0': 0,
 'is_hour_18.0': 0,
 'is_hour_19.0': 0,
 'is_hour_20.0': 0,
 'is_hour_21.0': 0,
 'is_hour_22.0': 0,
 'is_hour_23.0': 0,
 'is_hour_nan': 0
}


j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)
