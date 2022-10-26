from sqlalchemy import null, false, true, desc

from assoc_files import db
from assoc_files.database.modal import OrderTable

data = {
        "id": 4893196583145,#OrderId 4. column
        "admin_graphql_api_id": "gid://shopify/Order/4893196583145",
        "app_id": 580111,
        "browser_ip": "176.232.59.47",
        "buyer_accepts_marketing": true,
        "cancel_reason": null,
        "cancelled_at": null,
        "cart_token": "321ddfba02f618f96356c5569c7c0fab",
        "checkout_id": 33279732842729,
        "checkout_token": "56329a289ee593a310b057e8ec6a5c13",
        "client_details": {
            "accept_language": "tr-TR",
            "browser_height": null,
            "browser_ip": "176.232.59.47",
            "browser_width": null,
            "session_hash": null,
            "user_agent": "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908E) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36"
        },
        "closed_at": null,
        "confirmed": true,
        "contact_email": "trr676789@gmail.com",
        "created_at": "2022-09-27T17:22:30+03:00",#OrderDate
        "currency": "TRY",
        "current_subtotal_price": "875.00",
        "current_subtotal_price_set": {
            "shop_money": {
                "amount": "875.00",
                "currency_code": "TRY"
            },
            "presentment_money": {
                "amount": "875.00",
                "currency_code": "TRY"
            }
        },
        "current_total_discounts": "0.00",
        "current_total_discounts_set": {
            "shop_money": {
                "amount": "0.00",
                "currency_code": "TRY"
            },
            "presentment_money": {
                "amount": "0.00",
                "currency_code": "TRY"
            }
        },
        "current_total_duties_set": null,
        "current_total_price": "875.00",
        "current_total_price_set": {
            "shop_money": {
                "amount": "875.00",
                "currency_code": "TRY"
            },
            "presentment_money": {
                "amount": "875.00",
                "currency_code": "TRY"
            }
        },
        "current_total_tax": "64.81",
        "current_total_tax_set": {
            "shop_money": {
                "amount": "64.81",
                "currency_code": "TRY"
            },
            "presentment_money": {
                "amount": "64.81",
                "currency_code": "TRY"
            }
        },
        "customer_locale": "tr-TR",
        "device_id": null,
        "discount_codes": [],
        "email": "trr676789@gmail.com",
        "estimated_taxes": false,
        "financial_status": "paid",
        "fulfillment_status": null, #Order Status
        "gateway": "iyzico - Kredi ve Banka Kartları",
        "landing_site": "/collections/giyim-yeni-sezon?gclid=CjwKCAjwvsqZBhAlEiwAqAHElThi2W4_lEcQiBKes5G4gBJ_5qKhrj38IirRY3P37pz8XpXoU1buhBoC1kwQAvD_BwE",
        "landing_site_ref": null,
        "location_id": null,
        "name": "#35712",#OrderName
        "note": null,
        "note_attributes": [
            {
                "name": "language",
                "value": "tr"
            }
        ],
        "number": 34712,
        "order_number": 35712,
        "order_status_url": "https://www.viadellerose.com/26161709108/orders/69eb65c1db82b8b57a4d7dd49bcf0981/authenticate?key=30a5b8a8b293a648b151ec1b8eacebd6",
        "original_total_duties_set": null,
        "payment_gateway_names": [
            "iyzico - Kredi ve Banka Kartları"
        ],
        "phone": null,
        "presentment_currency": "TRY",
        "processed_at": "2022-09-27T17:22:28+03:00",
        "processing_method": "offsite",
        "reference": "c6c35e818bf7defd7e1ff41403f1faba",
        "referring_site": "https://www.google.com/",
        "source_identifier": "c6c35e818bf7defd7e1ff41403f1faba",
        "source_name": "web",
        "source_url": null,
        "subtotal_price": "875.00",
        "subtotal_price_set": {
            "shop_money": {
                "amount": "875.00",
                "currency_code": "TRY"
            },
            "presentment_money": {
                "amount": "875.00",
                "currency_code": "TRY"
            }
        },
        "tags": "",
        "tax_lines": [
            {
                "price": "64.81",
                "rate": 0.08,
                "title": "KDV",
                "price_set": {
                    "shop_money": {
                        "amount": "64.81",
                        "currency_code": "TRY"
                    },
                    "presentment_money": {
                        "amount": "64.81",
                        "currency_code": "TRY"
                    }
                },
                "channel_liable": false
            }
        ],
        "taxes_included": true,
        "test": false,
        "token": "69eb65c1db82b8b57a4d7dd49bcf0981",
        "total_discounts": "0.00",
        "total_discounts_set": {
            "shop_money": {
                "amount": "0.00",
                "currency_code": "TRY"
            },
            "presentment_money": {
                "amount": "0.00",
                "currency_code": "TRY"
            }
        },
        "total_line_items_price": "875.00",
        "total_line_items_price_set": {
            "shop_money": {
                "amount": "875.00",
                "currency_code": "TRY"
            },
            "presentment_money": {
                "amount": "875.00",
                "currency_code": "TRY"
            }
        },
        "total_outstanding": "0.00",
        "total_price": "875.00",
        "total_price_set": {
            "shop_money": {
                "amount": "875.00",
                "currency_code": "TRY"
            },
            "presentment_money": {
                "amount": "875.00",
                "currency_code": "TRY"
            }
        },
        "total_price_usd": "47.38",
        "total_shipping_price_set": {
            "shop_money": {
                "amount": "0.00",
                "currency_code": "TRY"
            },
            "presentment_money": {
                "amount": "0.00",
                "currency_code": "TRY"
            }
        },
        "total_tax": "64.81",
        "total_tax_set": {
            "shop_money": {
                "amount": "64.81",
                "currency_code": "TRY"
            },
            "presentment_money": {
                "amount": "64.81",
                "currency_code": "TRY"
            }
        },
        "total_tip_received": "0.00",
        "total_weight": 0,
        "updated_at": "2022-09-27T17:22:33+03:00",
        "user_id": null,
        "billing_address": {
            "first_name": "Anna",
            "address1": "Çağlayan mahallesi Barınaklar bulvarı 2070 sokak no.19 Pascha oto yıkama",
            "phone": "546 513 08 85",
            "city": "Antalya",
            "zip": "7230",
            "province": null,
            "country": "Turkey",
            "last_name": "Andriyanenko",
            "address2": "Muratpaşa",
            "company": null,
            "latitude": null,
            "longitude": null,
            "name": "Anna Andriyanenko",
            "country_code": "TR",
            "province_code": null
        },
        "customer": {
            "id": 6071845552361,
            "email": "trr676789@gmail.com",
            "accepts_marketing": true,
            "created_at": "2022-02-02T17:26:43+03:00",
            "updated_at": "2022-09-27T17:22:30+03:00",
            "first_name": "Anna",
            "last_name": "Andriyanenko",
            "orders_count": 2,
            "state": "enabled",
            "total_spent": "1110.00",
            "last_order_id": 4893196583145,
            "note": null,
            "verified_email": true,
            "multipass_identifier": null,
            "tax_exempt": false,
            "tags": "",
            "last_order_name": "#35712",
            "currency": "TRY",
            "phone": null,
            "accepts_marketing_updated_at": "2022-02-02T17:26:43+03:00",
            "marketing_opt_in_level": "single_opt_in",
            "tax_exemptions": [],
            "sms_marketing_consent": null,
            "admin_graphql_api_id": "gid://shopify/Customer/6071845552361",
            "default_address": {
                "id": 7937671954665,
                "customer_id": 6071845552361,
                "first_name": "Anna",
                "last_name": "Andriyanenko",
                "company": null,
                "address1": "Çağlayan mahallesi Barınaklar bulvarı 2070 sokak no.19 Pascha oto yıkama",
                "address2": "Muratpaşa",
                "city": "Antalya",
                "province": null,
                "country": "Turkey",
                "zip": "7230",
                "phone": "546 513 08 85",
                "name": "Anna Andriyanenko",
                "province_code": null,
                "country_code": "TR",
                "country_name": "Turkey",
                "default": true
            }
        },
        "discount_applications": [],
        "fulfillments": [],
        "line_items": [
            {
                "id": 12417543930089,
                "admin_graphql_api_id": "gid://shopify/LineItem/12417543930089",
                "fulfillable_quantity": 1,
                "fulfillment_service": "manual",
                "fulfillment_status": null,
                "gift_card": false,
                "grams": 0,
                "name": "YEŞİL CEKET 10320 - L",
                "origin_location": {
                    "id": 3202241822871,
                    "country_code": "TR",
                    "province_code": "",
                    "name": "MEHMET NESIH OZMEN MAH. KESTANE SOK. NO:13 K:2",
                    "address1": "MEHMET NESIH OZMEN MAH. KESTANE SOK. NO:13 K:2",
                    "address2": "ERSU İŞ HANI MERTER GÜNGÖREN",
                    "city": "Istanbul",
                    "zip": "34173"
                },
                "price": "875.00",
                "price_set": {
                    "shop_money": {
                        "amount": "875.00",
                        "currency_code": "TRY"
                    },
                    "presentment_money": {
                        "amount": "875.00",
                        "currency_code": "TRY"
                    }
                },
                "product_exists": true,
                "product_id": 7203530702999,
                "properties": [],
                "quantity": 1,
                "requires_shipping": true,
                "sku": "7887800306197",
                "taxable": true,
                "title": "YEŞİL CEKET 10320",
                "total_discount": "0.00",
                "total_discount_set": {
                    "shop_money": {
                        "amount": "0.00",
                        "currency_code": "TRY"
                    },
                    "presentment_money": {
                        "amount": "0.00",
                        "currency_code": "TRY"
                    }
                },
                "variant_id": 41152139493527,
                "variant_inventory_management": "shopify",
                "variant_title": "L",
                "vendor": "#VDR",
                "tax_lines": [
                    {
                        "channel_liable": false,
                        "price": "64.81",
                        "price_set": {
                            "shop_money": {
                                "amount": "64.81",
                                "currency_code": "TRY"
                            },
                            "presentment_money": {
                                "amount": "64.81",
                                "currency_code": "TRY"
                            }
                        },
                        "rate": 0.08,
                        "title": "KDV"
                    }
                ],
                "duties": [],
                "discount_allocations": []
            }
        ],
        "payment_terms": null,
        "refunds": [],
        "shipping_address": {
            "first_name": "Anna",
            "address1": "Çağlayan mahallesi Barınaklar bulvarı 2070 sokak no.19 Pascha oto yıkama",
            "phone": "546 513 08 85",
            "city": "Antalya",
            "zip": "7230",
            "province": null,
            "country": "Turkey",
            "last_name": "Andriyanenko",
            "address2": "Muratpaşa",
            "company": "Armonika",
            "latitude": null,
            "longitude": null,
            "name": "Anna Andriyanenko",# Customer name
            "country_code": "TR",
            "province_code": null
        },
        "shipping_lines": [
            {
                "id": 4057522110697,
                "carrier_identifier": "650f1a14fa979ec5c74d063e968411d4",
                "code": "Kargo Bedava",
                "delivery_category": null,
                "discounted_price": "0.00",
                "discounted_price_set": {
                    "shop_money": {
                        "amount": "0.00",
                        "currency_code": "TRY"
                    },
                    "presentment_money": {
                        "amount": "0.00",
                        "currency_code": "TRY"
                    }
                },
                "phone": null,
                "price": "0.00",
                "price_set": {
                    "shop_money": {
                        "amount": "0.00",
                        "currency_code": "TRY"
                    },
                    "presentment_money": {
                        "amount": "0.00",
                        "currency_code": "TRY"
                    }
                },
                "requested_fulfillment_service_id": null,
                "source": "shopify",
                "title": "Kargo Bedava",
                "tax_lines": [
                    {
                        "channel_liable": false,
                        "price": "0.00",
                        "price_set": {
                            "shop_money": {
                                "amount": "0.00",
                                "currency_code": "TRY"
                            },
                            "presentment_money": {
                                "amount": "0.00",
                                "currency_code": "TRY"
                            }
                        },
                        "rate": 0.18,
                        "title": "KDV"
                    }
                ],
                "discount_allocations": []
            }
        ]
    }


orderData = data["shipping_address"]

orders = OrderTable.query.filter_by(userId=5).order_by(desc(OrderTable.orderDate)).all()

for i in orders:
    print(i.orderDate)
