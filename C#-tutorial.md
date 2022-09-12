### Switch case

- A program is difficult to comprehend when there are too many if statement representing multiple selection constructs.
- To avoid using multiple if statements, in certain cases, the switch case approach can be used as an alternative.
- The switch case statement is used when a variable needs to be compared against different values.
```
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

```

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



https://gist.github.com/ybmadhu/12bcf8cb525d3bfe31c3c88703799f69