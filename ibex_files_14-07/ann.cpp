#include "/home/nico/Ibex/ibex-2.8.9/src/contractor/funtions_for_ANN.cpp"
#include "/home/nico/Ibex/ibex-2.8.9/kerasify/keras_model.h"
#include "/home/nico/Ibex/ibex-2.8.9/kerasify/keras_model.cc"
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cstdlib>

using namespace std;

float Model_output_recommend(string path, vector<float>& input,int size){
    KerasModel model;
    model.LoadModel(path);
    Tensor in(size),out;
    input=padWithZeros(input,size);
    normalize_l2(input);
    in.data_ = input;

    model.Apply(&in,&out);
    float proba=out.operator()(0);
    return proba;
}

vector<float> ANN_P(string path,vector<float>& input,int size ){
    KerasModel model;
    model.LoadModel(path);
    Tensor in(size),out;
    input=padWithZeros(input,size);
    normalize_l2(input);
    in.data_ = input;
    model.Apply(&in,&out);
    int dim =out.dims_[0];
    vector<float> precondi;
    for(int i=0;i<out.dims_[0];i++){
        precondi.push_back(out.operator()(i));
    }
    return precondi;
}