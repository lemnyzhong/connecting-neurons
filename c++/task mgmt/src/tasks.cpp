#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct tasks {
    // string id;
    float date;
    string task;
    bool priority;
};

vector<tasks> allTasks;

// void setID() {
    // get size of allTasks
    // concat. "e" + size 
    // store in tasks id type
//}

// void loadTasks() {
    // need function to load in from external file
    // so all tasks are recorded and in perpetuity
// }

// void saveTasks() {
    // store vector allTasks in external file for
    // retrieval and data perpetuity
// }

void addTask(float& d, string& t, bool& p) {
    tasks newTask = {d, t, p};
    allTasks.push_back(newTask);
    cout << "Task saved!" << endl;
}

// void editTask() {
    // find task to edit
    // adjust and assign user data for editing
// }

void deleteTask(int i) {
    allTasks.erase(allTasks.begin()+i);
    cout << "Task deleted!" << endl;
}

void printAllTasks() {
    for(int i = 0; i < allTasks.size(); i++) {
        cout << allTasks[i].date << endl;
        cout << allTasks[i].task << endl;

        if(allTasks[i].priority == true) {
            cout << "important!" << endl;
        }
        else {
            cout << "unimportant!" << endl;
        }
    }
}