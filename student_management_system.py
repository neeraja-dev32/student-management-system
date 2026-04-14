def load_students():
    students = []
    


    try:
       with open("student.txt", "r") as f:
          for line in f:
              line = line.strip()
              if line:
                  name, age = line.split(",")
                  students.append({
                     "name": name,
                     "age": int(age)
                  })
    except:
        pass
    return students
students = load_students()

while True:
    print("\n1.add student")
    print("2.view students")
    print("3.exit")
    print("4.delete student")

    choice = input("enter choice: ")

    if choice == "1":
        name = input("enter name: ")
        age = int(input("enter age: "))

        student = {
            "name": name,
            "age": age,
        }
        students.append(student)

        f = open("students.txt", "a")
        f.write(name + "," + str(age) + "\n")
        f.close()
        
        print("student added successfully")
        
    elif choice == "2":
        if len(students) == 0:
            print(" no students found")
        else:
            for d in students:
                print("name:", d["name"], "age:", d["age"])
    elif choice == "3":
        print("exiting...")
        break
    elif choice == "4":
        name = input("enter name to delete: ")

        found = False

        for d in students:
            if d["name"] == name:
                students.remove(d)
                print("student deleted successfully")
                found = True
                break
        if not found:
            print("student not found: ")


    

    
