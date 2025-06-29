def folding_technique(integer):
    integer = integer.replace('-', '')[:12]
    groups = [integer[i:i+4] for i in range(0, len(integer), 4)]
    reversed_groups = [int(i[::-1]) for i in groups]
    hash_code = sum(reversed_groups)
    return hash_code

def main():
    integer = input("Enter your IC number: ")
    print(folding_technique(integer))
    
if __name__ == '__main__':
    main()