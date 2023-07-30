#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct tasks {
    string id;
    float date;
    string task;
    bool priority;
};

vector<tasks> allTasks;

// void loadTasks() {
    // need function to load in from external file
    // so all tasks are recorded and in perpetuity
// }

// void saveTasks() {
    // store vector allTasks in external file for
    // retrieval and data perpetuity
// }

string createID() {
    // get size of allTasks
    // concat. "e" + size 
    // store in tasks id type
    return "e" + to_string(allTasks.size() + 1);
}

void addTask(float& d, string& t, bool& p) {
    string id = createID();
    tasks newTask = {id, d, t, p};
    allTasks.push_back(newTask);
    cout << "Task saved!" << endl;
}

void editTask(int sel, string newTask, bool newPrio) {
    // find task to edit
    // adjust and assign user data for editing
    
    allTasks[sel].task = newTask;
    allTasks[sel].priority = newPrio;
}

void deleteTask(int taskNumber) {
    // ** IMPORTANT **
    // SEG FAULT when trying to delete non existing
    // potential fix:
    // checks whether taskNumber exists in allTasks
    // if not break edit with message

    allTasks.erase(allTasks.begin() + taskNumber);
    cout << "Task deleted!" << endl;
}

void printAllTasks() {
    if(allTasks.size() == 0) {
            cout << endl;

            cout << "There are no tasks!" << endl;
            
            cout << endl;
    }
    else {
        for(int i = 0; i < allTasks.size(); i++) {

        cout << endl;
        
        cout << allTasks[i].id << endl;
        cout << allTasks[i].date << endl;
        cout << allTasks[i].task << endl;

        if(allTasks[i].priority == true) {
            cout << "important!" << endl;
        }
        else {
            cout << "unimportant!" << endl;
        }

        cout << endl;
        }
    }
}