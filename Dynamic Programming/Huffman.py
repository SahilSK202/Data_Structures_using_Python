import numpy as np

def Huffman(p):
    '''Return a Huffman code for an ensemble with distribution p.'''
    assert(round(sum(p.values()) ,2) == 1.0) # Ensure probabilities sum to 1

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(p) == 2):
        return dict(zip(p.keys(), ['0', '1'])) ## for root node

    # Create a new distribution by merging lowest prob. pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p) # keys of lowest prob
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)  # p_prime removes items a1 and a2 , value of items is in p1 & p2
    p_prime[a1 + a2] = p1 + p2 # new item added by combining above

    # Recurse and construct code on new distribution
    c = Huffman(p_prime)
    ca1a2 = c.pop(a1 + a2) # binary values of prev nodes , delete combined node
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1' # divide combined node and attach 0 and 1 to left ,right child resp.

    return c

def lowest_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities.'''
    assert(len(p) >= 2) # Ensure there are at least 2 symbols in the dist.

    sorted_p = sorted(p.items(), key=lambda x: x[1]) # sort dict items by 2nd value of dict
    return sorted_p[0][0], sorted_p[1][0]            # return 1st and 2nd key of sorted dict




def freqdict_to_probdict(freq_dict):
    
    prob = np.array(list(freq_dict.values())) / sum(freq_dict.values())
    new_dict = dict(zip(list(freq_dict.keys()),prob.round(5)))
    return new_dict


def str_to_probdict(my_str):
    import numpy as np
    letters = []
    frequency = []
    
    for letter in my_str:
        if letter not in letters: # for unique letters
            freq = my_str.count(letter)
            frequency.append(freq)
            letters.append(letter)
               
    letters,frequency = np.array(letters),np.array(frequency)      
    prob = np.array(frequency / np.sum(frequency))
    combined_dict = dict(zip(letters,prob))
    return combined_dict



def huffmanDecode (dictionary, text):
    res = ""
    while text:
        for k in dictionary.values():
            if text.startswith(k):
                res += str([key for(key,value) in dictionary.items() if value == k][0])
                text = text[len(k):]
                
    
    return res







################################# DRIVER CODE ######################

print("1.String to Huffman \n2.freq to huffman \n3.Probability to huffman\n4.Huffman Decode")
c = int(input("Please enter your choice  :"))

if (c == 1):
    my_str = input("Please enter a string to compress :")
    print("Your message is : ")
    print(my_str)
    old_size = len(my_str) * 8
    print("Your Data is of " , old_size , "bits !")
    newdict = str_to_probdict(my_str)
    huffmancode = Huffman(newdict)
    print(huffmancode)

    binary = ""

    for letter in my_str:
        binary += str(huffmancode[letter])
        
    print("Binary code is :" ,binary)
    new_size = len(binary)
    print("Your Compressed Data is of" , new_size , "bits !")
    print("you saved" , old_size - new_size , "Bits using Huffman Code for compression !")
    print("Average bits per character : ", round(new_size / len(my_str) ,2))
    print("Compression Ratio for this word is :", int(old_size/new_size) ,": 1")

if  (c == 2):

    n = int(input("Please enter no of items you want in dictionary  :"))

    dict_freq = {}

    for i in range(n):
        key = input("enter key :")
        print("Enter value for key : ",key)
        value = int(input())
        dict_freq[key] = value
        
    print("\n\n",dict_freq)

    old_size = sum(dict_freq.values()) * 8
    print("\nYour Data is of " , old_size , "bits !")
    newdict = freqdict_to_probdict(dict_freq)
    huffmancodedict = Huffman(newdict)


    sorted_old = dict(sorted(dict_freq.items(), key=lambda x: x[0])) # sort dict items by 2nd value of dict
    sorted_new = dict(sorted(huffmancodedict.items(), key=lambda x: x[0])) # sort dict items by 2nd value of dict

    print("\n\nThe Huffman code for given dictionary is : \n",sorted_new)

    new_bits = list(sorted_new.values()) 
    bits_len = np.array([len(i) for i in new_bits])

    len_dict = dict(zip(list(sorted_new.keys()),bits_len))
    print("\n\nThe New length of bits : \n",len_dict)


    freq = np.array(list(sorted_old.values()))

    new_size = sum(freq * bits_len)


    print("\n\nYour Compressed Data is of" , new_size , "bits !")
    print("\nyou saved" , old_size - new_size , "Bits using Huffman Code for compression !")
    print("Average bits per character: ", round(new_size / sum(dict_freq.values()) ,2))
    print("Compression Ratio is :", int(old_size/new_size) ,": 1")



if (c == 3):
    n = int(input("Please enter no of items you want in dictionary  :"))

    dict_prob = {}

    for i in range(n):
        key = input("enter key :")
        print("Enter value for key : ",key)
        value = float(input())
        dict_prob[key] = value
        
    print("\n\n",dict_prob)

    old_size = sum(dict_prob.values()) * 800
    print("\nYour Data is of " , old_size , "bits !")
    huffmancodedict = Huffman(dict_prob)


    sorted_old = dict(sorted(dict_prob.items(), key=lambda x: x[0])) # sort dict items by 2nd value of dict
    sorted_new = dict(sorted(huffmancodedict.items(), key=lambda x: x[0])) # sort dict items by 2nd value of dict

    print("\n\nThe Huffman code for given dictionary is : \n",sorted_new)

    new_bits = list(sorted_new.values()) 
    bits_len = np.array([len(i) for i in new_bits])

    len_dict = dict(zip(list(sorted_new.keys()),bits_len))
    print("\n\nThe New length of bits : \n",len_dict)


    freq = np.array(list(sorted_old.values()))

    new_size = round(sum(freq * bits_len)*100 ,2)


    print("\n\nYour Compressed Data is of" , new_size , "bits !")
    print("\nyou saved" , old_size - new_size , "Bits using Huffman Code for compression !")
    print("Average bits per character : ", round(new_size / 100 ,2))
    print("Compression Ratio is :", int(old_size/new_size) ,": 1")


if (c ==4):
    huffdict = {'a1': '0', 'a2': '10', 'a3': '1110', 'a4': '1111', 'a5': '1101', 'a6': '1100'}
    #huffdict = dict(reversed(list(huffdict.items()))) to reverse the list
    print("Huffman codes are :\n",huffdict)

    huffcode = "0101101010010000011000100"
    print("\nDecode the code : ",huffcode)

    msg = huffmanDecode(huffdict , huffcode)
    print("\nDeocded message is : ",msg)
