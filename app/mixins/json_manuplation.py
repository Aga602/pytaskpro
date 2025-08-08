import json
from dataclasses import dataclass
from collections import Counter

@dataclass
class Json:
    def count_duplicates(self,path):
        try:
            with open(path,"r") as file:
                check_dups = json.load(file)
                list_of_keys = []
                for dics in check_dups:
                    for k,v in dics.items():
                        list_of_keys.append(k)
                print(Counter(list_of_keys))
        except Exception as e:
            raise e
