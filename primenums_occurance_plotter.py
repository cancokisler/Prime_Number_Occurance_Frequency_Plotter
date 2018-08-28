import pandas as pd
import matplotlib.pyplot as plt
import math

file = open('prime_numbers.csv', 'w')
primes_list = [2]
limit = 1000
a = 0
for i in range(3, limit):
    gate = True
    if i % 2 == 0:
        gate = False
        continue
        ##
    for j in range(2, int(math.sqrt(i))+1):
        ##math.sqrt(i) + 1 --> because you only need to check until the number's sqr root.
        if i % j == 0:
            gate = False
            break

        if i % j != 0:
            pass
    if gate:
        primes_list.append(i)
        print(i)

file.write('prime_num')
for b in primes_list:
    file.write("\n" + str(b))
    print(b)
file.close()

df = pd.read_csv('prime_numbers.csv')
df2 = df.prime_num.tolist()
data = {}

upper_range = int(math.ceil(float(df2[-1] / 100)))
for counter in range(upper_range):
    data[counter * 100] = 0
    for i in range(len(df2)):

        if df2[i] > (counter * 100):
            break
        if df2[i] <= (counter * 100) and df2[i] > ((counter - 1) * 100):
            data[counter * 100] += 1

print(data)
x, y = zip(*sorted(data.items()))
plt.style.use('grayscale')
plt.ylabel('Prime Number Occurance Frequency')
plt.xlabel('Range of Num from X-100 to X')
plt.title('Frequency of Prime Number Occurances Between x-100 and x')
plt.plot(x, y)
plt.grid()
plt.show()
