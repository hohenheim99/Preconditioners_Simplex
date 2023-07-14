#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <Eigen/Dense>
#include <numeric>

using namespace std;
using namespace Eigen;

bool isVectorFilledWithZeroes(const std::vector<float>& vec) {
    for (const float& num : vec) {
        if (num != 0.0 && num>=0.001) {
            return false;
        }
    }
    return true;
}

vector<float> padWithZeros(vector<float> v, int N) {
    float originalSize = v.size();

    if (N > originalSize) {
        v.resize(N);
        fill(v.begin() + originalSize, v.end(), 0.0);
    }

    return v;
}
void normalize_l2(std::vector<float>& v) {
    float norm = std::sqrt(std::accumulate(v.begin(), v.end(), 0.0, [](float acc, float x) {
        return acc + x * x;
    }));

    if (norm != 0.0) {
        std::transform(v.begin(), v.end(), v.begin(), [norm](float x) {
            return x / norm;
        });
    }
}


vector<vector<float>> createVectors(const std::vector<float>& lst, int n) {
    vector<vector<float>> vectors;
    for (size_t i = 0; i < lst.size(); i += n) {
        vector<float> sublist;
        for (int j = i; j < i + n && j < lst.size(); j++) {
            sublist.push_back(lst[j]);
        }
    //    if(isVectorFilledWithZeroes(sublist)==false){
    //         vectors.push_back(sublist);
    //    }
        
        vectors.push_back(sublist);
    }
    return vectors;
}


// IntervalMatrix createMatrix(const vector<float>& lst, int n) {
//     IntervalMatrix matrix(vectors.size(),n);
//     for (size_t i = 0; i < lst.size(); i += n) {
//         Vector sublist;
//         for (int j = i; j < i + n && j < lst.size(); j++) {
//             sublist.push_back(lst[j]);

//         }

//     }
//     return matrix;
// }
