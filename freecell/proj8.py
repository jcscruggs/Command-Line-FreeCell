# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:00:18 2019

@author: jdogg
"""

import cards

def setup():
    """
    paramaters: None (deck can be created within this function)
    returns:
    - a foundation (list of 4 empty lists)
    - cell (list of 4 empty lists)
    - a tableau (a list of 8 lists, the dealt cards)
    """
    
    my_deck = cards.Deck()
    my_deck.shuffle()
    foundation = [[],[],[],[]] 
    cell = [[],[],[],[]]
    tableau = [[],[],[],[],[],[],[],[]]
    column = 0
    while not my_deck.is_empty():
        tableau[column].append(my_deck.deal())
        column += 1
        if column % 8 == 0:
            column = 0 

    return foundation,tableau,cell

def move_to_foundation(tableau,foundation,t_col,f_col):
    '''
    parameters: a tableau, a foundation, column of tableau, column of foundation
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a column of foundation
    This function can also be used to move a card from cell to foundation
    '''
    validity = False
   # get true index of embedded list 
   
    tab_index = t_col - 1
    found_index = f_col - 1
    
    # index is within the bounds of lists index
    if (t_col <= len(tableau) and t_col !=0) and (f_col <= len(foundation) and f_col != 0):
        
        if len(foundation[found_index]) == 0: # empty foundation pile
            
            tab_rank = tableau[tab_index][len(tableau[tab_index]) - 1].get_rank()
       
            if tab_rank == 1: # card must be an ace
                
                # remove card from tab and place at bottom of foundation 
                card = tableau[tab_index].pop()
                foundation[found_index].append(card)
                validity = True
                
        
        else: # foundation has been started
            
            
            # get rank of top foundation card
            found_rank = foundation[found_index][len(foundation[found_index]) - 1].get_rank()
            tab_rank = tableau[tab_index][len(tableau[tab_index]) - 1].get_rank()
            
            # get suit of tableau and foundation
            tab_suit = tableau[tab_index][len(tableau[tab_index]) - 1].get_suit()
            found_suit = foundation[found_index][len(foundation[found_index]) - 1].get_suit()
            
            if tab_suit == found_suit: # found and tab have same suit
            
                if found_rank == 13: # foundation pile is already complete
                    validity = False
                else: # foundation not complete
                    
                    next_rank = found_rank + 1 #get next rank in list 
                
                    if tab_rank == next_rank: # rank of tab card is one greater than foundation card
                        
                        card = tableau[tab_index].pop()
                        foundation[found_index].append(card)
                        validity = True
        
    return validity

def move_to_cell(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    validity = False
    
    tab_index = t_col - 1
    cell_index = c_col - 1
    
    
    
    if (t_col <= len(tableau) and t_col !=0) and (c_col <= len(cell) and c_col != 0):
        
        if len(cell[cell_index]) == 0:
            card = tableau[tab_index].pop()
            cell[cell_index].append(card)
            validity = True
    
    return validity
            
def move_to_tableau(cell,tableau,c_col,t_col):
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    remember to check validity of move
    
    '''
    
    validity = False
    tab_index = t_col - 1
    cell_index = c_col - 1
    
    if (t_col <= len(tableau) and t_col !=0) and (c_col <= len(cell) and c_col != 0):
        
        # if tableau is empty and cell is not empty
        if len(tableau[tab_index]) == 0 and len(cell[cell_index]) != 0:
            
            validity = True
            card = cell[cell_index].pop()
            tableau[tab_index].append(card)
            
        else: # tableau is not empty
        
            if len(cell[cell_index]) != 0: # cell is not empty
                
                cell_rank =  cell[cell_index][0].get_rank()
                tab_rank = tableau[tab_index][len(tableau[tab_index]) - 1].get_rank()
                
                # get suit of tableau and cell
                tab_suit = tableau[tab_index][len(tableau[tab_index]) - 1].get_suit()
                cell_suit = cell[cell_index][0].get_suit()
                
                # check that one card is red and other is black
                if ((tab_suit == 2 or tab_suit == 3) and (cell_suit == 1 or cell_suit == 4)) or ((tab_suit == 1 or tab_suit == 4) and (cell_suit == 2 or cell_suit == 3)):
                
                    if cell_rank == tab_rank - 1: # card from cell is 1 less than last card in tableau
                        
                        validity = True
                        card = cell[cell_index].pop()
                        tableau[tab_index].append(card)
                    
    return validity

def move_in_tableau(tableau,t_col_source,t_col_dest):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    remember to check validity of move
    '''
    source_index = t_col_source - 1
    dest_index = t_col_dest - 1
    
    validity = False
    
    
    if (t_col_source <= len(tableau) and t_col_source !=0) and (t_col_dest <= len(tableau) and t_col_dest != 0):
    
        if len(tableau[source_index]) != 0 and len(tableau[dest_index]) == 0:
            # tableau dest is empty and source is not
             validity = True
             card = tableau[source_index].pop()
             tableau[dest_index].append(card)
        else:
            if len(tableau[source_index]) != 0:
                
                tab1_rank =  tableau[source_index][len(tableau[source_index]) -1].get_rank()
                tab2_rank = tableau[dest_index][len(tableau[dest_index]) - 1].get_rank()
                
                # get suit of tableau and cell
                tab1_suit = tableau[source_index][len(tableau[source_index]) -1].get_suit()
                tab2_suit = tableau[dest_index][len(tableau[dest_index]) - 1].get_suit()
                
                # check that one card is red and other is black
                if ((tab1_suit == 2 or tab1_suit == 3) and (tab2_suit == 1 or tab2_suit == 4)) or ((tab1_suit == 1 or tab1_suit == 4) and (tab2_suit == 2 or tab2_suit == 3)):
                
                    if tab1_rank == tab2_rank - 1: # card from cell is 1 less than last card in tableau
                        
                        validity = True
                        card = tableau[source_index].pop()
                        tableau[dest_index].append(card)
            
    return validity  


def is_winner(foundation = [[],[],[],[]]):
    '''
    parameters: a foundation
    return: Boolean
    '''
    winner = False
    
    counter = 0
    # counter number of cards in foundation list
    for pile in foundation:
        counter += len(pile)
    
    # rules only allow alike suits to stack so no need to check if they are alike suits
    if counter == 52:
        winner = True
    return winner

def print_game(foundation, tableau,cell):
    """
    parameters: a tableau, a foundation and a cell
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  
        b) print foundation ( can print the top card only)
        c) print cells

    """
    print()
    print("                 Cells:                              Foundation:")
    # print cell and foundation labels in one line
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print('    ', end = '')
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print()  # carriage return at the end of the line

    # print cell and foundation cards in one line; foundation is only top card
    print(' '*7, end = '') 
    for c in cell:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:8s}'.format(str(c[0])), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')
            
    print('    ', end = '')
    for stack in foundation:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:8s}'.format(str(stack[-1])), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')

    print()  # carriage return at the end of the line
    print('----------')

    print("Tableau")
    for i in range(len(tableau)):  # print tableau headers
        print('{:8d}'.format(i + 1), end = '')
    print()  # carriage return at the end of the line

    # Find the length of the longest stack
    max_length = max([len(stack) for stack in tableau])

    # print tableau stacks row by row
    for i in range(max_length):  # for each row
        print(' '*7, end = '')  # indent each row
        for stack in tableau:
            # print if there is a card there; if not, exception prints spaces.
            try:
                print('{:8s}'.format(str(stack[i])), end = '')
            except:
                print('{:8s}'.format(''), end = '')
        print()  # carriage return at the end of the line
    print('----------')

def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    print("Rules of FreeCell")

    print("Goal")
    print("\tMove all the cards to the Foundations")

    print("Foundation")
    print("\tBuilt up by rank and by suit from Ace to King")

    print("Tableau")
    print("\tBuilt down by rank and by alternating color")
    print("\tThe bottom card of any column may be moved")
    print("\tAn empty spot may be filled with any card ")

    print("Cell")
    print("\tCan only contain 1 card")
    print("\tThe card may be moved")

def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    print("Responses are: ")
    print("\t t2f #T #F - move from Tableau to Foundation")
    print("\t t2t #T1 #T2 - move card from one Tableau column to another")
    print("\t t2c #T #C - move from Tableau to Cell")
    print("\t c2t #C #T - move from Cell to Tableau")
    print("\t c2f #C #F - move from Cell to Foundation")
    print("\t 'h' for help")
    print("\t 'q' to quit")
    
    
def play():
    ''' 
    Main program. Does error checking on the user input. 
    '''
    print_rules() 
    
    foundation, tableau, cell = setup() # start game
       
    show_help()
    while True:
        
        if is_winner(foundation):
            print('YOU WIN!!!!')
            print('congratulations')
            break
            
        else: # havent won the game
            
            print_game(foundation, tableau, cell)
            response = input("Command (type 'h' for help): ")
            response = response.strip()
            response_list = response.split()
            if len(response_list) > 0:
                r = response_list[0]
                
              
                if r == 't2f':
                    if  len(response_list) == 3:
                        if response_list[1].isdigit() and response_list[2].isdigit():
                            tab_col = int(response_list[1])
                            found_col = int(response_list[2])
                            
                            validity = move_to_foundation(tableau,foundation,tab_col,found_col)
                            if not validity:
                                print('invalid move: try again or ask for help')
                        else:
                            print('invalid columns: try again or ask for help')
                    else:
                        print('Unknown Command:')
                            
                                            
                elif r == 't2t':
                    
                    if  len(response_list) == 3:
                        if response_list[1].isdigit() and response_list[2].isdigit():
                            tab1_col = int(response_list[1])
                            tab2_col = int(response_list[2])
                            
                            validity = move_in_tableau(tableau,tab1_col,tab2_col)
                            
                            if not validity: # function returns false
                                print('invalid move: try again or ask for help')
                        else:
                            print('invalid columns: try again or ask for help')
                    else:
                        print('Unknown Command:')
                                             
                elif r == 't2c':
                    
                    if  len(response_list) == 3:
                        if response_list[1].isdigit() and response_list[2].isdigit():
                            tab_col = int(response_list[1])
                            cell_col = int(response_list[2])
                            
                            validity = move_to_cell(tableau,cell,tab_col,cell_col)
                            
                            if not validity:
                                print('invalid move: try again or ask for help')
                        else:
                            print('invalid columns: try again or ask for help')
                    else:
                        print('Unknown Command:')
                    
                              
                elif r == 'c2t':
                        
                    if  len(response_list) == 3:
                        if response_list[1].isdigit() and response_list[2].isdigit():
                            cell_col = int(response_list[1])
                            tab_col = int(response_list[2])
                            
                            validity = move_to_tableau(cell,tableau,cell_col,tab_col)
                            
                            if not validity:
                                print('invalid move: try again or ask for help')
                        else:
                            print('invalid columns: try again or ask for help')
                    else:
                        print('Unknown Command:')
                         
                elif r == 'c2f':
                    if  len(response_list) == 3:
                        if response_list[1].isdigit() and response_list[2].isdigit():
                            cell_col = int(response_list[1])
                            found_col = int(response_list[2])
                            
                            validity = move_to_foundation(cell,foundation,cell_col,found_col)
                            if not validity:
                                print('invalid move: try again or ask for help')
                        else:
                            print('invalid columns: try again or ask for help')
                    else:
                        print('Unknown Command:')
                    
                              
                elif r == 'q':
                    break
                elif r == 'h':
                    show_help()
                else:
                    print('Unknown command:',r)
            else:
                print("Unknown Command:",response)
                
    print('Thanks for playing')


play()
