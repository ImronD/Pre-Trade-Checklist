   #ASSUMING THAT THE TRADE FITS YOUR PLAN AND RISK MANAGEMENT. I'M NOT RESPONSIBLE FOR ANY WINS OR LOSSES YOU NET.



def eval():

  # Must haves and like to haves
  musts=["Does the trade offer you a high enough profit target?","Does the stock trade at more than 1m shares per day?","Did you make sure that there aren't any anticipated news that are to be released?","Did you make sure the stock is not up for more than 3 bars on the timefarme you're trading it?","Did you make sure that a longer timeframe doesn't interfere with your bias?"]

  likes=["Did you make sure there are no significant price levels on the left?","Does the stock show relative strength or weakness to the market?","Is there igniting/resting volume on the stock?","Is there a tail that points towards your anticipated stop loss?","Is the stock rested?","Is the stock near a whole or half number?"]


  # Recursive function used to try again
  def tryAgain():
    response=str(input('Would you like to try again? Y/N :'))
    if response.lower() == 'n' :
      print("Thank you for using our sevices!")
      return 0
    elif response.lower() == 'y' :
      eval()
    else:
      print('Invalid input')
      tryAgain()
  



  # Itterate over each must have condition 
  mustIndex=0
  while mustIndex in range(len(musts)):
    answer=str(input(musts[mustIndex]+str(' Y / N:')+"\n"))
    if answer.lower() == 'y':
      mustIndex+=1
    elif answer.lower() == 'n':
      print("You may not take this trade.")
      tryAgain()
      return 0
    else:
      print("Invalid response, please try again.")
  
  

  # Itterate over each like to have condition
  likeIndex=0
  selectvity=3
  while likeIndex in range(len(likes)):
    answer=str(input(likes[likeIndex]+str(' Y / N:')+"\n"))
    if answer.lower() == 'y':
      likeIndex+=1
    elif answer.lower() == 'n':
      likeIndex +=1
      selectvity -=1
    else:
      print("Invalid response, try again")
    if selectvity <= 0:
      print("You may not take this trade")
      tryAgain()
      return 0

  # Rate the setup if it has passed
  if selectvity == 3:
    print("This is a flawless setup.RuntimeWarning")
  elif selectvity == 2:
    print("This is a decent setup.")
  elif selectvity == 1:
    print("This is a mediocore setup. Be careful.")
  tryAgain()
  return 1
  





eval()
