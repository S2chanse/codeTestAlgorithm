from chained_hash import ChainHash

hash = ChainHash(13)

hash.add(14,14)
hash.add(29,29)
hash.add(69,69)
hash.add(17,17)
hash.add(5,5)
hash.add(6,6)
hash.add(20,20)
hash.add(33,33)

print(hash.dump())