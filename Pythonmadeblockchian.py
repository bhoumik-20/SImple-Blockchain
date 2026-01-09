import hashlib

#Defining Block
class Block:
    def __init__(self,index,data,p_hash):
        self.index = index
        self.data = data
        self.p_hash = p_hash
        self.nonce = 0
        self.hash = self.mine_block()

    def calculate_hash(self):
        block_string = str(self.index) + self.data + self.p_hash + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        print(f"Mining block number {self.index}")
        hash_value = self.calculate_hash()

        while not hash_value.startswith("0000"):
            self.nonce += 1
            hash_value = self.calculate_hash()

        print(f"Block {self.index} mined with nonce {self.nonce}")
        return hash_value


#Creating Blockchain
blockchain=[]

#Genesis Block
genesis_block=Block(0, "Genesis Block", "0")
blockchain.append(genesis_block)

#Blocks 1 and 2
for i in range(1,3,1):
    print(f"\nEnter details for Block {i} :-")
    name = input("Enter Name: ")
    reg_no = input("Enter Registration Number: ")
    branch = input("Enter Branch: ")

    data = f"Name: {name}, Reg_No: {reg_no}, Branch: {branch}"
    previous_hash = blockchain[i - 1].hash

    new_block = Block(i, data, previous_hash)
    blockchain.append(new_block)

#Display Blockchain 

print("\n--- BLOCKCHAIN --- ")
for block in blockchain:
    print("\n----------------------")
    print(f"Index         : {block.index}")
    print(f"Data          : {block.data}")
    print(f"Previous Hash : {block.p_hash}")
    print(f"Nonce         : {block.nonce}")
    print(f"Hash          : {block.hash}")
