#Sal's Shipping
#Calvin Le Roux

weight = 41.5

#Ground_Shipping:

if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping Cost: $", cost_ground)

premium_ground_shipping_cost = 125

print("Premium Ground Shipping Cost: $", premium_ground_shipping_cost)

# Drone Shipping

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Drone Shipping Cost: $", cost_drone)







