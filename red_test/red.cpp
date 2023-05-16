#include "/home/nico/Ibex/ibex-2.8.9/kerasify/keras_model.h"
#include "/home/nico/Ibex/ibex-2.8.9/kerasify/keras_model.cc"
#include "/home/nico/Ibex/ibex-2.8.9/src/contractor/funtions_for_ANN.cpp"


#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

std::vector<float> stringToFloatVector(const std::string& input) {
    std::vector<float> result;
    std::istringstream iss(input);
    std::string token;

    while (iss >> token) {
        try {
            float value = std::stof(token);
            result.push_back(value);
        } catch (const std::exception& e) {
            // Handle invalid float conversion
            std::cerr << "Error converting token: " << token << std::endl;
        }
    }

    return result;
}











int main(){



std::string input = "-14 15.8182 -7 5 6 8 -1 0.666667 11.6 7 -5 -6 -8 1 -1.2 0.836364 0.800001 -0 0 -0 -0 -1.5 1.04546 1 -0 0 2 -0 -1 1 0 -0 0 -0 -0 -0 1 0 -2 0 -0 -0 1 -1 0 -0 -2 -0 -0 -0 0 0 1 1 -0 -0 3.6 -11.5999 -7 5 6 8 -1 -0.399999 -15.8181 7 -5 -6 -8 1 -0.32 -0.48 0.800001 0 -0 0 0 -0.4 -0.599999 1 0 -0 2 0 1 2 0 1.200000000000001 0 1 0.1 0.8000000000000001 0.18 0.9000000000000001 0 1 25.65878878865224 40.94697812098965 -5.1103 24.6788 0.220185 2.27524 0 2.22045e-16 4.4409e-16 1.00001 -1.70664 8.10665 0.414668 2.51834";

std::vector<float> floatVector = stringToFloatVector(input);




KerasModel model;
model.LoadModel("/home/nico/Ibex/ibex-2.8.9/kerasify/predict_if_P.model");

Tensor in(295);

std::vector<float> tempo;
tempo=padWithZeros(floatVector,295);

normalize_l2(tempo);

 for (float value : tempo) {
        std::cout << value << " ";
    }
    std::cout << std::endl;


in.data_ = tempo;

Tensor out;
model.Apply(&in, &out);
// out.Print();
float proba=out.operator()(0);

cout<<endl;
cout<<"ANN output is: "<<proba<<endl;
cout<<endl;







}