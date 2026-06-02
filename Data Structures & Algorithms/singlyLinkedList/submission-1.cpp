class ListNode{    
public:
    ListNode *next;
    int val_;
    ListNode(int val):val_(val), next(nullptr){}
    ListNode(int val, ListNode* next):val_(val),next(next){}
};
class LinkedList {

private:
ListNode* head_;
ListNode* tail_;

public:
    LinkedList() {
        head_ = new ListNode(-1);
        tail_ = head_;
    }

    int get(int index) {
        auto curr = head_->next;
        auto i = 0;
        while(curr != nullptr){
            if (i==index){
                return curr->val_;
            }
            i++;
            curr=curr->next;
        }
        return -1;
    }

    void insertHead(int val) {
        auto head = new ListNode(val);
        head->next = head_->next;
        head_->next = head;
        if (head->next == nullptr){
            tail_ = head;
        }
    }
    
    void insertTail(int val) {
        tail_->next = new ListNode(val);
        tail_ = tail_->next;
    }

    bool remove(int index) {
        auto curr = head_;
        auto i=0;
        while((curr!=nullptr) &&(i<index)){
            
        i++;
        curr=curr->next;
        }
        if ((curr!=nullptr)&&(curr->next!=nullptr)){
            if(curr->next == tail_){
                tail_ = curr;
            }
            auto toDelete = curr->next;
            curr->next = curr->next->next;
            delete toDelete;
            return true;
            }
        return false;
    }

    vector<int> getValues() {
        vector<int> res;
        auto curr = head_->next;
        while(curr!=nullptr){
            res.push_back(curr->val_);
            curr=curr->next;            
        }        
        return res;
    }
};
