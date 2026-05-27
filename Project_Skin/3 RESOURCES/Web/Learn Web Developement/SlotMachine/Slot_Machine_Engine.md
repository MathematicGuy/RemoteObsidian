Slot Machine Engine
> slot machine reels. (or columns of the slot machine) - reel: cuộn phim/cuộn băng 
![[slotMachineReelSmaller.jpg]]

*Example & Images are for illustration purposes only*
1. Deposit Money
	Balance = Deposit_Money() - !! balance is a global value !! 
2. Choose number of lines (to bets)
	Number_of_lines = lines() 
3. Choose Bet (Bet per line. Condition < current_balance)
	Bet = bet_per_line()   
4. Spin machine
	1. Declare symbols
		Symbol_Count = { A:2, B:4 } -> array contain number of each symbol. The array contain: 2A , 4B 
		Symbol_Value = { A:4, B:3 } -> array symbol's value. A value is 4, B value is 3
	2. Create the slot machine (with n symbols )
		1. Declare a SymbolsArray contain all the available symbols
			Push all symbol from Symbol_Count to SymbolsArray - Loop (Ex: A:2 so push 2 A into SymbolsArray)
		2. Declare Reels = [ [], [], [] ]. Each Reel represent as []  in slot machine. Reels = [ [A, B, C], [A,C, D], [D, D, D] ] (1st Column or Reel contain A,B,C) 
			![[Pasted image 20231018164201.png]]
	3. Spin
		1. Declare a ReelsSymbol Array of Symbols (which is a copy of SymbolArray)
			Reason: to Delete chosen Element from ReelsSymbol array without effect the SymbolsArray. Keep SymbolsArray intact each replay   
		2. Push 3 random element to each reel in Reels - Loop
			1. SelectElement = select a random element from ReelsSymbol  
			2. Push it to Reels ("it" refer to the random element)
			4. Delete it from ReelsSymbol
	4. Reposition - Convert Column Reels to Row Reels
			newArray = []
			Push element at position i of column 1 to 3 to the newArray - Loop 
	5. Print out Reels interface:  
			A | B | C
			D | A | C
			D | D | D
5. Check Winning (return Money if Won)
	1. Declare Winning_Money & Winning_Condition;
	2. If each element in reel == 1st reel's element 
			Winning += Bet
	3. return Winning
6. Play Again 
	Put function above into 1 function: SlotPlay()
	Run under while(true) conditon
	If (balance <= 0) or (PlayerInput == "n")
		stop game
