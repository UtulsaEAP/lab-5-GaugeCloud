def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   total_cost = miles_driven * (dollars_per_gallon / miles_per_gallon)
   return(total_cost)

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon,miles_driven = 10):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon,miles_driven = 50):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon,miles_driven = 400):.2f}')
    #print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
   