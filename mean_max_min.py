
import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 100)

df = pd.read_csv("C:\\Users\\NEAK\\Documents\\Automobile_data.csv")
car_makers = df.groupby('company')
mileage_df = car_makers['company', 'average-mileage'].mean()
print(mileage_df)

car_df = pd.read_csv("C:\\Users\\NEAK\\Documents\\Automobile_data.csv")
cars_df = car_df.sort_values(by=['price', 'horsepower'], ascending=False)
result = cars_df.head(5)
print(result)

import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 100)


german_cars = {'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
cars_df1 = pd.DataFrame.from_dict(german_cars)
japanese_cars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}
cars_df2 = pd.DataFrame.from_dict(japanese_cars)
cars_df = pd.concat([cars_df1, cars_df2], keys=["Germany", "Japan"])
print(cars_df)
print()

Car_price = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'Price':[23845, 17995, 135925, 71400]}
cars_price_Df = pd.DataFrame.from_dict(Car_price)
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'horsepower': [141, 80, 182, 160]}
carHorsepowerDF = pd.DataFrame.from_dict(car_Horsepower)
carsDF = pd.merge(cars_price_Df, carHorsepowerDF, on='Company')
print(carsDF)
