
#ran the program with the different hash function to see the number of comparisons
#then found the avg of the number of comparisons.
hash1 = 4
hash2 = 3
hash3 = 5
hash4 = 0

class HashTableNode:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class HashTable:

    def __init__(self, table_size):
        self.table = [None] * table_size


    #hash function that uses the integer representation of each word to
    #hash it with the size of the table
    def hash(self, word):
        hash = 0
        for i in range(len(word)):
            letter = ord(word[i])
            letter = letter * pow(2,i)
            hash += letter
        return hash % len(self.table)


    def hash2(self, word):
        hash = 0
        for i in range(len(word)):
            letter = ord(word[i])
            letter = letter * pow(5, i)
            hash += letter
        return hash % len(self.table)


    def hash3(self, word):
        hash = 0
        for i in range(len(word)):
            letter = ord(word[i])
            letter = letter * pow(3, i)
            hash += letter
        return hash % len(self.table)

    def hash4(self, word):
        hash = 0
        for i in range(len(word)):
            letter = ord(word[i])
            letter = letter * pow(7, i)
            hash += letter
        return hash % len(self.table)


    def insert(self, k):
        loc = self.hash2(k)
        self.table[loc] = HashTableNode(k, self.table[loc])



    #search method uses a word comparison variable to see how many times
    #it compares itself with a node.
    def search(self, k):
        loc = self.hash2(k)
        word_comparisons = 0

        temp = self.table[loc]

        while temp is not None:
            if temp.item == k:
                return temp, word_comparisons

            word_comparisons += 1
            temp = temp.next

        return word_comparisons



    def get_load_factor(self):

        num_elements = 0
        for i in range(len(self.table)):
            temp = self.table[i]

            while temp is not None:
                num_elements += 1

                temp = temp.next

        return num_elements / len(self.table)





def load_table(word_file):
    word_table = HashTable(446250)

    for line in word_file:
        word = line.strip("\n")
        word_table.insert(word)
    word_file.close()

    return word_table



def avg_num_of_comparison():

    avg = hash1 + hash2 + hash3 + hash4

    return  avg / 4




def main():
    word_file = open("words_alpha.txt", "r")

    table = load_table(word_file)


    print(table.search("post"))

    print(avg_num_of_comparison())



main()








