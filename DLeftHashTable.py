import random


class Segment:
    """segments of d-left hash table"""
    def __init__(self, seg_capacity):
        self.seg_capacity = seg_capacity
        self.seg_hash_table = [[0, 0] for i in range(self.seg_capacity)]


class DLeftHashTable:
    """DLeftHashTable"""

    def __init__(self, capacity, segments):
        """
        Initialize
        :param capacity: number of Entries of this hash table
        :param segments: number of segments of this hash table
        """
        self.segments = segments
        self.capacity = capacity
        self.seg_capacity = int(capacity / segments)
        self.s = [0 for i in range(segments)]
        self.d_left_hash_table = [Segment(self.seg_capacity) for i in range(self.segments)]
        self.generateKHashFunctions()

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
            hash_index = (flow_id ^ self.s[i]) % self.seg_capacity
            if self.d_left_hash_table[i].seg_hash_table[hash_index][0] != 0:  # hash collision
                self.d_left_hash_table[i].seg_hash_table[hash_index][1] += 1
            else:  # no hash collision
                self.d_left_hash_table[i].seg_hash_table[hash_index][0] = flow_id
                self.d_left_hash_table[i].seg_hash_table[hash_index][0] += 1
                return


if __name__ == "__main__":

    # input
    capacity = int(input("Please input the capacity of the DLeftHashTable: "))
    number_of_flows = int(input("Please input the number of flows: "))
    segments = int(input("Please input the number of segments: "))

    hashtable_3 = DLeftHashTable(capacity, segments)

    # 创建flows[]
    flows = [random.randint(0, 1000000000) for i in range(int(number_of_flows))]

    # put the flow_id into the Hash Table
    for i in range(capacity):
        hashtable_3.put(flows[i])

    # for i in range(len(hashtable_3.s)):
    #     print(hashtable_3.d_left_hash_table[i].seg_hash_table)

    # output file
    doc = open('output3.txt', 'w')
    print()
    counter = 0
    for i in range(segments):
        for j in range(int(capacity/segments)):
            if hashtable_3.d_left_hash_table[i].seg_hash_table[j][0] != 0:
                counter += 1
    print("The number of flows in the table: " + str(counter))
    print("The number of flows in the table: " + str(counter), file=doc)

    # print the flow_id of each Entry
    for i in range(segments):
        for j in range(int(capacity/segments)):
            print("Entry[" + str(i) + "][" + str(j) + "]->"
                  + "Flow ID: " + str(hashtable_3.d_left_hash_table[i].seg_hash_table[j][0]))
            print("Entry[" + str(i) + "][" + str(j) + "]->"
                  + "Flow ID: " + str(hashtable_3.d_left_hash_table[i].seg_hash_table[j][0]), file=doc)







