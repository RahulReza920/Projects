#include <iostream>
#include <string>
using namespace std;

struct student {
    int rollno;
    string name, fname, cell, dob, address;
};

void get_data(student &s) {
    cout << "Enter student roll number: ";
    cin >> s.rollno;
    cout << "Enter student name: ";
    cin >> s.name;
    cout << "Enter student's father name: ";
    cin >> s.fname;
    cout << "Enter student's cell phone number: ";
    cin >> s.cell;
    cout << "Enter student's date of birth (dd/mm/yyyy): ";
    cin >> s.dob;
    cout << "Enter student's address: ";
    cin >> s.address;
}

void show_data(const student &s) {
    cout << s.rollno << "\t" << s.name << "\t" << s.fname << "\t" << s.cell << "\t" << s.dob << "\t" << s.address << endl;
}

int main() {
    const int MAX_STUDENTS = 50;
    student rec[MAX_STUDENTS];
    int ts = 0;

    while (true) {
        cout << "\n\t\tWhat do you want to do?" << endl;
        cout << "\t\t----------------------" << endl;
        cout << "\t\t1-Add student" << endl;
        cout << "\t\t2-Display students" << endl;
        cout << "\t\t3-Search student" << endl;
        cout << "\t\t4-Quit Program" << endl;
        cout << "\t\t----------------------" << endl;
        cout << "Enter your choice: ";

        int choice;
        cin >> choice;

        switch (choice) {
            case 1: // add student
                if (ts == MAX_STUDENTS) {
                    cout << "Maximum number of students reached." << endl;
                    break;
                }
                get_data(rec[ts]);
                ts++;
                break;

            case 2: // display students
                if (ts == 0) {
                    cout << "No students to display." << endl;
                    break;
                }
                cout << "Roll No\tName\tFather Name\tCell No.\tDate of Birth\tAddress" << endl;
                for (int i = 0; i < ts; i++) {
                    show_data(rec[i]);
                }
                break;

            case 3: // search student
                if (ts == 0) {
                    cout << "No students to search." << endl;
                    break;
                }
                int search_key;
                cout << "Enter student roll number to search: ";
                cin >> search_key;
                for (int i = 0; i < ts; i++) {
                    if (rec[i].rollno == search_key) {
                        show_data(rec[i]);
                        break;
                    }
                }
                break;

            case 4: // quit program
                return 0;

            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }
}
