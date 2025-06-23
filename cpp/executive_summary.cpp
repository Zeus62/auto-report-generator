#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

bool contains_keywords(const string& sentence, const vector<string>& keywords) {
    for (const auto& kw : keywords) {
        if (sentence.find(kw) != string::npos) return true;
    }
    return false;
}

int main() {
    string input, line;
    while (getline(cin, line)) {
        input += line + " ";
    }

    vector<string> accomplishments_keywords = {"finished", "completed", "implemented", "done", "delivered", "solved"};
    vector<string> blockers_keywords = {"blocked", "waiting", "issue", "problem", "stuck", "delay"};
    vector<string> deadline_keywords = {"deadline", "due", "asap", "urgent", "friday", "monday"};
    vector<string> support_keywords = {"need", "help", "support", "assistance", "request"};

    vector<string> achievements, blockers, urgent, needs;

    istringstream ss(input);
    string sentence;

    while (getline(ss, sentence, '.')) {
        string trimmed = sentence;
        trimmed.erase(remove_if(trimmed.begin(), trimmed.end(), ::isspace), trimmed.end());
        if (trimmed.empty()) continue;

        if (contains_keywords(sentence, accomplishments_keywords)) achievements.push_back(sentence);
        if (contains_keywords(sentence, blockers_keywords)) blockers.push_back(sentence);
        if (contains_keywords(sentence, deadline_keywords)) urgent.push_back(sentence);
        if (contains_keywords(sentence, support_keywords)) needs.push_back(sentence);
    }

    cout << "Summary:" << endl;
    for (auto& a : achievements) cout << "- " << a << "." << endl;

    cout << "\nBlocked:" << endl;
    for (auto& b : blockers) cout << "- " << b << "." << endl;

    cout << "\nUrgent:" << endl;
    for (auto& u : urgent) cout << "- " << u << "." << endl;

    cout << "\nNeeds Support:" << endl;
    for (auto& n : needs) cout << "- " << n << "." << endl;

    return 0;
}
