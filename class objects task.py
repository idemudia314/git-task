class Budget():
      def __init__(self, food, balance):
          self.food = food
          self.balance = balance
          
        

      def withdrawal(self):
          withdrawal = int(input('would you like to withdraw? (1) yes (2) no \n'))
          if(withdrawal == 1):
              print(f'money has been withdrawn from {self.food}' )

            
            
              clothing_budget.Deposit()
        


       
      
    
      def Deposit(self):
          selectedOption = int(input('would you like to deposit? (1) yes (2) no \n'))
          if(selectedOption == 1):
           print(f'money has been deposited from {food_budget}')
      
      def transfer(self):
          selectedAction = int(input('what do you wan to transfer to: (1) food (2) clothing (3) entertainment'))
          if(selectedAction == 1):
              print('you selected 1')
              
          transfer = int(input('how much do want to transfer '))
          if(transfer <= self.balance ):
              print('transfer succesful')
          if(selectedAction == 2):
              print('you selected 2')
              
          transfer = int(input('how much do want to transfer '))
          if(transfer <= self.balance):
              print('transfer succesful')

          if(selectedAction == 3):
              print('you selected 3')
              
          transfer = int(input('how much do want to transfer '))
          if(transfer <= self.balance):
              print('transfer succesful')

        
          
        

        
          
        

        
          
        
    
    
        
        


food_budget = Budget("food", 500)
clothing_budget = Budget("clothing", 600)
entertainment_budget = Budget('entertainment', 900)



clothing_budget.withdrawal()

food_budget.transfer()




       
       
       