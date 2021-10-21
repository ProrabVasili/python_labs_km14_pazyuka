format_tuple = (37.863, 'Brent', 3, 62.887, 1, 11)
print(f"The price of {format_tuple[1]} crude oil fell to $ {round(format_tuple[0],2)} per barrel, setting a {format_tuple[2]}-month anti-record. The current price is only {round(format_tuple[3],2)}% of last year's {format_tuple[1]} oil price on the same day ({str(format_tuple[-2]).zfill(2)}.{format_tuple[-1]})")
