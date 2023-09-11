import time
from tqdm import tqdm
from mydm import mydm
from custom_mydm import mydm as cmydm

end_lim = 50
slp_tim = 0.05


print("using tqdm")
for i in tqdm(range(end_lim)):
    time.sleep(slp_tim)

print("using mydm")
for i in mydm(range(end_lim)):
    time.sleep(slp_tim)

print("using custom_mydm")
for i in cmydm(range(end_lim)):
    time.sleep(slp_tim)
