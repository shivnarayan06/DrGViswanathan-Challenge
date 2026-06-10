class Solution {
public:
    vector<int> constructRectangle(int area) {
        int w = pow(area,0.5);
        while (area%w != 0){
            w--;
        }
        int l = area/w;
        return {l,w};
    }
};