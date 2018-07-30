# -*- coding: utf-8 -*-
def _cleanup_orders(txtfile):
    orders_file = open(txtfile, 'r+')
    lines = orders_file.readlines()
    orders_file.seek(0)
    for line in lines:
        if line.startswith(('\t0', '\t1', '\t2', '\t3', '\t4', '\t5', '\t6', '\t7', '\t8', '\t9')):
            orders_file.write(line)
    orders_file.close()
    return True


def _cleanup_capacity(txtfile):
    cap_file = open(txtfile, 'r')
    lines = cap_file.readlines()
    cap_file.seek(0)
    add_header = False
    for line in lines:
        # This if is only for keep the headers of the report
        if line.startswith(('\tMaterial')) == True and add_header == False:
            cap_file.write(line)
            add_header = True
        if line.startswith((' ', '\tMaterial')) == False and line.startswith((' ', '\t')):
            cap_file.write(line)
    cap_file.close()
    return True


def _main():
    import datetime as dt
    orders = 'C:/path/to/tsvfiles/orders_file_%s.txt' % dt.datetime.today().strftime('%m%d')
    capacity = 'C:/path/to/tsvfiles/capacity_file_%s.txt' % dt.datetime.today().strftime('%m%d')
    print('Done' if _cleanup_orders(orders) | _cleanup_capacity(capacity) else 'Something is wrong')


_main()
