# custom-tqdm

A simple Python implementation of the very popular progress bar, `tqdm`.  

## Usage
```python
import time
from tqdm import tqdm
from mydm import mydm
from custom_mydm import mydm as cmydm

# using tqdm (original)
for i in tqdm(range(100)):
    time.sleep(0.5)

# using mydm (reimplementing the original tqdm)
for i in mydm(range(100)):
    time.sleep(0.5)

# using custom_mydm (customized version of mydm)
for i in cmydm(range(100)):
    time.sleep(0.5)
```

You can edit `custom_mydm.py` and make your very own customized `tqdm` progress bar!
