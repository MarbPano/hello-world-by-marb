import time
#-------------------#
#Marb Pano
#Shopping list
#January 3rd, 2023
#-------------------#


#LIST
shopping_list = {
    
}
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
#FUNCTIONS
def print_list(shopping_list):
    print(" ")
    print("Items in your list:")
    
    for item, cost in list(shopping_list.items()):#for every item and cost in shopping_list print the {item} or key, {cost} or value. in dict
        print(f"{item} cost ${cost}")
        
    count_items(shopping_list)
       
        
def adding_list(shopping_list):
    print(" ")
    for_question = int(input("How many Items do you wanna add? "))
    
    for i in range(for_question):
        item = input("Enter item\n ")#the key in dictionary
        cost = float(input("Enter Cost of item\n "))#value in dictionary
        shopping_list[item] = cost#this is the only way I figured out how to add things to dictionary
        
    print_list(shopping_list)#im proud of this. prints list to show what item added

def count_items(a_list):
    print(" ")
    count = 0
    for item, cost in a_list.items():#variable cost and item is useless. but in this case the item represents the key and cost represent the value. In Dictionary
        count = count + 1
        
    print(f"You have: {count} items")
    
def remove_items(a_list):
    while True:
        print_list(a_list)#shopping_list should go in this "()"
        item_remove = str(input("What Item do you want to remove?('4' to exit)\n"))#since this is in a loop. exit option allows user to exit at any time
        
        if item_remove in a_list:#so that user can just keep removing items
            del a_list[item_remove]#removes a key in dictionary
            print_list(a_list)#prints list to show what's left in list
        
        elif item_remove == "4":#get out of loop
            break
            
        
        else:#if item not in list. it continues to play
            print("Not in list!")
            continue
        
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
#Main Code
        
while 1:
#asking a question #I used "str" to solve constant error for when you put random things in the input
    question = str(input("""
    Options:
    1. Print Current List
    2. Add Items to list
    3. Remove Items from list
    4. Exit
    """))
    
    if question == "1": #had to use "" because question = str(input(""))
        print_list(shopping_list)#plays print_list() function
        
        
      
    elif question == "2":#if 2 this plays
        while True:
            try:   
                adding_list(shopping_list)#plays adding_list() function
                break#after conditions are met and function is fully played. user is brought back to options menu
                
            except:
                print("Only Numbers")
                continue#plays function again if conditions are not yet met.
           
   
    elif question == "4":# if 4 this plays
        print("Things you need to buy:")
        print_list(shopping_list)
        time.sleep(5)
        break
    
    elif question == "3":#if 3 this plays
        remove_items(shopping_list)
        
    else:#if the question above does not meet conditions. It continues back again
        print("Only 1, 2, 3, 4")
        continue 
        
        
   

trying to understand github

