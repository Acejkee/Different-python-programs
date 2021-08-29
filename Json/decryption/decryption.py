"""

В этой задаче вам необходимо раскодировать текст, 
находящийся в данном текстовом файле. 
Ключ для декодирования располагается в json-файле. 
В качестве ответа нужно просто отправить получившийся текст.  
И обратите внимание, что раскодировать нужно только лишь буквы, 
все остальные символы(цифры, знаки пунктуации и т.д.) необходимо выводить как есть.

"""

import json
result = ""
with open(***path to json file***) as file:
    data_txt = open(***path to txt file***)
    data = json.load(file)
    for i in data_txt:
        for j in i:
            if j in data:
                result += data[j]
            else:
                result += j
    print(result)

