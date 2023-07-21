#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <variant>

using namespace std;

struct tasks {
    float date;
    string task;
    bool priority;
};

vector<tasks> allTasks;

// void loadTasks() {
    // need function to load in from external file
    // so all tasks are recorded and in perpetuity
// }

void addTask(float& d, string& t, bool& p) {
    tasks newTask = {d, t, p};
    allTasks.push_back(newTask);
    cout << "Task saved!" << endl;
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