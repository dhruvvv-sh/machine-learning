import pandas as pd
dataset = {
    'cars': ["BMW", "Volvo", "Ford"],
  'fuel capacity in litres': [3, 7, 2]
}
myvar = pd.DataFrame(dataset)
print(myvar)