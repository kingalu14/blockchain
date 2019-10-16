# Initializing our (empty) blockchain list
blockchain = []
open_transaction = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1 :
       return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]

def mine_block():
    pass


def add_value(transaction_amount, last_transaction=[1]):
    """ 
    Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    user_input = float(input('Your transaction amount please: '))
    return user_input

def get_user_choice():
    user_input = input("Your Choice: ")  
    return user_input  

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    """    
    block_index = 0
    is_valid=True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
            block_index += 1
        else:
            is_valid = False   
            break 
    return is_valid
    """
    for(index,block) in enumurate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] == hash_block(blockchain[index-1]):
            return False
    return True
 


# Get the first transaction input and add the value to the blockchain
"""
tx_amount = get_transaction_value()
add_value(tx_amount)

"""
waiting_for_input = True
while waiting_for_input:
    print('Please choose')
    print('1:Add a new transaction value')
    print('2:Output the blockchain blocks')
    print('h:Manupulate the blockchain')
    print('q:Quit')
    user_choice = get_user_choice()
    if  user_choice=="1":
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice=="2":
    # Output the blockchain list to the console
         print_blockchain_elements()
    elif user_choice=="h":
        if len(blockchain) >= 1:
            blockchain[0]=[2]    
    elif user_choice=="q":  
        waiting_for_input = False 
    else:
        print('İnput Was invalid, please pick the value from the list!')
    if not verify_chain():
          print('İnvalid blockchain')
          break
else:
    print('User Left')
print('Done!')
