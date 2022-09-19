import requests
mynums=[3,7,19,22,39,8]
def nag(lst):
 minusmynums = []
 plusmynums = []
 url="https://api.opap.gr/draws/v3.0/1100/last-result-and-active"
 r = requests.get(url)
 data = r.json()
 result = data["last"]["winningNumbers"]["list"]
 for i in range(len(mynums)):
  minusmynums.append(str(int(mynums[i])-1))
  plusmynums.append(str(int(mynums[i]+1)))
 for i in range(len(minusmynums)):
  mynums.append(minusmynums[i])
  mynums.append(plusmynums[i])
 if set(mynums) & set(result) == set():
  mywinnums="NO WINNING NUMBERS"
 else:
  mywinnums = set(mynums) & set(result)
 y =len(mywinnums)
 return y




nag(mynums)
