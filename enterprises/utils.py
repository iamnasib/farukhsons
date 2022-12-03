def invoice_data_processor(invoice_post_data):
    print(invoice_post_data)
    processed_invoice_data = {}

    processed_invoice_data['invoice_number'] = invoice_post_data['invoice-number']
    processed_invoice_data['invoice_date'] = invoice_post_data['invoice-date']

    processed_invoice_data['invoice_order_number'] = invoice_post_data['invoice-order-number']
    processed_invoice_data['invoice_order_number_2'] = invoice_post_data['invoice-order-number-2']
    processed_invoice_data['invoice_to'] = invoice_post_data['invoice-to']
    processed_invoice_data['invoice_heading'] = invoice_post_data['invoice-heading']
    processed_invoice_data['gst_rate'] = invoice_post_data['gst-rate']



    processed_invoice_data['items'] = []

    processed_invoice_data['invoice_total_amt'] = float(invoice_post_data['invoice-total-amt'])


    invoice_post_data = dict(invoice_post_data)
    for idx, product in enumerate(invoice_post_data['invoice-product']):
        if product:
            print(idx, product)
            item_entry = {}
            item_entry['invoice_product'] = product
            if invoice_post_data['invoice-qty'][idx]:
                item_entry['invoice_qty'] = int(invoice_post_data['invoice-qty'][idx])
            else:
                item_entry['invoice_qty'] = 0
            
            item_entry['invoice_unit'] = invoice_post_data['invoice-unit'][idx]
            item_entry['invoice_product_rate'] = invoice_post_data['invoice-product-rate'][idx]
            item_entry['invoice_product_amt'] = invoice_post_data['invoice-product-amt'][idx]

            

            processed_invoice_data['items'].append(item_entry)

    return processed_invoice_data