#question one#
class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.q = [None] * size
        self.front = self.rear = -1

def enqueue(self,x):
    if(self.rear + 1) % self.size == self.front:
        print("Queue full"); return
    if self.front == -1:
        self.front = 0
    self.rear = (self.rear + 1) % self.size  
    self.q[self.rear] = x

def dequeue(self):
    if self.front == -1:
        print("Queue empty");return
    x = self.q[self.front]
    if self.front == self.rear:
        self.front = self.rear = -1
    else:
        self.front = (self.front + 1) % self.size
    return x



# Question four #
def sum_n(n):
    return 0 if n == 0 else n +sum_n(n-1)

def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

def fib_series(n, i=0):
    if i == n: return 
    print(fib(i), end ="")
    fib_series(n, i+1)



# Question five #
queue = []
def enqueue(x):queue.append(x)
def enqueue():
    if not queue: print("Empty"); return
    return queue.pop(0)
enqueue(1); enqueue(2)
print(dequeue(),queue)


# Question Six #
m = [[0,0,3], [0,0,0],[4,0,5]]
sparse = [[i,j,m[i][j]]] for i in range(3) for j in range(3) if m[i][j] != 0
print ("Row Col Value")
for r in sparse: print(*r)


# Question Seven #
int dq[N], front = -1, rear = -1;

void insertFront(int x){
    if ((rear + 1)% N == front){printf("Full\n"); return;}
    if (front == -1) front = rear = 0;
    else front = (front - 1 + N) % N;
    dq[front] = x;
}
void insertRear(int x){
    if ((rear + 1) % N == front) {printf ("Full\n"); return;}
    if (front == -1) front = rear = 0;
    else rear = (rear + 1) % N;
    dq[rear] = x;
}
void deleteFront() {
    if (front == -1){printf("Empty\n");return;}
    if (front == rear) front = rear = -1;
    else front = (front + 1) % N;
}
void deleteRear() {
    if (front == -1) {printf("Empty\n"); return 0;}
    if (front == rear) front = rear = -1;
    else rear = (rear - 1 + N) % N;
}