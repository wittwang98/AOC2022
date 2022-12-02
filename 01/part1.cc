#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

//part 1

int main()
{

    string filename{"input.txt"};

    ifstream ifs{filename};

    vector<int> elves{};

    string line{};
    int temp{};
    getline(ifs, line);
    do
    {
        if (line == "")
        {
            elves.push_back(temp);
            temp = 0;
             getline(ifs, line);
        }

        temp += stoi(line);       
    }
    while (getline(ifs,line));

    cout << *max_element(elves.begin(), elves.end()) << endl;

    //part 2

    sort(elves.begin(), elves.end(), greater<int>());

    cout << accumulate(elves.begin(), elves.begin()+3, 0) << '\n';
}