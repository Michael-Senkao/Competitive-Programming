class Solution {
public:
    int countSetBits(int num){
        int setBits = 0;
        while(num > 0){
            setBits += (num&1);
            num >>= 1;
        }

        return setBits;
    }
    int minimizeXor(int num1, int num2) {
        int num1_bits, num2_bits, need_to_set;
        num1_bits = countSetBits(num1);
        num2_bits = countSetBits(num2);
        need_to_set = num2_bits - num1_bits;

        if(need_to_set == 0){
            return num1;
        }else if(need_to_set > 0){
            int position = 0;
            while(need_to_set > 0){
                if((num1 & (1 << position)) == 0){
                    num1 |= (1 << position);
                    
                    need_to_set -= 1;
                }
                position++;
            }
        }else{
            int position = 0;
        
            while(need_to_set < 0){
                if((num1 & (1 << position))){
                    num1 ^= (1 << position);
                    
                    need_to_set += 1;
                }
                position++;
            }
        }
        
        
        return num1;
    }
};