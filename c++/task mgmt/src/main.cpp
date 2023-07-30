#include <iostream>
#include "buffer.cpp"
#include "tasks.cpp"

using namespace std;


int main() {
    cout << "Welcome to Tsk Ops. Where we take ops of tsks srsly." << endl;
    cout << "Please select an option: " << endl;
    cout << "1. Enter Task      2. Edit Task        3. View Tasks       4. Exit" << endl;

    int choice;
    while(cin >> choice) {
        
        // enter task
        if(choice == 1) {
            float currDate;
            string currTask;
            bool currPrio;

            clearBuffer();
            
            cout << "Please enter the date: ";
            cin >> currDate;
            
            clearBuffer();
            
            cout << "Please enter the task: " << endl;
            getline(cin >> ws, currTask);

            cout << "Top priority? [true/false]: ";
            cin >> currPrio;
            
            addTask(currDate, currTask, currPrio);
        }

        // edit task
        else if(choice == 2) {
            int selection;
            string choice;

            clearBuffer();

            cout << "Which task would you like to edit/delete?" << endl;
            cin >> selection;

            cout << "Would you like to edit or delete?" << endl;
            cin >> choice;
            
            if(choice == "delete") {
                deleteTask(selection);
            }
            else {
                string t;
                bool p;
                
                clearBuffer();
                
                cout << "Please enter the new task:" << endl;
                getline(cin >> ws, t);

                cout << "What priority would you like to change to [0/1]: ";
                cin >> p;

                editTask(selection, t, p);
            }
        }

        // view task
        else if(choice == 3) {
            // clearBuffer();
            //cout << "Here are your current tasks." << endl;
            printAllTasks();
        }

        // exit
        else if(choice == 4) {
            cout << "Goodbye." << endl;
            break;
        }

        // invalid selection
        else {
            cout << "You didn't enter a proper selection. Try again." << endl;
        }

        clearBuffer();

        cout << "Please select an option: " << endl;
        cout << "1. Enter Task      2. Edit Task        3. View Tasks       4. Exit" << endl;
    }

    return 0;
}
