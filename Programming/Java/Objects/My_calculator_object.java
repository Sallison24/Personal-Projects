public class Calculator{
  // A calculator object, it will check if a value passed is 0< or = 0 and pass an error if you try to divide by zero. It also only works with the first passed int 'a' divided by 'b'
  public Calculator() {
    
  }
  public int add(int a,int b) {
    return a + b ; 
  }
  
  public int subtract(int a, int b){
    return a - b ;
  }
  
  public int multiply(int a, int b){
    return a * b ; 
  }
  public int divide(int a, int b){
       if(b <= 0){
      System.out.println("Error! Dividing by zero is not allowed.");
         return 0;
    }
      else {return a % b; 
           }
    }
  public int modulo(int a, int b){
         if(b <= 0){
      System.out.println("Error! Dividing by zero is not allowed.");
         return 0;
    }
    else{
      return a%b;
    }
  }
  
  public static void main(String[] args){
    System.out.println(16 / 8);
    Calculator myCalculator = new Calculator();
    System.out.println(myCalculator.add(5,7));
    System.out.println(myCalculator.subtract(45, 11));
    System.out.println(myCalculator.add(5, 7));
  }
}