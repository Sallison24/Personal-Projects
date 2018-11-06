// My GradeAnalyzer program by Scott Allison
// this is the creation of a object called GradeAnalyzer and it uses a method called getAverage
// the method cheks to see that the array passed to it is greater than 0
// the method returns the average of the grades in the array by using the "for each" loop 

import java.util.ArrayList;
public class GradeAnalyzer{
  
  
  public GradeAnalyzer(){
    
  }
  
  public int getAverage(ArrayList<Integer>grades){
     // Below grades.size turns the array into a int
    if (grades.size() < 1){
      System.out.println("Error, Array List has to be greater than 0");
      return 0;
    }
    else{
      int sum = 0;
	  // for each loop
      for (int grade : grades){
        sum += grade;
      }
      
      int average;
      
      average = sum / grades.size();
      
      System.out.println(average);
      
      return average;
    }
  }
  
  
  public static void main(String[] args) {
    
    ArrayList<Integer> myClassroom = new ArrayList<Integer>();
    myClassroom.add(98);
    myClassroom.add(92);
    myClassroom.add(88);
    myClassroom.add(75);
    myClassroom.add(61);
    myClassroom.add(89);
    myClassroom.add(95);
	// creation of a new object called myAnalyzer
  GradeAnalyzer myAnalyzer = new GradeAnalyzer();
    myAnalyzer.getAverage(myClassroom);
  }
  
}