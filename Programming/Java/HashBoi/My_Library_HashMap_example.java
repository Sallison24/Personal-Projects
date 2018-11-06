///
///
///

import java.util.HashMap;
public class Library{
  public Library() {
    
  }
  public void getFinishedBooks(HashMap<String, Boolean>library){
    if (library.size()<1){
     System.out.println("Error, Hash Map has to be greater than 0");
    }
    else {
      //this for each loop iterates through each book the the key set of library
      for(String book : library.keySet()){
        // Below line alows you to check the completion status of each book in the iteration and if it == true. Then it will print out the book
				if(library.get(book) == true){
          System.out.println(book);
        }
      }
    }
  }

  
  
  public static void main(String[] args){
    HashMap<String, Boolean> myBooks = new HashMap<String, Boolean>();
    myBooks.put("Road Down The Funnel", true);
    myBooks.put("Rat: A Biology", false);
    myBooks.put("TimeIn", true);
    myBooks.put("3D Food Printing", false);
    Library myLibrary = new Library();
    myLibrary.getFinishedBooks(myBooks);
  }
  
}