C sharp introduced by Microsoft. C# is designed to be a simple, modern, general-purpose, object-oriented programming language, borrowing key concepts from several other language, most notably Java.

C# was developed by Anders Hejlsberg and his team during the development of .Net framework.

### We can use C# for Building variety of Application.
- Windows Application:-
    using console application or winform application.

- Mobile Application:-
    For phones such as Nokia Lumia (built-in support) but we can use a third party tool or library called "XAMARIN" to create mobile application for ANDROID and IOS as well.

- Web Application: 
    Using ASP.NET web forms or ASP.NET MVC.

- Gaming Application: unity.


### What is .Net framework
- > .NET is a programming created by Microsoft that developers can use to create application more easily.
- > A framework is just a bunch of code that the programmer can call without having to write it explicity.

- > It provides a controlled programming environment where software can be developed, installed and executed on Windows-based operating systems.

- > It us basically a collection of libraries.

- > Is a programming platform that is used for developing Windows, Web-based, and mobile software.

- > It has a number of pre-coded solution that manage the execution of program written specifically for the framework.

- > A programmer can develop application using one of the language supported by .NET .

### Microsoft C# was Developed to:
- > Create a very simple and yet powerful for building interoperable and robust application.

- > Create a complete object-oriented architecture.

- > Support powerful component-oriented development.

### Common Language Runtime (CLR) in Dotnet framework
- > The CLR:
- Is the foundation of the .Net framework.
- Acts as an execution engine for the .Net framework.
- Manages the execution of program and provides a suitable environment for program to run.
- Provides a multi-language execution environment.


### What is Namespace
- A namespace is used to organise your code and is collection of classes, interface, structs, enums and delegates.

* If you don't want to use namespace you can use fully qualified name (FQN).

# What is Main Method
- Main method is the entry point into your application.

- Void is return type

## First program :-
``` using System;
    namespace Hello
    {
        class Program
        {
            public static void Main(string[] args)
            {
                Console.WriteLine("Hello world");
            }
        }
    }
```
``` using System
    namespace MyApplication
    {
        public class program
        {
            public static void Main(string [] args)
            {
                string name = "John";
                int age = 35
                Console.WriteLine("Your name is " + name);
                Console.WriteLine("You was " + age + " year old"); 
            }
        }
    }
```

### Convert into string to integer
``` using System
    namespace MyApplication
    {
        class Program
        {
            public static void Main(string[] args)
            {
                Console.Write("Enter your username ");
                string username = Console.ReadLine();
                Console.Write(" Enter you age");
                int age = Convert.ToInt32(Console.ReadLine());
                double age = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine("Username = "+ username);
                Console.WriteLine(" you are " + age);
            }
        }
    }
```

 
### Conversion (Two types of Conversion)
- Implicit:- It means builtin for example int to float 
    int a=20;
    float b =a;//Implicit
- Explicit:- When C# compiler think that its data loss then not doing implicit conversion that why use explicit conversion.
For example:
    float a = 20;
    int b = int(a);


    float a = 20;
    int b = Convert.ToInt32(a);



### Nested switch case:-
- C# allows the switch case construct to be nested. That is, a case block of a switch case construct can contain another switch case construct.
- Also, the case constants of the inner switch case construct can have values that are identical to the constants of the outer construct.

```
using System;
namespace Selection_Statement
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter your pizza flavour: ");
            string pizza = Console.ReadLine();
            switch(pizza){
                case "Fajita":
                    Console.WriteLine("You are selected Fajita Pizza");
                    break;
                case "Supreme":
                    Console.WriteLine("You are selected Supreme Pizza");
                    break;
                case "Vegetable":
                    Console.WriteLine("Enter your vegetable: ")
                    string veg = Console.ReadLine();
                    switch(veg)
                    {
                        case "Olive":
                    Console.WriteLine("You are selected Olives Pizza");
                    break;
                        case "Onion":
                    Console.WriteLine("You are selected Onion Pizza");
                    break;
                        case "Mushrooms":
                    Console.WriteLine("You are selected Mushrooms Pizza");
                    break;
                        default :
                            Console.WriteLine("This vegetable is not available");
                            break;
                    }
                    break;
                case "Cheeze":
                    Console.WriteLine("You are selected Cheeze Pizza");
                    break;
                default :
                    Console.WriteLine("Invalid ");
                    break;
            }
        }
    }
}
```

## Create marksheet application:
```
    using System;
    namespace MarksheetApplication
    {
        class Program
        {
            Console.WriteLine("Enter your name");
            string name=Console.ReadLine();
            Console.WriteLine("Enter your roll no");
            string rollNo=Console.ReadLine();
            Console.WriteLine("Enter your class");
            string standard=Console.ReadLine();
            Console.WriteLine("Enter your Mathematics marks");
            int m = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter your physics marks");
            int p = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter your Chemistry marks");
            int c = int.Parse(Console.ReadLine());


            Console.ReadLine();
            int obt = m+p+c;
            int per = obt*100/300
            Console.WriteLine("Your obtained marks are: {0}", obt);

        } 
    }

```

### Loop Constructs:
- Loops allow you to execute a single statement or a block of statements repetitively.
- The most common uses of loops include displaying a series of numbers and taking repetitive input.
- In software programming, a loop construct contains a condition that help the compiler identify the number of times a specific block will be executed.
- If the condition is not specified, the loop continues infinitely and is termed as an infinite loop.


- The loop constructs are also referred to as iteration statement.
* C# supports four types of loop constructs such as:-
1) The for loop
2) While loop
3) do while loop
4) foreach loop(Mainly used in array )

# The For loop:-
- The for statement is similar to the while statement in its function.
- The statement within the body of the loop are executed as long as the condition is true. 
- Here too, the condition is checked before the statement are executed.


* There are 3 things in For loop:-
- Initialization
- Condition
- Increment/decrement

```
using System;
namespace Statement
{
    class Program
    {
        static void Main(string[] args)
        {
            for(int i=0;i<10;i++) // Variable name is Counter variable.
            {
                Console.WriteLine(i);
            }
            Console.WriteLine("For terminate");
            Console.ReadLine();
        }
    }
}
```
```
using Systemp;
namespace Statement
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number ");
            int number=int.Parse(Console.ReadLine());
            for(int i=0;i<=10;i++) 
            {
                Console.WriteLine(number + "X" +i+ "=" + number*i);
            }
            Console.WriteLine("For loop terminate");
            Console.ReadLine();
        }
    }
}
```

# use Decrement 
```
using System;
namespace Statement
{
    class Program
    {
        static void Main(string[] args)
        {
            for(int i=10;i>0;i--) // Variable name is Counter variable.
            {
                Console.WriteLine(i);
            }
            Console.WriteLine("For terminate");
            Console.ReadLine();
        }
    }
}
```


### While loop:-

- The while loop is used to execute a block of code repetively as long as the condition of the loop remains true.
- The while loop consists of the while statement, which begins with the while keyword followed by a boolean condition.
- If the condition evaluates to true, the block of statement after the while statement is executed.

```
using System;
namespace Condition
{
    class Program
    {
        int number = 2;
        int i = 0;
        while( i <= 10)
        {
            Console.WriteLine(number + "X" + i + "=" + number*i);
            i++;
        }
        Console.WriteLine("While loop terminates");
    }
}
```
* After each iteration, the control is transferred back to the while statement and the condition is checked again for another round of execution.

* When the condition is evaluated to false, the block of statements following the while statement is ignored and the statement appearing after the block is executed by the compiler.



### Do while loop:-
- The do-while loop is similar to the while loop; however, it is always executed at least once without the condition being checked.
- The loop starts with the do keyword and is followed by a block of executable statements.
- The while statement along with the condition appears at the end of the block.

```
using System;
namespace Condition
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = 0;
            do
            {
                Console.WriteLine(i);
                i++;
            }
            while(i <= 0);
            Console.WriteLine("Do while terminate");
        }
    }
}
```

```
using System;
namespace Condition
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = 0;
            do
            {
                Console.WriteLine(i);
                i++;
            }
            while(i <= 10);
            Console.WriteLine("Do while terminate");
        }
    }
}
```
```
using System;
namespace Condition
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = 1;
            do
            {
                Console.WriteLine(i);
                i++;
            }
            while(i < 0);
            Console.WriteLine("Do while terminate");
        }
    }
}
```
- The statement in the do-while loop are executed as long as the specified condition remains true.
- When the condition evaluates to false, the block of statement adter the do keyword are ignored and the immediate statement after the while statement is executed.



### Nested for loop:-
- The nested for loop consists of multiple for statements.
- When one for loop is enclosed inside another for loop, the loops are said to be nested.
- The for loop that enclosed the other for loop is referred to as the outer for loop whereas the enclosed for loop is referred to as the inner for loop.
- The outer for loop determines the number of times the inner for loop will be invoked.
```
using System;
namespace nestedForLoop
{
    class Program
    {
        static void Main(string[] args)
        {
            for(int i=1; i<=3; i++)
            {
                Console.WriteLine("Hello");
                for (int j=0; i<=3; j++)
                {
                    Console.WriteLine("Hey");
                }
            }
            Console.ReadLine();
        }
    }
}
```
### Jump statement in C#:-
- Jump statement are used to transfer control from one point in a program to another.
- There will be situations where you need to exit out of a loop prematurely and continue with the program.
- In such cases, jump statement are used. Jump statement unconditionally transfer control of a program to a different location.

* C# supports four types of jump statements. These are as follows:-
. break
. continue
. goto
. return



## How to restart program again and again:-
```
using System;
namespace Loops_Csharp
{
    class Program
    {
        static void Main(string[] args){
            string confirm;
            do{
                Console.WriteLine("Enter first number: ");
                int first_num = int.Parse(Console.ReadLine());
                Console.WriteLine("Enter second number: ");
                int sec_num = int.Parse(Console.ReadLine());
                int add =  first_num +sec_num;
                Console.WriteLine("Addition number is: " +add);
                Console.WriteLine("Do you want to repeat your program? Yes/No");
                confirm = Console.ReadLine().ToLower();
            }
            while(confirm=="yes");

            Console.ReadLine();
        }
    }
}
```
* ToLower() // Convert the lower case and print the condition.


### Arrays in C#:-

- An array is a collection of elements of a single data type store in adjacent memory locations.

- You can store multiple variables of the same type in an array data structure.

- An array can be single-dimensional, multidimensional or jagged.

- 7 Memory location inside the RAM. 

- An array always stores values of a single data types.

* In array declare many types in array to given below.
```
using System;
namespace Array_program
{
    class Program
    {
        static void Main(string[] args){
            int[] my_array = new int[3];
            <!-- my_array = {11,32,22}; -->
            my_array[0] = 11;
            my_array[1] = 32;
            my_array[2] = 22;
            Console.WriteLine(my_array[2]);
        }
    }
}
```
```
using System;
namespace Array_program
{
    class Program
    {
        static void Main(string[] args){
            string[] my_array = new string[] {"Adil", "Ali", "Osama"};
            
        }
    }
}
```
* Another way to declare array:-

string[] my_array = {"Musraful", "Adil", "Sohail"};

* This means that the first array element has an index number zero while the last element has an index number n-1, where n stands for the total number of elements in the array.

* n-1 means last of number in array.

## Declaration in Array:-
- An array declaration specifies the type of data that it can hold and an identifier.
- This identifier is basically an array name and is used with a subscript to retrieve or set the data value at that location.  



### Using the Foreach loop for arrays:-
- In c# is an extension of the for loop.
- Is used to perform specific action on large data collection and can even be used on arrays.
- Read every element in the specified array.
- Allows you to execute a block of code for each element in the array.
- Is particularly useful for reference types, such as strings.

* How to use in for loop 
```
using System;
namespace Array
{
    class Program
    {
        static void Main(string[] args){
            int[] numbers = new int[4];
            numbers[0] = 10;
            numbers[1] = 20;
            numbers[2] = 30;
            numbers[3] = 40;
            for (int i = 0; i < numbers.Length;i++)
            {
                Console.WriteLine(numbers[i]);
            }
            Console.ReadLine();
        }
    }
}
```

* Using foreach loop in given below:-
```
using System;
namespace Array
{
    class Program
    {
        static void Main(string[] args){
            int[] numbers = new int[4];
            numbers[0] = 10;
            numbers[1] = 20;
            numbers[2] = 30;
            numbers[3] = 40;
            foreach( int item in numbers){
                Console.WriteLine(item);
            }
        }
    }
}
```
### Types in array:-
Two types in array:-
- Single-dimesional array
- Multi-Dimensional array

# Single dimensional array:-
- Elements of a single-dimensional array stored in a single row in allocated memory.
- Declaration/Initialization of array.
- Elements indexed from 0 to (n-1), where n is the total number of elements in the array.

# Multi-dimensional array:-
- A multi-dimensional array allows you to store combination of values of a single type in two or more dimensions.
- The dimensions of the array are represented as rows and columns similar to the rows and columns of a Microsoft Excel sheets.
* Two types in multi-dimensional array
- Rectangular
- Jagged array
```
using System;
namespace Array_cSharp
{
    class Program{
        static void Main(string[] args){
            int[,] my_array = new int[3,4] // This is the declare of multi-dimensional arrys and int[3,4] this is defined 3 rows and 4 columns
            {
                {23,43,54,1},
                {12,32,54,12},
                {13,23,14,32}
            };
            Console.WriteLine(my_array[1,2]);
            Console.WriteLine(my_array.GetLength(1));
            Console.WriteLine(my_array.Rank);
            Console.ReadLine();
        }
    }
}
```
```
using System;
namespace Array_cSharp
{
    class Program{
        static void Main(string[] args){
            int[,] my_array = new int[3,4] // This is the declare of multi-dimensional arrys and int[3,4] this is defined 3 rows and 4 columns
            {
                {23,43,54,1},
                {12,32,54,12},
                {13,23,14,32}
            };
            for(int i = 0; i < my_array.GetLength(0);i++)
            {
                for (int j = 0; j< my_array.GetLength(1); j++)
                {
                    Console.WriteLine(my_array[i,j]+ "");
                }
            }
            Console.ReadLine();
        }
    }
}
```
* Rectangular multidimensional array
```
using System;
namespace Array_cSharp
{
    class Program{
        static void Main(string[] args){
            int[,] my_array = new int[3,4] // This is the declare of multi-dimensional arrys and int[3,4] this is defined 3 rows and 4 columns
            {
                {23,43,54,1},
                {12,32,54,12},
                {13,23,14,32}
            };
            foreach (int i in my_array)
            {
                Console.WriteLine(i);
            }
            Console.ReadLine();
        }
    }
}
```
# Jagged array :-
- Is a multidimensional array where one of the specified dimension can have varying sizes.
- Can have unequal number of columns for each now.

```
using System;
namespace Array_cSharp
{
    class Program{
        static void Main(string[] args){
            int[][] my_array1 = new int[3][];            my_array1[0] = new[] {11,22,33,44,23,45,23};
            my_array1[1] = new[] {55,66,77,88,12,53};
            my_array1[2] = new[] {12,23,63,24,32};

            Console.WriteLine(my_array1[0][4]);
            foreach (int[] items in my_array1)
            {
                foreach( int i in items)
                {
                    Console.WriteLine(i + " ");
                }
                
            }

            Console.ReadLine();
        }
    }
}
```
# Note :- There are 3 ways to initialize multidimensional array in c# while declaration.
int[,] arr = new int[3,3] = {{1,2,3},{4,5,6},{7,8,9}};
- We can omit the array size.
- int[,] arr =new int[,] {{1,2,3},{4,5,6},{7,8,9}};
- We can omit the new operator also.
int[,] arr = {{1,2,3},{4,5,6},{7,8,9}};



## Initializing array with user input in c#:
```
using System;
namespace Array
{
    class Program
    {
        static void Main(string[] args){
            Console.WriteLine("How many number of items u want to store in an array: ");
            int num = int.Parse(Console.ReadLine());
            int[] numbers = new int[num];
            for (int i = 0; i < num; i++)
            {
                Console.WriteLine("Enter data: ");
                int data = int.Parse(Console.ReadLine());
                numbers[i] = data;
            }
            Console.WriteLine("----------Your Data---------);
            foreach( int item in numbers)
            {
                Console.WriteLine(item);
            }
            Console.ReadLine();
        }
    }
}
```

### Switch case

- A program is difficult to comprehend when there are too many if statement representing multiple selection constructs.
- To avoid using multiple if statements, in certain cases, the switch case approach can be used as an alternative.
- The switch case statement is used when a variable needs to be compared against different values.

using System;
namespace selection_statement 
{
    class Program
    {
        static void Main(String[] args)
        {
            int week_number = 2;
            switch(week_number)
            {
                case 1:
                    Console.WriteLine("Monday");
                    break;
                case 2:
                    Console.WriteLine("Tuesday");
                    break;
                case 3:
                    Console.WriteLine("Wednesday");
                    break;
                case 4:
                    Console.WriteLine("Thursday");
                    break;
                case 5:
                    Console.WriteLine("Friday");
                    break;
                case 6:
                    Console.WriteLine("Saturday");
                    break;
                case 7:
                    Console.WriteLine("Sunday");
                    break;
                default:
                    Console.WriteLine("Invalid week number");
                    break;
            }
        }
    }
}



###
'''
Console.WriteLine("Enter your name");
Console.ReadLine();
'''

### Method or Function in C#:-

- A method is a group of statement that together perform a task
- Methods are functions declared in a class and may be used to perform operation on class variables.
- They are blocks of code that can take parameters and may or may not return a value.
- It is used to perform specific task.
- Method are reusable.
- Every C# program has at least one class with a method named Main.

* Convension to be followed for naming methods state that a method name:-
- The following syntax is used to create a method:
- Cannot be a C# keyword, cannot contain spaces, and cannot begin with a digit can begin with a letter, underscore, or the "@".
- Some examples of valid method names are: Add(), Sum_Add(), and @Add().

```
using System;
namespace methodFunction
{
    class Program{
        public void show()   // Declaring a method //non-static // instance method
        {
            Console.WriteLine("Welcome to C# programming..");
            Console.WriteLine("Hey Bro whatsup");
        }
        public static void show1() // static method  
        {
            Console.WriteLine("Welcome to Musraful");
            Console.WriteLine("Hey Bro whatsup");
        }

        static void Main(string[] args){
            Program p1 = new Program();
            p1.show(); // Calling the method
            Console.ReadLine();
        }
    }
}
```

## Static method:-
```
using System;
namespace methodFunction
{
    class Program{
        public void show()   // Declaring a method //non-static // instance method
        {
            Console.WriteLine("Welcome to C# programming..");
            Console.WriteLine("Hey Bro whatsup");
        }
        public static void show1() // static method  
        {
            Console.WriteLine("Welcome to Musraful");
            Console.WriteLine("Hey Bro whatsup");
        }

        static void Main(string[] args){
            Program.show1();
            Program p1 = new Program();
            p1.show(); // Calling a method
            Console.ReadLine();
        }
    }
}
```
# Take parameter in method
```
using System;
namespace methodFunction
{
    class Program{
        public static void Add(int a, int b){
            int result = a+b;
            Console.WriteLine(result);
        }

        static void Main(string[] args){
            // user input
            Console.WriteLine("Enter first number");
            int a = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter second number");
            int b = int.Parse(Console.ReadLine());
            Program.Add(4,5);
            Console.ReadLine();
        }
    }
}
```

```
using System;
namespace methodFunction
{
    class Program{
        public static void Add(string name){
            
            Console.WriteLine("Your name is: " +name);
        }

        static void Main(string[] args){
            // user input
            Program.Add("Musraful");
            Console.ReadLine();
        }
    }
}

```

```
using System;
namespace methodFunction
{
    class Program{
        public static void Show_Name_Age(string name, int age){
            
            Console.WriteLine("Your name is: " +name );
            Console.WriteLine("Your age is: " +age );

        }

        static void Main(string[] args){
            // user input
            Program.Show_Name_Age("Musraful", 22);
            Program.Show_Name_Age(age:22, name:"Musraful"); //Named arguments
            Console.ReadLine();
        }
    }
}

```
# Return statement in Method
- The return statement is used to return value.
- When a program call a function, the program control is transferred to the called function.

```
using System;
namespace methodFunction
{
    class Program{
        public static int Add(int a, int b){
            int result = a+b;
            return result;
        }

        static void Main(string[] args){
            Console.WriteLine(Program.Add(4,5));
            Console.ReadLine();
        }
    }
}
```

## Defining methods in C#

- The syntax for defining a method in C# is as follows -
```
- <Acces specifier> <Return type> <Method Name> (Parameter List)
{
    method body
}
```

## Invoking methods:
- To use a method, you need to - 
Define the method
Call the method

- A method can be invoked in a class by creating an object of the class where the object name is followed by a period(.) and the name of the method followed by parantheses.

- In C#, a method is always invoked from another method.
- This is referred to as the calling method and the invoked method is referred as the called method.

## Method Parameter and argunents:-
- Parameter:- The variable included in a method definition are called parameter.
- Which may have zero or more parameter, enclosed in parentheses and separated by commas.
- If the method takes no parameters, it is indicated by empty parantheses.

# Arguments:-
- When the method is called, the data that you send into the arguments methods parameters are called arguments.


### Advantages of using the methods:-

There are many advantages of using methods. Some of them are listed below:-
- It makes the program well structured.
- Methods enhance the readability of the code.
- It provides an effective way for the user to reuse the existing code. 
- It optimizes the execution time and memory space.


## Create a simple calculator:-
using System;
namespace methodFunction
{
    class Program{
        
        public static void Add(int a, int b){
            int result = a + b;
            Console.WriteLine("Addition result is: {0} ", result);
        }
        public static void sub(int a, int b){
            int result = a-b;
            Console.WriteLine("Substraction result is: {0} ", result);
        }
        public static void mul(int a, int b){
            int result = a*b;
            Console.WriteLine("Multiplication result is: {0} ", result);
        }
            public static void div(int a, int b){
            int result = a/b;
            Console.WriteLine("Division result is: {0} ", result);
        }
        

        static void Main(string[] args)
        {
            string confirm;
            do
            {
                Console.WriteLine("Enter first number:");
                int num1 = int.Parse(Console.ReadLine());
                Console.WriteLine("Enter sec number:");
                int num2 = int.Parse(Console.ReadLine());
                Console.WriteLine("Enter operator(+,-,*,/)");
                string op = Console.ReadLine();
                
                if (op == "+"){
                    Program.Add(num1, num2);
                }
                else if (op == "-"){
                    Program.sub(num1, num2);
                }
                else if (op == "*"){
                    Program.mul(num1, num2);
                }
                else if (op == "/"){
                    Program.div(num1, num2);
                }
                else{
                    Console.WriteLine("Invalid operator");
                }
                
                Console.WriteLine("Do you want to continue: yes/or");
                confirm = Console.ReadLine().ToLower();
            }
            while(confirm == "yes");
            Console.ReadLine();
        }
        
    }
}

## Two types of datatypes :- Struct, Reference.
- Struct   ---value type--- Stack memory
- Class   ---Reference---  Heap memory
- Syntax
```
struct Employee{
    public int salary;
    public int Age;
}
class Program
{
    static void Main(string[] args)
    {
        Employee e = new Employee();
        e.salary =5000;
        e.Age == 23;
        Employee e1 = e;
        Employee e2 = e;
        e.Age = 25;
        Console.WriteLine(e1.Age);
        Console.WriteLine(e2.Age);
        Console.ReadLine();
    }
}
```
## Reference type
```
class Employee{
    public int salary;
    public int Age;
}
class Program
{
    static void Main(string[] args)
    {
        Employee e = new Employee();
        e.salary =5000;
        e.Age == 23;
        Employee e1 = e;
        Employee e2 = e;
        e.Age = 25;
        Console.WriteLine(e1.Age);
        Console.WriteLine(e2.Age);
        Console.ReadLine();
    }
}
```

### Var and Dynamic keyword in C#:-
* Var Keyword:-
- Var was introduced in c# 3.0.
- Var keyword is used to store any type of data in its variable.
- Value of var variable is decided at compile time.
- We have to initialize the variable with var keyword.
- If we want to check the type of value which is stored in var variable then we can use GetType() method with the var variable.



