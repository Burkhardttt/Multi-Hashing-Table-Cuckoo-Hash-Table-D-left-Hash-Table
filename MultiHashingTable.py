import random


class MultiHashingTable:
    """MultiHashingTable"""
    def __init__(self, capacity, k):
        """
        Initialize
        :param capacity: number of Entries(size of the hash table)
        :param k: number of hash functions
        """
        self.capacity = capacity
        self.k = k
        self.s = [0 for i in range(k)]  # k个hash function就需要一个长度为k的s[]数组
        self.multi_hash_table = [[0, 0] for i in range(self.capacity)]

    def generateKHashFunctions(self):
        """
        array s[] to compute XOR with flow ID
        :return:
        """
        for i in range(len(self.s)):
            self.s[i] = random.randint(0, 100000000)

    def put(self, flow_id):
        """
        put the flow_id into the hash table
        :param flow_id:
        :return:
        """
        for i in range(len(self.s)):
            hash_index = (flow_id ^ self.s[i]) % self.capacity
            if self.multi_hash_table[hash_index][0] != 0:  # 发生冲突
                self.multi_hash_table[hash_index][1] += 1
            else:  # 没有冲突
                self.multi_hash_table[hash_index][0] = flow_id
                self.multi_hash_table[hash_index][1] += 1
                return


if __name__ == "__main__":

    # input
    capacity = input("Please input the capacity of the MultiHashing table: ")
    number_of_flows = input("Please input the number of flows: ")
    k = input("Please input the number of hash functions: ")

    hashtable_1 = MultiHashingTable(int(capacity), int(k))
    hashtable_1.generateKHashFunctions()

    # 创建flows[]
    flows = [random.randint(0, 100000000) for i in range(0, int(number_of_flows))]

    # put flow_id into the Hash Table
    for i in range(int(capacity)):
        hashtable_1.put(flows[i])
    # print(hashtable_1.multi_hash_table)

    # output file
    print()
    doc = open('output1.txt', 'w')
    counter = 0
    for i in range(int(capacity)):
        if hashtable_1.multi_hash_table[i][0] != 0:
            counter += 1
    print("The number of flows in the table: " + str(counter))
    print("The number of flows in the table: " + str(counter), file=doc)

    # print the flow_id of each Entry
    for i in range(int(capacity)):
        print("Entry[" + str(i) + "]->" + "Flow ID: " + str(hashtable_1.multi_hash_table[i][0]))
        print("Entry[" + str(i) + "]->" + "Flow ID: " + str(hashtable_1.multi_hash_table[i][0]), file=doc)