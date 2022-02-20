from flask import *

app = Flask(__name__)

# default constructor
class Queue():
 
    # To initialize and take the capacity as argument
    def __init__(self, c):
         
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c
        
 
    # insert element at the rear of the queue
    def enque(self, data):
 
        # Check queue is full
        if(self.capacity == self.rear):
            #print the error
            print("Queue is full")
        else:
            self.queue.append(data)
            self.rear += 1
 
    # Pop element from the front
    def deque(self):
        if(self.front == self.rear):
            print("Queue is empty")

        else:
            x = self.queue.pop(0)
            self.rear -= 1
    
    #check the number of sorted elements
    def sortednum(self):             
      
        i = 0
        flag = 0
        if(self.front == self.rear):
            print("Queue is empty")
        for num in self.queue:
            if self.queue[i] <= self.queue[i+1]:
                flag = flag + 1 

        if flag > 0:
            return flag - 1
        else:
            return ("Queue is empty")


#create global queue
queue = Queue(10)

#get a new queue of capacity a 
@app.route("/<int:a>", methods=['POST'])
def createq(a):  
    queue.capacity = a                    
    return jsonify({"Queue":queue.queue, "Capacity": queue.capacity}), 200

#get a the queue
@app.route("/", methods=['GET'])
def getq():   

    return jsonify({"Queue":queue.queue}), 200


#append to the queue
@app.route("/add/<int:b>", methods=['POST'])
def addq(b):
    queue.enque(b)     
    
    return jsonify({"Queue":queue.queue, "Capacity": queue.capacity}), 200

#delete from the queue, the left most will be deleted
@app.route("/delete", methods=['DELETE'])
def deletq():
    queue.deque()     
    
    return jsonify({"Queue":queue.queue}), 200

#Get number of sorted items
@app.route("/numSorted", methods=['GET'])
def getSorted():
    sorted = queue.sortednum() 

    return jsonify({"Number of items sorted":sorted, "Queue":queue.queue}), 200




if __name__ == '__main__':
    app.run(port = 7777)


