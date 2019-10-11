#include <iostream>
#include <cmath>
#include <bitset>
using namespace std;

void initial_input(long long int &p, long long int &q, long long int &s)
{
    cout << "Enter Prime number 'p' (where p % 4 = 3) : ";
    cin >> p;

    cout << "Enter Prime number 'q' (where q % 4 = 3) : ";
    cin >> q;

    cout << "Enter Seed 's' (s is relative prime to 'p * q') : ";
    cin >> s;
}
int main(){
    long long int p, q; // two prime
    long long int s;    // seed
    initial_input(p, q, s);

    // gernerate binary string
    long long int n = p * q;
    long long int x0 = (s * s) % n;    // x0 is also represent x(i - 1)
    bool random[8000];
    long long int xi;
    long long int s_2 = s * s;
    cout << "-----------Initial input parameter---------------" << endl;
    cout << "p : " << p << endl;
    cout << "q : " << q << endl;
    cout << "n(p * q) : " << n << endl;
    cout << "x0 : " << x0 << endl;
    cout << "--------------------------------------------------" << endl;
    for (int i = 0;i < 8000;i++){
         // x0 is also represent x(i - 1) in there
        xi = (x0 * x0) % n;
        random[i] = xi % 2;
        x0 = xi;
    }


    for (int k = 1;k <= 8;k++)
    {
        // print gernerate random number
        cout << "When k = " << k << ", binary string -> " << endl;
        for (int i = 0;i < k * 1000;i++)
            cout << random[i];
        cout << endl;
        /* confirm uniform distribution */
        // 驗證時，使用int 格式來驗證比較方便
        int num_range = (int) pow(2, k);   // num range 0 ~ (2^k) - 1, Ex: 當k = 3; 有(2^3) - 1 = 7種數字
        int string_appear_times[num_range];
        for (int i = 0;i < num_range;i++)  // initialize count arrary 
            string_appear_times[i] = 0;

        int index_count = 0;   // 紀錄處理到第幾個bit
        // 計算每種數字出現過幾遍
        for (int i = 0;i < 1000;i++) // 因為測試長度為1000 * k, 故為每個k都有1000小段
        {
            int count_num = 0; // 因為 random是 binary格式，利用 count_num變數以計數的方式 紀錄每一小段(k bit)轉成10進位後數字為多少
            for (int j = 0;j < k;j++, index_count++)
            {
                count_num *= 2;
                if (random[index_count] == true)
                    count_num +=1;
            }
            string_appear_times[count_num]++;
        }

        int max_stringNum_appear = 0; // 儲存出現次數最大值
        int min_stringNum_appear = 1000;    // 儲存出現次數最小值
        for (int i = 0;i < num_range;i++)
        {
            if (string_appear_times[i] > max_stringNum_appear) max_stringNum_appear = string_appear_times[i];
            if (string_appear_times[i] < min_stringNum_appear) min_stringNum_appear = string_appear_times[i];
            switch (k){
                case 1: cout << bitset<1> (i); break;
                case 2: cout << bitset<2> (i); break;
                case 3: cout << bitset<3> (i); break;
                case 4: cout << bitset<4> (i); break;
                case 5: cout << bitset<5> (i); break;
                case 6: cout << bitset<6> (i); break;
                case 7: cout << bitset<7> (i); break;
                case 8: cout << bitset<8> (i); break;
                default: cout << "Error happened!" << endl; return 0;
            }

            cout << " : " << string_appear_times[i] << " / " << "1000" << endl;
        }
        cout << "diffenece(Max - Min) : " << max_stringNum_appear - min_stringNum_appear << " / 1000" << "\n\n";






    }



}
