import random


class CuckooHashTable:
    """CuckooHashTable"""
    def __init__(self, capacity, k, cs):
        """
        Initialize the Cuckoo HashTable
        :param capacity: number of Entries
        :param k: number of hash functions
        :param cs: number of cuckoo steps
        """
        self.capacity = capacity
        self.k = k
        self.cs = cs
        self.s = [0 for i in range(k)]
        self.cuckoo_hash_table = [[0, 0] for i in range(self.capacity)]

    def generateKHashFunctions(self):
        """array s[] to compute XOR with flow id"""
        for i in range(len(self.s)):
            self.s[i] = random.randint(0, 1000000000)

    def put(self, flow_id):
        """
        put the flow_id into the hashtable
        :param flow_id:
        :return:
        """
        # no need for cuckoo moving
        for i in range(len(self.s)):
            hash_index = (flow_id ^ self.s[i]) % self.capacity
            # hash collision
            if self.cuckoo_hash_table[hash_index][0] != 0:
                self.cuckoo_hash_table[hash_index][1] += 1
            # no hash collision
            else:
                self.cuckoo_hash_table[hash_index][0] = flow_id
                self.cuckoo_hash_table[hash_index][1] += 1
                return

        # need for cuckoo moving
        for i in range(self.k):
            hash_index = (flow_id ^ self.s[i]) % self.capacity
            existing_flow_id = self.cuckoo_hash_table[hash_index][0]
            if self.move(existing_flow_id, self.cs):
                self.cuckoo_hash_table[hash_index][0] = flow_id
                self.cuckoo_hash_table[hash_index][1] += 1
                return

    # def move(self, existing_flow_id, cs):
    #     """
    #     move the existing flow_id to another place in the hashtable
    #     :param existing_flow_id:
    #     :param cs:
    #     :return:
    #     """
    #     if cs == 0:
    #         return False
    #
    #     for i in range(self.k):
    #         hash_index = (existing_flow_id ^ self.s[i]) % self.capacity
    #         if self.cuckoo_hash_table[hash_index][0] == 0:
    #             self.cuckoo_hash_table[hash_index][0] = existing_flow_id
    #             return True
    #     return self.move(existing_flow_id, cs - 1)
    def move(self, existing_flow_id, cs):
        """
        move the existing flow_id to another place in the hashtable
        :param existing_flow_id:
        :param cs:
        :return:
        """
        if cs == 0:
            return False

        for i in range(self.k):
            hash_index = (existing_flow_id ^ self.s[i]) % self.capacity
            if self.cuckoo_hash_table[hash_index][0] != existing_flow_id and self.cuckoo_hash_table[hash_index][0] == 0:
                self.cuckoo_hash_table[hash_index][0] = existing_flow_id
                return True
        for i in range(self.k):
            if self.cuckoo_hash_table[hash_index][0] != existing_flow_id and self.move(existing_flow_id, cs - 1):
                self.cuckoo_hash_table[hash_index][0] = existing_flow_id
                return True
        return False


if __name__ == "__main__":
    # input
    capacity = input("Please input the capacity of the CuckooHash table: ")
    number_of_flows = input("Please input the number of flows: ")
    k = input("Please input the number of hash functions: ")
    cs = input("Please input the number of cuckoo steps: ")

    hashtable_2 = CuckooHashTable(int(capacity), int(k), int(cs))
    hashtable_2.generateKHashFunctions()

    # 创建flows[]
    flows = [random.randint(0, 1000000000) for i in range(0, int(number_of_flows))]

    # put flow_id into the hash table
    for i in range(int(capacity)):
        hashtable_2.put(flows[i])
    # print(hashtable_2.cuckoo_hash_table)

    # output file
    doc = open('output2.txt', 'w')
    print()
    counter = 0
    for i in range(int(capacity)):
        if hashtable_2.cuckoo_hash_table[i][0] != 0:
            counter += 1
    print("The number of flows in the table: " + str(counter))
    print("The number of flows in the table: " + str(counter), file=doc)

    # print the flow_id of each Entry
    for i in range(int(capacity)):
        print("Entry[" + str(i) + "]->" + "Flow ID: " + str(hashtable_2.cuckoo_hash_table[i][0]))
        print("Entry[" + str(i) + "]->" + "Flow ID: " + str(hashtable_2.cuckoo_hash_table[i][0]), file=doc)

























