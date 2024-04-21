def cheapest_cost_of_shipping(weight):
  #Ground shipping normal  
  if weight <= 2:
    cost = weight
    cost*=1.50
    cost += 20
    
  elif weight > 2 and weight <= 6:
    cost = weight
    cost*=3.00
    cost += 20
    
  elif weight > 6 and weight <= 10:
    cost = weight
    cost*=4.00
    cost += 20
    
  elif weight > 10:
    cost = weight
    cost*=4.75
    cost += 20
  ground_shipping = cost
  print(f'''Weight of Object: {weight}
Cost through ground shipping: ${ground_shipping}''')

  #Ground shipping premium
  cost = weight
  cost += 125.00
  ground_shipping_premium = cost
  print(f'''Cost through ground shipping premium: ${ground_shipping_premium}''')

  #Drone shipping
  if weight <= 2:
    cost = weight
    cost*=4.50
    
    
  elif weight > 2 and weight <= 6:
    cost = weight
    cost*=9.00
    
    
  elif weight > 6 and weight <= 10:
    cost = weight
    cost*=12.00
    
    
  elif weight > 10:
    cost = weight
    cost*=14.25
  drone_shipping = cost
  print(f'''Cost through drone shipping: ${drone_shipping}''')

  if ground_shipping < ground_shipping_premium and ground_shipping < drone_shipping :
     cheapest_shipping = ground_shipping
     print(f"Cheapest shipping offerered is ground shipping with ${cheapest_shipping}")
  elif ground_shipping_premium < ground_shipping and ground_shipping_premium < drone_shipping :
     cheapest_shipping = ground_shipping_premium
     print(f"Cheapest shipping offerered is ground shipping premium with ${cheapest_shipping}")
  elif drone_shipping < ground_shipping and drone_shipping < ground_shipping_premium :
     cheapest_shipping = drone_shipping
     print(f"Cheapest shipping offerered is drone shipping with ${cheapest_shipping}")

cheapest_cost_of_shipping(float(input("Weight of item - ")))

