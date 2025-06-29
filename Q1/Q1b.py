from datetime import timedelta, datetime
import random

def generate_random_birthdate():
    start_date = datetime(1940, 1, 1)
    end_date = datetime.now()
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    birth_date = start_date + timedelta(days=random_days)
    return birth_date.strftime("%y%m%d")
    
birthplace_code = [
    '01', '21', '22', '23', '24',               #Johor
    '02', '25', '26', '27',                     #Kedah
    '03', '28', '29',                           #Kelantan
    '04', '30',                                 #Malacca
    '05', '31', '59',                           #Negeri Sembilan
    '06', '32', '33',                           #Pahang
    '07', '34', '35',                           #Penang
    '08', '36', '37', '38', '39',               #Perak
    '09', '40',                                 #Perlis
    '10', '14', '15', '16', '41', '54', '58',   #Federal Territory
    '42', '55', '43', '56', '44', '57',
    '11', '45', '46',                           #Terengganu
    '12', '47', '48', '49',                     #Sabah
    '13', '50', '51', '52', '53'                #Sarawak
]

def generate_ic_number():
    birth_date = generate_random_birthdate()
    state_code = random.choice(birthplace_code)
    serial = random.randint(1,9999)
    return f"{birth_date}{state_code}{serial:04d}"

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
    
    def insert_item(self, data):
        index = self.hash_function(data)
        self.table[index].append(data)
    
    def hash_function(self, integer):
        groups = [str(integer)[i:i+4] for i in range(0, len(integer), 4)]
        reversed_groups = [int(i[::-1]) for i in groups]
        hash_code = sum(reversed_groups)
        return hash_code % self.capacity 
    
    def display_hash(self):
        for i in range(self.capacity):
            print(f"Table with index {i}", end="")
            for value in self.table[i]:
                print(f" --> {value}", end="")
            print()
    
    def count_collisions(self):
        collisions = 0
        for bucket in self.table:
            if len(bucket)>1:
                collisions += len(bucket) - 1
        return collisions

def main():
    size1 = 1009
    size2 = 2003
    hash1 = HashTable(size1)
    hash2 = HashTable(size2)
    round = 10
    count1 = []
    count2 = []
    prev_collision1 = 0
    prev_collision2 = 0
    for x in range(round):
        for i in range(1000):
            ic = generate_ic_number()
            hash1.insert_item(ic)
            hash2.insert_item(ic)
        c1 = hash1.count_collisions()
        c2 = hash2.count_collisions()
        count1.append(c1 - prev_collision1)
        count2.append(c2 - prev_collision2)
        prev_collision1 = c1
        prev_collision2 = c2
    avr1 = sum(count1)/round
    avr2 = sum(count2)/round
    hash1.display_hash()
    print("\nHash table with size 1009")
    for i in range(round):
        print(f"Total collisions for round {i+1}: {count1[i]}")
    print("\nHash table with size 2003")
    for i in range(round):
        print(f"Total collisions for round {i+1}: {count2[i]}")
    print(f"\nAverage collision for hash table with size 1009 is {avr1}")
    print(f"Average collision for hash table with size 2003 is {avr2}")

if __name__=="__main__":
    main()
