# Simple Blockchain
### This blockchain is formed using basic python script where I have defined a new class **"BLOCK🧊"** with different parameters like *Index* , *Data*, *Previous Hash*, *Nounce*, *Hash*.

## Proof of Work 🔨
### In this blockchain, the proof of work is verified by checking whether the hash for current block starts with **"0️⃣0️⃣0️⃣0️⃣"**, and for this the miners check the hash value for different nonce values.

## Block Mining Process ⛏️

1. Initialize nonce to 0.
2. Compute hash using block data and nonce.
3. Check if hash satisfies difficulty condition.
4. Increment nonce if condition is not met.
5. Repeat until a valid hash is found.
