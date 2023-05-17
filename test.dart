//void: similar class system to java\javascript
//start function
void main() {
  //int
  int age = 30;
  print(age);

  //string
  String name = "chun-li";
  print(name);

  //boolean
  bool isNight = false;
  print(isNight);

  //dynamic variables can be changed later
  dynamic name2 = 'chun-li';
  print(name2);
  name2 = 30;
  print(name2);

  //functions

  String greet = greeting();
  print(greet);

  age = getAge();
  print(age);

  //list

  List names = ['chun-li', 'yoshi', 'mario'];
  //append
  names.add('luigi');
  //pop
  names.remove('yoshi');
  //mixed data
  names.add(30);
  print(names);

  //List<var type>
  //filters a list to hold only one data type
  List<String> strNames = ['chun-li', 'yoshi', 'mario'];
  print(strNames);

  //invoking clases
  User userOne = User('luigi', 24);
  print(userOne.username);
  print(userOne.age);
  userOne.login();

  User userTwo = User('mario', 25);
  print(userTwo.username);
  print(userTwo.age);
  userTwo.login();

  //invoking inherited classes
  SuperUser userThree = SuperUser('yoshi', 30);
  print(userThree.username);
  print(userThree.age);
  userThree.login();
  userThree.publish();
}

//short hand return if there is no logic for a function
String greeting() => 'hello';

int getAge() {
  return 31;
}

//classes
class User {
  String username = "";
  int age = 0;

  //default constructor
  User(String username, int age) {
    this.username = username;
    this.age = age;
  }

  void login() {
    print('user logged in');
  }
}

//inheritance
class SuperUser extends User {
  //creates a constructor for the super user
  //pulls the values from User
  SuperUser(String username, int age) : super(username, age);

  void publish() {
    print("published update");
  }
}
