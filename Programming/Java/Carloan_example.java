public class CarLoan {
	public static void main(String[] args) {
// calculates montly payment on a car plus interest
	int carLoan = 10000;
  int loanLength = 3; // in years
  int interestRate = 5; //5%
  int downPayment = 2000; 
    
    /// Below if checks to make sure it is a valid loan
  if ((carLoan < 0) || (interestRate < 0)){
    System.out.println("Error! You must take out a valid car loan.");
  } else if (downPayment > carLoan){
    System.out.println("The care can be paid in full");
  } else {
    int remainingBalance = carLoan - downPayment;
    int months = loanLength*12;
    int monthlyBalance = remainingBalance/months;
    int interest = ((monthlyBalance*interestRate)/100);
    int monthlyPayment = monthlyBalance + interest;
    System.out.println(monthlyPayment);
  }
	}
}