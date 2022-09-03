class MyCalendar {
    private:
        map<int, int> booked_days;
public:
    MyCalendar() {
    }
//     map internally stores elements in a sorted order of keys -- USE THIS -- 
    bool book(int start, int end) {
        booked_days[start]++;
        booked_days[end]--;
        int sum=0;
        for(auto it=booked_days.begin();it != booked_days.end(); it++){
            sum+= it->second;
            if (sum > 1)
            {
                booked_days[start]--;
                booked_days[end]++;
                return false;
            }
        }
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */